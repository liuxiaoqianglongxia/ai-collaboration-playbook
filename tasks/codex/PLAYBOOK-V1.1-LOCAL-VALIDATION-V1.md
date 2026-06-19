# PLAYBOOK-V1.1-LOCAL-VALIDATION-V1

## 1. Task Name

```text
PLAYBOOK-V1.1-LOCAL-VALIDATION-V1
```

## 2. Goal

Perform a narrow local validation of ChatGPT's direct V1.1 operational cleanup on `ai-collaboration-playbook`.

This task exists because ChatGPT completed safe documentation and pointer cleanup directly through GitHub, but could not run local shell-level checks such as full `git diff --check` and repository-wide grep.

Codex must validate quality, not redo the design.

## 3. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
base branch: main
suggested branch if fixes are required: docs/playbook-v1-1-local-validation-v1
```

## 4. Current Facts To Read

```text
CHATGPT_START_HERE.md
reports/latest.md
README.md
AI_AGENT_ONBOARDING.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
protocols/GITHUB_AI_COLLABORATION.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/claude/latest.md
reports/chatgpt/task-packages/PLAYBOOK-V1.1-OPERATIONAL-CLEANUP-V1.md
```

## 5. Allowed Scope

Read-only validation is preferred.

Allowed write scope only if a clear issue is found:

```text
reports/codex/playbook-v1-1-local-validation-v1.md
reports/codex/latest.md
tasks/codex/latest.md
reports/latest.md
```

If small documentation corrections are required, open a branch and PR. Do not write additional broad changes directly to main.

## 6. Forbidden Scope

Do not modify:

```text
AI_COLLABORATION_MODE_V4.md
lab/
archive/
whitepapers/
modules/
business repositories
production systems
databases
credentials or secrets
automation publish chains
```

Do not:

```text
force push
merge your own PR
promote Hermes into the default model
make Claude Code the final integrator
start a V0.3 redesign
change the meaning of V1.1 simplification
```

## 7. Required Validation

Run and record:

```bash
git status -sb
git branch --show-current
git remote -v
git fetch origin --prune
git rev-parse origin/main
git log --oneline -12 origin/main
git diff --check HEAD~12..HEAD || true
```

Search for stale state in active files:

```bash
grep -R "V1.1_CANDIDATE\|Candidate for PLAYBOOK_OPERATIONAL_BASELINE_V1.1\|READY_AFTER_CHATGPT_ACCEPTANCE\|ACTIVE_CLAUDE_TASK" -n \
  CHATGPT_START_HERE.md README.md AI_AGENT_ONBOARDING.md standards protocols tasks reports/latest.md reports/codex/latest.md reports/claude/latest.md templates || true
```

Verify expected active state:

```bash
grep -n "PLAYBOOK_OPERATIONAL_BASELINE_V1.1" reports/latest.md
grep -n "V1.1 Operational Cleanup: PASS" reports/latest.md
grep -n "NO_ACTIVE_CODEX_TASK" tasks/codex/latest.md
grep -n "NO_ACTIVE_CLAUDE_TASK" tasks/claude/latest.md
grep -n "Stable in" standards/TASK_PACKAGE_REGISTRY_V1_1.md
grep -n "使用层极简" CHATGPT_START_HERE.md reports/latest.md README.md standards/TASK_PACKAGE_REGISTRY_V1_1.md
```

Verify forbidden areas not touched in the recent cleanup window as best possible from local git history:

```bash
git diff --name-only 5fe21aec9eccb87df0e318fc376cf1852129b2d7..HEAD
```

Flag if that diff includes:

```text
AI_COLLABORATION_MODE_V4.md
lab/
archive/
whitepapers/
modules/
```

## 8. Acceptance Criteria

PASS if:

```text
No stale active candidate terms remain in active files.
latest pointers are cleared to none / NO_ACTIVE_*.
reports/latest.md remains PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS and records V1.1 Operational Cleanup: PASS.
CHATGPT_START_HERE.md gives a clear new-session entry.
README, onboarding, standard, and protocol consistently describe user-layer simplification plus strong hidden execution.
No forbidden areas changed.
No local diff/check issue matters for markdown quality.
```

PARTIAL PASS if:

```text
Core state is correct but minor documentation wording or formatting needs a follow-up PR.
```

FAIL if:

```text
The cleanup introduced contradictory current facts or touched forbidden areas.
```

BLOCKED if:

```text
Repository identity or local checkout state cannot be verified safely.
```

## 9. Report Format

Write:

```text
reports/codex/playbook-v1-1-local-validation-v1.md
```

Report format:

```text
# PLAYBOOK-V1.1-LOCAL-VALIDATION-V1 Codex Report

## 1. Conclusion
PASS / PARTIAL PASS / FAIL / BLOCKED

## 2. Repository
- Repo:
- Branch:
- HEAD:

## 3. Files Read

## 4. Validation Commands

## 5. Findings

## 6. Forbidden Scope Confirmation

## 7. Files Changed

## 8. Remaining Issues

## 9. Next Step
```

Then update:

```text
reports/codex/latest.md
```

After PASS, clear:

```text
tasks/codex/latest.md -> none / NO_ACTIVE_CODEX_TASK
```

## 10. Stop Conditions

Stop and report BLOCKED if:

```text
local repo is not liuxiaoqianglongxia/ai-collaboration-playbook
main branch identity cannot be verified
validation would require touching forbidden paths
validation would require production, database, credential, or automation work
```

## 11. User-Facing Next Instruction

After this task is assigned, the user can tell Codex:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```