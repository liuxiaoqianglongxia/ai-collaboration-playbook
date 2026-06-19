# Quick Start | Task Hall V3 RC1

This page is the **single one-page entry** for a new ChatGPT / Codex / Claude Code session entering the playbook repository or applying it to another project.

For the canonical standard, see `standards/TASK_HALL_V3.md`.

## Current status

```text
stable baseline: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
Task Hall V3 RC1 candidate: in evaluation (this branch)
```

V3 RC1 is being evaluated on this branch. V2 remains the stable baseline until V3 RC1 is explicitly accepted and merged.

## One-line model

```text
Drive handles daily work. GitHub handles stable results. Task Hall V3 provides the formal task/workbench layer.
```

- ChatGPT: controller, task design, acceptance, release decision.
- Codex: local execution, validation, integration, reports.
- Claude Code: WSL/local engineering execution tool coordinated by Codex; editable by default unless the task says read-only.
- Drive Task Hall: daily tasks, reports, board, acceptance queue, context pack.
- GitHub main: stable docs, version anchors, reusable artifacts.

## Minimum read order for a new session

```text
QUICK_START.md                          - you are here
standards/TASK_HALL_V3.md               - canonical V3 standard
checklists/V3_TASK_HALL_PROJECT_INTAKE_CHECKLIST.md  - project intake
CHATGPT_START_HERE.md                   - ChatGPT operating notes
reports/latest.md                       - latest status report
reports/codex/latest.md                 - latest Codex report
templates/task-hall-v3/                 - default template
```

## Critical bootstrap gate

Before creating or writing any Task Hall task package, ChatGPT must check whether the target project's Drive workbench already exists.

Required minimum project workbench:

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

Verify with: `python3 -m taskhall check --path <project>/task-hall --mode workbench`

If the workbench is missing, ChatGPT must **not** use Drive upload/import/create document to bootstrap. It must return a plain-text Codex instruction and let Codex create the workbench through local Drive sync.

Reference standard: `standards/TASK_HALL_V3.md` (Section 9 Bootstrap Gate)

## Correct bootstrap fallback instruction

When the Drive workbench is missing, ChatGPT should give the user this kind of short instruction for Codex:

```text
Create the minimal Drive Task Hall workbench in the local Google Drive sync directory for the current project.

Create only the collaboration base. Do not change business code.

Target structure:
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

Report back with:
- PASS / PARTIAL PASS / FAIL / BLOCKED
- Drive local path
- Whether task-hall/ was created
- Whether 00_BOARD.md / 01_NOW.md / 02_ACCEPTANCE_QUEUE.md were created
- Whether no business code was changed
- Whether ChatGPT may now write the official Task Hall task
```

## Daily Task Hall flow after bootstrap

```text
Board: task-hall/00_BOARD.md
Task: task-hall/tasks/YYYYMMDD/<TASK_ID>.md
Report: task-hall/reports/YYYYMMDD/<TASK_ID>_REPORT.md
Acceptance: task-hall/02_ACCEPTANCE_QUEUE.md
Fixed Docs registry: task-hall/docs/active/fixed-docs.json
```

Fixed Google Docs may be used as sockets only after the workbench exists. The official task and report files must live under `task-hall/tasks/` and `task-hall/reports/`.

## What belongs in GitHub

```text
stable docs
stable code
release summary
rollback note
milestone summary
reusable templates
final acceptance reports
```

## What stays in Drive

```text
daily tasks
temporary reports
screenshots
raw materials
daily logs
handoffs
temporary acceptance notes
decision drafts
```

## Hard boundaries

```text
Do not edit main branch directly.
Do not touch business projects or production code.
Do not deploy to production.
Do not store or manage credentials/secrets.
Do not delete branches, tags, or repositories.
Do not force push.
Do not restore GitHub daily dispatch registry as default.
```

## Codex / Claude / ChatGPT minimal chain

```text
ChatGPT -> writes task package to Drive workbench
Codex   -> reads task, executes locally, writes report
Claude  -> engineering execution, patch drafting, tests, or review coordinated by Codex
ChatGPT -> reads report from acceptance queue, renders verdict
Codex   -> on PASS, syncs stable results to GitHub
```

V3 RC1 is under evaluation on the `release/playbook-v3-task-hall-rc1` branch. "Do not create V3" from the V2 baseline is superseded for this branch: V3 RC1 already exists and is being evaluated. The gate is acceptance, not creation.
