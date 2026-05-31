# Codex Latest Task Package

Current task package:

```text
tasks/codex/PLAYBOOK-V1.1-EXECUTION-LANE-AND-CLAUDE-STABILIZATION-V1.md
```

Current execution status:

```text
ACTIVE_CODEX_TASK
```

Rules:

- This file is the stable GitHub entry point for Codex task packages in this playbook repository.
- ChatGPT updates this file when assigning or clearing the next Codex task.
- Codex must not infer tasks from chat history.
- Codex must read the named task package before modifying project files.
- After a task is completed and accepted, this pointer should be cleared back to `none / NO_ACTIVE_CODEX_TASK` unless another task is immediately assigned.
- If this pointer conflicts with `TASKS.md` or `reports/latest.md`, stop and report `BLOCKED`.

Previous completed task evidence:

```text
reports/codex/playbook-v1-1-local-validation-v1.md
reports/chatgpt/task-packages/PLAYBOOK-V1.1-OPERATIONAL-CLEANUP-V1.md
```