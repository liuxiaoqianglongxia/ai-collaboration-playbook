# Execution Lane Management Standard V1

> **Standard ID**: `EXECUTION_LANE_MANAGEMENT_V1`
> **Status**: Stable in `PLAYBOOK_OPERATIONAL_BASELINE_V1.1`
> **Maintained in**: `ai-collaboration-playbook/standards/EXECUTION_LANE_MANAGEMENT_V1.md`

---

## Purpose

Define how many active execution lanes may exist during one project stage.

The rule is simple:

```text
One stage has one active execution lane.
Default: one active Codex task at a time.
```

This keeps the user-facing layer simple while preserving full execution power behind the scenes.

## Core Rule

- A project stage must not have more than one active Codex execution lane.
- If `tasks/codex/latest.md` points to an active Codex task, ChatGPT must not create another active Codex task.
- The current Codex task must end with `PASS`, `PARTIAL PASS`, `FAIL`, or `BLOCKED` before a new Codex task becomes active.
- New findings during an active task become candidate next steps, not new active task pointers.
- ChatGPT may prepare notes, acceptance checklists, or future task drafts, but must not move latest pointers to a new active task while the current task is unfinished.

## Claude Code During An Active Codex Task

Claude Code may support the active Codex task, but it is not a second default execution lane.

Allowed patterns:

```text
Codex coordinates Claude Code inside the active Codex task.
Codex may use tasks/claude/latest.md for a bounded read-only review or analysis subtask.
Codex reads and verifies Claude Code output before using it.
Codex remains final integrator and report owner.
```

Disallowed patterns:

```text
Claude Code independently becomes final integrator.
Claude Code output is treated as direct merge or deploy authority.
ChatGPT creates a new active Codex task while the previous Codex task is still active.
Multiple agents write overlapping files without a single responsible integrator.
```

## Allowed While Waiting For An Active Task

While an active Codex task is open, ChatGPT and other agents may:

- read status from GitHub fact-source files;
- explain scope to the user;
- prepare an acceptance checklist;
- collect candidate next steps;
- perform read-only review that does not change the active pointer.

They must not:

- create a new active execution task for the same stage;
- reassign the latest pointer to unrelated work;
- broaden the current task without updating its allowed scope and report;
- claim a task is complete before the report and validation exist.

## latest Pointer Requirements

During active execution:

```text
tasks/codex/latest.md: <current task path> / ACTIVE_CODEX_TASK
tasks/claude/latest.md: none / NO_ACTIVE_CLAUDE_TASK
```

If Claude Code is coordinated as an internal subtask:

```text
tasks/claude/latest.md: <bounded Claude task path> / ACTIVE_CLAUDE_TASK
```

After completion:

```text
tasks/codex/latest.md: none / NO_ACTIVE_CODEX_TASK
tasks/claude/latest.md: none / NO_ACTIVE_CLAUDE_TASK
```

## Stop Conditions

Stop and report `BLOCKED` when:

- another active Codex task already exists for the same stage;
- latest pointers disagree with the named task package;
- `CURRENT.md`, `TASKS.md`, or `reports/latest.md` contradict the active execution state and the task does not authorize reconciling that state;
- completing the task requires changing `AI_COLLABORATION_MODE_V4.md`;
- completing the task requires production, database, credential, deployment, or automation authority without explicit authorization.
