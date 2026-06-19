# PLAYBOOK-V1.2-DRIVE-FIRST-MAIN-TAG-CLAUDE-FIRST-V1

> Note: this file keeps the previous path `tasks/codex/PLAYBOOK-V1.1-SPEED-MODE-IMPLEMENTATION-V1.md` because it was already the active task pointer. The task content is intentionally corrected before execution. Do not create another active Codex task.

## 0. User-Facing Summary

Upgrade the playbook from a GitHub-heavy V1.1 flow into a faster V1.2 candidate.

It should achieve:

```text
1. Add Drive-first daily workflow: Drive is the daily task/report/material workbench.
2. Keep code out of Drive: WSL/local Git remains the real development workspace.
3. Keep GitHub for main + tags: GitHub is for milestone code, release anchors, production references, and rollback points.
4. Reduce branches: version by tag, branch only when a real review/integration boundary is useful.
5. Make Claude-first / Codex-final real: Codex coordinates Claude Code; the user does not manually assign Claude Code.
6. Update user-facing guide, routing, and personalization candidates for this new model.
```

User instruction stays:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```

## 1. Task Name

```text
PLAYBOOK-V1.2-DRIVE-FIRST-MAIN-TAG-CLAUDE-FIRST-V1
```

## 2. Background

The current V1.1 has passed, but it is still too GitHub-heavy for daily development.

The user wants a fast practical workflow:

```text
Drive handles daily tasks, reports, screenshots, materials, and handoffs.
WSL/local Git handles real code editing and tests.
GitHub main stores milestone code.
GitHub tags store version anchors and release/rollback references.
Claude Code performs safe first-pass engineering work.
Codex coordinates Claude Code, then performs final integration, validation, push, tag, PR when needed, and report.
ChatGPT remains controller and acceptance owner.
```

The key correction:

```text
The user should not directly assign Claude Code in daily flow.
Codex should invoke or coordinate Claude Code inside the active task.
Claude Code is a first-pass worker, not final integrator.
Codex is final integrator.
```

## 3. Read First

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
```

Also inspect templates, checklists, lab notes, archive notes, and historical reports as evidence. Do not treat lab/archive as stable without explicit promotion.

## 4. Allowed Scope

Allowed documentation/template/report changes:

```text
standards/DRIVE_FIRST_WORKFLOW_V1.md
standards/MAIN_ONLY_TAG_VERSIONING_V1.md
standards/CLAUDE_FIRST_CODEX_FINAL_V1.md
standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
templates/drive-project-workbench/00_CURRENT.md
templates/drive-project-workbench/01_TASKS.md
templates/drive-project-workbench/02_DECISIONS.md
templates/drive-project-workbench/03_CODEX_TASK.md
templates/drive-project-workbench/04_CODEX_REPORT.md
templates/drive-project-workbench/05_CHATGPT_ACCEPTANCE.md
templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
templates/CLAUDE_PATCH_WORKER_TASK.md
templates/CODEX_CLAUDE_ORCHESTRATION.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
protocols/GITHUB_AI_COLLABORATION.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
reports/latest.md
reports/codex/playbook-v1-2-drive-first-main-tag-claude-first-v1.md
reports/codex/latest.md
tasks/codex/latest.md
```

Do not modify `AI_COLLABORATION_MODE_V4.md`. Keep V4 role model intact.

## 5. Required Work

### Step 1: Preflight

Run and record:

```bash
git status -sb
git branch --show-current
git fetch origin --prune
git rev-parse origin/main
git log --oneline -12 origin/main
```

Confirm:

```text
repo is liuxiaoqianglongxia/ai-collaboration-playbook
active task is this corrected task
no second active Codex task exists
```

### Step 2: Add Drive-first workflow standard

Create `standards/DRIVE_FIRST_WORKFLOW_V1.md`.

It must say:

```text
Drive is the daily workbench for tasks, reports, screenshots, materials, handoffs, and temporary acceptance notes.
Drive is not the live code workspace.
Code stays in WSL/local Git.
GitHub stays the milestone version source.
```

Include project workbench layout:

```text
Google Drive/AI工作台/<project>/
  00_CURRENT.md
  01_TASKS.md
  02_DECISIONS.md
  03_CODEX_TASK.md
  04_CODEX_REPORT.md
  05_CHATGPT_ACCEPTANCE.md
  screenshots/
  materials/
  exports/
  archive/
```

Define what each file is for.

### Step 3: Add main-only + tag versioning standard

Create `standards/MAIN_ONLY_TAG_VERSIONING_V1.md`.

It must say:

```text
Default: main only.
Use tags for versions.
Use branch only for real review/integration needs.
Do not use branch as version record.
Delete stale merged/closed branches.
Enable automatic branch cleanup when available.
```

Include suggested tags:

```text
dev-ok-YYYYMMDD
pre-prod-YYYYMMDD
prod-YYYYMMDD
rollback-before-YYYYMMDD
```

### Step 4: Add Claude-first / Codex-final standard

Create `standards/CLAUDE_FIRST_CODEX_FINAL_V1.md`.

It must say:

```text
The user does not manually assign Claude Code in normal flow.
Codex coordinates Claude Code inside the active Codex task.
Claude Code can do bounded first-pass engineering work.
Codex reviews Claude output and remains final integrator.
```

Include:

```text
Claude-first task types
Codex-first task types
when Claude may edit files
when Claude should produce patch only
how Codex invokes/coordinates Claude Code
how Codex rejects out-of-scope changes
how Codex summarizes Claude evidence
```

### Step 5: Add maximum practical authorization standard

Create `standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md`.

Intent:

```text
Ordinary work should be allowed by default.
Do not ask the user to approve every small action.
Only a small protected zone requires explicit confirmation.
Project routing profile can override defaults.
```

Keep the protected zone concise and practical.

### Step 6: Add Drive workbench templates

Create templates under:

```text
templates/drive-project-workbench/
```

Each file should be short and usable directly.

### Step 7: Add Claude worker templates

Create:

```text
templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
templates/CLAUDE_PATCH_WORKER_TASK.md
templates/CODEX_CLAUDE_ORCHESTRATION.md
```

Important: templates must make clear that Codex assigns Claude Code and Codex owns final integration.

### Step 8: Update user-facing docs

Update only concise pointers in:

```text
guides/USER_OPERATING_GUIDE_V1.md
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
protocols/GITHUB_AI_COLLABORATION.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
```

Daily use should become:

```text
User talks to ChatGPT.
ChatGPT writes/reads Drive daily workbench.
Codex reads Drive task.
Codex coordinates Claude Code first-pass where useful.
Codex finalizes in WSL/local Git.
Codex pushes GitHub main at milestone.
Codex creates tag when release/rollback anchor is needed.
ChatGPT validates from Drive + GitHub + runtime facts depending on stage.
```

Do not say the user should directly run Claude Code in daily workflow.

### Step 9: Update personalization candidate

Revise candidate so it is trigger-based and not too heavy:

```text
normal chat: no project mode
project terms trigger project controller mode
ChatGPT is controller
Codex is executor/final integrator
Claude Code is first-pass worker coordinated by Codex
Drive daily workbench / GitHub milestone source
```

### Step 10: Update reports/latest.md

Mark this as a candidate upgrade, not final freeze:

```text
PLAYBOOK_OPERATIONAL_BASELINE_V1.2_CANDIDATE
Drive-first / main+tag / Claude-first layer: PASS if successful
```

Do not erase V1.1 history.

### Step 11: Report and close

Write:

```text
reports/codex/playbook-v1-2-drive-first-main-tag-claude-first-v1.md
```

Update:

```text
reports/codex/latest.md
tasks/codex/latest.md
```

After completion, clear:

```text
tasks/codex/latest.md -> none / NO_ACTIVE_CODEX_TASK
```

## 6. Validation

Run and record:

```bash
git status -sb
git branch --show-current
git diff --name-only origin/main...HEAD
git diff --stat origin/main...HEAD
git diff --check origin/main...HEAD
```

Content checks:

```bash
grep -R "Drive-first\|Google Drive\|AI工作台" -n README.md CHATGPT_START_HERE.md guides standards templates reports/latest.md || true
grep -R "main-only\|tag\|MAIN_ONLY_TAG" -n README.md CHATGPT_START_HERE.md guides standards reports/latest.md || true
grep -R "Claude-first\|Codex-final\|first-pass" -n README.md CHATGPT_START_HERE.md guides standards templates reports/latest.md || true
grep -R "用户.*Claude Code\|directly assign Claude" -n README.md CHATGPT_START_HERE.md guides standards templates || true
```

The last grep is to catch wrong wording that implies the user directly assigns Claude Code.

## 7. Acceptance Criteria

PASS only if:

```text
Drive-first daily workflow standard exists.
Main-only + tag versioning standard exists.
Claude-first / Codex-final standard exists.
Maximum practical authorization standard exists.
Drive workbench templates exist.
Claude worker templates exist.
User-facing docs explain Drive daily / GitHub milestone.
No doc tells the user to directly assign Claude Code in normal flow.
reports/latest.md records V1.2 candidate without erasing V1.1 history.
tasks/codex/latest.md is cleared after completion.
V4 four-piece role model remains intact.
```

PARTIAL PASS if most docs exist but personalization/pro-review needs follow-up.

FAIL if code is placed in Drive, GitHub is removed as code/version source, Claude Code becomes final integrator, or V4 is rewritten.

BLOCKED if repo identity or active task state cannot be verified.

## 8. Report Format

```text
# PLAYBOOK-V1.2-DRIVE-FIRST-MAIN-TAG-CLAUDE-FIRST-V1 Codex Report

## 1. Conclusion
PASS / PARTIAL PASS / FAIL / BLOCKED

## 2. Repository

## 3. User-Facing Result

## 4. Files Read

## 5. Files Changed

## 6. Drive-First Daily Workflow

## 7. Main-Only Tag Versioning

## 8. Claude-First Codex-Final

## 9. Maximum Practical Authorization

## 10. Templates Added

## 11. Personalization Candidate

## 12. Validation

## 13. Remaining Issues

## 14. Next Step
```

## 9. User Instruction

The user should only need to send Codex:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```