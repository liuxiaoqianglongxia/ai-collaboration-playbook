# Task Package Registry Standard V1.1

> **Standard ID**: `TASK_PACKAGE_REGISTRY_V1_1`
> **Status**: Candidate for `PLAYBOOK_OPERATIONAL_BASELINE_V1.1`
> **Maintained in**: `ai-collaboration-playbook/standards/TASK_PACKAGE_REGISTRY_V1_1.md`

---

## Purpose

Define a project-level registry for executable AI task packages so ChatGPT, Codex, Claude Code, and GitHub can coordinate through files instead of relying on long chat transcripts.

The registry gives each project stable entry points for current Codex and Claude Code tasks, plus a durable archive of ChatGPT task-package and acceptance snapshots.

## Status

`TASK_PACKAGE_REGISTRY_V1_1` is a candidate layer for `PLAYBOOK_OPERATIONAL_BASELINE_V1.1`.

It is not final until a pull request containing this standard passes independent read-only ChatGPT acceptance and is merged through a separate closeout task.

## Relationship to PLAYBOOK_OPERATIONAL_BASELINE_V1

`PLAYBOOK_OPERATIONAL_BASELINE_V1` remains stable.

V1.1 adds a task-package registry layer on top of V1. It does not invalidate the existing onboarding, template, report, checklist, or execution-environment ownership standards.

## Relationship to AI_COLLABORATION_MODE_V4

This standard does not replace `AI_COLLABORATION_MODE_V4.md`.

The four-piece model remains unchanged:

```text
ChatGPT: total control, task package design, acceptance
GitHub: single source of truth
Codex: delivery lead and final integrator
Claude Code: local engineering analysis and review support
```

## Core Principle

Task packages must be GitHub files before execution.

ChatGPT writes and updates task packages. Codex and Claude Code read the assigned task package from the relevant registry pointer. No agent should infer execution scope from chat history when a project registry exists.

## Dogfooding Requirement

The playbook repository should use its own `tasks/` registry for V1.1 follow-up tasks.

A stable registry standard should not only provide copyable templates. It should be supported by:

- at least one real project canary;
- one playbook self-dogfood task;
- a Codex latest pointer for closeout work;
- a Claude Code latest pointer for read-only review work;
- reports that show the registry can be executed without replacing V4.

Claude Code must receive read-only review tasks through `tasks/claude/latest.md`, not through ad hoc chat instructions.

## Required Project Structure

Projects that adopt V1.1 should add this copyable structure:

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

This is a project-level structure. The playbook repository provides reusable templates and standards, but it does not replace the project repository as the execution fact source.

## Codex Task Registry

`tasks/codex/latest.md` is the stable entry point for the current Codex task.

Rules:

- ChatGPT updates `tasks/codex/latest.md` when assigning a Codex task.
- The pointer must name a durable task file such as `tasks/codex/<TASK-ID>.md`, or explicitly say there is no active Codex task.
- Codex must read the pointed task file before modifying project files.
- Codex remains responsible for the final diff, validation, report, branch, and PR.
- Codex must not treat chat text as a replacement for a GitHub task file.

## Claude Code Task Registry

`tasks/claude/latest.md` is the stable entry point for the current Claude Code analysis or review task.

Rules:

- ChatGPT updates `tasks/claude/latest.md` when assigning a Claude Code task.
- The pointer must name a durable task file such as `tasks/claude/<TASK-ID>.md`, or explicitly say there is no active Claude Code task.
- Claude Code must stay within the task's allowed read/write boundary.
- Claude Code does not replace Codex as final integrator.

## ChatGPT Task Package Snapshot Archive

`reports/chatgpt/task-packages/` stores ChatGPT-issued task-package snapshots, independent acceptance snapshots, and review summaries.

These files are evidence for a specific project. They are not global playbook standards, and they do not upgrade the playbook by themselves.

## latest.md Pointer Rules

`latest.md` files are pointers, not long-term history.

Rules:

- `tasks/codex/latest.md` points to the active Codex task package.
- `tasks/claude/latest.md` points to the active Claude Code task package.
- Historical task packages must be saved as named files.
- Do not overwrite a named task file to repurpose it for a different task.
- If a latest pointer conflicts with `CURRENT.md`, `TASKS.md`, or `reports/latest.md`, the executor must stop and report `BLOCKED`.

## Task Package Lifecycle

1. ChatGPT reads the project fact source.
2. ChatGPT writes a named task package.
3. ChatGPT updates the relevant latest pointer.
4. Codex or Claude Code reads the pointer and named task package.
5. The executor performs only the allowed work.
6. The executor writes a report.
7. ChatGPT performs read-only acceptance from GitHub facts.
8. The task status is reflected in `TASKS.md`, `reports/latest.md`, and the relevant agent report.

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
```

## Acceptance Rules

ChatGPT acceptance must verify:

- the task package existed before execution;
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

## Forbidden Uses

The registry must not be used to:

- bypass `CURRENT.md`, `TASKS.md`, or `reports/latest.md`;
- authorize deployment, database changes, credential handling, or production changes without a separate safety task package;
- turn chat-only instructions into execution authority;
- copy project-specific business facts into generic templates;
- promote experimental lab material into a stable module without a separate promotion gate;
- change the V4 four-piece responsibility model.

## Canary-to-Stable Promotion Gate

A registry pattern may be promoted from project canary to playbook standard only when all conditions are met:

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
