# TASKS Template — Task Tracking List

> **Purpose**: Track all open tasks with priority, assignee, acceptance criteria, and dependencies.
> **Applies to**: Any project using the four-piece collaboration pattern.
> **Place at**: Project root as `TASKS.md`. Works with `CURRENT.md`.

> **V3 Task Hall compatibility note**: This template represents the GitHub root-level `TASKS.md` style. Under V3 Task Hall, the default daily dispatch surface is `task-hall/00_BOARD.md` and `task-hall/tasks/YYYYMMDD/<TASK_ID>.md` in the project Drive workbench. `TASKS.md` remains as compatibility/history — it is not the default daily dispatch when V3 Task Hall is enabled.

> **Template Authority**: This file is an upstream template from `ai-collaboration-playbook`. When copied into a project repository, remove the `_TEMPLATE` suffix and keep the priority structure. The project-local copy becomes the execution authority for that project, while this template remains the upstream baseline.

## How to use

- Tasks are organized by priority: P0 (immediate), P1 (near-term), P2 (future).
- Update status as tasks progress.
- Each task has clear input, output, acceptance criteria, and stop conditions.

---

## P0 — Immediate (Must complete before next phase)

| ID | Task | Assignee | Status | Input | Output | Acceptance Criteria | Stop Condition | Dependencies |
|----|------|----------|--------|-------|--------|---------------------|----------------|-------------|
| P0-001 | [Task description] | [Claude Code / Codex / ChatGPT] | Open / In Progress / Done / Blocked | [What's needed to start] | [What gets produced] | [How we know it's done] | [When to stop and report] | [Task IDs this depends on] |
| P0-002 | [Task description] | [Agent] | Open | [Input] | [Output] | [Criteria] | [Stop condition] | — |

## P1 — Near-Term (Complete after P0)

| ID | Task | Assignee | Status | Input | Output | Acceptance Criteria | Stop Condition | Dependencies |
|----|------|----------|--------|-------|--------|---------------------|----------------|-------------|
| P1-001 | [Task description] | [Agent] | Open | [Input] | [Output] | [Criteria] | [Stop condition] | — |

## P2 — Future (Plan for later phases)

| ID | Task | Assignee | Status | Input | Output | Acceptance Criteria | Stop Condition | Dependencies |
|----|------|----------|--------|-------|--------|---------------------|----------------|-------------|
| P2-001 | [Task description] | [Agent] | Open | [Input] | [Output] | [Criteria] | [Stop condition] | — |

## Completed Tasks

| ID | Task | Completed By | Date | Result | Notes |
|----|------|-------------|------|--------|-------|
| P0-010 | [Task description] | [Agent] | YYYY-MM-DD | PASS / PARTIAL PASS / FAIL | [Brief note] |

## Blocked Tasks

| ID | Task | Blocked By | Reason | Action Needed |
|----|------|-----------|--------|---------------|
| P0-003 | [Task description] | [Decision / Access / Risk] | [Why blocked] | [What needs to happen to unblock] |
