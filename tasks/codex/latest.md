# Codex Latest Task Package

Current task package:

```text
tasks/codex/PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1.md
```

Current execution status:

```text
READY_AFTER_CHATGPT_ACCEPTANCE
```

Rules:

- This file is the stable GitHub entry point for Codex task packages in this playbook repository.
- ChatGPT updates this file when assigning the next Codex task.
- Codex must not infer tasks from chat history.
- Codex must not execute this merge closeout task until ChatGPT gives explicit independent PASS for PR #6.
- If this pointer conflicts with `TASKS.md` or `reports/latest.md`, stop and report `BLOCKED`.
