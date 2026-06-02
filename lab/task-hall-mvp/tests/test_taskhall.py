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
