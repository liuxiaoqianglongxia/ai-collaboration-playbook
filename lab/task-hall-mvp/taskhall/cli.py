from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STATE_ORDER = [
    "DRAFT",
    "READY",
    "CLAIMED",
    "IN_PROGRESS",
    "NEEDS_ACCEPTANCE",
    "NEEDS_REVISION",
    "ACCEPTED",
    "BLOCKED",
    "ARCHIVED",
]
FINAL_STATES = {"ACCEPTED", "ARCHIVED"}
ALLOWED_TRANSITIONS = {
    "DRAFT": {"READY", "ARCHIVED"},
    "READY": {"CLAIMED", "BLOCKED", "ARCHIVED"},
    "CLAIMED": {"IN_PROGRESS", "BLOCKED", "ARCHIVED"},
    "IN_PROGRESS": {"NEEDS_ACCEPTANCE", "BLOCKED", "ARCHIVED"},
    "NEEDS_ACCEPTANCE": {"ACCEPTED", "NEEDS_REVISION", "BLOCKED", "ARCHIVED"},
    "NEEDS_REVISION": {"READY", "BLOCKED", "ARCHIVED"},
    "BLOCKED": {"READY", "ARCHIVED"},
}
TASK_ID_RE = re.compile(r"^TASK-HALL-(\d{8})-(\d{3})$")
FIELD_RE = re.compile(r"^([A-Z][A-Z0-9_]*):\s*(.*)$")
TASK_BLOCK_RE = re.compile(r"TASK_BEGIN\s*(.*?)\s*TASK_END", re.DOTALL)
REPORT_FIELD_RE = re.compile(r"^([A-Z][A-Z0-9_]*):\s*(.*)$")

DIRS = [
    "docs/active",
    "docs/archive",
    "db",
    "tasks/{date}",
    "reports/{date}",
    "acceptance/{date}",
    "agents/codex-local-01/inbox",
    "agents/codex-local-01/outbox",
    "agents/claude-code-01/inbox",
    "agents/claude-code-01/outbox",
    "agents/hermes-local-01/inbox",
    "agents/hermes-local-01/outbox",
    "indexes",
    "rollups/daily",
    "rollups/weekly",
    "web/assets",
    "archive",
    "quarantine/parse_failed",
    "quarantine/conflict",
]

DOC_LINK_FILES = {
    "task_inbox": "TASK_INBOX_DOC_LINK.md",
    "report_outbox": "REPORT_INBOX_DOC_LINK.md",
    "acceptance_log": "ACCEPTANCE_DOC_LINK.md",
    "decision_log": "DECISIONS_DOC_LINK.md",
    "control_index": "CONTROL_DOC_LINK.md",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def today_yyyymmdd() -> str:
    return datetime.now().strftime("%Y%m%d")


def workbench_path(raw: str | Path) -> Path:
    return Path(raw).expanduser().resolve()


def ensure_json(path: Path, default: Any) -> Any:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(default, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def state_paths(wb: Path) -> dict[str, Path]:
    db = wb / "db"
    return {
        "tasks": db / "tasks_current.json",
        "reports": db / "reports_current.json",
        "events": db / "events.jsonl",
        "sqlite": db / "taskhall.sqlite",
    }


def sqlite_connect(wb: Path) -> sqlite3.Connection:
    paths = state_paths(wb)
    paths["sqlite"].parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(paths["sqlite"])
    con.execute("PRAGMA journal_mode=WAL")
    con.execute(
        "CREATE TABLE IF NOT EXISTS tasks ("
        "task_id TEXT PRIMARY KEY, status TEXT NOT NULL, title TEXT, "
        "owner TEXT, priority TEXT, risk TEXT, updated_at TEXT NOT NULL, "
        "payload_json TEXT NOT NULL)"
    )
    con.execute(
        "CREATE TABLE IF NOT EXISTS events ("
        "event_id TEXT PRIMARY KEY, task_id TEXT, event_type TEXT NOT NULL, "
        "agent TEXT, created_at TEXT NOT NULL, payload_json TEXT NOT NULL)"
    )
    con.execute(
        "CREATE TABLE IF NOT EXISTS reports ("
        "task_id TEXT PRIMARY KEY, status TEXT NOT NULL, report_path TEXT, "
        "updated_at TEXT NOT NULL, payload_json TEXT NOT NULL)"
    )
    con.commit()
    return con


def upsert_task_sqlite(wb: Path, task: dict[str, Any]) -> None:
    with sqlite_connect(wb) as con:
        con.execute(
            "INSERT INTO tasks(task_id,status,title,owner,priority,risk,"
            "updated_at,payload_json) VALUES(?,?,?,?,?,?,?,?) "
            "ON CONFLICT(task_id) DO UPDATE SET "
            "status=excluded.status,title=excluded.title,owner=excluded.owner,"
            "priority=excluded.priority,risk=excluded.risk,"
            "updated_at=excluded.updated_at,payload_json=excluded.payload_json",
            (
                task["task_id"],
                task.get("status", "READY"),
                task.get("title", ""),
                task.get("owner", ""),
                task.get("priority", ""),
                task.get("risk", ""),
                task.get("updated_at", utc_now()),
                json.dumps(task, ensure_ascii=False, sort_keys=True),
            ),
        )
        con.commit()


def upsert_report_sqlite(wb: Path, report: dict[str, Any]) -> None:
    with sqlite_connect(wb) as con:
        con.execute(
            "INSERT INTO reports(task_id,status,report_path,updated_at,"
            "payload_json) VALUES(?,?,?,?,?) "
            "ON CONFLICT(task_id) DO UPDATE SET status=excluded.status,"
            "report_path=excluded.report_path,updated_at=excluded.updated_at,"
            "payload_json=excluded.payload_json",
            (
                report["task_id"],
                report.get("status", ""),
                report.get("report_path", ""),
                report.get("updated_at", utc_now()),
                json.dumps(report, ensure_ascii=False, sort_keys=True),
            ),
        )
        con.commit()


def append_event(
    wb: Path,
    event_type: str,
    task_id: str | None = None,
    agent: str | None = None,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    paths = state_paths(wb)
    payload = payload or {}
    event_count = 0
    if paths["events"].exists():
        event_count = sum(1 for _ in paths["events"].open("r", encoding="utf-8"))
    event = {
        "event_id": f"EVT-{event_count + 1:06d}",
        "event_type": event_type,
        "task_id": task_id,
        "agent": agent,
        "created_at": utc_now(),
        "payload": payload,
    }
    append_jsonl(paths["events"], event)
    with sqlite_connect(wb) as con:
        con.execute(
            "INSERT INTO events(event_id,task_id,event_type,agent,created_at,"
            "payload_json) VALUES(?,?,?,?,?,?)",
            (
                event["event_id"],
                task_id,
                event_type,
                agent,
                event["created_at"],
                json.dumps(payload, ensure_ascii=False, sort_keys=True),
            ),
        )
        con.commit()
    return event


def load_tasks(wb: Path) -> dict[str, Any]:
    return ensure_json(state_paths(wb)["tasks"], {"updated_at": utc_now(), "tasks": {}})


def save_tasks(wb: Path, tasks_state: dict[str, Any]) -> None:
    tasks_state["updated_at"] = utc_now()
    write_json(state_paths(wb)["tasks"], tasks_state)
    for task in tasks_state.get("tasks", {}).values():
        upsert_task_sqlite(wb, task)


def load_reports(wb: Path) -> dict[str, Any]:
    return ensure_json(
        state_paths(wb)["reports"], {"updated_at": utc_now(), "reports": {}}
    )


def save_reports(wb: Path, reports_state: dict[str, Any]) -> None:
    reports_state["updated_at"] = utc_now()
    write_json(state_paths(wb)["reports"], reports_state)
    for report in reports_state.get("reports", {}).values():
        upsert_report_sqlite(wb, report)


def parse_fields(text: str, field_re: re.Pattern[str]) -> dict[str, str]:
    fields: dict[str, list[str]] = {}
    current: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        match = field_re.match(line)
        if match:
            current = match.group(1)
            fields[current] = [match.group(2).strip()]
        elif current:
            fields[current].append(line)
    return {key: "\n".join(value).strip() for key, value in fields.items()}


def date_from_task_id(task_id: str) -> str:
    match = TASK_ID_RE.match(task_id)
    return match.group(1) if match else today_yyyymmdd()


def task_paths(wb: Path, task_id: str) -> tuple[Path, Path]:
    day = date_from_task_id(task_id)
    base = wb / "tasks" / day
    return base / f"{task_id}.md", base / f"{task_id}.json"


def validate_task(fields: dict[str, str]) -> list[str]:
    required = [
        "TASK_ID",
        "PROJECT",
        "TITLE",
        "STATUS",
        "OWNER",
        "RISK",
        "PRIORITY",
        "GOAL",
        "SCOPE",
        "ACCEPTANCE",
    ]
    errors = [f"missing {key}" for key in required if not fields.get(key)]
    if fields.get("TASK_ID") and not TASK_ID_RE.match(fields["TASK_ID"]):
        errors.append("invalid TASK_ID; expected TASK-HALL-YYYYMMDD-NNN")
    status = fields.get("STATUS", "READY")
    if status not in STATE_ORDER:
        errors.append(f"unsupported STATUS {status}")
    return errors


def task_to_record(fields: dict[str, str]) -> dict[str, Any]:
    now = utc_now()
    task_id = fields["TASK_ID"]
    return {
        "task_id": task_id,
        "project": fields.get("PROJECT", ""),
        "title": fields.get("TITLE", ""),
        "status": fields.get("STATUS", "READY"),
        "owner": fields.get("OWNER", ""),
        "claude_mode": fields.get("CLAUDE_MODE", "none"),
        "hermes_mode": fields.get("HERMES_MODE", "none"),
        "risk": fields.get("RISK", ""),
        "priority": fields.get("PRIORITY", ""),
        "goal": fields.get("GOAL", ""),
        "scope": fields.get("SCOPE", ""),
        "inputs": fields.get("INPUTS", ""),
        "outputs": fields.get("OUTPUTS", ""),
        "acceptance": fields.get("ACCEPTANCE", ""),
        "needs_chatgpt_read": fields.get("NEEDS_CHATGPT_READ", ""),
        "limits": fields.get("LIMITS", ""),
        "created_at": now,
        "updated_at": now,
    }


def render_task_markdown(task: dict[str, Any]) -> str:
    lines = [
        f"# {task['task_id']} | {task.get('title', '')}",
        "",
        f"- Status: {task.get('status', '')}",
        f"- Project: {task.get('project', '')}",
        f"- Owner: {task.get('owner', '')}",
        f"- Priority: {task.get('priority', '')}",
        f"- Risk: {task.get('risk', '')}",
        f"- Claude mode: {task.get('claude_mode', '')}",
        f"- Hermes mode: {task.get('hermes_mode', '')}",
        "",
        "## Goal",
        task.get("goal", ""),
        "",
        "## Scope",
        task.get("scope", ""),
        "",
        "## Inputs",
        task.get("inputs", ""),
        "",
        "## Outputs",
        task.get("outputs", ""),
        "",
        "## Acceptance",
        task.get("acceptance", ""),
        "",
        "## Needs ChatGPT Read",
        task.get("needs_chatgpt_read", ""),
        "",
        "## Limits",
        task.get("limits", ""),
        "",
    ]
    return "\n".join(lines)


def quarantine(
    wb: Path, kind: str, name: str, content: str, metadata: dict[str, Any]
) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", name).strip("-") or "item"
    target_dir = wb / "quarantine" / kind
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{safe}.txt"
    target.write_text(
        content
        + "\n\n--- metadata ---\n"
        + json.dumps(metadata, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    return target


def register_fixed_docs(wb: Path, fixed_docs_path: Path) -> None:
    fixed_docs = json.loads(fixed_docs_path.read_text(encoding="utf-8"))
    target = wb / "docs" / "active" / "fixed-docs.json"
    write_json(target, fixed_docs)
    docs = fixed_docs.get("documents", {})
    for key, filename in DOC_LINK_FILES.items():
        info = docs.get(key, {})
        text = (
            f"# {info.get('title', key)}\n\n"
            f"- id: {info.get('id', '')}\n"
            f"- url: {info.get('url', '')}\n"
            f"- source: {fixed_docs.get('source', '')}\n"
        )
        (wb / "docs" / "active" / filename).write_text(text, encoding="utf-8")


def cmd_init(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    day = args.date or today_yyyymmdd()
    for pattern in DIRS:
        (wb / pattern.format(date=day)).mkdir(parents=True, exist_ok=True)
    ensure_json(state_paths(wb)["tasks"], {"updated_at": utc_now(), "tasks": {}})
    ensure_json(state_paths(wb)["reports"], {"updated_at": utc_now(), "reports": {}})
    state_paths(wb)["events"].parent.mkdir(parents=True, exist_ok=True)
    state_paths(wb)["events"].touch(exist_ok=True)
    sqlite_connect(wb).close()
    heartbeat = {
        "agent_id": "hermes-local-01",
        "status": "stub_only",
        "updated_at": utc_now(),
        "note": "MVP runs without Hermes; inbox/outbox and heartbeat are reserved.",
    }
    write_json(wb / "agents" / "hermes-local-01" / "heartbeat.json", heartbeat)
    readme = (
        "# Task Hall Workbench\n\n"
        "Doc-first file-native MVP workbench. ChatGPT writes fixed Google Docs; "
        "local tools maintain this file-native task hall.\n\n"
        "Entry points:\n\n"
        "- `00_BOARD.md`\n"
        "- `01_NOW.md`\n"
        "- `02_ACCEPTANCE_QUEUE.md`\n"
        "- `docs/active/fixed-docs.json`\n"
        "- `db/tasks_current.json`\n"
        "- `db/events.jsonl`\n"
        "- `web/index.html`\n"
    )
    (wb / "README.md").write_text(readme, encoding="utf-8")
    if args.fixed_docs_json:
        register_fixed_docs(wb, Path(args.fixed_docs_json))
    build_board_files(wb)
    append_event(wb, "WORKBENCH_INITIALIZED", payload={"date": day})
    print(f"initialized {wb}")
    return 0


def cmd_ingest(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    source = Path(args.source).resolve()
    text = source.read_text(encoding="utf-8")
    blocks = TASK_BLOCK_RE.findall(text)
    if not blocks:
        quarantine(wb, "parse_failed", source.name, text, {"reason": "no blocks"})
        append_event(wb, "INGEST_FAILED", payload={"reason": "no blocks"})
        return 1
    tasks_state = load_tasks(wb)
    existing = set(tasks_state.get("tasks", {}).keys())
    seen: set[str] = set()
    created = 0
    failed = 0
    for index, block in enumerate(blocks, start=1):
        fields = parse_fields(block, FIELD_RE)
        errors = validate_task(fields)
        task_id = fields.get("TASK_ID", f"UNKNOWN-{index}")
        if task_id in seen or task_id in existing:
            errors.append("duplicate TASK_ID")
            qpath = quarantine(
                wb, "conflict", f"{task_id}-{index}", block, {"errors": errors}
            )
            append_event(
                wb,
                "DUPLICATE_DETECTED",
                task_id=task_id,
                payload={"quarantine_path": str(qpath), "errors": errors},
            )
            failed += 1
            continue
        if errors:
            qpath = quarantine(
                wb, "parse_failed", f"{task_id}-{index}", block, {"errors": errors}
            )
            append_event(
                wb,
                "TASK_PARSE_FAILED",
                task_id=task_id,
                payload={"quarantine_path": str(qpath), "errors": errors},
            )
            failed += 1
            continue
        task = task_to_record(fields)
        md_path, json_path = task_paths(wb, task["task_id"])
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(render_task_markdown(task), encoding="utf-8")
        write_json(json_path, task)
        tasks_state.setdefault("tasks", {})[task["task_id"]] = task
        seen.add(task["task_id"])
        created += 1
        append_event(
            wb,
            "CREATED",
            task_id=task["task_id"],
            agent="taskhall-ingest",
            payload={"task_md": str(md_path), "task_json": str(json_path)},
        )
    save_tasks(wb, tasks_state)
    build_board_files(wb)
    print(json.dumps({"created": created, "failed": failed}, ensure_ascii=False))
    return 0 if created else 1



def validate_transition(task_id: str, current: str, target: str) -> None:
    if current in FINAL_STATES:
        raise SystemExit(f"task is final: {task_id} {current}")
    allowed = ALLOWED_TRANSITIONS.get(current, set())
    if target not in allowed:
        allowed_text = ", ".join(sorted(allowed)) or "none"
        raise SystemExit(
            f"invalid transition for {task_id}: {current} -> {target}; "
            f"allowed: {allowed_text}"
        )


def update_task_status(
    wb: Path,
    task_id: str,
    status: str,
    agent: str | None,
    event_type: str,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if status not in STATE_ORDER:
        raise SystemExit(f"unsupported status: {status}")
    tasks_state = load_tasks(wb)
    task = tasks_state.get("tasks", {}).get(task_id)
    if not task:
        raise SystemExit(f"task not found: {task_id}")
    current_status = task.get("status", "")
    validate_transition(task_id, current_status, status)
    task["status"] = status
    task["updated_at"] = utc_now()
    tasks_state["tasks"][task_id] = task
    save_tasks(wb, tasks_state)
    md_path, json_path = task_paths(wb, task_id)
    md_path.write_text(render_task_markdown(task), encoding="utf-8")
    write_json(json_path, task)
    append_event(wb, event_type, task_id=task_id, agent=agent, payload=extra or {})
    build_board_files(wb)
    return task


def cmd_claim(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    task = update_task_status(
        wb, args.task_id, "CLAIMED", args.agent, "CLAIMED", {"agent": args.agent}
    )
    outbox = wb / "agents" / args.agent / "outbox" / f"{args.task_id}-claim.json"
    write_json(
        outbox,
        {
            "task_id": args.task_id,
            "agent": args.agent,
            "status": task["status"],
            "created_at": utc_now(),
        },
    )
    print(f"claimed {args.task_id} by {args.agent}")
    return 0


def cmd_start(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    update_task_status(
        wb, args.task_id, "IN_PROGRESS", args.agent, "STARTED", {"agent": args.agent}
    )
    print(f"started {args.task_id} by {args.agent}")
    return 0


def parse_report(path: Path) -> dict[str, str]:
    return parse_fields(path.read_text(encoding="utf-8"), REPORT_FIELD_RE)


def cmd_submit_report(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    report_source = Path(args.report).resolve()
    fields = parse_report(report_source)
    for key in ["TASK_ID", "STATUS", "SUMMARY"]:
        if not fields.get(key):
            raise SystemExit(f"report missing {key}")
    task_id = fields["TASK_ID"]
    day = date_from_task_id(task_id)
    dest = wb / "reports" / day / f"{task_id}-report.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if report_source != dest.resolve():
        shutil.copyfile(report_source, dest)
    reports_state = load_reports(wb)
    report = {
        "task_id": task_id,
        "status": fields.get("STATUS", ""),
        "summary": fields.get("SUMMARY", ""),
        "changed_files": fields.get("CHANGED_FILES", ""),
        "new_files": fields.get("NEW_FILES", ""),
        "removed_files": fields.get("REMOVED_FILES", ""),
        "test_commands": fields.get("TEST_COMMANDS", ""),
        "test_results": fields.get("TEST_RESULTS", ""),
        "needs_chatgpt_read": fields.get("NEEDS_CHATGPT_READ", ""),
        "blockers": fields.get("BLOCKERS", ""),
        "next_recommended_task": fields.get("NEXT_RECOMMENDED_TASK", ""),
        "report_path": str(dest),
        "updated_at": utc_now(),
    }
    reports_state.setdefault("reports", {})[task_id] = report
    save_reports(wb, reports_state)
    update_task_status(
        wb,
        task_id,
        "NEEDS_ACCEPTANCE",
        fields.get("CLAUDE_USED") or "report-submitter",
        "REPORT_SUBMITTED",
        {"report_path": str(dest), "report_status": fields.get("STATUS")},
    )
    build_acceptance_queue(wb)
    print(f"submitted report for {task_id}")
    return 0


def cmd_accept(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    verdict = args.verdict.upper().replace(" ", "_")
    allowed = {"PASS", "PARTIAL_PASS", "FAIL", "BLOCKED"}
    if verdict not in allowed:
        raise SystemExit(f"unsupported verdict: {args.verdict}; expected one of {sorted(allowed)}")
    if verdict == "PASS":
        status = "ACCEPTED"
    elif verdict == "BLOCKED":
        status = "BLOCKED"
    else:
        status = "NEEDS_REVISION"
    task = update_task_status(
        wb,
        args.task_id,
        status,
        "chatgpt-acceptance",
        "ACCEPTED" if status == "ACCEPTED" else "REVISION_REQUESTED",
        {"verdict": verdict},
    )
    day = date_from_task_id(args.task_id)
    acceptance = wb / "acceptance" / day / f"{args.task_id}-acceptance.json"
    write_json(
        acceptance,
        {
            "task_id": args.task_id,
            "verdict": verdict,
            "status": task["status"],
            "accepted_at": utc_now(),
        },
    )
    build_acceptance_queue(wb)
    print(f"accepted {args.task_id} verdict={verdict}")
    return 0


def read_events(wb: Path) -> list[dict[str, Any]]:
    path = state_paths(wb)["events"]
    if not path.exists():
        return []
    events = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            events.append(json.loads(line))
    return events


def build_acceptance_queue(wb: Path) -> None:
    tasks = load_tasks(wb).get("tasks", {})
    reports = load_reports(wb).get("reports", {})
    rows = []
    for task_id, task in sorted(tasks.items()):
        if task.get("status") == "NEEDS_ACCEPTANCE":
            report = reports.get(task_id, {})
            rows.append(
                (
                    task_id,
                    task.get("title", ""),
                    report.get("status", ""),
                    report.get("report_path", ""),
                    report.get("needs_chatgpt_read", ""),
                )
            )
    lines = [
        "# Acceptance Queue",
        "",
        "| task_id | title | report_status | report_path | needs_chatgpt_read |",
        "| --- | --- | --- | --- | --- |",
    ]
    if rows:
        for row in rows:
            lines.append(
                "| " + " | ".join(str(cell).replace("\n", " ") for cell in row) + " |"
            )
    else:
        lines.append("| none | none | none | none | none |")
    (wb / "02_ACCEPTANCE_QUEUE.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def build_board_files(wb: Path) -> None:
    tasks = load_tasks(wb).get("tasks", {})
    counts = {state: 0 for state in STATE_ORDER}
    for task in tasks.values():
        status = task.get("status", "DRAFT")
        counts[status] = counts.get(status, 0) + 1
    lines = [
        "# Task Hall Board",
        "",
        f"Updated: {utc_now()}",
        "",
        "## Status counts",
        "",
    ]
    for state in STATE_ORDER:
        lines.append(f"- {state}: {counts.get(state, 0)}")
    lines.extend(
        [
            "",
            "## Tasks",
            "",
            "| status | priority | task_id | title | owner | risk |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    if tasks:
        def sort_key(item: dict[str, Any]) -> tuple[int, str, str]:
            status = item.get("status", "DRAFT")
            idx = STATE_ORDER.index(status) if status in STATE_ORDER else 99
            return idx, item.get("priority", ""), item.get("task_id", "")

        for task in sorted(tasks.values(), key=sort_key):
            title = task.get("title", "").replace("|", "/")
            lines.append(
                f"| {task.get('status','')} | {task.get('priority','')} | "
                f"{task.get('task_id','')} | {title} | {task.get('owner','')} | "
                f"{task.get('risk','')} |"
            )
    else:
        lines.append("| none | none | none | none | none | none |")
    (wb / "00_BOARD.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    active = [
        task
        for task in tasks.values()
        if task.get("status")
        in {"READY", "CLAIMED", "IN_PROGRESS", "NEEDS_ACCEPTANCE", "NEEDS_REVISION"}
    ]
    now_lines = [
        "# Now",
        "",
        f"Updated: {utc_now()}",
        "",
        "## Active lane",
        "",
    ]
    if active:
        task = sorted(
            active, key=lambda item: (item.get("priority", "P9"), item.get("task_id", ""))
        )[0]
        now_lines.extend(
            [
                f"- task_id: {task.get('task_id')}",
                f"- title: {task.get('title')}",
                f"- status: {task.get('status')}",
                f"- owner: {task.get('owner')}",
                "- next gate: ChatGPT reads report if status is NEEDS_ACCEPTANCE; "
                "otherwise assigned agent continues.",
            ]
        )
    else:
        now_lines.append("- none")
    (wb / "01_NOW.md").write_text("\n".join(now_lines) + "\n", encoding="utf-8")
    build_acceptance_queue(wb)


def cmd_build_board(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    build_board_files(wb)
    print(f"built board for {wb}")
    return 0


def iter_manifest(root: Path) -> list[dict[str, Any]]:
    skip_dirs = {
        ".git",
        "node_modules",
        ".venv",
        "venv",
        "__pycache__",
        ".pytest_cache",
        "dist",
        "build",
    }
    rows: list[dict[str, Any]] = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in skip_dirs for part in rel.parts):
            continue
        if path.is_dir():
            continue
        if len(rows) >= 2000:
            break
        try:
            stat = path.stat()
        except OSError:
            continue
        rows.append({"path": rel.as_posix(), "size": stat.st_size, "suffix": path.suffix.lower()})
    return rows


def safe_first_line(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            return fh.readline().strip()[:180]
    except OSError:
        return ""


def cmd_build_context_pack(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    project_root = Path(args.project_root).resolve()
    manifest = iter_manifest(project_root)
    indexes = wb / "indexes"
    indexes.mkdir(parents=True, exist_ok=True)
    write_json(
        indexes / "file_manifest.json",
        {
            "project_root_name": project_root.name,
            "generated_at": utc_now(),
            "files": manifest,
        },
    )
    with (indexes / "code_index.jsonl").open("w", encoding="utf-8", newline="\n") as fh:
        for row in manifest:
            if row["suffix"] in {".py", ".js", ".ts", ".tsx", ".jsx", ".json", ".yml", ".yaml"}:
                fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    with (indexes / "report_index.jsonl").open("w", encoding="utf-8", newline="\n") as fh:
        for row in manifest:
            if row["path"].startswith("reports/") and row["suffix"] == ".md":
                fh.write(
                    json.dumps(
                        {
                            "path": row["path"],
                            "title": safe_first_line(project_root / row["path"]),
                            "size": row["size"],
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                    )
                    + "\n"
                )
    with (indexes / "decision_index.jsonl").open("w", encoding="utf-8", newline="\n") as fh:
        for row in manifest:
            if row["path"].startswith("decisions/") or "DECISION" in row["path"].upper():
                fh.write(
                    json.dumps(
                        {
                            "path": row["path"],
                            "title": safe_first_line(project_root / row["path"]),
                            "size": row["size"],
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                    )
                    + "\n"
                )
    tasks = load_tasks(wb).get("tasks", {})
    reports = load_reports(wb).get("reports", {})
    brief = [
        "# Project Brief",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Stable baseline",
        "",
        "PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS. Drive is the daily fact source; "
        "GitHub is stable result surface.",
        "",
        "## Task Hall snapshot",
        "",
        f"- tasks: {len(tasks)}",
        f"- reports: {len(reports)}",
        "- ChatGPT read set: 01_NOW.md, 02_ACCEPTANCE_QUEUE.md, "
        "project_brief.md, current report, and NEEDS_CHATGPT_READ files.",
        "- High risk actions still require explicit authorization.",
        "",
        "## Fixed docs",
        "",
    ]
    fixed = wb / "docs" / "active" / "fixed-docs.json"
    if fixed.exists():
        docs = json.loads(fixed.read_text(encoding="utf-8")).get("documents", {})
        for key, info in docs.items():
            brief.append(f"- {key}: {info.get('title')} ({info.get('url')})")
    else:
        brief.append("- not registered")
    (indexes / "project_brief.md").write_text(
        "\n".join(brief) + "\n", encoding="utf-8"
    )
    append_event(wb, "CONTEXT_PACK_BUILT", payload={"project_root_name": project_root.name})
    print(f"built context pack at {indexes}")
    return 0


def build_ui(wb: Path) -> Path:
    tasks = load_tasks(wb).get("tasks", {})
    reports = load_reports(wb).get("reports", {})
    events = read_events(wb)[-80:]
    groups: dict[str, list[dict[str, Any]]] = {state: [] for state in STATE_ORDER}
    for task in tasks.values():
        groups.setdefault(task.get("status", "DRAFT"), []).append(task)
    cards = []
    for state in STATE_ORDER:
        items = groups.get(state, [])
        card_lines = [f"<section class='lane'><h2>{html.escape(state)} <span>{len(items)}</span></h2>"]
        if not items:
            card_lines.append("<p class='empty'>No tasks</p>")
        for task in sorted(items, key=lambda item: item.get("task_id", "")):
            report = reports.get(task.get("task_id", ""), {})
            card_lines.append(
                "<article class='task'>"
                f"<strong>{html.escape(task.get('task_id',''))}</strong>"
                f"<h3>{html.escape(task.get('title',''))}</h3>"
                f"<p>{html.escape(task.get('goal','')[:180])}</p>"
                "<dl>"
                f"<dt>agent</dt><dd>{html.escape(task.get('owner',''))}</dd>"
                f"<dt>risk</dt><dd>{html.escape(task.get('risk',''))}</dd>"
                f"<dt>report</dt><dd>{html.escape(report.get('report_path','none'))}</dd>"
                f"<dt>acceptance</dt><dd>{html.escape(task.get('status',''))}</dd>"
                "</dl>"
                "</article>"
            )
        card_lines.append("</section>")
        cards.append("\n".join(card_lines))
    event_items = "\n".join(
        f"<li><time>{html.escape(event.get('created_at',''))}</time>"
        f"<b>{html.escape(event.get('event_type',''))}</b>"
        f"<span>{html.escape(str(event.get('task_id') or 'workspace'))}</span></li>"
        for event in events
    ) or "<li>No events</li>"
    html_text = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Task Hall Canary</title>
<style>
:root {{ --ink:#17211d; --muted:#62736b; --paper:#f7f1df; --card:#fffaf0; --line:#d8caa3; --accent:#0f6b5f; --accent2:#d36b2c; --shadow:0 18px 45px rgba(28,42,35,.14); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:"Aptos Serif","Georgia",serif; color:var(--ink); background:radial-gradient(circle at 15% 10%, #ffe4b7 0 16rem, transparent 17rem), linear-gradient(135deg,#f7f1df,#e9f1df 55%,#d8ece8); }}
header {{ padding:48px 5vw 24px; }}
.kicker {{ text-transform:uppercase; letter-spacing:.18em; color:var(--accent); font:700 12px "Trebuchet MS",sans-serif; }}
h1 {{ max-width:980px; margin:10px 0; font-size:clamp(40px,7vw,84px); line-height:.92; }}
.summary {{ display:flex; gap:14px; flex-wrap:wrap; margin-top:22px; }}
.summary span {{ border:1px solid var(--line); border-radius:999px; padding:9px 14px; background:rgba(255,250,240,.72); }}
.board {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:18px; padding:18px 5vw 42px; }}
.lane {{ background:rgba(255,250,240,.82); border:1px solid var(--line); border-radius:28px; box-shadow:var(--shadow); padding:18px; backdrop-filter:blur(8px); }}
.lane h2 {{ display:flex; align-items:center; justify-content:space-between; margin:0 0 16px; font:800 18px "Trebuchet MS",sans-serif; letter-spacing:.08em; }}
.lane h2 span {{ background:var(--ink); color:white; border-radius:999px; padding:3px 9px; }}
.task {{ border-top:1px solid var(--line); padding:14px 0; }}
.task strong {{ color:var(--accent2); font:800 12px "Trebuchet MS",sans-serif; letter-spacing:.08em; }}
.task h3 {{ margin:6px 0; font-size:22px; }}
.task p {{ color:var(--muted); }}
dl {{ display:grid; grid-template-columns:auto 1fr; gap:4px 10px; font-size:13px; }}
dt {{ color:var(--muted); text-transform:uppercase; font-family:"Trebuchet MS",sans-serif; }}
dd {{ margin:0; overflow-wrap:anywhere; }}
.timeline {{ margin:0 5vw 56px; padding:22px; border-radius:28px; background:#17211d; color:#fffaf0; box-shadow:var(--shadow); }}
.timeline h2 {{ margin-top:0; }}
.timeline ol {{ list-style:none; padding:0; margin:0; display:grid; gap:10px; }}
.timeline li {{ display:grid; grid-template-columns:minmax(0,220px) minmax(0,1fr) minmax(0,220px); gap:12px; border-top:1px solid rgba(255,255,255,.16); padding-top:10px; }}
.timeline time {{ color:#b8d8ce; }}
.empty {{ color:var(--muted); font-style:italic; }}
@media (max-width:720px) {{ header {{ padding-top:32px; }} .timeline li {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<header><div class="kicker">Doc-first file-native MVP</div><h1>Task Hall Canary</h1><p>Local board for fixed Docs, file-native tasks, reports, acceptance, agents, and events.</p><div class="summary"><span>{len(tasks)} tasks</span><span>{len(reports)} reports</span><span>{len(events)} recent events</span></div></header>
<main class="board">{''.join(cards)}</main>
<section class="timeline"><h2>Event timeline</h2><ol>{event_items}</ol></section>
</body>
</html>
"""
    target = wb / "web" / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html_text, encoding="utf-8")
    return target


def cmd_serve(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    target = build_ui(wb)
    append_event(wb, "UI_BUILT", payload={"port": args.port, "once": args.once})
    print(f"built UI at {target}")
    if args.once:
        return 0
    import functools
    import http.server
    import socketserver

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(wb / "web"))
    with socketserver.TCPServer(("127.0.0.1", args.port), handler) as httpd:
        print(f"serving http://127.0.0.1:{args.port}/")
        httpd.serve_forever()
    return 0


def cmd_archive(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    agent = getattr(args, "agent", None) or "taskhall-archive"
    update_task_status(
        wb, args.task_id, "ARCHIVED", agent, "ARCHIVED", {"reason": getattr(args, "reason", "")}
    )
    print(f"archived {args.task_id}")
    return 0


def cmd_revive(args: argparse.Namespace) -> int:
    wb = workbench_path(args.workbench)
    agent = getattr(args, "agent", None) or "taskhall-revive"
    update_task_status(
        wb, args.task_id, "READY", agent, "REVIVED", {"agent": agent}
    )
    print(f"revived {args.task_id}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="taskhall", description="Doc-first file-native Task Hall MVP canary"
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init")
    p.add_argument("--workbench", required=True)
    p.add_argument("--date", default=None)
    p.add_argument("--fixed-docs-json", default=None)
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("ingest")
    p.add_argument("--workbench", required=True)
    p.add_argument("--source", required=True)
    p.set_defaults(func=cmd_ingest)

    p = sub.add_parser("claim")
    p.add_argument("--workbench", required=True)
    p.add_argument("--task-id", required=True)
    p.add_argument("--agent", required=True)
    p.set_defaults(func=cmd_claim)

    p = sub.add_parser("start")
    p.add_argument("--workbench", required=True)
    p.add_argument("--task-id", required=True)
    p.add_argument("--agent", required=True)
    p.set_defaults(func=cmd_start)

    p = sub.add_parser("submit-report")
    p.add_argument("--workbench", required=True)
    p.add_argument("--report", required=True)
    p.set_defaults(func=cmd_submit_report)

    p = sub.add_parser("accept")
    p.add_argument("--workbench", required=True)
    p.add_argument("--task-id", required=True)
    p.add_argument("--verdict", required=True)
    p.set_defaults(func=cmd_accept)

    p = sub.add_parser("archive")
    p.add_argument("--workbench", required=True)
    p.add_argument("--task-id", required=True)
    p.add_argument("--agent", default=None)
    p.add_argument("--reason", default="")
    p.set_defaults(func=cmd_archive)

    p = sub.add_parser("revive")
    p.add_argument("--workbench", required=True)
    p.add_argument("--task-id", required=True)
    p.add_argument("--agent", default=None)
    p.set_defaults(func=cmd_revive)

    p = sub.add_parser("build-board")
    p.add_argument("--workbench", required=True)
    p.set_defaults(func=cmd_build_board)

    p = sub.add_parser("build-context-pack")
    p.add_argument("--workbench", required=True)
    p.add_argument("--project-root", required=True)
    p.set_defaults(func=cmd_build_context_pack)

    p = sub.add_parser("serve")
    p.add_argument("--workbench", required=True)
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--once", action="store_true")
    p.set_defaults(func=cmd_serve)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
