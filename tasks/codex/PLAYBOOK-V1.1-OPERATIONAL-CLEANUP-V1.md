# PLAYBOOK-V1.1-OPERATIONAL-CLEANUP-V1

## 1. Task Name

```text
PLAYBOOK-V1.1-OPERATIONAL-CLEANUP-V1
```

## 2. Goal

Clean up the playbook repository after `PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS` so future ChatGPT sessions no longer see conflicting candidate/active-task state.

The user-facing goal is:

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

V1.1 should work like a browser: the user gives a short goal; the repository and agents handle the complexity behind the scenes.

## 3. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
base: main
recommended working branch: docs/playbook-v1-1-operational-cleanup-v1
current baseline: PLAYBOOK_OPERATIONAL_BASELINE_V1.1
current baseline closeout/main HEAD before this task: 5fe21aec9eccb87df0e318fc376cf1852129b2d7
```

## 4. Current Facts To Verify

Read before changing anything:

```text
reports/latest.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
NEW_PROJECT_BOOTSTRAP.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
protocols/GITHUB_AI_COLLABORATION.md
tasks/README.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/codex/latest.md
reports/claude/latest.md
reports/codex/playbook-v1-1-merge-closeout-v1.md
rollouts/TASK_PACKAGE_REGISTRY_ROLLOUT_WAVE1.md
```

Controller-observed conflicts to resolve:

```text
1. reports/latest.md is already PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS.
2. README.md still describes PLAYBOOK_OPERATIONAL_BASELINE_V1.1 as Candidate.
3. standards/TASK_PACKAGE_REGISTRY_V1_1.md still says Candidate and not final until PR acceptance/merge.
4. tasks/codex/latest.md still points to completed merge closeout with READY_AFTER_CHATGPT_ACCEPTANCE.
5. tasks/claude/latest.md still shows ACTIVE_CLAUDE_TASK for the completed PR #6 review.
6. reports/claude/latest.md still explains PARTIAL PASS as pending ChatGPT acceptance even though PR #6 has been accepted and merged.
7. V1.1 does not clearly define the capability boundary when ChatGPT has no GitHub write access.
8. V1.1 does not yet make the simplified user layer explicit enough.
```

## 5. Allowed Scope

Codex may update only documentation, task registry pointers, templates, and reports required to remove the contradictions above.

Allowed write paths:

```text
README.md
AI_AGENT_ONBOARDING.md
NEW_PROJECT_BOOTSTRAP.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/TASK_PACKAGE_REGISTRY_BOOTSTRAP_TASK.md
templates/tasks/README.md
templates/tasks/codex/latest.md
templates/tasks/claude/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/claude/latest.md
reports/codex/latest.md
reports/codex/playbook-v1-1-operational-cleanup-v1.md
reports/latest.md
reports/chatgpt/task-packages/PLAYBOOK-V1.1-OPERATIONAL-CLEANUP-V1.md
```

Optional additions if absent and useful for future new sessions:

```text
CHATGPT_START_HERE.md
CURRENT.md
TASKS.md
```

These optional files must remain playbook-specific and must not import business project state.

## 6. Forbidden Scope

Do not modify:

```text
AI_COLLABORATION_MODE_V4.md
lab/
archive/
whitepapers/
modules/
any business repository
maijian-wechat-content-lab
shanxi-edu-hot
sub2api-maijian
production servers
databases
secrets, tokens, cookies, .env files
automation integrations
```

Do not:

```text
write directly to main for the cleanup implementation
force push
delete branches
merge your own PR
promote Hermes into the default four-piece model
make Claude Code the final integrator
turn this into a broad V0.3 / automation / MCP / heartbeat redesign
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
git log --oneline -8 origin/main
```

Confirm:

```text
repository is liuxiaoqianglongxia/ai-collaboration-playbook
origin/main is at or after 5fe21aec9eccb87df0e318fc376cf1852129b2d7
working branch is not main for implementation
```

### Step 2: Read and map current contradiction state

Read all files listed in section 4.

Produce a short internal map of:

```text
stable facts
stale candidate facts
stale active pointers
files requiring updates
files that must not be touched
```

### Step 3: Make V1.1 stable status consistent

Update active docs so they consistently say:

```text
PLAYBOOK_OPERATIONAL_BASELINE_V1.1 is the current stable baseline.
PR #6 has been merged.
reports/latest.md is the primary current-status entry.
V4 four-piece model remains unchanged.
TASK_PACKAGE_REGISTRY_V1_1 is no longer candidate-only.
```

Minimum required updates:

```text
README.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
```

The standard must keep historical promotion-gate language, but it must not describe the already-merged V1.1 as still waiting for review.

### Step 4: Add simplified user-layer rule

Document the default user experience:

```text
User says a short goal.
ChatGPT reads GitHub fact source.
ChatGPT decides risk and route.
If GitHub write access exists, ChatGPT writes/updates the GitHub task package and latest pointer.
If GitHub write access does not exist, ChatGPT must say so and provide a Codex landing instruction; it must not claim the task is already in GitHub.
Codex executes tasks/codex/latest.md.
Codex writes reports/codex/latest.md.
ChatGPT validates from GitHub and outputs PASS / PARTIAL PASS / FAIL / BLOCKED.
```

Add this rule to the most appropriate files, likely:

```text
standards/TASK_PACKAGE_REGISTRY_V1_1.md
protocols/GITHUB_AI_COLLABORATION.md
AI_AGENT_ONBOARDING.md
```

Do not make users manually copy long Claude Code tasks. Claude Code remains coordinated through Codex and `tasks/claude/latest.md` when needed.

### Step 5: Add pointer hygiene after task completion

Define and apply a rule:

```text
After a task is completed and accepted, latest pointers must not continue to present it as active or waiting.
They should either show no active task, or show a short previous-task record while Current task package is none.
```

Update:

```text
tasks/codex/latest.md
tasks/claude/latest.md
reports/claude/latest.md
templates/tasks/codex/latest.md
templates/tasks/claude/latest.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
```

Expected state after cleanup:

```text
tasks/codex/latest.md:
  Current task package: none
  Current execution status: NO_ACTIVE_CODEX_TASK
  Previous completed task: tasks/codex/PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1.md
  Previous report: reports/codex/playbook-v1-1-merge-closeout-v1.md

tasks/claude/latest.md:
  Current task package: none
  Current execution status: NO_ACTIVE_CLAUDE_TASK
  Previous completed task: tasks/claude/PLAYBOOK-PR6-READONLY-REVIEW-V1.md
  Previous report: reports/claude/playbook-pr6-readonly-review-v1.md
```

`reports/claude/latest.md` should say the PR #6 read-only review is historical accepted evidence after closeout, not a currently pending gate.

### Step 6: Add a new-session entry if useful

If `CHATGPT_START_HERE.md` is absent, create a concise playbook-specific entry that says:

```text
Read order:
1. reports/latest.md
2. README.md
3. AI_AGENT_ONBOARDING.md
4. AI_COLLABORATION_MODE_V4.md
5. standards/TASK_PACKAGE_REGISTRY_V1_1.md
6. tasks/codex/latest.md
7. tasks/claude/latest.md
8. reports/codex/latest.md
9. reports/claude/latest.md

Current baseline:
PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS

Controller rule:
Do not rely on old chat history.
Do not treat candidate-era files as current if reports/latest.md says otherwise.
Use simplified V1.1 mode.
```

If creating `CURRENT.md` and `TASKS.md`, keep them short and aligned with `reports/latest.md`. Do not create a large new governance layer.

### Step 7: Reports and status files

Write:

```text
reports/codex/playbook-v1-1-operational-cleanup-v1.md
```

Update:

```text
reports/codex/latest.md
reports/latest.md
```

`reports/latest.md` must remain:

```text
PLAYBOOK_OPERATIONAL_BASELINE_V1.1
PASS
```

It may add:

```text
V1.1 Operational Cleanup: PASS
```

only after this task is complete.

## 8. Validation

Run and record:

```bash
git diff --name-only origin/main...HEAD
git diff --stat origin/main...HEAD
git diff --check origin/main...HEAD
```

Required content checks:

```bash
grep -n 'PLAYBOOK_OPERATIONAL_BASELINE_V1.1' reports/latest.md
grep -n 'PASS' reports/latest.md
grep -n 'NO_ACTIVE_CODEX_TASK' tasks/codex/latest.md
grep -n 'NO_ACTIVE_CLAUDE_TASK' tasks/claude/latest.md
grep -n 'PLAYBOOK_OPERATIONAL_BASELINE_V1.1' standards/TASK_PACKAGE_REGISTRY_V1_1.md
```

Forbidden drift checks:

```bash
git diff --name-only origin/main...HEAD | grep -x 'AI_COLLABORATION_MODE_V4.md' && exit 1 || true
git diff --name-only origin/main...HEAD | grep -E '^(lab/|archive/|whitepapers/|modules/)' && exit 1 || true
grep -R "Hermes.*默认\|五件套" -n README.md AI_AGENT_ONBOARDING.md NEW_PROJECT_BOOTSTRAP.md standards protocols templates tasks reports || true
grep -R "Candidate for `PLAYBOOK_OPERATIONAL_BASELINE_V1.1`\|V1.1_CANDIDATE" -n README.md AI_AGENT_ONBOARDING.md NEW_PROJECT_BOOTSTRAP.md standards protocols tasks reports/latest.md reports/codex/latest.md reports/claude/latest.md && exit 1 || true
grep -R "READY_AFTER_CHATGPT_ACCEPTANCE\|ACTIVE_CLAUDE_TASK" -n tasks/codex/latest.md tasks/claude/latest.md reports/claude/latest.md && exit 1 || true
```

Historical reports may still mention old candidate states. Do not rewrite historical evidence unless it is the active latest pointer/report.

## 9. Acceptance Criteria

PASS only if:

```text
README.md no longer describes V1.1 as merely Candidate.
standards/TASK_PACKAGE_REGISTRY_V1_1.md no longer describes current V1.1 as pending merge.
tasks/codex/latest.md is no longer waiting on the completed PR #6 closeout.
tasks/claude/latest.md is no longer an active completed PR #6 review task.
reports/claude/latest.md no longer says PR #6 is pending ChatGPT acceptance as current state.
Simplified user-layer rule is documented.
GitHub-write capability boundary is documented.
reports/latest.md remains PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS.
V4 four-piece model remains unchanged.
No business project, deployment, database, secrets, automation, lab/archive/whitepapers/modules changes occurred.
A PR is created for review; it is not self-merged.
```

PARTIAL PASS if the core contradictions are fixed but optional new-session entry files are deferred with clear reason.

FAIL if forbidden scope is touched or V4 role boundaries change.

BLOCKED if repository identity, base branch, or current facts cannot be verified safely.

## 10. Report Format

```text
# PLAYBOOK-V1.1-OPERATIONAL-CLEANUP-V1 Codex Report

## 1. Conclusion
PASS / PARTIAL PASS / FAIL / BLOCKED

## 2. Repository
- Repo:
- Branch:
- Base:
- PR:
- HEAD:

## 3. Facts Read

## 4. Contradictions Found

## 5. Files Changed

## 6. Key Fixes
- Stable V1.1 status cleanup:
- Latest pointer hygiene:
- Simplified user-layer rule:
- GitHub-write capability boundary:
- New-session entry:

## 7. Validation

## 8. Forbidden Scope Confirmation

## 9. Remaining Issues

## 10. Next Step
```

## 11. Stop Conditions

Stop and report `BLOCKED` when:

```text
repository is not liuxiaoqianglongxia/ai-collaboration-playbook
main HEAD cannot be verified
implementation would require changing AI_COLLABORATION_MODE_V4.md
implementation would require touching business repositories
implementation would require deployment, database, secrets, or automation
candidate/stable contradictions are broader than listed and cannot be safely resolved in this task
```

## 12. Next Step After Codex PASS

ChatGPT should read:

```text
PR diff
reports/codex/playbook-v1-1-operational-cleanup-v1.md
reports/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
README.md
```

Then ChatGPT should output:

```text
PASS / PARTIAL PASS / FAIL / BLOCKED
```

If PASS, the user can update Personal Details / Custom Instructions against the cleaned V1.1 baseline.