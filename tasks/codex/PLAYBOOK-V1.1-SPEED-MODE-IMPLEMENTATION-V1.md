# PLAYBOOK-V1.1-SPEED-MODE-IMPLEMENTATION-V1

## 0. User-Facing Summary

Implement the research result from `PLAYBOOK-V1.1-PROCESS-SPEED-RESEARCH-V1` as a stable V1.1 speed-mode layer.

It should achieve:

```text
1. Add GitHub Backend Mode as a stable operating option.
2. Add default-branch-first routing for low-risk coordination files.
3. Add a broad working-permission model with a small protected-area exception.
4. Add Claude-first / Codex-final execution guidance.
5. Add concrete Claude Code first-pass worker templates.
6. Update user guide and Pro review entry with the new speed-mode route.
```

User instruction:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```

## 1. Task Name

```text
PLAYBOOK-V1.1-SPEED-MODE-IMPLEMENTATION-V1
```

## 2. Goal

Turn the speed-mode research report into practical docs and templates.

Source report:

```text
reports/codex/playbook-v1-1-process-speed-research-v1.md
```

Core direction:

```text
GitHub remains the durable fact source, but should not be the user's daily work surface.
Low-risk coordination work should usually go to main directly.
Claude Code should handle safe first-pass engineering work.
Codex should own final integration, validation, commits, PRs when needed, and reports.
```

## 3. Current Facts To Read

Read before changing anything:

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
tasks/codex/latest.md
tasks/claude/latest.md
reports/claude/latest.md
```

## 4. Allowed Scope

Allowed docs and template changes:

```text
standards/GITHUB_BACKEND_MODE_V1.md
standards/MAIN_FIRST_ROUTING_V1.md
standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md
standards/CLAUDE_FIRST_CODEX_FINAL_V1.md
templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
templates/CLAUDE_PATCH_WORKER_TASK.md
templates/CODEX_CLAUDE_INVOCATION_PATTERNS.md
checklists/HIGH_RISK_CONFIRMATION_GATE.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
protocols/GITHUB_AI_COLLABORATION.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
reports/latest.md
reports/codex/playbook-v1-1-speed-mode-implementation-v1.md
reports/codex/latest.md
tasks/codex/latest.md
```

Do not modify `AI_COLLABORATION_MODE_V4.md` in this task.

## 5. Required Work

### Step 1: Add GitHub Backend Mode

Create a standard that says:

```text
GitHub is the durable fact ledger and sync layer.
The user should not manage routine GitHub mechanics.
Agents handle routine task/report/pointer sync in the background.
Low-risk coordination changes can go directly to main.
PRs are used when review or integration protection is useful.
```

Include:

```text
user sees
agent handles
start-of-task sync
end-of-task sync
pointer lag handling
when to stop
```

### Step 2: Add Main-First Routing

Create a routing standard with three classes:

```text
main-first
review branch / PR
special confirmation
```

Use the research report as the basis. Keep language practical and not overly conservative.

### Step 3: Add Maximum Practical Authorization

Create a standard that reflects the user's preference:

```text
Tools should have broad permission for ordinary project work.
Do not ask for approval on every small action.
Keep only a small protected zone that requires explicit confirmation.
Project-specific routing files may override defaults.
```

Do not remove all boundaries. The point is fewer blocks, not no control.

### Step 4: Add Claude-First / Codex-Final

Create a standard that says:

```text
Claude Code is not only a reviewer.
Claude Code can perform bounded first-pass implementation work.
Codex coordinates Claude Code and owns final integration.
Codex validates, commits, pushes, creates PRs when needed, and writes reports.
```

Include:

```text
Claude-first task types
Codex-first task types
ChatGPT-direct task types
when Claude may edit files
when Claude should produce a patch only
how Codex verifies Claude output
how to summarize Claude work in reports
```

### Step 5: Add Claude worker templates

Add templates for:

```text
bounded implementation worker
patch worker
Codex -> Claude invocation patterns
```

They must include:

```text
goal
allowed files
excluded areas
steps
expected output
evidence format
Codex verification requirements
stop conditions
```

### Step 6: Update user-facing docs

Update guide/start-here/README/onboarding only with concise pointers.

User guide should explain:

```text
For low-risk coordination work, GitHub runs in the background.
For ordinary engineering work, Claude Code may do first-pass work and Codex finalizes.
For complex or risky work, Codex leads directly.
```

### Step 7: Update Pro review entry and personalization candidate

Add concise notes so tomorrow's Pro session can review the new Speed Mode.

Personalization candidate should not become too long.

### Step 8: Report and close

Write:

```text
reports/codex/playbook-v1-1-speed-mode-implementation-v1.md
```

Update:

```text
reports/codex/latest.md
reports/latest.md
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
grep -R "GitHub Backend Mode\|main-first\|Speed Mode" -n README.md CHATGPT_START_HERE.md guides standards protocols reports/latest.md || true
grep -R "Claude-first\|Codex-final\|first-pass" -n README.md CHATGPT_START_HERE.md guides standards templates reports/latest.md || true
grep -R "maximum practical\|broad permission\|protected zone" -n standards guides reports/chatgpt || true
```

## 7. Acceptance Criteria

PASS only if:

```text
GitHub Backend Mode standard exists.
Main-first routing standard exists.
Maximum Practical Authorization standard exists.
Claude-first / Codex-final standard exists.
Claude Code worker templates exist.
User-facing docs point to Speed Mode.
reports/latest.md remains PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS.
tasks/codex/latest.md is cleared after completion.
V4 role model remains intact.
```

PARTIAL PASS if docs are added but personalization/pro-review updates need a follow-up.

FAIL if the task makes Claude Code final integrator or removes GitHub fact-source discipline.

BLOCKED if repo identity or active task state cannot be verified.

## 8. Report Format

```text
# PLAYBOOK-V1.1-SPEED-MODE-IMPLEMENTATION-V1 Codex Report

## 1. Conclusion
PASS / PARTIAL PASS / FAIL / BLOCKED

## 2. Repository

## 3. User-Facing Result

## 4. Files Read

## 5. Files Changed

## 6. GitHub Backend Mode

## 7. Main-First Routing

## 8. Maximum Practical Authorization

## 9. Claude-First / Codex-Final

## 10. Claude Worker Templates

## 11. Validation

## 12. Remaining Issues

## 13. Next Step
```

## 9. User Instruction

The user should only need to send Codex:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```