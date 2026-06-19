# Task Package Registry Standard V1.1

> **Standard ID**: `TASK_PACKAGE_REGISTRY_V1_1`
> **Status**: Historical stable baseline from `PLAYBOOK_OPERATIONAL_BASELINE_V1.1`
> **Current V2 note**: historical compatibility layer only. `PLAYBOOK_OPERATIONAL_BASELINE_V2` uses Drive task packages by default.
> **Maintained in**: `ai-collaboration-playbook/standards/TASK_PACKAGE_REGISTRY_V1_1.md`

---

## Purpose

Define a project-level GitHub-backed compatibility registry for executable AI task packages so ChatGPT, GitHub, Codex, and Claude Code can coordinate through files when a project explicitly chooses repository-backed dispatch.

The registry gives each opted-in project stable compatibility entry points for Codex and Claude Code tasks, plus a durable archive of ChatGPT task-package and acceptance snapshots.

In Drive-native V2 this registry is optional compatibility infrastructure, not the default daily dispatch mechanism.

## Status

`TASK_PACKAGE_REGISTRY_V1_1` was stabilized in `PLAYBOOK_OPERATIONAL_BASELINE_V1.1` and is now historical compatibility material under V2.

Promotion history:

```text
PR #6: docs: add task package registry standard v1.1
merge commit: 6cbadf2702286dce3b7c888a2b4f5e0e1d481c56
closeout commit: 5fe21aec9eccb87df0e318fc376cf1852129b2d7
current status source: reports/latest.md
status: PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS
```

Historical candidate reports remain as evidence, but active sessions must treat `reports/latest.md` as the current status source.

## Relationship to PLAYBOOK_OPERATIONAL_BASELINE_V1

`PLAYBOOK_OPERATIONAL_BASELINE_V1.1` adds a task-package registry layer on top of V1. It does not invalidate the existing onboarding, template, report, checklist, or execution-environment ownership standards.

The registry is now paired with:

```text
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
```

## Relationship to AI_COLLABORATION_MODE_V4

This standard does not replace `AI_COLLABORATION_MODE_V4.md`.

The four-piece model remains unchanged:

```text
ChatGPT: total control, architecture judgment, task-package design, acceptance
GitHub: single source of truth, project state machine, trace log
Codex: delivery lead, final integrator, report submitter
Claude Code: local engineering enhancement, deep code analysis, local draft, review
```

Hermes, Qwen, MCP, heartbeat, automation, and subagents are not default members. They may enter only when a specific project fact source or explicit user authorization requires them.

## Operating Principle

V1.1 exists to make the user layer simple while keeping the execution layer strong.

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

The user should normally give a short goal. The controller and repository should carry the complexity.

Bad pattern:

```text
User repeatedly copies long task packages across chats.
Every small task becomes a ceremony.
GitHub maintenance becomes the main workload.
```

Good pattern:

```text
User states the goal.
ChatGPT reads Drive daily facts and GitHub stable facts, then chooses the route.
Daily task package and report live in Drive by default.
Codex executes the current Drive task entry.
Claude Code is coordinated only when useful.
ChatGPT validates from Drive reports and GitHub stable evidence.
```

## One Active Execution Lane

One project stage should have one active execution lane.

Default rule:

```text
one active Codex task at a time
```

If `tasks/codex/latest.md` is `ACTIVE_CODEX_TASK`, ChatGPT must not create another active Codex task for the same stage. New findings become candidate next steps until the current task reports `PASS`, `PARTIAL PASS`, `FAIL`, or `BLOCKED`.

Claude Code may be coordinated inside the active Codex task, but it is not a separate default execution lane and does not replace Codex as final integrator.

While waiting for an active task, ChatGPT may read status, explain scope, or prepare an acceptance checklist. It must not activate new execution work for the same stage.

## User-Facing Task Announcement

For current V2 work, ChatGPT should give the user a short Drive task announcement instead of pasting the full task package by default:

```text
任务：<TASK-ID>
能实现：
- <one concrete outcome>
- <one concrete outcome>
- <one concrete outcome>
不做：<key boundary>
你发给 Codex：任务已写入 Drive：tasks/codex/YYYYMMDD/<task-name>.md；请读取该任务包执行，完成后写 Drive 报告。
详情：任务包已在 Drive。
```

When a project explicitly enables the GitHub-backed registry compatibility layer, use the project's declared compatibility entry. Do not claim the task package is in GitHub unless it actually exists in the repository.

## GitHub Write Capability Boundary

ChatGPT must be honest about its current capability.

If ChatGPT has GitHub write access in the current session:

```text
ChatGPT may write or update task packages, latest pointers, documentation, acceptance snapshots, and lightweight reports within the allowed scope.
ChatGPT should use that ability instead of forcing the user to copy long text.
```

If ChatGPT does not have GitHub write access:

```text
ChatGPT must say it cannot directly write GitHub in this session.
ChatGPT must not claim a task package has been written to GitHub.
ChatGPT may provide a compact Codex landing instruction or a complete task package for Codex to commit.
```

## Capability Split

ChatGPT should not outsource everything to Codex. Use the available capability correctly.

ChatGPT should usually do directly:

```text
read GitHub facts
write documentation and task packages when write access exists
update latest pointers when safe
perform read-only acceptance
summarize next action for the user
```

Codex should usually do:

```text
local repository operations
code changes
tests and validation commands
multi-file integration
branch / PR delivery
reports/codex/latest.md updates
```

Claude Code should usually do, through Codex or `tasks/claude/latest.md`:

```text
deep code reading
call-chain analysis
test failure localization
local fix drafts
review / second opinion
```

## Required Project Structure

Projects that explicitly adopt the GitHub-backed registry compatibility layer should add this structure:

```text
tasks/README.md
tasks/codex/_template.md
tasks/codex/latest.md
tasks/codex/<TASK-ID>.md
tasks/claude/_template.md
tasks/claude/latest.md
tasks/claude/<TASK-ID>.md
reports/chatgpt/task-packages/README.md
reports/chatgpt/task-packages/<TASK-ID>-ACCEPTANCE.md
```

This is a project-level compatibility structure. The playbook repository provides reusable templates and standards, but it does not replace the project Drive workbench as the default daily fact source.

## Codex Task Registry

Inside this compatibility registry, `tasks/codex/latest.md` is the repository-backed entry point for the current Codex task.

Rules:

- ChatGPT updates `tasks/codex/latest.md` when assigning or clearing a Codex task.
- The pointer must name a durable task file such as `tasks/codex/<TASK-ID>.md`, or explicitly say there is no active Codex task.
- Codex must read the pointed task file before modifying project files.
- Codex remains responsible for the final diff, validation, report, branch, and PR.
- Codex must not treat chat text as a replacement for a GitHub task file.
- A stage must not have a second active Codex task while the current latest pointer is `ACTIVE_CODEX_TASK`.

## Claude Code Task Registry

Inside this compatibility registry, `tasks/claude/latest.md` is the repository-backed entry point for the current Claude Code analysis or review task.

Rules:

- ChatGPT updates `tasks/claude/latest.md` when assigning or clearing a Claude Code task.
- The pointer must name a durable task file such as `tasks/claude/<TASK-ID>.md`, or explicitly say there is no active Claude Code task.
- Claude Code must stay within the task's allowed read/write boundary.
- Claude Code does not replace Codex as final integrator.
- Users should not be asked to manually relay long Claude Code task packages when Codex can coordinate the local toolchain.
- Claude Code outputs are evidence for Codex and ChatGPT to review, not direct authority to merge, deploy, or change final status.

## ChatGPT Task Package Snapshot Archive

`reports/chatgpt/task-packages/` stores ChatGPT-issued task-package snapshots, independent acceptance snapshots, and review summaries.

These files are evidence for a specific project. They are not global playbook standards, and they do not upgrade the playbook by themselves.

## latest.md Pointer Rules

`latest.md` files are pointers, not long-term history.

Rules:

- `tasks/codex/latest.md` points to one active Codex task package or says `NO_ACTIVE_CODEX_TASK`.
- `tasks/claude/latest.md` points to one active Claude Code task package or says `NO_ACTIVE_CLAUDE_TASK`.
- Historical task packages must be saved as named files.
- Do not overwrite a named task file to repurpose it for a different task.
- If a latest pointer conflicts with `CURRENT.md`, `TASKS.md`, or `reports/latest.md`, the executor must stop and report `BLOCKED`.
- After a task is completed and accepted, latest pointers must not continue to present it as active, waiting, or pending.
- Completed tasks may be listed briefly as previous task evidence, but current task should be `none` when no task is active.

## Task Package Lifecycle

1. ChatGPT reads the project fact source.
2. ChatGPT decides whether it can safely do the work directly or should assign Codex.
3. ChatGPT writes a named task package when a task needs execution.
4. ChatGPT updates the relevant latest pointer.
5. Codex or Claude Code reads the pointer and named task package.
6. The executor performs only the allowed work.
7. The executor writes a report.
8. ChatGPT performs read-only acceptance from GitHub facts.
9. The task status is reflected in `TASKS.md`, `reports/latest.md`, and the relevant agent report.
10. Completed latest pointers are cleared or marked no-active.

## Status Vocabulary

Use only these top-level acceptance results:

```text
PASS
PARTIAL PASS
FAIL
BLOCKED
```

Task pointers may use operational status labels such as:

```text
NO_ACTIVE_CODEX_TASK
ACTIVE_CODEX_TASK
NO_ACTIVE_CLAUDE_TASK
ACTIVE_CLAUDE_TASK
READY_FOR_REVIEW
READY_FOR_CODEX
READY_FOR_CHATGPT_ACCEPTANCE
```

Do not use stale waiting labels after the gate has passed.

## Acceptance Rules

ChatGPT acceptance must verify:

- the task package existed before execution when execution was required;
- the latest pointer referenced the correct task;
- the executor stayed within allowed scope;
- required reports were written;
- `CURRENT.md`, `TASKS.md`, and `reports/latest.md` do not contradict the result;
- prohibited environments, data, credentials, and deployment paths were not touched.

## Anti-Drift Rules

- `TASKS.md` records the queue and lifecycle state.
- `tasks/*/latest.md` records only the current execution pointer.
- `reports/latest.md` records the latest project-level result.
- `reports/chatgpt/task-packages/` preserves ChatGPT task and acceptance evidence.
- If these files diverge, execution must stop until the controller resolves the conflict.
- Candidate-era wording must not override a later stable closeout recorded in `reports/latest.md`.

## Forbidden Uses

The registry must not be used to:

- bypass `CURRENT.md`, `TASKS.md`, or `reports/latest.md`;
- authorize deployment, database changes, credential handling, or production changes without a separate safety task package;
- turn chat-only instructions into execution authority;
- copy project-specific business facts into generic templates;
- promote experimental lab material into a stable module without a separate promotion gate;
- change the V4 four-piece responsibility model;
- make GitHub itself the user-facing workload.

## Promotion Gate for Future Registry Changes

A future registry pattern may be promoted from project canary to playbook standard only when all conditions are met:

- at least one real project has completed the flow;
- a Codex report exists;
- ChatGPT has completed read-only acceptance;
- closeout fix or final acceptance evidence exists;
- business content has been removed from generic templates;
- V4 remains intact;
- no production, database, credential, or deployment authority is added implicitly.

## Stop Conditions

Stop and report `BLOCKED` when:

- the project repository identity cannot be verified;
- the latest pointer and named task file disagree;
- the registry conflicts with `CURRENT.md`, `TASKS.md`, or `reports/latest.md`;
- the task requires work outside the allowed scope;
- the task requires production, deployment, database, credential, or automation authority without a separate safety package;
- the registry would need changes to `AI_COLLABORATION_MODE_V4.md` to make sense.
