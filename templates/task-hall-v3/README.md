# Task Hall V3 Project Template

Copy this template into a new project's Drive workbench root.

## Structure

```text
<project>/
  00_HOME.md          — project identity, routing, decision log pointer
  01_CURRENT.md       — current active task, blocker, next action
  02_INDEX.md         — index of all tasks and reports by date
  task-hall/
    00_BOARD.md       — task board with status counts and task table
    01_NOW.md         — single active lane: current task in progress
    02_ACCEPTANCE_QUEUE.md — tasks awaiting ChatGPT acceptance
    docs/active/      — fixed Google Docs socket links
    tasks/            — task packages by date (YYYYMMDD/TASK_ID.md)
    reports/          — execution reports by date
    indexes/          — file manifest, code/report/decision indexes
    db/               — tasks_current.json, reports_current.json, events.jsonl, taskhall.sqlite
```

## Usage

1. Copy all files into the project's Drive sync root.
2. Run `taskhall init --workbench <project>/task-hall` to create state files.
3. Run `taskhall check --path <project>/task-hall` to verify PASS.

See `standards/TASK_HALL_V3.md` for the full standard.
