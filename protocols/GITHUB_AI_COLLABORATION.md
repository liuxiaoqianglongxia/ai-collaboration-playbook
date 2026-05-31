# GitHub AI Collaboration Protocol

> **Purpose**: Define how ChatGPT, GitHub, Codex, and Claude Code collaborate using GitHub as the central hub without making GitHub maintenance the user's daily burden.
> **Version**: 1.1
> **Maintained in**: `ai-collaboration-playbook/protocols/GITHUB_AI_COLLABORATION.md`

---

## 1. Four-Piece Model

| Role | Agent | Metaphor | Core Responsibility |
|------|-------|----------|---------------------|
| Total Control | ChatGPT | Brain | Communication, judgment, task packages, acceptance, lightweight GitHub writes when available |
| Fact Source | GitHub | Memory | Save facts, tasks, reports, decisions, code, acceptance evidence |
| Delivery Lead | Codex | Hands | Local execution, integration, tests, PR, delivery reports |
| Engineering Muscle | Claude Code | Muscle | Code exploration, draft fixes, failure analysis, review |

V1.1 does not add a fifth default member. Hermes, Qwen, MCP, automation, heartbeat, and subagents are optional project-specific tools only.

## 2. Design Goal

The user-facing layer must stay simple:

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

The user should be able to say a short goal. The system behind it may be complex, but the complexity belongs to ChatGPT, GitHub, Codex, Claude Code, and project files.

## 3. How ChatGPT Uses GitHub

ChatGPT should read GitHub before judging current project status:

1. Read `CHATGPT_START_HERE.md` when present.
2. Read `CURRENT.md` when present.
3. Read `TASKS.md` when present.
4. Read `DECISIONS.md` when present.
5. Read `reports/latest.md`.
6. If V1.1 registry exists, read `tasks/codex/latest.md`, `tasks/claude/latest.md`, `reports/codex/latest.md`, and `reports/claude/latest.md`.
7. Read only the source files relevant to the task.

Never act on chat history alone when repository facts are needed.

## 4. How GitHub Serves as Fact Source

GitHub holds the authoritative state through these files:

| File | Purpose | Update Trigger |
|------|---------|----------------|
| `CHATGPT_START_HERE.md` | New-session entry | Project onboarding or major status shift |
| `CURRENT.md` | Project state card | Phase change, milestone, risk identified |
| `TASKS.md` | Task list and lifecycle | Task created, completed, blocked |
| `tasks/codex/latest.md` | Current Codex task pointer | ChatGPT assigns or clears Codex task package |
| `tasks/claude/latest.md` | Current Claude Code task pointer | ChatGPT assigns or clears Claude Code task package |
| `DECISIONS.md` | Decision log | Architecture choice made, alternative rejected |
| `AGENTS.md` | Execution rules | Team composition, repo commands, safety boundary |
| `CLAUDE.md` | Claude Code boundary | Local review or analysis mode changes |
| `reports/latest.md` | Latest project-level result | Execution or acceptance closes out |
| `reports/codex/latest.md` | Latest Codex result | Codex completes work |
| `reports/claude/latest.md` | Latest Claude Code result | Claude Code completes review or analysis |
| `reports/chatgpt/task-packages/` | ChatGPT task and acceptance snapshots | Task package or acceptance issued |
| Source code | Application logic | Code changes committed and reviewed |

GitHub is the source of truth, but the user should not be forced to operate every detail manually.

## 5. ChatGPT Direct-Work Rule

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

## 6. Codex Execution Rule

Codex is the delivery lead that turns assigned tasks into integrated results:

1. Receive task packages from `tasks/codex/latest.md` when the registry exists.
2. Verify repository identity, branch, and allowed scope.
3. Execute the task: apply fixes, run tests, verify.
4. Use Claude Code or other local tools only within task boundaries.
5. Commit with clear messages following project conventions.
6. Push to a feature branch or prepare the requested diff.
7. Create PR when required.
8. Report delivery results to `reports/codex/latest.md`.

Codex should not infer scope from chat when a GitHub task package exists.

## 7. Claude Code Coordination Rule

Claude Code is a local engineering enhancement tool. It should be used when it adds real value:

```text
deep code reading
call-chain analysis
complex bug localization
local fix drafts
review or second opinion
```

Claude Code does not replace Codex as final integrator.

Users should not be asked to manually relay long Claude Code tasks when Codex can coordinate Claude Code through `tasks/claude/latest.md`.

## 8. Risk-Based Routing

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

High-risk task:

```text
Production, deployment, database, secrets, data deletion, force push, service restart, automation publish chain.
Must use a separate safety task package and explicit user authorization.
```

## 9. Branches and PRs

| Scenario | Branch Pattern | Notes |
|----------|----------------|-------|
| Small doc fix by ChatGPT | direct or `docs/...` | Direct write is acceptable only when low risk and allowed by user/context |
| Small code fix | `fix/short-description` | PR preferred |
| Feature | `feature/feature-name` | May require multiple PRs |
| Audit | `audit/audit-type-date` | Read-only, no code changes |
| Experiment | `experiment/experiment-name` | High risk, clear labeling |
| Emergency | `hotfix/issue-description` | Fast track, minimal scope |

Do not force push unless explicitly authorized.

## 10. PR and Report Traceability

Every significant change should be traceable:

1. Task in `TASKS.md` or `tasks/*/latest.md`.
2. Branch or direct commit according to risk.
3. PR when appropriate.
4. Report written.
5. ChatGPT acceptance from GitHub facts.

If a task is blocked, the reason should appear in the relevant task/report files, not only in chat.

## 11. Preventing Copy-Paste Chaos

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