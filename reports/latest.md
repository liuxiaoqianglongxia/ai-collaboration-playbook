# Latest Report | PLAYBOOK_OPERATIONAL_BASELINE_V2 + Task Hall V3 RC1 Candidate

## Status

```text
PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
Task Hall V3 RC1 candidate: in evaluation (this branch)
```

## Conclusion

PASS.

`PLAYBOOK_OPERATIONAL_BASELINE_V2` remains the stable baseline on GitHub main.

Task Hall V3 RC1 is a candidate extension on top of V2. It provides a file-native task/workbench layer that can be used on Drive or any local filesystem. V3 does not replace V2; it formalizes the task-hall workbench pattern that V2 already assumed.

## V3 RC1 surfaces

```text
standard:       standards/TASK_HALL_V3.md
checklist:      checklists/V3_TASK_HALL_PROJECT_INTAKE_CHECKLIST.md
template:       templates/task-hall-v3/
entry:          QUICK_START.md
CLI:            lab/task-hall-mvp/ (taskhall check added)
```

## Current model

```text
V2 baseline: stable collaboration baseline
Task Hall V3 RC1: candidate daily task/workbench extension
Drive Task Hall: daily tasks, reports, board, acceptance queue, context pack
GitHub main: stable docs, version anchor, reusable artifacts
Codex: local executor and final integrator
Claude Code: WSL/local engineering execution tool coordinated by Codex; editable by default unless the task says read-only
ChatGPT: controller, task design, acceptance, release decision
```

## Task Hall V3 RC1

```text
status: V3 RC1 candidate (branch: release/playbook-v3-task-hall-rc1)
entry: QUICK_START.md
standard: standards/TASK_HALL_V3.md
workbench entry (Drive): <project>/task-hall/00_BOARD.md
workbench entry (local sync): G:/.../<project>/task-hall/00_BOARD.md
```

Task Hall provides:

```text
fixed Google Docs sockets
file-native task packages
task board
acceptance queue
reports
JSONL event log
SQLite local canary state
static local UI
context pack index
```

## Minimum new-session read order

```text
QUICK_START.md                          - single one-page entry
standards/TASK_HALL_V3.md               - canonical V3 standard
checklists/V3_TASK_HALL_PROJECT_INTAKE_CHECKLIST.md  - project intake
templates/task-hall-v3/                 - default template
reports/latest.md                       - you are here
reports/codex/latest.md                 - latest Codex report
```

## Daily task flow when Task Hall is enabled

Drive workbench paths (default):

```text
Board: <project>/task-hall/00_BOARD.md
Task: <project>/task-hall/tasks/YYYYMMDD/<TASK_ID>.md
Report: <project>/task-hall/reports/YYYYMMDD/<TASK_ID>_REPORT.md
Acceptance: <project>/task-hall/02_ACCEPTANCE_QUEUE.md
```

When discussing local Drive sync explicitly, prepend the full local path:

```text
Board: G:/My Drive/<project>/task-hall/00_BOARD.md
Task: G:/My Drive/<project>/task-hall/tasks/YYYYMMDD/<TASK_ID>.md
Report: G:/My Drive/<project>/task-hall/reports/YYYYMMDD/<TASK_ID>_REPORT.md
Acceptance: G:/My Drive/<project>/task-hall/02_ACCEPTANCE_QUEUE.md
```

GitHub `tasks/codex/latest.md` remains compatibility-only. It is not the default daily dispatch entry.

## Boundaries

```text
V2 remains the previous stable baseline until explicit acceptance/merge of V3 RC1.
Do not treat Task Hall as replacing V2.
Do not process PR #10 unless explicitly assigned.
Do not mix business project state into this playbook repository.
Do not use GitHub as the daily task queue when Task Hall is enabled.
```
