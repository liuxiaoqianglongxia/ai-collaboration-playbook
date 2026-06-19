# Codex Latest Task Package

Current task package:

```text
none
```

Current execution status:

```text
NO_ACTIVE_CODEX_TASK
```

Rules:

- This file is the stable GitHub entry point for Codex task packages.
- ChatGPT updates this file when assigning or clearing the next Codex task.
- Codex must not infer tasks from chat history.
- Codex must read the named task package before modifying project files.
- After a task is completed and accepted, this pointer should be cleared back to `none / NO_ACTIVE_CODEX_TASK` unless another task is immediately assigned.
- If this pointer conflicts with `CURRENT.md`, `TASKS.md`, or `reports/latest.md`, stop and report `BLOCKED`.