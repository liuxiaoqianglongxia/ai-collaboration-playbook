# Claude Code Latest Task Package

Current task package:

```text
none
```

Current execution status:

```text
NO_ACTIVE_CLAUDE_TASK
```

Rules:

- This file is the stable GitHub entry point for Claude Code review tasks in this playbook repository.
- ChatGPT updates this file when assigning or clearing a Claude Code task.
- Claude Code must not infer tasks from chat history.
- Claude Code may edit and run tests when the task allows engineering execution; restrict it to read-only only when the task explicitly says read-only audit.
- Claude Code does not replace Codex as final integrator.
- After a task is completed and accepted, this pointer should be cleared back to `none / NO_ACTIVE_CLAUDE_TASK` unless another task is immediately assigned.

Previous completed task evidence:

```text
reports/claude/playbook-pr6-readonly-review-v1.md
reports/chatgpt/task-packages/PLAYBOOK-V1.1-OPERATIONAL-CLEANUP-V1.md
```
