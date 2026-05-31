# Codex Latest Task Package

Current task package:

```text
tasks/codex/PLAYBOOK-V1.1-PROCESS-SPEED-RESEARCH-V1.md
```

Current execution status:

```text
ACTIVE_CODEX_TASK
```

Rules:

- Codex must execute only the named task package.
- Codex must not infer scope from chat history.
- After completion, Codex must update `reports/codex/latest.md` and clear this pointer back to `none / NO_ACTIVE_CODEX_TASK`.
- If this pointer conflicts with `reports/latest.md`, stop and report `BLOCKED`.

Previous completed task evidence:

```text
reports/codex/playbook-v1-1-final-user-guide-routing-pro-review-v1.md
tasks/codex/PLAYBOOK-V1.1-FINAL-USER-GUIDE-ROUTING-PRO-REVIEW-V1.md
reports/codex/playbook-v1-1-execution-lane-and-claude-stabilization-v1.md
reports/codex/playbook-v1-1-local-validation-v1.md
```