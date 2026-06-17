# PLAYBOOK-V1.2-SELF-DOGFOOD-STABLE-FREEZE-V1

## 0. User-Facing Summary

Use `ai-collaboration-playbook` itself as the test project and freeze V1.2 as the current stable operating baseline if the self-test passes.

It should achieve:

```text
1. Dogfood V1.2 inside this playbook repository.
2. Verify Drive-first / main+tag / Claude-first / Codex-final is understandable and internally consistent.
3. Promote V1.2 from candidate wording to stable wording if checks pass.
4. Produce final Personal Details and Custom Instructions content for the user.
5. Keep the workflow fast: direct main for this documentation-only freeze, no PR unless a blocking reason appears.
```

User instruction:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```

## 1. Task Name

```text
PLAYBOOK-V1.2-SELF-DOGFOOD-STABLE-FREEZE-V1
```

## 2. Background

V1.2 candidate has already been implemented and pushed on main.

Current status:

```text
PLAYBOOK_OPERATIONAL_BASELINE_V1.2_CANDIDATE
PASS
```

The user does not want to wait for another business project before making the playbook usable. This repository is itself a project and can serve as the immediate test bed.

Core user intent:

```text
Stop treating GitHub mechanics as the main work.
Use Drive as daily workbench, not code workspace.
Use GitHub main and tags for milestones.
Use Claude Code as first-pass worker coordinated by Codex.
Keep Codex as final integrator.
Make the final user instructions usable now.
```

## 3. Current Facts To Read

Read first:

```text
reports/latest.md
reports/codex/latest.md
reports/codex/playbook-v1-2-drive-first-main-tag-claude-first-v1.md
CHATGPT_START_HERE.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
standards/DRIVE_FIRST_WORKFLOW_V1.md
standards/MAIN_ONLY_TAG_VERSIONING_V1.md
standards/CLAUDE_FIRST_CODEX_FINAL_V1.md
standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/drive-project-workbench/00_CURRENT.md
templates/drive-project-workbench/01_TASKS.md
templates/drive-project-workbench/02_DECISIONS.md
templates/drive-project-workbench/03_CODEX_TASK.md
templates/drive-project-workbench/04_CODEX_REPORT.md
templates/drive-project-workbench/05_CHATGPT_ACCEPTANCE.md
templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
templates/CLAUDE_PATCH_WORKER_TASK.md
templates/CODEX_CLAUDE_ORCHESTRATION.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/claude/latest.md
```

## 4. Allowed Scope

This is a documentation and self-test freeze task.

Allowed changes:

```text
reports/latest.md
README.md
CHATGPT_START_HERE.md
guides/USER_OPERATING_GUIDE_V1.md
AI_AGENT_ONBOARDING.md
protocols/GITHUB_AI_COLLABORATION.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
reports/chatgpt/personalization/PERSONALIZATION_FINAL_V1_2.md
reports/codex/playbook-v1-2-self-dogfood-stable-freeze-v1.md
reports/codex/latest.md
tasks/codex/latest.md
reports/codex/self-test/playbook-v1-2-drive-workbench/
```

Do not modify `AI_COLLABORATION_MODE_V4.md`.

Only adjust existing V1.2 standards if a clear inconsistency prevents freezing. If that happens, record it clearly in the report.

## 5. Required Work

### Step 1: Preflight

Run and record:

```bash
git status -sb
git branch --show-current
git fetch origin --prune
git rev-parse origin/main
git log --oneline -12 origin/main
git tag --list | grep -E 'dev-ok-20260601|v1.2|PLAYBOOK' || true
```

Confirm:

```text
repo is liuxiaoqianglongxia/ai-collaboration-playbook
active Codex task is this task
no second active Codex task exists
current branch is main or a clearly documented branch
```

### Step 2: Self-dogfood V1.2 using this repository

Create a self-test workbench under:

```text
reports/codex/self-test/playbook-v1-2-drive-workbench/
```

Use the Drive workbench templates to create these files:

```text
00_CURRENT.md
01_TASKS.md
02_DECISIONS.md
03_CODEX_TASK.md
04_CODEX_REPORT.md
05_CHATGPT_ACCEPTANCE.md
```

This folder is a repository-local simulation of the Drive daily workbench. It proves the template is usable without requiring the real Google Drive path during this freeze task.

The self-test should describe:

```text
project: ai-collaboration-playbook
mode: V1.2 self-dogfood
current task: stable freeze
execution lane: one active Codex task
Claude Code: coordinated by Codex, not by user
GitHub: main + tag milestone layer
Drive: daily workbench concept represented by the self-test folder
```

### Step 3: Verify key V1.2 rules

Check and record whether the docs say:

```text
Drive is daily workbench, not live code workspace.
GitHub is milestone source and tag anchor.
Code stays in WSL/local Git.
Claude Code is coordinated by Codex.
User does not directly assign Claude Code in normal flow.
Codex is final integrator.
V4 role model remains intact.
Ordinary chat does not trigger project controller mode.
```

### Step 4: Promote V1.2 wording to stable if checks pass

If the self-test passes, update active entry docs from candidate to stable:

```text
PLAYBOOK_OPERATIONAL_BASELINE_V1.2
```

Keep V1.1 as historical stable baseline. Do not erase history.

Expected `reports/latest.md` result:

```text
status: PLAYBOOK_OPERATIONAL_BASELINE_V1.2
conclusion: PASS
V1.1 history retained
V1.2 stable layer: PASS
current pointers: none / NO_ACTIVE
```

Update README / START_HERE / user guide / onboarding only enough to remove confusing candidate language.

### Step 5: Finalize Personal Details and Custom Instructions

Create or update:

```text
reports/chatgpt/personalization/PERSONALIZATION_FINAL_V1_2.md
```

It must include:

```text
Personal Details final copy
Custom Instructions final copy
Codex-side execution note
New project / new chat start prompt
```

Rules:

```text
normal chat does not enter project controller mode
project terms trigger controller mode
Drive daily workbench / GitHub milestone source are both represented
Codex is executor and final integrator
Claude Code is first-pass worker coordinated by Codex
Google Drive is not a fifth agent
```

### Step 6: Update Pro review entry

Update Pro entry so tomorrow's Pro session audits the final V1.2 stable baseline, not only candidate.

Pro should still be allowed to find problems, but V1.2 should be usable immediately unless Pro finds blockers.

### Step 7: Tag stable result

After successful validation and commit, create and push a stable tag if local tooling permits:

```text
playbook-v1.2-stable-20260601
```

If tag creation is blocked, report it as a remaining issue, but do not fail the entire task if docs and validation pass.

### Step 8: Report and close

Write:

```text
reports/codex/playbook-v1-2-self-dogfood-stable-freeze-v1.md
```

Update:

```text
reports/codex/latest.md
tasks/codex/latest.md
```

Clear:

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
grep -R "PLAYBOOK_OPERATIONAL_BASELINE_V1.2" -n reports/latest.md README.md CHATGPT_START_HERE.md guides/USER_OPERATING_GUIDE_V1.md reports/chatgpt/personalization || true
grep -R "V1.2_CANDIDATE" -n reports/latest.md README.md CHATGPT_START_HERE.md guides/USER_OPERATING_GUIDE_V1.md reports/chatgpt/personalization || true
grep -R "Drive.*live code\|live code workspace" -n standards guides README.md CHATGPT_START_HERE.md || true
grep -R "Claude Code.*directly assign\|用户.*Claude Code" -n README.md CHATGPT_START_HERE.md guides standards templates reports/chatgpt || true
grep -R "Claude.*Codex.*final\|Codex.*final" -n standards guides README.md CHATGPT_START_HERE.md reports/latest.md || true
```

The `V1.2_CANDIDATE` grep may still find historical report references. It must not remain as the current status in active entry docs.

## 7. Acceptance Criteria

PASS only if:

```text
V1.2 self-dogfood workbench files exist.
V1.2 is promoted to current stable status in active entry docs.
V1.1 history remains visible.
Drive-first / main+tag / Claude-first / Codex-final rules remain intact.
No normal-flow doc tells user to directly assign Claude Code.
Personalization final V1.2 copy exists.
Pro review entry points to final V1.2 baseline.
reports/codex/latest.md points to this report.
tasks/codex/latest.md is cleared after completion.
V4 remains unchanged.
```

PARTIAL PASS if all docs are correct but stable tag creation fails.

FAIL if Drive is treated as live code workspace, GitHub milestone role is removed, Claude Code becomes final integrator, or V4 is rewritten.

BLOCKED if repo identity or active task state cannot be verified.

## 8. Report Format

```text
# PLAYBOOK-V1.2-SELF-DOGFOOD-STABLE-FREEZE-V1 Codex Report

## 1. Conclusion
PASS / PARTIAL PASS / FAIL / BLOCKED

## 2. Repository

## 3. User-Facing Result

## 4. Files Read

## 5. Self-Dogfood Workbench

## 6. Stable Promotion

## 7. Personalization Final

## 8. Pro Review Entry

## 9. Validation

## 10. Tag Result

## 11. Remaining Issues

## 12. Next Step
```

## 9. User Instruction

The user should only need to send Codex:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```