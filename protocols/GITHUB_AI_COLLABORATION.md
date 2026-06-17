# GitHub AI Collaboration Protocol

> **Purpose**: Define how ChatGPT, Drive, GitHub, Codex, and Claude Code collaborate without making repository maintenance the user's daily burden.
> **Version**: 1.2
> **Status**: historical compatibility protocol. Current default baseline is `PLAYBOOK_OPERATIONAL_BASELINE_V2`; read `QUICK_START.md`, `standards/DRIVE_NATIVE_WORKFLOW_V2.md`, and `protocols/drive-native-v2/` first.
> **Maintained in**: `ai-collaboration-playbook/protocols/GITHUB_AI_COLLABORATION.md`

---

## 1. Four-Piece Model

| Role | Agent | Metaphor | Core Responsibility |
|------|-------|----------|---------------------|
| Total Control | ChatGPT | Brain | Communication, judgment, task packages, acceptance, lightweight GitHub writes when available |
| Fact Source | GitHub | Memory | Save facts, tasks, reports, decisions, code, acceptance evidence |
| Delivery Lead | Codex | Hands | Local execution, integration, tests, PR, delivery reports |
| Engineering Muscle | Claude Code | Muscle | Code exploration, draft fixes, failure analysis, review |

V1.2 does not add a fifth default engineering member. Drive is a daily workbench layer, not a code executor or final fact source. Hermes, Qwen, MCP, automation, heartbeat, and subagents are optional project-specific tools only.

## 2. Design Goal

The user-facing layer must stay simple:

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

The user should be able to say a short goal. The system behind it may be complex, but the complexity belongs to ChatGPT, Drive daily files, GitHub durable facts, Codex, Claude Code, and project files.

## 3. How ChatGPT Uses GitHub

In V2, ChatGPT reads the project Drive workbench for daily facts and GitHub for stable facts. For projects that still use this historical GitHub-backed protocol, ChatGPT should read GitHub before judging stable project status:

1. Read `CHATGPT_START_HERE.md` when present.
2. Read `CURRENT.md` when present.
3. Read `TASKS.md` when present.
4. Read `DECISIONS.md` when present.
5. Read `reports/latest.md`.
6. If a GitHub-backed registry compatibility layer exists, read `tasks/codex/latest.md`, `tasks/claude/latest.md`, `reports/codex/latest.md`, and `reports/claude/latest.md`.
7. Read only the source files relevant to the task.

Never act on chat history alone when repository facts are needed.

## 4. Drive Daily Workbench And GitHub Fact Source

Drive may hold daily working material:

```text
tasks
reports
screenshots
handoffs
temporary acceptance notes
materials and exports
```

GitHub remains the durable milestone source:

```text
main code
task packages
reports
decisions
acceptance snapshots
tags
production references
rollback anchors
```

Drive notes should sync back to GitHub when they become execution instructions, milestone decisions, acceptance evidence, release anchors, production references, or rollback references.

## 5. How GitHub Serves as Fact Source

For projects that explicitly enable GitHub-backed compatibility, GitHub holds repository-level state through these files. In V2, Drive remains the default daily fact source.

| File | Purpose | Update Trigger |
|------|---------|----------------|
| `CHATGPT_START_HERE.md` | New-session entry | Project onboarding or major status shift |
| `CURRENT.md` | Project state card | Phase change, milestone, risk identified |
| `TASKS.md` | Task list and lifecycle | Task created, completed, blocked |
| `tasks/codex/latest.md` | Compatibility Codex task pointer | ChatGPT assigns or clears repository-backed Codex task package |
| `tasks/claude/latest.md` | Compatibility Claude Code task pointer | ChatGPT assigns or clears repository-backed Claude Code task package |
| `DECISIONS.md` | Decision log | Architecture choice made, alternative rejected |
| `AGENTS.md` | Execution rules | Team composition, repo commands, safety boundary |
| `CLAUDE.md` | Claude Code boundary | Local review or analysis mode changes |
| `reports/latest.md` | Latest project-level result | Execution or acceptance closes out |
| `reports/codex/latest.md` | Latest Codex result | Codex completes work |
| `reports/claude/latest.md` | Latest Claude Code result | Claude Code completes review or analysis |
| `reports/chatgpt/task-packages/` | ChatGPT task and acceptance snapshots | Task package or acceptance issued |
| Source code | Application logic | Code changes committed and reviewed |
| Tags | Version anchors | dev-ok, pre-prod, prod, rollback, or project-specific milestones |

GitHub is the source of truth, but the user should not be forced to operate every detail manually.

## 6. ChatGPT Direct-Work Rule

ChatGPT is not merely a dispatcher.

If the current ChatGPT session has GitHub write access and the work is safe, ChatGPT may directly:

```text
update documentation
write task packages
update latest pointers
write acceptance snapshots
update lightweight reports
revise PR descriptions
perform read-only acceptance
```

ChatGPT should not hand these tasks to Codex merely to prove that Codex exists.

If the current ChatGPT session does not have GitHub write access, ChatGPT must say so clearly and must not claim that a task package or report has been written to GitHub.

## 7. Codex Execution Rule

Codex is the delivery lead that turns assigned tasks into integrated results:

1. Receive task packages from Drive by default, or from `tasks/codex/latest.md` when the GitHub-backed registry compatibility layer is explicitly enabled.
2. Verify repository identity, branch, and allowed scope.
3. Execute the task: apply fixes, run tests, verify.
4. Use Claude Code or other local tools only within task boundaries.
5. Commit with clear messages following project conventions.
6. Push to main when the task is low-risk and direct-main is authorized.
7. Create a tag when the task needs a version, production, or rollback anchor.
8. Create PR when review or integration protection is useful.
9. Report delivery results to `reports/codex/latest.md`.

Codex should not infer scope from chat when a GitHub task package exists.

One stage should have one active execution lane. If `tasks/codex/latest.md` already points to `ACTIVE_CODEX_TASK`, do not create another active Codex task for the same stage. New findings should be recorded as candidate next steps until the active task reports `PASS`, `PARTIAL PASS`, `FAIL`, or `BLOCKED`.

## 8. Claude Code Coordination Rule

Claude Code is a local engineering enhancement tool. It should be used when it adds real value:

```text
bounded first-pass implementation
deep code reading
call-chain analysis
complex bug localization
local fix drafts
review or second opinion
```

Claude Code does not replace Codex as final integrator.

Codex should coordinate Claude Code through a bounded prompt, patch-worker task, or `tasks/claude/latest.md` when that adds value.

Claude Code outputs are report evidence, not final authority. Codex verifies the output, decides what enters the final diff, and remains final integrator.

## 8.1 User-Facing Task Announcement

When ChatGPT assigns a V2 Drive task package, chat should stay short:

```text
任务：<TASK-ID>
能实现：
- <one concrete outcome>
- <one concrete outcome>
- <one concrete outcome>
不做：<key boundary>
你发给 Codex：任务已写入 Drive：tasks/codex/YYYYMMDD/<task-name>.md；请读取该任务包执行，完成后写 Drive 报告。
详情：任务包已在 Drive。
```

Use the old repository-backed latest-pointer wording only when a project explicitly enables the GitHub-backed compatibility registry. Do not paste the full task package in chat as routine behavior, and do not claim it is in Drive or GitHub unless the file exists there.

## 9. Risk-Based Routing

Light task:

```text
ChatGPT may directly update docs, task packages, pointers, reports, or acceptance notes.
```

Normal engineering task:

```text
ChatGPT writes the task package.
Codex executes and reports.
ChatGPT accepts.
```

Medium-risk task:

```text
Codex may coordinate Claude Code for review, failure analysis, or local fix drafts.
```

V2 normal engineering task:

```text
Drive holds daily task packages and reports.
GitHub holds stable outcomes, release notes, rollback notes, or milestone reports.
Codex executes in WSL/local Git.
Claude Code may provide first-pass support.
Codex pushes main, tags, or opens PR according to task risk.
```

High-risk task:

```text
Production, deployment, database, secrets, data deletion, force push, service restart, automation publish chain.
Must use a separate safety task package and explicit user authorization.
```

## 10. Main, Tags, Branches, And PRs

Default:

```text
main only
```

Use tags for version anchors:

```text
dev-ok-YYYYMMDD
pre-prod-YYYYMMDD
prod-YYYYMMDD
rollback-before-YYYYMMDD
```

Use branches only when a real review or integration boundary is useful. Do not use branches as version records.

| Scenario | Branch Pattern | Notes |
|----------|----------------|-------|
| Small doc fix by ChatGPT | direct or `docs/...` | Direct write is acceptable only when low risk and allowed by user/context |
| Small code fix | `fix/short-description` | PR preferred |
| Feature | `feature/feature-name` | May require multiple PRs |
| Audit | `audit/audit-type-date` | Read-only, no code changes |
| Experiment | `experiment/experiment-name` | High risk, clear labeling |
| Emergency | `hotfix/issue-description` | Fast track, minimal scope |

Do not force push unless explicitly authorized.

## 11. PR, Tag, And Report Traceability

Every significant change should be traceable:

1. Task in `TASKS.md` or `tasks/*/latest.md`.
2. Branch or direct commit according to risk.
3. Tag when a version, production, or rollback anchor is needed.
4. PR when appropriate.
5. Report written.
6. ChatGPT acceptance from durable facts.

If a task is blocked, the reason should appear in the relevant task/report files, not only in chat.

## 12. Preventing Copy-Paste Chaos

The main failure mode is relying on chat history instead of GitHub:

1. No state in chat only: if project state changes, update GitHub files.
2. No code in chat only: if code changes, commit or create a PR.
3. No decisions in chat only: record key decisions in `DECISIONS.md`.
4. New session means fresh read from GitHub.
5. Chat is for direction and judgment; GitHub is for durable facts.

But the reverse failure also matters: do not turn GitHub into busywork for the user.

The correct balance is:

```text
User: short goal / short approval / short review.
ChatGPT: reads, judges, writes lightweight facts, validates.
Codex: executes heavy local work and reports.
Claude Code: supports deep local engineering when useful.
GitHub: keeps the durable state.
```
