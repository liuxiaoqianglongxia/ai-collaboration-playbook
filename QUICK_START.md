# Quick Start | Drive-native V2 + Task Hall Optional Stable Extension

This page is for a new ChatGPT / Codex / Claude Code session entering the playbook repository or applying it to another project.

## Current stable baseline

```text
PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
Task Hall optional stable extension: PASS
```

## One-line model

```text
Drive handles daily work. GitHub handles stable results. Task Hall is the optional daily task/workbench extension.
```

- ChatGPT: controller, task design, acceptance, release decision.
- Codex: local execution, validation, integration, reports.
- Claude Code: first-pass engineering review coordinated by Codex.
- Drive Task Hall: daily tasks, reports, board, acceptance queue, context pack.
- GitHub main: stable docs, version anchors, reusable artifacts.

## Minimum read order for a new session

```text
QUICK_START.md
CHATGPT_START_HERE.md
reports/latest.md
reports/codex/latest.md
lab/task-hall-mvp/README.md
reports/codex/20260602/PLAYBOOK_TASK_HALL_OPTIONAL_STABLE_EXTENSION_CLOSEOUT.md
standards/DRIVE_TASK_HALL_BOOTSTRAP_GATE_V1.md
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

If the project folder or `task-hall/` skeleton is missing, ChatGPT must not use Drive upload/import/create document to bootstrap the project. It must return a plain-text Codex instruction and let Codex create the workbench through local Drive sync.

Reference standard:

```text
standards/DRIVE_TASK_HALL_BOOTSTRAP_GATE_V1.md
```

## Correct bootstrap fallback instruction

When the Drive workbench is missing, ChatGPT should give the user this kind of short instruction for Codex:

```text
请在本地 Google Drive 同步目录中，为当前项目创建最小 Drive Task Hall 工作台。

只创建协作底座，不改业务代码。

目标结构：
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

完成后回报：
- PASS / PARTIAL PASS / FAIL / BLOCKED
- Drive 本地路径
- 是否创建 task-hall/
- 是否创建 00_BOARD.md / 01_NOW.md / 02_ACCEPTANCE_QUEUE.md
- 是否没有改业务代码
- 下一步是否可以让 ChatGPT 写正式 Task Hall 任务
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

## Do not do this

```text
Do not create root-level Google Docs as bootstrap task packages.
Do not restore GitHub tasks/codex/latest.md as the default daily task queue.
Do not create V3.
Do not treat Task Hall as replacing V2.
Do not copy the whole playbook into business projects.
Do not change business code when the task only asks for collaboration bootstrap.
```
