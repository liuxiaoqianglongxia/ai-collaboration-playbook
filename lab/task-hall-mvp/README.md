# Task Hall Doc-first File-native MVP Canary

This canary implements the minimal `TASK_HALL_DOC_FIRST_FILE_NATIVE_MVP`
flow for `ai-collaboration-playbook`.

## Purpose

The module keeps ChatGPT's daily task packages in fixed Google Docs and moves
the high-frequency operating state into local files:

- task markdown and JSON files
- append-only `events.jsonl`
- `tasks_current.json` and `reports_current.json`
- SQLite with FTS-ready tables
- board and acceptance queue markdown
- static local UI
- lightweight context pack indexes

GitHub remains the stable code/report surface. The daily task hall lives in the
Drive workbench.

## Commands

Run from this directory:

```bash
python -m taskhall init --workbench PATH
python -m taskhall ingest --workbench PATH --source FILE
python -m taskhall claim --workbench PATH --task-id ID --agent codex-local-01
python -m taskhall start --workbench PATH --task-id ID --agent codex-local-01
python -m taskhall submit-report --workbench PATH --report FILE
python -m taskhall accept --workbench PATH --task-id ID --verdict PASS
python -m taskhall build-board --workbench PATH
python -m taskhall build-context-pack --workbench PATH --project-root PATH
python -m taskhall serve --workbench PATH --port 8765
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
`accept --verdict PASS` moves it to `ACCEPTED`; other verdicts move it to
`NEEDS_REVISION`.

## Risk boundary

The canary does not deploy, restart services, alter production databases, read
or rotate secrets, delete protected branches/tags, force push, release, or
rollback.
