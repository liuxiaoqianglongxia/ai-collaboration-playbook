# DRIVE_TASK_HALL_BOOTSTRAP_GATE_V1

## Status

```text
stable: yes
applies_to: PLAYBOOK_OPERATIONAL_BASELINE_V2 + Task Hall optional stable extension
```

## Purpose

This standard prevents ChatGPT from creating or uploading Google Docs in the Drive root during Task Hall bootstrap.

Task Hall works only after the project Drive workbench exists. If the workbench or Task Hall folders do not exist yet, ChatGPT must not create a task package through Google Drive tools. It must first issue a plain-text Codex instruction so Codex can create the project workbench through local Drive sync.

## Bootstrap gate

Before writing any Task Hall task package, ChatGPT must perform this gate:

```text
1. Check whether the project Drive workbench exists.
2. Check whether task-hall/ exists under that workbench.
3. Check whether these files or folders exist:
   - task-hall/00_BOARD.md
   - task-hall/01_NOW.md
   - task-hall/02_ACCEPTANCE_QUEUE.md
   - task-hall/docs/active/
   - task-hall/tasks/
   - task-hall/reports/
   - task-hall/indexes/
   - task-hall/db/
4. If any required item is missing, do not upload, import, create, or update a Google Doc as a task package.
5. Return a plain-text Codex bootstrap instruction to create the missing workbench and Task Hall skeleton.
6. After Codex reports completion, verify the Drive workbench again.
7. Only after verification may ChatGPT write or update official Task Hall task packages.
```

## Forbidden during bootstrap

```text
Do not use Drive upload/import/create document to bootstrap a project.
Do not create root-level Google Docs as task packages.
Do not create root-level TASK_PACKAGE_FOR_CODEX_* docs.
Do not treat a root-level temporary Doc as the official Task Hall task file.
Do not restore GitHub tasks/codex/latest.md as the default daily dispatch entry.
```

## Correct bootstrap fallback

If the Drive workbench is missing or incomplete, ChatGPT should return a plain-text instruction like this:

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

## Official Task Hall paths after bootstrap

```text
Board: task-hall/00_BOARD.md
Current lane: task-hall/01_NOW.md
Acceptance queue: task-hall/02_ACCEPTANCE_QUEUE.md
Task: task-hall/tasks/YYYYMMDD/<TASK_ID>.md
Report: task-hall/reports/YYYYMMDD/<TASK_ID>_REPORT.md
Fixed Docs registry: task-hall/docs/active/fixed-docs.json
```

## Rule for other projects

Other projects must not copy the entire playbook repository. They only need a minimal Drive workbench and Task Hall skeleton. Business code remains untouched unless the user explicitly assigns a business-code task.
