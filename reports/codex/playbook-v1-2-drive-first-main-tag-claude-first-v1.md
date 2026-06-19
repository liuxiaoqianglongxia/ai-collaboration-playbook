# PLAYBOOK-V1.2-DRIVE-FIRST-MAIN-TAG-CLAUDE-FIRST-V1 Codex Report

## 1. Conclusion

PASS.

The active task content was `PLAYBOOK-V1.2-DRIVE-FIRST-MAIN-TAG-CLAUDE-FIRST-V1`, even though the active task path remained `tasks/codex/PLAYBOOK-V1.1-SPEED-MODE-IMPLEMENTATION-V1.md`.

This task implemented the V1.2 candidate operating layer:

```text
Drive-first daily workflow
main-only + tag versioning
Claude-first-pass / Codex-final execution
maximum practical authorization
Drive workbench templates
Claude worker templates
user-facing guide and personalization updates
```

`AI_COLLABORATION_MODE_V4.md` was read and left unchanged.

## 2. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
local_path: /Users/liuxiaoqiang/code/ai-collaboration-playbook
branch: main
origin/main_before_work: b1dcbdfdc487fc599d6f897557cf292322612c8a
active_task: tasks/codex/PLAYBOOK-V1.1-SPEED-MODE-IMPLEMENTATION-V1.md
active_task_content: PLAYBOOK-V1.2-DRIVE-FIRST-MAIN-TAG-CLAUDE-FIRST-V1
```

Preflight confirmed:

```text
repo remote: https://github.com/liuxiaoqianglongxia/ai-collaboration-playbook.git
current branch: main
working tree before edits: clean
tasks/codex/latest.md: ACTIVE_CODEX_TASK
tasks/claude/latest.md: NO_ACTIVE_CLAUDE_TASK
no second active Codex task was created
```

## 3. User-Facing Result

The playbook now has a V1.2 candidate layer:

```text
Drive handles daily tasks, reports, screenshots, materials, handoffs, and temporary acceptance notes.
Drive does not replace GitHub as durable milestone fact source.
WSL/local Git remains the real code workspace.
GitHub main stores milestone code and collaboration facts.
GitHub tags store version, production, and rollback anchors.
Claude Code performs bounded first-pass support only when Codex coordinates it.
Codex remains final integrator, validator, push/tag/PR/report owner.
```

## 4. Files Read

```text
reports/latest.md
reports/codex/latest.md
reports/codex/playbook-v1-1-process-speed-research-v1.md
CHATGPT_START_HERE.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
templates/PROJECT_ROUTING_PROFILE.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/claude/latest.md
templates/CODEX_TASK_PACKAGE.md
templates/CLAUDE_CODE_READONLY_ANALYSIS_TASK.md
templates/tasks/claude/_template.md
```

## 5. Files Changed

New standards:

```text
standards/DRIVE_FIRST_WORKFLOW_V1.md
standards/MAIN_ONLY_TAG_VERSIONING_V1.md
standards/CLAUDE_FIRST_CODEX_FINAL_V1.md
standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md
```

New templates:

```text
templates/drive-project-workbench/00_CURRENT.md
templates/drive-project-workbench/01_TASKS.md
templates/drive-project-workbench/02_DECISIONS.md
templates/drive-project-workbench/03_CODEX_TASK.md
templates/drive-project-workbench/04_CODEX_REPORT.md
templates/drive-project-workbench/05_CHATGPT_ACCEPTANCE.md
templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
templates/CLAUDE_PATCH_WORKER_TASK.md
templates/CODEX_CLAUDE_ORCHESTRATION.md
```

Updated docs and reports:

```text
README.md
CHATGPT_START_HERE.md
guides/USER_OPERATING_GUIDE_V1.md
AI_AGENT_ONBOARDING.md
protocols/GITHUB_AI_COLLABORATION.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
reports/latest.md
reports/codex/latest.md
tasks/codex/latest.md
reports/codex/playbook-v1-2-drive-first-main-tag-claude-first-v1.md
```

## 6. Drive-First Daily Workflow

Added `standards/DRIVE_FIRST_WORKFLOW_V1.md`.

It defines:

```text
Drive daily workbench purpose
Google Drive/AI工作台/<project>/ layout
00_CURRENT through 05_CHATGPT_ACCEPTANCE file purposes
screenshots/materials/exports/archive purposes
Drive-to-GitHub sync triggers
Drive is not live code workspace
Drive is not durable milestone fact source
```

## 7. Main-Only Tag Versioning

Added `standards/MAIN_ONLY_TAG_VERSIONING_V1.md`.

It defines:

```text
default main only
tags as version anchors
branches only for review/integration boundaries
branches not used as version records
stale merged/closed branch cleanup
suggested tags: dev-ok, pre-prod, prod, rollback-before
```

Expected task tag after commit:

```text
dev-ok-20260601
```

## 8. Claude-First Codex-Final

Added `standards/CLAUDE_FIRST_CODEX_FINAL_V1.md`.

It defines:

```text
Claude-first task types
Codex-first task types
when Claude may edit files
when Claude should produce patch only
how Codex invokes or coordinates Claude Code
how Codex rejects out-of-scope changes
how Codex summarizes Claude evidence
```

Codex coordinated Claude Code during this task as a read-only first-pass reviewer:

```text
mode: claude -p with Read/Grep/Glob tools
scope: active task and relevant docs
write access: none requested
Codex accepted: Drive-to-GitHub sync rule, Drive not fact source, WSL/local Git boundary, concise protected zone, tag/branch distinction, V4 unchanged declarations
Codex rejected: no change that would make Drive final source, Claude final integrator, or optional tools default members
```

## 9. Maximum Practical Authorization

Added `standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md`.

It defines:

```text
ordinary work allowed by default inside active task and routing profile
protected zone requiring explicit confirmation
project routing profile overrides
approval pattern
maximum practical authorization is not blanket authorization
```

Protected zone includes production, database, secrets, process killing, destructive cleanup, force push, automation publish chains, access control, cross-repository writes, and private data exposure.

## 10. Templates Added

Drive workbench templates:

```text
templates/drive-project-workbench/00_CURRENT.md
templates/drive-project-workbench/01_TASKS.md
templates/drive-project-workbench/02_DECISIONS.md
templates/drive-project-workbench/03_CODEX_TASK.md
templates/drive-project-workbench/04_CODEX_REPORT.md
templates/drive-project-workbench/05_CHATGPT_ACCEPTANCE.md
```

Claude orchestration templates:

```text
templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
templates/CLAUDE_PATCH_WORKER_TASK.md
templates/CODEX_CLAUDE_ORCHESTRATION.md
```

All new templates are short and directly usable.

## 11. Personalization Candidate

Updated `reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md`.

Key changes:

```text
ordinary chat does not trigger project controller mode
project terms trigger project controller mode
ChatGPT remains controller
Codex remains executor and final integrator
Claude Code becomes first-pass worker coordinated by Codex
Drive daily workbench and GitHub milestone source are both represented
```

## 12. Validation

Preflight commands run:

```text
git status -sb
git branch --show-current
git fetch origin --prune
git rev-parse origin/main
git log --oneline -12 origin/main
```

Preflight result:

```text
branch: main
origin/main: b1dcbdfdc487fc599d6f897557cf292322612c8a
repo identity: liuxiaoqianglongxia/ai-collaboration-playbook
active Codex task: confirmed
second active Codex task: none created
Claude task pointer: none / NO_ACTIVE_CLAUDE_TASK
```

Content checks run:

```text
grep -R "Drive-first\|Google Drive\|AI工作台" -n README.md CHATGPT_START_HERE.md guides standards templates reports/latest.md || true
grep -R "main-only\|tag\|MAIN_ONLY_TAG" -n README.md CHATGPT_START_HERE.md guides standards reports/latest.md || true
grep -R "Claude-first\|Codex-final\|first-pass" -n README.md CHATGPT_START_HERE.md guides standards templates reports/latest.md || true
grep -R "用户.*Claude Code\|directly assign Claude" -n README.md CHATGPT_START_HERE.md guides standards templates || true
```

Content check result:

```text
Drive-first terms present: yes
main/tag terms present: yes
Claude-first/Codex-final or first-pass terms present: yes
wrong user-direct-Claude wording: no matches
```

Diff whitespace check:

```text
git diff --check
result: PASS
```

Final post-commit validation to run before push:

```text
git status -sb
git branch --show-current
git diff --name-only origin/main...HEAD
git diff --stat origin/main...HEAD
git diff --check origin/main...HEAD
```

## 13. Remaining Issues

No blocking issues.

Known candidate-stage considerations:

```text
Drive-first requires each project to define sync discipline so Drive and GitHub do not diverge.
Production tag names may need project-specific release conventions.
Claude Code write-capable workflows should remain bounded and verified by Codex.
```

## 14. Next Step

```text
1. Commit and push main.
2. Create and push tag dev-ok-20260601.
3. ChatGPT should do read-only acceptance from GitHub facts.
4. Keep V1.2 as candidate until accepted or revised by ChatGPT/Pro review.
```
