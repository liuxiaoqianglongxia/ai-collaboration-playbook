# PLAYBOOK-V1.1-PROCESS-SPEED-RESEARCH-V1 Codex Report

## 1. Conclusion

PASS.

This task produced an implementation-oriented speed research report for PLAYBOOK_OPERATIONAL_BASELINE_V1.1.

Core recommendation:

```text
Keep GitHub as the durable fact source, but stop making GitHub the user's daily work surface.
Default low-risk coordination work to direct main.
Reserve PRs for review or integration protection.
Use Claude Code as the first-pass implementation worker where bounded.
Keep Codex as final integrator, diff reviewer, test runner, committer, pusher, reporter, and fallback.
```

This report does not modify stable standards. It identifies the concrete follow-up standards and templates needed to make the faster mode stable.

## 2. Repository

Repository:

```text
liuxiaoqianglongxia/ai-collaboration-playbook
```

Local path:

```text
/Users/liuxiaoqiang/code/ai-collaboration-playbook
```

Execution branch:

```text
main
```

Reason for main-first execution:

```text
The current task only allows low-risk coordination files:
- reports/codex/playbook-v1-1-process-speed-research-v1.md
- reports/codex/latest.md
- tasks/codex/latest.md

This is exactly the category this report recommends for direct main work.
No PR is needed for this task's write scope.
```

Baseline observed before writing:

```text
origin/main HEAD: 8726e0d0a1bdacc7aeaac2578ef3da40c63ac754
current branch: main
working tree: clean
```

## 3. User Goal Interpreted

The user's goal is not simply to reduce risk. The goal is to increase useful throughput.

The desired operating model is:

```text
GitHub behaves like a background sync drive for collaboration state.
The user gives compact intent.
Agents read and write GitHub facts mostly in the background.
The user does not repeatedly handle PRs, latest pointers, reports, closeouts, or sync confirmations.
```

The requested emphasis is implementation speed:

```text
- design GitHub Backend Mode
- design main-first routing
- design maximum practical authorization
- make Claude-first / Codex-final real
- give concrete workflows, not only principles
- give Pro implementation questions for the next round
```

This report therefore treats existing conservative blockers as friction to redesign, not as a reason to stop.

## 4. Sources Read

Primary current-task sources:

```text
tasks/codex/latest.md
tasks/codex/PLAYBOOK-V1.1-PROCESS-SPEED-RESEARCH-V1.md
reports/codex/latest.md
reports/latest.md
README.md
CHATGPT_START_HERE.md
guides/USER_OPERATING_GUIDE_V1.md
AI_COLLABORATION_MODE_V4.md
```

Standards and protocols inspected:

```text
standards/TASK_PACKAGE_REGISTRY_V1_1.md
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
protocols/GITHUB_AI_COLLABORATION.md
protocols/TEAM_BOSS_ROUTING.md
```

Templates and checklists inspected:

```text
templates/CODEX_TASK_PACKAGE.md
templates/CLAUDE_CODE_READONLY_ANALYSIS_TASK.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
templates/PROJECT_ROUTING_PROFILE.md
templates/CLAUDE_TEMPLATE.md
checklists/TASK_PACKAGE_REGISTRY_REVIEW.md
checklists/CODEX_BEFORE_EXECUTION_CHECK.md
```

Historical and research sources inspected:

```text
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/task-packages/PLAYBOOK-V1.1-OPERATIONAL-CLEANUP-V1.md
reports/claude/README.md
reports/codex/*
reports/claude/*
whitepapers/*
lab/*
```

Local Claude Code capability evidence from recent playbook validation:

```text
claude command path: /Users/liuxiaoqiang/.local/bin/claude
claude version: 2.1.158
non-interactive print mode: claude -p
available controls observed: --tools, --allowedTools, --permission-mode, --max-turns, --bare
known Mac constraint: GNU timeout is not available by default
```

## 5. Current Overhead Diagnosis

The current V1.1 discipline is strong, but it has become too user-facing.

Main overhead sources:

```text
1. GitHub is acting as both fact source and daily operating surface.
2. Low-risk coordination files often go through PR-style ceremony.
3. The user is repeatedly asked to care about latest pointers, reports, closeout, mergeability, and sync state.
4. Pointer mismatch is treated as a hard stop even when the active task file is clear and low risk.
5. Codex is used for too much first-pass work that Claude Code could perform under bounds.
6. Claude Code is documented mostly as reviewer or analyzer, while practical implementation-worker patterns exist but are not yet first-class.
```

Specific friction found:

```text
tasks/codex/latest.md can be ACTIVE while reports/latest.md says no active task.
The current registry language says a pointer conflict should stop execution.
For low-risk task/report work, that turns a sync lag into a false BLOCKED condition.
```

Recommended interpretation:

```text
Pointer mismatch should be a hard stop only when it creates scope ambiguity or write-risk ambiguity.
For low-risk coordination files with a clear task package and user confirmation, treat it as background sync lag, continue, and reconcile the pointers during closeout.
```

## 6. Background-Sync Operating Mode

### Target Mode

GitHub remains the single durable fact source, but user attention moves away from GitHub mechanics.

Operational target:

```text
User says what outcome is needed.
ChatGPT / Codex / Claude Code read GitHub facts in the background.
Agents update task packages, reports, latest pointers, and closeout files without repeated user prompts when risk is low.
User receives a short outcome report, not a stream of GitHub bookkeeping chores.
```

### GitHub Backend Mode

GitHub Backend Mode should be formalized as:

```text
GitHub is the append-only collaboration ledger and sync layer.
It is not the user's primary workflow UI.
The agent layer absorbs ordinary sync operations.
```

Default behavior:

```text
1. Read facts from GitHub before acting.
2. Detect active task and allowed write scope.
3. Execute within scope.
4. Write report and latest pointer automatically.
5. Clear active pointer automatically after PASS / PARTIAL PASS / FAIL / BLOCKED.
6. Commit and push direct main for low-risk coordination changes.
7. Open PR only when review or integration protection is useful.
8. Report the final result in chat.
```

User-facing behavior:

```text
The user should not need to manually inspect latest pointers, merge routine PRs, request closeouts, or confirm every coordination sync.
```

### Backend Queue Concept

Low-risk sync artifacts can be treated as backend queue items:

```text
task package -> active pointer -> execution report -> latest report -> pointer clear
```

The user only sees:

```text
task accepted
work completed
status PASS / PARTIAL PASS / FAIL / BLOCKED
next recommended action
```

### Pointer Lag Handling

Current hard-stop behavior should be replaced with a risk-sensitive rule:

```text
If tasks/codex/latest.md points to a concrete active task and the user explicitly says to execute it,
and the task allows only low-risk coordination writes,
then reports/latest.md mismatch is treated as sync lag, not BLOCKED.
```

Hard stop remains when:

```text
- repository identity is unclear
- allowed write scope is unclear
- active task points to a missing file
- two active execution lanes conflict
- the task could touch business code, production, database, secrets, deployment, or irreversible operations
```

## 7. Default-Branch / Review-Branch Routing

### Direct Main by Default

These should default to direct main when repository identity and allowed scope are clear:

```text
task packages
tasks/*/latest.md pointers
reports/*/latest.md pointers
named execution reports
reports/latest.md status synchronization
user guides
lightweight documentation
README / onboarding clarifications
templates
checklists
low-risk standards drafts
task announcements
acceptance snapshots
typo, formatting, and link fixes
small factual status updates
non-runtime archive index updates
```

Direct main requirements:

```text
1. no production impact
2. no business code behavior change
3. no secret or credential handling
4. no database or deployment action
5. no irreversible deletion
6. clear file allowlist
7. concise report or commit message
```

### PR Still Recommended

Use PR when review, integration protection, or rollback visibility has real value:

```text
business code changes
multi-file refactors
dependency changes
lockfile changes
CI or GitHub Actions changes
runtime behavior changes
deployment-related config
database migration files
large standards rewrites
cross-project policy changes
generated artifacts with review value
changes that affect test strategy or release behavior
changes where Claude Code produced substantial implementation that Codex must inspect before merge
```

### Separate Explicit Confirmation Required

These remain hard-confirmation items:

```text
API keys
secrets
credentials
auth cookies
production deployment
production database changes
schema changes against real data
irreversible delete
force push
history rewrite
destructive cleanup
service restarts that affect users
automation that can write, merge, deploy, delete, or spend money
cross-repository writes not named in the active task
```

### Main-First Routing Rule

Proposed rule:

```text
If a change is low-risk coordination work and inside an explicit allowlist, commit direct main.
If a change affects behavior, runtime, dependencies, CI, release, or broad standards, use PR.
If a change touches secrets, production, database, irreversible actions, force push, or write-capable automation, require explicit confirmation.
```

## 8. Tool Responsibility Model

### ChatGPT-Direct

Use ChatGPT direct GitHub work for:

```text
task package creation
latest pointer updates
lightweight report acceptance
small documentation updates
user-facing task announcements
GitHub issue / PR text edits
low-risk status synchronization
```

ChatGPT should not become the executor for:

```text
local tests
repository build validation
complex code integration
production actions
database actions
secret handling
```

### Claude Code

Use Claude Code as an implementation worker, not only a reviewer.

Best-fit work:

```text
deep code reading
localized bug diagnosis
first-pass file edits
mechanical multi-file changes with an allowlist
test failure first repair
low-risk refactor drafts
patch generation
draft documentation from existing facts
large diff summarization
```

Boundaries:

```text
Claude Code does not own final integration.
Claude Code does not push final changes unless a project explicitly authorizes that mode.
Claude Code outputs files, patches, logs, or reports that Codex reviews.
```

### Codex

Use Codex as final executor and integrator:

```text
repository verification
scope enforcement
Claude Code orchestration
diff review
test execution
final edits
commit
push
PR creation or merge when needed
final report
fallback when Claude Code fails or produces unsafe output
```

### GitHub

Use GitHub as:

```text
fact source
state ledger
branch and commit history
artifact registry
PR layer only when review is useful
```

Do not use GitHub as:

```text
the user's manual checklist for every low-risk coordination update
```

## 9. Claude-First / Codex-Final Model

### Principle

Claude Code should be first-pass worker when the work is bounded and expensive for Codex to do manually.

Codex should be final integrator when the work must become repository state.

### Claude-First Tasks

Default Claude-first:

```text
localized code fix draft
test failure first diagnosis and candidate patch
mechanical rename or terminology pass with file allowlist
large file reading and summarization
localized refactor draft
documentation extraction from existing code
candidate unit test generation
patch proposal for repetitive edits
review of a narrow diff before Codex integration
```

### Codex-First Tasks

Default Codex-first:

```text
active task execution and closeout
repository state verification
final diff acceptance
test command selection
commits and pushes
PR creation, update, merge, or closeout
changes involving toolchain or CI behavior
high-level routing judgment
multi-agent orchestration
any task where Claude output needs adaptation before it is safe
```

### Escalation From Claude to Codex

Codex takes over when:

```text
Claude Code cannot run
Claude Code exceeds scope
Claude Code edits files outside allowlist
Claude Code produces unclear or oversized changes
tests still fail after first repair
global design judgment is needed
final integration is required
```

### Why This Speeds Work Up

This model saves Codex time and user attention:

```text
Claude Code handles first-pass reading and draft labor.
Codex spends effort on judgment, verification, integration, and delivery.
The user receives one coherent closeout instead of managing two agents manually.
```

## 10. Claude Code First-Pass Patterns

### Pattern A: Claude Code Bounded Implementation Worker

Use when a task has a clear file allowlist and expected behavior.

Flow:

```text
1. Codex verifies repo and task scope.
2. Codex writes or selects a bounded Claude task.
3. Claude Code edits only allowed files.
4. Claude Code reports changed files, tests run, and remaining risks.
5. Codex inspects git diff.
6. Codex runs or selects tests.
7. Codex finalizes, commits, pushes, and reports.
```

Recommended controls:

```text
explicit allowed files
explicit forbidden files
max-turns
restricted tools where practical
no push
no PR
no production action
Codex diff review required
```

### Pattern B: Claude Code Patch Worker

Use when direct file mutation by Claude Code is less desirable.

Flow:

```text
1. Claude Code reads context.
2. Claude Code outputs a patch file or proposed diff.
3. Codex applies the patch selectively.
4. Codex owns final verification and commit.
```

Best for:

```text
shared modules
uncertain code paths
changes that need human-readable review before application
```

### Pattern C: Codex Invokes Claude Code Non-Interactively

Use for low-friction worker calls.

Observed local capability:

```text
claude -p "..."
```

Recommended wrapper shape:

```text
claude -p --max-turns 1 --allowedTools "<bounded tools>" "<task prompt>"
```

Mac note:

```text
Do not assume GNU timeout exists on this Mac.
If timeout behavior is required, use a local wrapper that is known to exist on macOS or implement timeout outside the shell command.
```

### Pattern D: Claude Code Direct Edit, Codex Diff Review

Use when speed matters and write scope is low risk.

Flow:

```text
1. Codex records clean git state.
2. Codex invokes Claude Code with allowed files.
3. Claude Code edits files.
4. Codex runs git diff --name-status.
5. Codex rejects out-of-scope files.
6. Codex runs tests or checks.
7. Codex commits only accepted files.
```

### Pattern E: Claude Code Read-Heavy Analyst

Use when the bottleneck is comprehension.

Flow:

```text
1. Claude Code reads a bounded code area.
2. Claude Code writes findings and candidate edit plan.
3. Codex chooses whether to implement directly or send a bounded implementation follow-up.
```

This remains useful, but should not be the only Claude Code mode.

## 11. Reference Findings

### Existing Playbook Strengths

The repository already contains stable foundations:

```text
GitHub as fact source
single active execution lane
Codex final integration role
Claude Code coordination standard
routing extensibility standard
task package templates
execution checklists
Pro review entry points
```

The missing piece is not discipline. The missing piece is a faster default route for low-risk work.

### Existing Friction to Change

Current language over-weights stopping:

```text
Pointer conflict -> stop
Low-risk docs -> often PR ceremony
Claude Code -> mostly review / analysis framing
User -> repeatedly asked to acknowledge sync state
```

Recommended change:

```text
Retain hard stops for real high risk.
Turn low-risk sync problems into agent-handled reconciliation.
```

### OpenClaw / Hermes / Skill-Style Patterns to Absorb

Do not promote OpenClaw, Hermes, MCP, automation, heartbeat, or subagent into default members merely because they are interesting.

Absorb stable patterns only:

```text
capability manifests
explicit trigger rules
allowed-tool lists
file allowlists
stop conditions
bounded worker prompts
evidence reports
project-scoped routing profiles
skill-style task packaging
```

Stable rule:

```text
Borrow the routing and capability description pattern.
Do not add new default runtime dependencies until they are proven and explicitly authorized.
```

## 12. Proposed Follow-Up Files

Recommended next files to add or update:

```text
standards/GITHUB_BACKEND_MODE_V1.md
standards/MAIN_FIRST_ROUTING_V1.md
standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md
standards/CLAUDE_FIRST_CODEX_FINAL_V1.md
templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
templates/CLAUDE_PATCH_WORKER_TASK.md
templates/CODEX_CLAUDE_INVOCATION_PATTERNS.md
checklists/HIGH_RISK_CONFIRMATION_GATE.md
templates/PROJECT_ROUTING_PROFILE.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
guides/USER_OPERATING_GUIDE_V1.md
```

Recommended edits:

```text
1. Add GitHub Backend Mode as a standard operating mode.
2. Add main-first routing table.
3. Replace blanket pointer-conflict stop with risk-sensitive sync-lag handling.
4. Add maximum practical authorization tiers.
5. Add Claude-first / Codex-final standard.
6. Add concrete Claude Code worker templates.
7. Update user guide so the user sees short task announcements, not GitHub mechanics.
```

## 13. Pro Review Notes

### 给 Pro 的实现问题

Pro review should not only audit wording. It should decide how to land this mode.

#### 1. GitHub 后台化

Implementation questions:

```text
How should task/latest/report/closeout writes be collapsed into one backend sync operation?
Which files are safe for ChatGPT-direct or Codex-direct main writes?
How should pointer lag be represented without becoming BLOCKED?
Should reports/latest.md become a summary index while tasks/*/latest.md remains the active execution source?
```

#### 2. main-first

Implementation questions:

```text
What exact file classes are direct-main by default?
Should direct-main require a fixed commit message prefix?
Should low-risk standards drafts be direct-main while accepted stable standards still use PR?
How should main-first work when the local branch is behind origin/main?
```

#### 3. 最大实用授权

Implementation questions:

```text
What can ChatGPT, Codex, and Claude Code do without asking again?
Which operations need only after-the-fact reporting?
Which operations need pre-confirmation every time?
How should "ordinary project file" be defined per repository?
How should a project override default authorization tiers?
```

#### 4. Claude-first / Codex-final

Implementation questions:

```text
Which task types should automatically invoke Claude Code first?
Which Claude Code modes can write files directly?
Which modes must output patches only?
How should Codex detect and reject out-of-scope Claude Code changes?
What minimum evidence should Claude Code return for Codex review?
```

#### 5. OpenClaw / Hermes / skill-style 路由和能力清单

Implementation questions:

```text
Which stable patterns can be absorbed without adding experimental tools as default members?
Should each tool have a capability manifest with allowed actions, forbidden actions, and escalation rules?
Can skill-style files define project-scoped triggers and bounded worker modes?
How should Hermes / OpenClaw remain optional until project facts authorize them?
```

## 14. Validation

Commands requested by task:

```text
git status -sb
git branch --show-current
git fetch origin --prune
git diff --check origin/main...HEAD
```

Observed before writing:

```text
git status -sb: ## main...origin/main
git branch --show-current: main
git fetch origin --prune: completed
baseline HEAD: 8726e0d0a1bdacc7aeaac2578ef3da40c63ac754
```

Validation to perform after writing:

```text
git diff --check
git diff --check origin/main...HEAD
git status -sb
```

Write-scope validation:

```text
Only allowed files should change:
- reports/codex/playbook-v1-1-process-speed-research-v1.md
- reports/codex/latest.md
- tasks/codex/latest.md
```

## 15. Remaining Issues

Remaining issues are design follow-ups, not blockers for this report:

```text
1. standards/TASK_PACKAGE_REGISTRY_V1_1.md still contains conservative pointer-conflict stop language.
2. The stable user guide does not yet fully hide GitHub mechanics from the user.
3. Claude Code implementation-worker templates are not yet first-class files.
4. Main-first routing is proposed here but not yet added as a stable standard.
5. Maximum practical authorization tiers are proposed here but not yet codified.
```

No stable standard was modified in this task because the active task explicitly limited writes to reports and latest pointers.

## 16. Next Step

Recommended next task for ChatGPT / Pro:

```text
Create a small implementation task to add:
- standards/GITHUB_BACKEND_MODE_V1.md
- standards/MAIN_FIRST_ROUTING_V1.md
- standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md
- standards/CLAUDE_FIRST_CODEX_FINAL_V1.md
- templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
- templates/CLAUDE_PATCH_WORKER_TASK.md

Then update the user guide and task registry so low-risk sync lag no longer blocks execution.
```

Recommended immediate operating rule:

```text
For low-risk coordination files, use direct main.
For runtime-impacting changes, use PR.
For secrets, production, database, irreversible delete, force push, and write-capable automation, require explicit confirmation.
```
