# PLAYBOOK-V1.1-FINAL-USER-GUIDE-ROUTING-PRO-REVIEW-V1

## 0. User-Facing Summary

This is the final productization task before freezing the user's Personal Details and Custom Instructions.

It should achieve:

```text
1. Produce a user-facing operating guide so the user knows how to use V1.1 without reading long task packages.
2. Add routing and extensibility guidance so different projects can reuse the common playbook without becoming rigid.
3. Prepare a Pro review entry for a future ChatGPT Pro deep review pass.
4. Prepare candidate Personal Details and Custom Instructions, but do not treat them as final until ChatGPT accepts this task.
```

The user-facing instruction should stay simple:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```

Detailed scope and validation live in this file.

## 1. Task Name

```text
PLAYBOOK-V1.1-FINAL-USER-GUIDE-ROUTING-PRO-REVIEW-V1
```

## 2. Background

`PLAYBOOK_OPERATIONAL_BASELINE_V1.1` is stable on main after PR #7.

Current stable capabilities include:

```text
TASK_PACKAGE_REGISTRY_V1_1
EXECUTION_LANE_MANAGEMENT_V1
CLAUDE_CODE_COORDINATION_V1
USER_FACING_TASK_ANNOUNCEMENT template
```

The user now needs the playbook to be understandable by:

```text
1. The user as a daily operating manual.
2. New ChatGPT sessions.
3. Codex sessions.
4. Project-specific repositories adopting the playbook.
5. A future ChatGPT Pro deep-review session.
```

The user also needs final Personal Details and Custom Instructions, but those should be produced as candidates first and finalized by ChatGPT after this task is accepted.

## 3. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
base branch: main
recommended branch: docs/playbook-v1-1-final-user-guide-routing-pro-review-v1
```

## 4. Current Facts To Read

Read before changing anything:

```text
CHATGPT_START_HERE.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
templates/CODEX_TASK_PACKAGE.md
templates/CLAUDE_CODE_READONLY_ANALYSIS_TASK.md
templates/tasks/codex/_template.md
templates/tasks/claude/_template.md
checklists/TASK_PACKAGE_REGISTRY_REVIEW.md
checklists/CODEX_BEFORE_EXECUTION_CHECK.md
checklists/CLAUDE_CODE_HARDENING.md
```

Also inspect, read-only only:

```text
lab/
archive/
whitepapers/
reports/codex/
reports/claude/
```

Use them only as evidence. Do not wholesale promote experiments.

## 5. Allowed Scope

Codex may add or update documentation only in these areas:

```text
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
NEW_PROJECT_BOOTSTRAP.md
standards/
protocols/
templates/
checklists/
docs/
guides/
reports/codex/
reports/chatgpt/
reports/latest.md
tasks/codex/latest.md
```

Recommended deliverables:

```text
guides/USER_OPERATING_GUIDE_V1.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
templates/PROJECT_ROUTING_PROFILE.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
reports/codex/playbook-v1-1-final-user-guide-routing-pro-review-v1.md
```

If the repository has a better existing location, use it and explain the choice.

## 6. Forbidden Scope

Do not modify:

```text
AI_COLLABORATION_MODE_V4.md
business repositories
production systems
databases
credentials or secrets
automation publish chains
```

Avoid modifying these unless only adding a pointer is explicitly necessary:

```text
lab/
archive/
whitepapers/
modules/
```

Do not:

```text
force push
merge your own PR
promote Hermes, Qwen, MCP, heartbeat, automation, or subagents into the default four-piece model
make Claude Code the final integrator
create a V0.3 redesign
turn the playbook into a rigid one-size-fits-all process
```

## 7. Required Work

### Step 1: Preflight

Run and record:

```bash
git status -sb
git branch --show-current
git remote -v
git fetch origin --prune
git rev-parse origin/main
git log --oneline -12 origin/main
```

Confirm:

```text
repo is liuxiaoqianglongxia/ai-collaboration-playbook
there is no active Codex or Claude Code task before assigning this task locally
the task is running on a branch, not directly on main
```

### Step 2: Create user operating guide

Create a guide for the user, not for agents only.

The guide must explain:

```text
What the playbook is.
What the user needs to say in daily use.
What ChatGPT does behind the scenes.
What Codex does.
What Claude Code does.
When Qwen / Hermes / MCP / automation may enter.
Why GitHub is the fact source but not the user's daily burden.
What a task assignment should look like.
What a Codex report should look like.
How to know whether a task is active, done, blocked, or waiting.
What not to do.
```

Style requirements:

```text
Chinese-first.
Direct and practical.
No excessive theory.
Use diagrams in text form where useful.
Include a simple flow diagram that ChatGPT can later turn into an image/PDF.
Do not require the user to read long task packages for daily use.
```

### Step 3: Add routing and extensibility guidance

Create a stable routing/extensibility standard that defines:

```text
Universal layer: applies to all projects.
Project layer: each project keeps its own facts and local rules.
Execution lane: one active execution lane per stage.
Tool lane: optional tools used inside an active task.
Research lane: read-only investigation before promotion.
High-risk lane: production/deployment/database/credential work requiring separate authorization.
```

Include a routing matrix for:

```text
ChatGPT direct work
Codex execution
Claude Code review / analysis
Qwen or other cheap model batch work
Hermes project-specific automation or historical tool use
GitHub facts
Pro deep review
```

Required boundary:

```text
Optional tools can be routed in, but they are not default members unless the project fact source explicitly says so.
The playbook must remain flexible, not rigid.
General standards stay general. Project-specific facts stay in the project repository.
```

### Step 4: Deep research on Codex coordinating Claude Code

Research from local repository evidence and available public/official docs if internet is available.

Focus on practical operating patterns:

```text
Can Codex call Claude Code directly from local shell?
Can Codex use Claude Code in non-interactive mode?
Can Codex drive Claude Code interactive mode safely?
What needs a TTY or human confirmation?
What can be done with file-based handoff instead?
What is safe to standardize now?
What should stay experimental?
```

If live Claude Code is available locally, Codex may run a narrow read-only experiment:

```text
version / help check
read-only review of a markdown diff
no repository writes by Claude Code unless explicitly allowed
no secrets
no auth changes
no production commands
```

If live Claude Code is not available or requires unsafe interaction, do not block. Document the limitation and propose a safe future experiment.

### Step 5: Create Pro review entry

Create a single file for tomorrow's ChatGPT Pro deep review.

It should include:

```text
Current stable status.
Read order.
What has been solved.
What still needs higher-level review.
Questions for Pro reasoning.
Known uncertainties from current controller.
What must not be changed casually.
How to judge whether the playbook is stable enough to freeze Personal Details and Custom Instructions.
```

This file should be usable as the first message or source reference for a future Pro review session.

### Step 6: Create personalization candidate

Create a candidate file with two sections:

```text
Personal Details Candidate
Custom Instructions Candidate
```

Requirements:

```text
Keep it short enough for ChatGPT personalization fields.
Include only stable general rules.
Do not include temporary PR numbers unless truly needed.
Do not include business project facts.
Do not overfit to ai-collaboration-playbook internals.
Mention V1.1 stable baseline and GitHub fact-source rule.
Mention one-active-execution-lane rule.
Mention user-facing task announcement format.
Mention Codex / Claude Code roles.
Mention Hermes / Qwen / MCP / automation as optional project-specific tools, not defaults.
```

Do not present this as final. It is candidate content for ChatGPT to accept after this task.

### Step 7: Update active entries

Update as needed:

```text
README.md
CHATGPT_START_HERE.md
reports/latest.md
```

Only add concise pointers. Do not duplicate entire new docs into every entry file.

### Step 8: Reports and closure

Write:

```text
reports/codex/playbook-v1-1-final-user-guide-routing-pro-review-v1.md
```

Update:

```text
reports/codex/latest.md
```

After completion, clear:

```text
tasks/codex/latest.md -> none / NO_ACTIVE_CODEX_TASK
```

Open a PR for review. Do not self-merge.

## 8. Validation

Run and record:

```bash
git diff --name-only origin/main...HEAD
git diff --stat origin/main...HEAD
git diff --check origin/main...HEAD
```

Required content checks:

```bash
grep -R "USER_OPERATING_GUIDE\|使用说明\|用户使用" -n README.md CHATGPT_START_HERE.md guides docs reports/chatgpt || true
grep -R "ROUTING_AND_EXTENSIBILITY\|routing\|路由\|扩展" -n README.md CHATGPT_START_HERE.md standards protocols templates reports/chatgpt || true
grep -R "PRO_REVIEW\|Pro review\|Pro 深度" -n reports/chatgpt README.md CHATGPT_START_HERE.md || true
grep -R "Personal Details Candidate\|Custom Instructions Candidate\|个人详情\|自定义指令" -n reports/chatgpt || true
grep -R "one active\|active execution lane\|NO_ACTIVE_CODEX_TASK" -n README.md CHATGPT_START_HERE.md standards protocols templates tasks reports/latest.md || true
grep -R "Claude Code.*final integrator\|Claude Code.*replace Codex\|Hermes.*default\|五件套" -n README.md CHATGPT_START_HERE.md standards protocols templates reports/chatgpt || true
```

Forbidden-path check:

```bash
git diff --name-only origin/main...HEAD | grep -E '^(AI_COLLABORATION_MODE_V4.md|lab/|archive/|whitepapers/|modules/)' && exit 1 || true
```

## 9. Acceptance Criteria

PASS only if:

```text
A user-facing operating guide exists.
Routing and extensibility guidance exists.
A Pro review entry exists.
Personalization candidate content exists.
Codex/Claude Code interaction research is documented.
README or CHATGPT_START_HERE links to the new guide/review/candidate files.
reports/latest.md remains PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS.
tasks/codex/latest.md is cleared after completion.
No forbidden scope is touched.
```

PARTIAL PASS if:

```text
Core docs exist but live Claude Code testing could not be safely performed or a PDF/image-ready artifact remains for ChatGPT to generate after acceptance.
```

FAIL if:

```text
The task changes V4 role boundaries, promotes optional tools into defaults, or mixes project-specific facts into general standards.
```

BLOCKED if:

```text
repo identity, branch state, or active task state cannot be verified safely.
```

## 10. Report Format

```text
# PLAYBOOK-V1.1-FINAL-USER-GUIDE-ROUTING-PRO-REVIEW-V1 Codex Report

## 1. Conclusion
PASS / PARTIAL PASS / FAIL / BLOCKED

## 2. Repository
- Repo:
- Branch:
- HEAD:
- PR:

## 3. User-Facing Result

## 4. Files Read

## 5. Files Changed

## 6. User Guide

## 7. Routing And Extensibility

## 8. Codex / Claude Code Research

## 9. Pro Review Entry

## 10. Personalization Candidate

## 11. Validation Commands

## 12. Forbidden Scope Confirmation

## 13. Remaining Issues

## 14. Next Step
```

## 11. Stop Conditions

Stop and report BLOCKED if:

```text
repo is not liuxiaoqianglongxia/ai-collaboration-playbook
another active Codex task already exists and is not this task
work would require changing AI_COLLABORATION_MODE_V4.md
work would require business repository, production, database, credential, or automation publish-chain work
```

## 12. User Instruction

The user should only need to send Codex:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```