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

- This file is the stable GitHub entry point for Claude Code review or analysis tasks.
- ChatGPT updates this file when assigning or clearing a Claude Code task.
- Claude Code must not infer tasks from chat history.
- Claude Code remains read-only unless a task explicitly allows a narrow report write.
- Claude Code does not replace Codex as final integrator.
- After a task is completed and accepted, this pointer should be cleared back to `none / NO_ACTIVE_CLAUDE_TASK` unless another task is immediately assigned.