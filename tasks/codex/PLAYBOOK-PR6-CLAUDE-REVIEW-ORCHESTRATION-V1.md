# PLAYBOOK-PR6-CLAUDE-REVIEW-ORCHESTRATION-V1

## 1. Task Name

```text
PLAYBOOK-PR6-CLAUDE-REVIEW-ORCHESTRATION-V1
```

## 2. Goal

Codex must orchestrate the already-registered Claude Code read-only review for PR #6.

Correct chain:

```text
ChatGPT writes GitHub task package
Codex reads tasks/codex/latest.md
Codex invokes or coordinates Claude Code through tasks/claude/latest.md
Claude Code produces a read-only review report
Codex verifies and records the orchestration result
ChatGPT performs final independent acceptance
```

This task exists because Claude Code is not a user-copy-paste target. Claude Code is a local engineering enhancement tool coordinated through Codex and GitHub task files.

## 3. Repository

Allowed repository only:

```text
liuxiaoqianglongxia/ai-collaboration-playbook
```

Target branch:

```text
docs/task-package-registry-v1-1
```

Target PR:

```text
PR #6 docs: add task package registry standard v1.1
```

## 4. Current Project State

PR #6 is the candidate PR for:

```text
PLAYBOOK_OPERATIONAL_BASELINE_V1.1_CANDIDATE
TASK-PACKAGE-REGISTRY-V1.1
```

The playbook repository has already added:

```text
tasks/README.md
tasks/codex/latest.md
tasks/claude/latest.md
tasks/claude/PLAYBOOK-PR6-READONLY-REVIEW-V1.md
reports/claude/latest.md
rollouts/TASK_PACKAGE_REGISTRY_ROLLOUT_WAVE1.md
```

## 5. Allowed Scope

Codex may:

```text
Read PR #6 and the current branch.
Read tasks/claude/latest.md.
Read tasks/claude/PLAYBOOK-PR6-READONLY-REVIEW-V1.md.
Invoke or coordinate Claude Code locally if available.
Collect Claude Code's read-only review result.
Write reports/claude/playbook-pr6-readonly-review-v1.md if Claude Code does not write it directly but provides the report output to Codex.
Update reports/claude/latest.md to point to the named Claude report.
Write reports/codex/playbook-pr6-claude-review-orchestration-v1.md.
Update reports/codex/latest.md to point to the Codex orchestration report.
Update tasks/codex/latest.md after orchestration is complete so it again points to tasks/codex/PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1.md with status READY_AFTER_CHATGPT_ACCEPTANCE.
```

## 6. Forbidden Scope

Codex must not:

```text
Merge PR #6.
Directly write main.
Force push.
Modify AI_COLLABORATION_MODE_V4.md.
Modify lab/ archive/ whitepapers/.
Modify business projects.
Modify maijian-wechat-content-lab.
Modify sub2api-maijian.
Deploy.
Change databases.
Read, print, commit, or modify secrets, tokens, cookies, .env, or credentials.
Add automation integration.
Promote Hermes to a default component.
Change the V4 four-piece model.
Treat Claude Code as final integrator.
```

## 7. Required Work

### Step 1: Preflight

Run and record:

```bash
git status -sb
git branch --show-current
git remote -v
git log --oneline -8
```

Confirm repository and branch match the task.

### Step 2: Read task pointers

Read:

```text
tasks/codex/latest.md
tasks/claude/latest.md
tasks/claude/PLAYBOOK-PR6-READONLY-REVIEW-V1.md
reports/latest.md
```

Confirm:

```text
tasks/claude/latest.md points to tasks/claude/PLAYBOOK-PR6-READONLY-REVIEW-V1.md
Claude status is ACTIVE_CLAUDE_TASK
reports/latest.md still marks PR #6 as V1.1 candidate / not final
```

### Step 3: Coordinate Claude Code review

Use the local Claude Code workflow available to Codex to execute the task in:

```text
tasks/claude/PLAYBOOK-PR6-READONLY-REVIEW-V1.md
```

Claude Code must remain read-only except for producing its review report.

Expected Claude report path:

```text
reports/claude/playbook-pr6-readonly-review-v1.md
```

If Claude Code is unavailable, not configured, or cannot be safely invoked, stop and report `BLOCKED`.

Do not ask the user to copy the Claude task manually.

### Step 4: Verify Claude report

Verify the Claude report exists and contains:

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Repository
Branch
PR
Files inspected
Findings
Validation
Forbidden scope confirmation
Next step
```

Update:

```text
reports/claude/latest.md
```

so it points to the named Claude report and records the Claude conclusion.

### Step 5: Write Codex orchestration report

Create:

```text
reports/codex/playbook-pr6-claude-review-orchestration-v1.md
```

Report must include:

```text
# PLAYBOOK-PR6-CLAUDE-REVIEW-ORCHESTRATION-V1 Codex Report

## 1. Conclusion
PASS / PARTIAL PASS / FAIL / BLOCKED

## 2. Repository
- Repo:
- Branch:
- PR:
- HEAD:

## 3. Task Pointers Verified
- tasks/codex/latest.md:
- tasks/claude/latest.md:
- Claude task file:

## 4. Claude Coordination Result
- Claude Code invoked or coordinated:
- Claude report path:
- Claude conclusion:

## 5. Files Changed

## 6. Safety Confirmation
- No main write:
- No PR merge:
- No force push:
- No V4 change:
- No business project change:
- No deployment:
- No database:
- No secrets:
- Claude remained read-only:

## 7. Validation Commands

## 8. Remaining Issues

## 9. Next Recommended Action
ChatGPT should read PR #6, reports/claude/latest.md, and this Codex orchestration report. If both are PASS, ChatGPT may perform independent acceptance and then explicitly authorize tasks/codex/PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1.md.
```

### Step 6: Restore Codex latest pointer after orchestration

After the Claude orchestration is complete, update:

```text
tasks/codex/latest.md
```

so it points back to:

```text
tasks/codex/PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1.md
```

with status:

```text
READY_AFTER_CHATGPT_ACCEPTANCE
```

This keeps merge closeout blocked until ChatGPT gives explicit independent PASS.

## 8. Validation

Run and record:

```bash
git diff --name-only
git diff --stat
git diff --check
```

Verify:

```bash
test -f reports/claude/playbook-pr6-readonly-review-v1.md
test -f reports/codex/playbook-pr6-claude-review-orchestration-v1.md
grep -n 'reports/claude/playbook-pr6-readonly-review-v1.md' reports/claude/latest.md
grep -n 'tasks/codex/PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1.md' tasks/codex/latest.md
grep -n 'READY_AFTER_CHATGPT_ACCEPTANCE' tasks/codex/latest.md
```

Verify forbidden files were not changed:

```bash
git diff --name-only | grep -x 'AI_COLLABORATION_MODE_V4.md' && exit 1 || true
git diff --name-only | grep -E '^(lab/|archive/|whitepapers/)' && exit 1 || true
```

## 9. Acceptance Criteria

PASS only if:

```text
Claude Code review task was coordinated through Codex, not user copy-paste.
Claude report exists under reports/claude/.
reports/claude/latest.md points to the Claude report.
Codex orchestration report exists under reports/codex/.
tasks/codex/latest.md is restored to merge closeout waiting state.
PR #6 remains open and unmerged.
AI_COLLABORATION_MODE_V4.md remains unchanged.
No business project was modified.
No deployment, database, secrets, or automation work occurred.
```

PARTIAL PASS if Claude report exists but pointer/report cleanup is incomplete.

FAIL if Codex modifies forbidden files, merges PR #6 without ChatGPT acceptance, changes V4, or touches business projects.

BLOCKED if Claude Code cannot be invoked safely or repository identity is unclear.

## 10. Next Step

If PASS:

```text
ChatGPT performs independent read-only acceptance of PR #6 using:
- PR #6 metadata and diff
- standards/TASK_PACKAGE_REGISTRY_V1_1.md
- tasks/codex/latest.md
- tasks/claude/latest.md
- reports/claude/latest.md
- reports/codex/latest.md
- reports/latest.md
- rollouts/TASK_PACKAGE_REGISTRY_ROLLOUT_WAVE1.md
```

If ChatGPT acceptance is PASS, Codex may later execute `tasks/codex/PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1.md` only after explicit ChatGPT authorization.
