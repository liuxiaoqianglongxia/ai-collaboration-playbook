# Task Hall Doc-first File-native MVP Canary

**Classification**: lab — experimental canary. The V3 standard is `standards/TASK_HALL_V3.md`.

Task Hall is an optional stable extension on top of `PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS`.

It is not V3 and it does not replace Drive-native V2. It provides a daily task/workbench layer when a project has a Drive workbench.

## Purpose

The module keeps ChatGPT's daily task packages in fixed Google Docs sockets and moves the high-frequency operating state into local/Drive files:

- task markdown and JSON files
- append-only `events.jsonl`
- `tasks_current.json` and `reports_current.json`
- SQLite with FTS-ready tables
- board and acceptance queue markdown
- static local UI
- lightweight context pack indexes

GitHub remains the stable code/report surface. The daily task hall lives in the Drive workbench.

## Bootstrap gate

Before ChatGPT writes or updates any Task Hall task package, the target project must already have a Drive workbench and Task Hall skeleton.

Minimum skeleton:

```text
<project-name>/
  00_HOME.md
  01_CURRENT.md
  02_INDEX.md
  task-hall/
    00_BOARD.md
    01_NOW.md
    02_ACCEPTANCE_QUEUE.md
    docs/active/
    tasks/
    reports/
    indexes/
    db/
```

If this skeleton is missing, ChatGPT must not upload, import, create, or update a Google Doc as a bootstrap task package. It should return a plain-text Codex instruction so Codex can create the workbench through local Drive sync.

Reference:

```text
standards/DRIVE_TASK_HALL_BOOTSTRAP_GATE_V1.md
```

## Official paths after bootstrap

```text
Board: task-hall/00_BOARD.md
Task: task-hall/tasks/YYYYMMDD/<TASK_ID>.md
Report: task-hall/reports/YYYYMMDD/<TASK_ID>_REPORT.md
Acceptance: task-hall/02_ACCEPTANCE_QUEUE.md
Fixed Docs registry: task-hall/docs/active/fixed-docs.json
```

Fixed Google Docs are sockets, not the official task storage. Official task packages and reports must be file-native under `task-hall/tasks/` and `task-hall/reports/`.

## Commands

Run from this directory:

```bash
python -m taskhall init --workbench PATH
python -m taskhall ingest --workbench PATH --source FILE
python -m taskhall claim --workbench PATH --task-id ID --agent codex-local-01
python -m taskhall start --workbench PATH --task-id ID --agent codex-local-01
python -m taskhall submit-report --workbench PATH --report FILE
python -m taskhall accept --workbench PATH --task-id ID --verdict PASS
python -m taskhall archive --workbench PATH --task-id ID
python -m taskhall revive --workbench PATH --task-id ID
python -m taskhall build-board --workbench PATH
python -m taskhall build-context-pack --workbench PATH --project-root PATH
python -m taskhall serve --workbench PATH --port 8765
python -m taskhall check --path PATH [--mode workbench|project]
```

For a non-blocking UI generation smoke test, use:

```bash
python -m taskhall serve --workbench PATH --port 8765 --once
```

## State machine

Supported states:

```text
DRAFT -> READY -> CLAIMED -> IN_PROGRESS -> NEEDS_ACCEPTANCE -> ACCEPTED
DRAFT -> READY -> BLOCKED
NEEDS_ACCEPTANCE -> NEEDS_REVISION -> READY
any non-final state -> ARCHIVED
```

`submit-report` moves the referenced task to `NEEDS_ACCEPTANCE`.
`accept --verdict PASS` moves it to `ACCEPTED`; other verdicts move it to `NEEDS_REVISION`.

## Risk boundary

The canary does not deploy, restart services, alter production databases, read or rotate secrets, delete protected branches/tags, force push, release, or rollback.
