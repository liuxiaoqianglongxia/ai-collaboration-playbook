# CHATGPT_START_HERE

## Current baseline

```text
stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
optional extension: Task Hall optional stable extension / PASS
```

This repository is the general AI collaboration playbook. It is not a business project repository and does not contain production application code.

## Minimum read order

Read these first:

```text
QUICK_START.md
reports/latest.md
reports/codex/latest.md
lab/task-hall-mvp/README.md
reports/codex/20260602/PLAYBOOK_TASK_HALL_OPTIONAL_STABLE_EXTENSION_CLOSEOUT.md
standards/DRIVE_TASK_HALL_BOOTSTRAP_GATE_V1.md
```

Read `tasks/codex/latest.md` and `tasks/claude/latest.md` only when the current project explicitly uses the GitHub-backed compatibility registry.

If files conflict, treat `reports/latest.md` as the current status source and historical reports as evidence, not current state.

## Operating mode

```text
Drive handles daily work.
GitHub handles stable results.
Task Hall is the optional daily task/workbench extension.
```

V2 remains the stable baseline. Task Hall does not create V3 and does not replace Drive-native V2.

## Mandatory bootstrap gate for Task Hall

Before writing, uploading, importing, creating, or updating any Google Doc task package, ChatGPT must check whether the target project's Drive workbench exists.

Minimum required workbench:

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

If the project folder or `task-hall/` skeleton is missing, ChatGPT must not use Google Drive upload/import/create document. It must return a plain-text Codex instruction so Codex can create the workbench through local Drive sync.

Reference:

```text
standards/DRIVE_TASK_HALL_BOOTSTRAP_GATE_V1.md
```

## Correct first response when the Drive workbench is missing

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

## Role model

```text
ChatGPT: controller, architecture judgment, task package, acceptance, safe stable documentation writes when available
Drive: daily fact source and daily task/report/material/acceptance/decision workspace
GitHub: stable result, version management, release, rollback, reusable docs
Codex: delivery lead, local execution, final integration, reports
Claude Code: local engineering enhancement, first-pass draft fixes, deep analysis, review coordinated by Codex
```

Hermes, Qwen, MCP, heartbeat, automation, and subagents are not default members. Use them only when a project fact source or explicit user authorization requires them.

## Daily Task Hall flow after bootstrap

```text
Board: task-hall/00_BOARD.md
Task: task-hall/tasks/YYYYMMDD/<TASK_ID>.md
Report: task-hall/reports/YYYYMMDD/<TASK_ID>_REPORT.md
Acceptance: task-hall/02_ACCEPTANCE_QUEUE.md
Fixed Docs registry: task-hall/docs/active/fixed-docs.json
```

GitHub `tasks/codex/latest.md` remains compatibility-only and is not the default Drive Task Hall dispatch surface.

## Safety boundary

Do not modify:

```text
business repositories
production servers
databases
credentials or secrets
automation publish chains
```

Do not promote experimental lab material into stable standards without a separate promotion gate.

## Next recommended action

Use this playbook as the stable V2 baseline plus Task Hall optional stable extension. For each project, check the Drive workbench first; if the workbench is missing, send plain-text bootstrap instructions to Codex instead of creating root-level Google Docs.
