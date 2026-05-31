# TASK-PACKAGE-REGISTRY-V1.1 Task Package Snapshot

## Task Name

```text
PLAYBOOK-TASK-PACKAGE-REGISTRY-V1.1
```

## Goal

Add a project-level task-package registry standard and copyable templates to `liuxiaoqianglongxia/ai-collaboration-playbook` as a candidate layer for `PLAYBOOK_OPERATIONAL_BASELINE_V1.1`.

The goal is to preserve V4 while adding stable GitHub task entry points for Codex and Claude Code.

## Allowed Scope

```text
standards/TASK_PACKAGE_REGISTRY_V1_1.md
templates/TASK_PACKAGE_REGISTRY_BOOTSTRAP_TASK.md
templates/tasks/
templates/reports/chatgpt/task-packages/
checklists/TASK_PACKAGE_REGISTRY_REVIEW.md
reports/codex/task-package-registry-v1-1.md
reports/chatgpt/task-packages/TASK-PACKAGE-REGISTRY-V1-1.md
README.md
AI_AGENT_ONBOARDING.md
NEW_PROJECT_BOOTSTRAP.md
templates/README.md
checklists/README.md
protocols/GITHUB_AI_COLLABORATION.md
reports/latest.md
reports/codex/latest.md
```

## Forbidden Actions

```text
Do not modify business repositories.
Do not modify AI_COLLABORATION_MODE_V4.md.
Do not modify lab/, archive/, whitepapers/, or modules/.
Do not add project-specific business content to generic templates.
Do not add deployment, database, credential, secret, or automation authority.
Do not force push.
Do not merge the PR.
Do not write directly to main.
```

## Acceptance Criteria

```text
Repository is correct.
Independent branch is used.
V1.1 standard is added.
templates/tasks/ structure is added.
templates/reports/chatgpt/task-packages/ structure is added.
Registry review checklist is added.
Protocol, onboarding, bootstrap, template indexes, and latest reports are updated.
reports/latest.md uses V1.1 candidate status.
AI_COLLABORATION_MODE_V4.md is unchanged.
High-risk directories are unchanged.
PR is created and left unmerged.
```

## Stop Conditions

```text
Wrong repository.
Existing stable registry conflict.
Need to modify V4 core.
Need to modify lab/, archive/, whitepapers/, or modules/.
Need production, database, credentials, or automation.
Unseparable local changes.
```

## Next Plan

ChatGPT should perform independent read-only PR review. If accepted, a separate merge and closeout task can promote the candidate to stable V1.1.

## Dogfood Supplement

`PLAYBOOK-V1.1-DOGFOOD-AND-ROLLOUT-PREFLIGHT-V1` extends PR #6 so the playbook repository uses the registry it defines:

```text
tasks/README.md
tasks/codex/latest.md
tasks/codex/PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1.md
tasks/claude/latest.md
tasks/claude/PLAYBOOK-PR6-READONLY-REVIEW-V1.md
reports/claude/latest.md
rollouts/TASK_PACKAGE_REGISTRY_ROLLOUT_WAVE1.md
```

This supplement does not merge PR #6. It prepares the review path: Claude Code read-only review first, then ChatGPT independent acceptance, then a separate Codex merge closeout only after explicit PASS.
