# GitHub AI Collaboration Protocol

> **Purpose**: Define how ChatGPT, GitHub, Claude Code, and Codex collaborate using GitHub as the central hub.
> **Version**: 1.0
> **Maintained in**: `ai-collaboration-playbook/protocols/GITHUB_AI_COLLABORATION.md`

---

## The Four-Piece Model

| Role | Agent | Metaphor | Core Responsibility |
|------|-------|----------|-------------------|
| Total Control | ChatGPT | Brain | Communication, judgment, task packages, acceptance |
| Memory | GitHub | Memory | Save facts, tasks, reports, decisions, code |
| Delivery Lead | Codex | Hands | Task scheduling, integration, PR, delivery reports |
| Engineering Muscle | Claude Code | Muscle | Code exploration, draft, failure analysis, review |

## How ChatGPT Reads GitHub

1. **Read `CURRENT.md` first** — understand project state before any judgment.
2. **Read `TASKS.md`** — know what work is open and who owns it.
3. **Read `DECISIONS.md`** — understand past decisions and their reasoning.
4. **Read relevant source files** — only the files needed for the current task.
5. **Never act on chat history alone** — if it's not in GitHub, it doesn't exist.

## How GitHub Serves as Fact Source

GitHub holds the authoritative state through these files:

| File | Purpose | Update Trigger |
|------|---------|---------------|
| `CURRENT.md` | Project state card | Phase change, milestone hit, risk identified |
| `TASKS.md` | Task list | Task created, completed, blocked |
| `DECISIONS.md` | Decision log | Architecture choice made, alternative rejected |
| `AGENTS.md` | Role rules | Team composition changes |
| `reports/` | Execution reports | Agent completes a task |
| Source code | Application logic | Code changes committed and reviewed |

## How Claude Code Generates Local Reports

Claude Code operates locally and produces reports that feed back to GitHub:

1. **Explore**: Read files, understand code, identify issues.
2. **Analyze**: Compare actual state against expected behavior.
3. **Report**: Write findings to `reports/claude/latest.md` or a dated report.
4. **Recommend**: Suggest fixes but do not apply them without authorization.

Report format follows the Execution Report Template.

## How Codex Integrates

Codex is the delivery lead that turns plans into shipped code:

1. **Receive** task packages from ChatGPT via `TASKS.md`.
2. **Execute** the task: apply fixes, run tests, verify.
3. **Commit** with clear messages following project conventions.
4. **Push** to a feature branch.
5. **Create PR** with description linking to relevant reports.
6. **Report** delivery results to `reports/codex/latest.md`.

## How to Use Branches for Tasks

| Scenario | Branch Pattern | Notes |
|----------|---------------|-------|
| Small fix | `fix/short-description` | Direct PR to main |
| Feature | `feature/feature-name` | May require multiple PRs |
| Audit | `audit/audit-type-date` | Read-only, no code changes |
| Experiment | `experiment/experiment-name` | High risk, clear labeling |
| Emergency | `hotfix/issue-description` | Fast track, minimal scope |

## How to Use PRs and Reports for Traceability

Every significant change should be traceable:

1. **Task** in `TASKS.md` → **Branch** created → **PR** opened → **Report** written.
2. PR description should reference the task ID and link to relevant Claude Code reports.
3. Acceptance criteria from the task must be verifiable from the PR.
4. If a task is blocked, the reason should be in `TASKS.md` AND in the PR comments.

## How to Prevent Copy-Paste Chaos

The #1 failure mode in AI collaboration is relying on chat history instead of GitHub:

1. **No state in chat**: If project state changes, update GitHub files — don't just tell the agent in chat.
2. **No code in chat**: If code changes, commit to a branch — don't paste diffs in chat.
3. **No decisions in chat**: If a decision is made, record in `DECISIONS.md` — don't just agree in chat.
4. **New session = fresh read**: Every new ChatGPT session must re-read GitHub files from scratch.
5. **Chat is for direction, not facts**: Use chat to say "do X" — not to describe what X should do in detail when `TASKS.md` already exists.
