# PLAYBOOK-V1.1-DOGFOOD-AND-ROLLOUT-PREFLIGHT-V1 Task Package Snapshot

## Task Name

```text
PLAYBOOK-V1.1-DOGFOOD-AND-ROLLOUT-PREFLIGHT-V1
```

## Goal

Extend PR #6 so the playbook repository dogfoods `TASK-PACKAGE-REGISTRY-V1.1`, creates real Codex and Claude Code task pointers, and documents rollout wave 1 without changing any business project.

## Allowed Scope

```text
tasks/
reports/claude/
rollouts/TASK_PACKAGE_REGISTRY_ROLLOUT_WAVE1.md
reports/codex/playbook-v1-1-dogfood-and-rollout-preflight-v1.md
reports/chatgpt/task-packages/PLAYBOOK-V1.1-DOGFOOD-AND-ROLLOUT-PREFLIGHT-V1.md
README.md
AI_AGENT_ONBOARDING.md
NEW_PROJECT_BOOTSTRAP.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
reports/latest.md
reports/codex/latest.md
reports/chatgpt/task-packages/TASK-PACKAGE-REGISTRY-V1-1.md
```

## Forbidden Actions

```text
Do not merge PR #6.
Do not write directly to main.
Do not force push.
Do not modify AI_COLLABORATION_MODE_V4.md.
Do not modify lab/, archive/, or whitepapers/.
Do not modify business projects.
Do not deploy.
Do not modify databases.
Do not modify secrets.
Do not add automation.
```

## Acceptance Criteria

```text
PR #6 remains open and unmerged.
Playbook has a live tasks/ registry.
Codex latest points to merge closeout and waits for ChatGPT acceptance.
Claude latest points to a read-only PR #6 review task.
reports/claude/latest.md exists.
Rollout wave 1 exists and does not modify business projects.
V4 core remains unchanged.
High-risk directories remain unchanged.
```

## Stop Conditions

```text
PR #6 branch is not writable.
Repository routing is wrong.
Task requires modifying V4 core.
Task requires modifying business projects, deployment, database, secrets, or automation.
```

## Next Plan

Run Claude Code read-only review from `tasks/claude/latest.md`. After Claude report exists, ChatGPT should perform independent PR #6 acceptance.
