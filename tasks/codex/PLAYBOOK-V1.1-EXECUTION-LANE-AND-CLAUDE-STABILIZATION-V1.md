# PLAYBOOK-V1.1-EXECUTION-LANE-AND-CLAUDE-STABILIZATION-V1

## 0. User-Facing Summary

This task should make the playbook easier to use while preserving full execution power.

It should achieve:

```text
1. Add the one-active-execution-lane rule.
2. Add a standard short user-facing task announcement format.
3. Stabilize how Codex coordinates Claude Code without making the user copy long Claude tasks.
4. Review existing lab notes about Claude Code and promote only stable, useful rules into standards/protocols/templates.
```

The user-facing instruction should stay simple:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```

Detailed scope and validation live in this file.

## 1. Task Name

```text
PLAYBOOK-V1.1-EXECUTION-LANE-AND-CLAUDE-STABILIZATION-V1
```

## 2. Background

`PLAYBOOK_OPERATIONAL_BASELINE_V1.1` is now stable and local validation has passed.

The user clarified the desired operating model:

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

Simplification means the user-facing layer should be short and convenient. It does not mean reducing capability. ChatGPT, Codex, Claude Code, Qwen, Hermes, GitHub, task packages, reports, and validation may be complex behind the scenes when that complexity improves delivery.

A new controller rule must be stabilized:

```text
One stage should have only one active execution lane.
If an active Codex task exists, do not create another active Codex task.
If Claude Code is needed during that stage, Codex should coordinate it inside the current Codex task.
New findings should be recorded as candidate next steps, not immediately activated while the current task is unfinished.
```

The user also requested a better task assignment UX:

```text
ChatGPT should tell the user what the task roughly achieves and what to send to Codex.
The detailed task package should stay in GitHub.
The chat should not paste long task packages unless explicitly requested.
```

## 3. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
base branch: main
recommended branch: docs/playbook-v1-1-execution-lane-claude-stabilization-v1
```

## 4. Current Facts To Read

Read before changing anything:

```text
CHATGPT_START_HERE.md
reports/latest.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
protocols/GITHUB_AI_COLLABORATION.md
checklists/TASK_PACKAGE_REGISTRY_REVIEW.md
templates/tasks/codex/_template.md
templates/tasks/claude/_template.md
templates/tasks/codex/latest.md
templates/tasks/claude/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

Also inspect existing lab / experimental / archive material for Claude Code usage and boundaries:

```text
lab/
archive/
whitepapers/
reports/claude/
reports/codex/
```

Only promote content that is stable, useful, and aligned with V4/V1.1. Do not wholesale promote experiments.

## 5. Allowed Scope

Codex may update or add files in these areas only:

```text
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
NEW_PROJECT_BOOTSTRAP.md
standards/
protocols/
templates/
checklists/
tasks/codex/latest.md
tasks/claude/latest.md
reports/codex/
reports/claude/
reports/latest.md
reports/chatgpt/task-packages/
```

Recommended new or updated docs:

```text
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
templates/tasks/codex/_template.md
templates/tasks/claude/_template.md
checklists/TASK_PACKAGE_REGISTRY_REVIEW.md
```

If a better file layout is chosen, explain it in the report.

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

Do not:

```text
force push
merge your own PR
promote Hermes into the default four-piece model
make Claude Code the final integrator
start a broad V0.3 redesign
turn Qwen / Hermes / MCP / heartbeat into default stable members
copy project-specific facts into generic standards
```

Avoid modifying `lab/`, `archive/`, `whitepapers/`, or `modules/` unless only adding a short pointer or report is strictly necessary. Prefer reading them as evidence.

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
current active task is this task
no other active Codex or Claude Code task exists unless created as an internal subtask of this task
```

### Step 2: Read current facts

Read all files listed in section 4.

Create an internal map of:

```text
current stable V1.1 facts
current task pointer state
existing Claude Code docs / reports / lab references
places where one-active-execution-lane should be documented
places where user-facing task summary should be documented
```

### Step 3: Add one-active-execution-lane standard

Add or update a standard that clearly says:

```text
One stage has only one active execution lane.
Default: one active Codex task at a time.
Do not create a new active Codex task before the current one reports PASS / PARTIAL PASS / FAIL / BLOCKED.
If Claude Code is needed, Codex coordinates it inside the active Codex task through tasks/claude/latest.md or local workflow.
New findings during an active task become candidate next steps, not new active tasks.
ChatGPT may prepare notes but must not update latest pointers to a new task until the current task is closed.
```

Also define what is allowed while waiting for an active task:

```text
read status
explain scope
prepare acceptance checklist
do not create new active execution work
```

### Step 4: Add user-facing task announcement standard

Create or update a template so future ChatGPT task assignments look like this in chat:

```text
任务：<TASK-ID>
能实现：
- <one concrete outcome>
- <one concrete outcome>
- <one concrete outcome>
不做：<key boundary>
你发给 Codex：执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
详情：任务包已在 GitHub。
```

Rules:

```text
Do not paste the full task package in chat by default.
Do not hide what the task is for.
Do not overload the user with implementation steps.
Do not claim the task package is in GitHub unless it actually is.
```

### Step 5: Stabilize Claude Code coordination

Create or update standards/protocols/templates to clarify:

```text
Claude Code is used for deep code reading, failure analysis, local fix drafts, and review.
Claude Code is not a default execution lane by itself.
Claude Code does not replace Codex as final integrator.
Codex coordinates Claude Code during an active Codex task when useful.
Users should not manually relay long Claude Code task packages when Codex can coordinate the local workflow.
Claude Code outputs should be report evidence, not direct authority to merge or deploy.
Claude Code report acceptance must be read by ChatGPT or Codex before affecting final status.
```

If Claude CLI / Claude Code is locally available, Codex may run a read-only review of the final diff or the proposed standard text.

If Claude Code is not available, do not block the whole task. Report `PARTIAL PASS` only if the missing Claude review leaves material risk; otherwise document that no live Claude invocation occurred and rely on local validation.

### Step 6: Update templates and checklists

Update task package templates so they include:

```text
User-facing summary
Execution lane status
Whether Claude Code is allowed / required / forbidden
What happens if a new issue is discovered during an active task
Stop condition when another active task already exists
```

Update checklist to verify:

```text
only one active execution lane exists
latest pointers are consistent
user-facing task summary exists
Codex / Claude Code boundary is explicit
```

### Step 7: Reports

Write:

```text
reports/codex/playbook-v1-1-execution-lane-and-claude-stabilization-v1.md
```

Update:

```text
reports/codex/latest.md
reports/latest.md
tasks/codex/latest.md
```

After completion, `tasks/codex/latest.md` should be cleared to:

```text
none / NO_ACTIVE_CODEX_TASK
```

If a Claude subtask is used, `tasks/claude/latest.md` should also be cleared after the review completes.

## 8. Validation

Run and record:

```bash
git diff --name-only origin/main...HEAD
git diff --stat origin/main...HEAD
git diff --check origin/main...HEAD
```

Required searches:

```bash
grep -R "one active\|active execution lane\|NO_ACTIVE_CODEX_TASK\|NO_ACTIVE_CLAUDE_TASK" -n README.md CHATGPT_START_HERE.md AI_AGENT_ONBOARDING.md standards protocols templates checklists tasks reports/latest.md || true
grep -R "Claude Code.*final integrator\|Claude Code.*replace Codex\|Hermes.*default\|五件套" -n README.md CHATGPT_START_HERE.md AI_AGENT_ONBOARDING.md standards protocols templates checklists || true
grep -R "执行 tasks/codex/latest.md" -n templates standards protocols README.md CHATGPT_START_HERE.md AI_AGENT_ONBOARDING.md || true
```

Forbidden-path check:

```bash
git diff --name-only origin/main...HEAD | grep -E '^(AI_COLLABORATION_MODE_V4.md|business|lab/|archive/|whitepapers/|modules/)' && exit 1 || true
```

Adjust the forbidden-path command if `business` is not a repository path in this repo.

## 9. Acceptance Criteria

PASS only if:

```text
One-active-execution-lane rule is documented.
User-facing task announcement template exists or is documented.
Claude Code coordination boundary is documented.
Codex remains final integrator.
Claude Code does not become a separate default execution lane.
Future task templates include user-facing summary and execution-lane controls.
Latest pointers are cleared after completion.
reports/latest.md remains PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS.
No forbidden scope touched.
```

PARTIAL PASS if:

```text
Core standards are updated but live Claude Code review could not be performed or minor template follow-up remains.
```

FAIL if:

```text
The task changes V4 role boundaries, introduces another default member, or touches forbidden scope.
```

BLOCKED if:

```text
repository identity, active task state, or local workspace safety cannot be verified.
```

## 10. Report Format

```text
# PLAYBOOK-V1.1-EXECUTION-LANE-AND-CLAUDE-STABILIZATION-V1 Codex Report

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

## 6. Execution Lane Rule

## 7. User-Facing Task Announcement Rule

## 8. Claude Code Coordination Rule

## 9. Validation Commands

## 10. Forbidden Scope Confirmation

## 11. Remaining Issues

## 12. Next Step
```

## 11. Stop Conditions

Stop and report `BLOCKED` when:

```text
repo is not liuxiaoqianglongxia/ai-collaboration-playbook
another active Codex task already exists and is not this task
work would require changing AI_COLLABORATION_MODE_V4.md
work would require touching business repositories or runtime systems
work would require secrets or automation publish-chain work
```

## 12. User Instruction

The user should only need to send Codex:

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```