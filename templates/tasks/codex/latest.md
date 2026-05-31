# Codex Latest Task Package

Current task package:

```text
<tasks/codex/TASK-ID.md or none>
```

Current execution status:

```text
NO_ACTIVE_CODEX_TASK
```

Rules:

- This file is the stable GitHub entry point for Codex task packages.
- ChatGPT updates this file when assigning the next Codex task.
- Codex must not infer tasks from chat history.
- If this pointer conflicts with `CURRENT.md` / `TASKS.md` / `reports/latest.md`, stop and report `BLOCKED`.
