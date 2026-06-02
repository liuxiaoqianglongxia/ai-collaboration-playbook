import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "samples"


def run_cmd(*args, cwd=ROOT):
    return subprocess.run(
        [sys.executable, "-m", "taskhall", *args],
        cwd=cwd,
        text=True,
        capture_output=True,
        check=True,
    )


def test_end_to_end_taskhall_flow(tmp_path):
    wb = tmp_path / "task-hall"
    run_cmd(
        "init",
        "--workbench",
        str(wb),
        "--date",
        "20260602",
        "--fixed-docs-json",
        str(SAMPLES / "fixed-docs.canary.json"),
    )
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    run_cmd(
        "claim",
        "--workbench",
        str(wb),
        "--task-id",
        "TASK-HALL-20260602-001",
        "--agent",
        "codex-local-01",
    )
    run_cmd(
        "start",
        "--workbench",
        str(wb),
        "--task-id",
        "TASK-HALL-20260602-001",
        "--agent",
        "codex-local-01",
    )
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))
    run_cmd("accept", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--verdict", "PASS")
    run_cmd("serve", "--workbench", str(wb), "--port", "8765", "--once")
    run_cmd("build-context-pack", "--workbench", str(wb), "--project-root", str(ROOT))

    tasks = json.loads((wb / "db" / "tasks_current.json").read_text(encoding="utf-8"))["tasks"]
    assert tasks["TASK-HALL-20260602-001"]["status"] == "ACCEPTED"
    assert tasks["TASK-HALL-20260602-002"]["status"] == "READY"
    assert (wb / "tasks" / "20260602" / "TASK-HALL-20260602-001.md").exists()
    assert (wb / "db" / "events.jsonl").read_text(encoding="utf-8").count("CREATED") >= 2
    assert (wb / "db" / "taskhall.sqlite").exists()
    assert (wb / "00_BOARD.md").exists()
    assert (wb / "02_ACCEPTANCE_QUEUE.md").exists()
    assert (wb / "web" / "index.html").exists()
    assert (wb / "indexes" / "project_brief.md").exists()
    assert (wb / "docs" / "active" / "fixed-docs.json").exists()
    assert (wb / "agents" / "hermes-local-01" / "heartbeat.json").exists()


def test_duplicate_and_malformed_tasks_are_quarantined(tmp_path):
    wb = tmp_path / "task-hall"
    source = tmp_path / "bad_tasks.txt"
    source.write_text(
        """
TASK_BEGIN
TASK_ID: TASK-HALL-20260602-003
PROJECT: ai-collaboration-playbook
TITLE: Good task
STATUS: READY
OWNER: codex-local-01
RISK: low
PRIORITY: P2
GOAL: Create one good task.
SCOPE: Test only.
ACCEPTANCE: Task is created.
TASK_END
TASK_BEGIN
TASK_ID: TASK-HALL-20260602-003
PROJECT: ai-collaboration-playbook
TITLE: Duplicate task
STATUS: READY
OWNER: codex-local-01
RISK: low
PRIORITY: P2
GOAL: Duplicate should be quarantined.
SCOPE: Test only.
ACCEPTANCE: Duplicate is quarantined.
TASK_END
TASK_BEGIN
TASK_ID: broken
PROJECT: ai-collaboration-playbook
STATUS: READY
TASK_END
""".strip(),
        encoding="utf-8",
    )
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(source))
    tasks = json.loads((wb / "db" / "tasks_current.json").read_text(encoding="utf-8"))["tasks"]
    assert set(tasks) == {"TASK-HALL-20260602-003"}
    assert list((wb / "quarantine" / "conflict").glob("*.txt"))
    assert list((wb / "quarantine" / "parse_failed").glob("*.txt"))


def test_accept_rejects_unknown_verdict(tmp_path):
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "taskhall",
            "accept",
            "--workbench",
            str(wb),
            "--task-id",
            "TASK-HALL-20260602-001",
            "--verdict",
            "UNKNOWN",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode != 0
    assert "unsupported verdict" in result.stderr


def test_start_rejects_ready_without_claim(tmp_path):
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "taskhall",
            "start",
            "--workbench",
            str(wb),
            "--task-id",
            "TASK-HALL-20260602-001",
            "--agent",
            "codex-local-01",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode != 0
    assert "invalid transition" in result.stderr


def test_accept_requires_needs_acceptance(tmp_path):
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "taskhall",
            "accept",
            "--workbench",
            str(wb),
            "--task-id",
            "TASK-HALL-20260602-001",
            "--verdict",
            "PASS",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode != 0
    assert "invalid transition" in result.stderr


# ---------------------------------------------------------------------------
# RC1 gap 1: final-state lock – ACCEPTED / ARCHIVED reject further mutations
# ---------------------------------------------------------------------------

def _setup_accepted_task(wb):
    """Run the happy-path up to ACCEPTED so we can test post-ACCEPTED guards."""
    run_cmd(
        "init",
        "--workbench",
        str(wb),
        "--date",
        "20260602",
        "--fixed-docs-json",
        str(SAMPLES / "fixed-docs.canary.json"),
    )
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    run_cmd("claim", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("start", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))
    run_cmd("accept", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--verdict", "PASS")


def test_final_state_accepted_rejects_claim(tmp_path):
    wb = tmp_path / "task-hall"
    _setup_accepted_task(wb)
    result = subprocess.run(
        [sys.executable, "-m", "taskhall", "claim",
         "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001",
         "--agent", "codex-local-01"],
        cwd=ROOT, text=True, capture_output=True,
    )
    assert result.returncode != 0
    assert "task is final" in result.stderr


def test_final_state_accepted_rejects_start(tmp_path):
    wb = tmp_path / "task-hall"
    _setup_accepted_task(wb)
    result = subprocess.run(
        [sys.executable, "-m", "taskhall", "start",
         "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001",
         "--agent", "codex-local-01"],
        cwd=ROOT, text=True, capture_output=True,
    )
    assert result.returncode != 0
    assert "task is final" in result.stderr


def test_final_state_accepted_rejects_accept_again(tmp_path):
    wb = tmp_path / "task-hall"
    _setup_accepted_task(wb)
    result = subprocess.run(
        [sys.executable, "-m", "taskhall", "accept",
         "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001",
         "--verdict", "PASS"],
        cwd=ROOT, text=True, capture_output=True,
    )
    assert result.returncode != 0
    assert "task is final" in result.stderr


def test_final_state_archived_rejects_mutation(tmp_path):
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    # READY -> ARCHIVED is allowed (from ALLOWED_TRANSITIONS)
    run_cmd("archive", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001")
    # After ARCHIVED, no more mutations
    result = subprocess.run(
        [sys.executable, "-m", "taskhall", "claim",
         "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001",
         "--agent", "codex-local-01"],
        cwd=ROOT, text=True, capture_output=True,
    )
    assert result.returncode != 0
    assert "task is final" in result.stderr


# ---------------------------------------------------------------------------
# RC1 gap 2: NEEDS_REVISION -> READY -> resubmit -> PASS revision cycle
# ---------------------------------------------------------------------------

def test_revision_cycle(tmp_path):
    """Full cycle: submit → FAIL verdict → resubmit → PASS verdict."""
    wb = tmp_path / "task-hall"
    run_cmd(
        "init", "--workbench", str(wb), "--date", "20260602",
        "--fixed-docs-json", str(SAMPLES / "fixed-docs.canary.json"),
    )
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    run_cmd("claim", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("start", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))

    # Verdict FAIL → task should go to NEEDS_REVISION
    run_cmd("accept", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--verdict", "FAIL")
    tasks = json.loads((wb / "db" / "tasks_current.json").read_text(encoding="utf-8"))["tasks"]
    assert tasks["TASK-HALL-20260602-001"]["status"] == "NEEDS_REVISION"

    # NEEDS_REVISION -> READY (transition back for rework)
    run_cmd("revive", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001")
    tasks = json.loads((wb / "db" / "tasks_current.json").read_text(encoding="utf-8"))["tasks"]
    assert tasks["TASK-HALL-20260602-001"]["status"] == "READY"

    # Re-claim, re-start, re-submit
    run_cmd("claim", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("start", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))

    # Verdict PASS → ACCEPTED
    run_cmd("accept", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--verdict", "PASS")
    tasks = json.loads((wb / "db" / "tasks_current.json").read_text(encoding="utf-8"))["tasks"]
    assert tasks["TASK-HALL-20260602-001"]["status"] == "ACCEPTED"


# ---------------------------------------------------------------------------
# RC1 gap 3: FAIL and PARTIAL_PASS verdict behavior
# ---------------------------------------------------------------------------

def test_fail_verdict_sends_to_needs_revision(tmp_path):
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    run_cmd("claim", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("start", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))
    run_cmd("accept", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--verdict", "FAIL")
    tasks = json.loads((wb / "db" / "tasks_current.json").read_text(encoding="utf-8"))["tasks"]
    assert tasks["TASK-HALL-20260602-001"]["status"] == "NEEDS_REVISION"
    # acceptance record should record FAIL verdict
    day = "20260602"
    acc = json.loads((wb / "acceptance" / day / "TASK-HALL-20260602-001-acceptance.json").read_text(encoding="utf-8"))
    assert acc["verdict"] == "FAIL"


def test_partial_pass_verdict_sends_to_needs_revision(tmp_path):
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    run_cmd("claim", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("start", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))
    run_cmd("accept", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--verdict", "PARTIAL_PASS")
    tasks = json.loads((wb / "db" / "tasks_current.json").read_text(encoding="utf-8"))["tasks"]
    assert tasks["TASK-HALL-20260602-001"]["status"] == "NEEDS_REVISION"
    day = "20260602"
    acc = json.loads((wb / "acceptance" / day / "TASK-HALL-20260602-001-acceptance.json").read_text(encoding="utf-8"))
    assert acc["verdict"] == "PARTIAL_PASS"


def test_blocked_verdict_sends_to_blocked(tmp_path):
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    run_cmd("claim", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("start", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))
    run_cmd("accept", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--verdict", "BLOCKED")
    tasks = json.loads((wb / "db" / "tasks_current.json").read_text(encoding="utf-8"))["tasks"]
    assert tasks["TASK-HALL-20260602-001"]["status"] == "BLOCKED"


# ---------------------------------------------------------------------------
# RC1 gap 4: SQLite data integrity assertions
# ---------------------------------------------------------------------------

def test_sqlite_tasks_reflect_json_state(tmp_path):
    """SQLite tasks table should contain the same tasks as tasks_current.json."""
    wb = tmp_path / "task-hall"
    run_cmd(
        "init", "--workbench", str(wb), "--date", "20260602",
        "--fixed-docs-json", str(SAMPLES / "fixed-docs.canary.json"),
    )
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    run_cmd("claim", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("start", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))
    run_cmd("accept", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--verdict", "PASS")

    import sqlite3
    db_path = wb / "db" / "taskhall.sqlite"
    con = sqlite3.connect(str(db_path))
    # Check tasks table has exactly the two ingested tasks
    rows = con.execute("SELECT task_id, status FROM tasks ORDER BY task_id").fetchall()
    assert len(rows) == 2
    task_ids = {r[0] for r in rows}
    assert task_ids == {"TASK-HALL-20260602-001", "TASK-HALL-20260602-002"}
    # Verify final status matches JSON
    status_map = dict(rows)
    assert status_map["TASK-HALL-20260602-001"] == "ACCEPTED"
    assert status_map["TASK-HALL-20260602-002"] == "READY"
    con.close()


def test_sqlite_events_reflect_jsonl(tmp_path):
    """SQLite events table should contain every event from events.jsonl."""
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))

    jsonl_path = wb / "db" / "events.jsonl"
    jsonl_events = [json.loads(line) for line in jsonl_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    jsonl_event_ids = {e["event_id"] for e in jsonl_events}

    import sqlite3
    db_path = wb / "db" / "taskhall.sqlite"
    con = sqlite3.connect(str(db_path))
    sqlite_event_ids = {
        r[0] for r in con.execute("SELECT event_id FROM events").fetchall()
    }
    con.close()
    # SQLite should contain at least all JSONL events (it may have more from init)
    assert jsonl_event_ids <= sqlite_event_ids


def test_sqlite_reports_reflect_json_state(tmp_path):
    """SQLite reports table should contain reports matching reports_current.json."""
    wb = tmp_path / "task-hall"
    run_cmd("init", "--workbench", str(wb), "--date", "20260602")
    run_cmd("ingest", "--workbench", str(wb), "--source", str(SAMPLES / "sample_task_inbox.txt"))
    run_cmd("claim", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("start", "--workbench", str(wb), "--task-id", "TASK-HALL-20260602-001", "--agent", "codex-local-01")
    run_cmd("submit-report", "--workbench", str(wb), "--report", str(SAMPLES / "sample_report.md"))

    import sqlite3
    db_path = wb / "db" / "taskhall.sqlite"
    con = sqlite3.connect(str(db_path))
    rows = con.execute("SELECT task_id, status FROM reports").fetchall()
    con.close()
    assert len(rows) == 1
    assert rows[0][0] == "TASK-HALL-20260602-001"
    assert rows[0][1] == "PASS"  # report status from the submitted report
