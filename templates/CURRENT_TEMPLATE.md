# CURRENT Template — Project State Card

> **Purpose**: The single source of truth for "what is this project doing right now."
> **Applies to**: Any project using the four-piece AI collaboration pattern (ChatGPT + GitHub + Claude Code + Codex).
> **Place at**: Project root as `CURRENT.md`.

> **Template Authority**: This file is an upstream template from `ai-collaboration-playbook`. When copied into a project repository, remove the `_TEMPLATE` suffix and customize project-specific fields. The project-local copy becomes the execution authority for that project, while this template remains the upstream baseline.

## How to use

- Update this file every time the project phase changes or a milestone is hit.
- ChatGPT reads this FIRST in every new session — before reading anything else.
- Never rely on chat history for project state. If it's not in this file or GitHub, it doesn't exist.

---

## Project: [Project Name]

| Field | Value |
|-------|-------|
| **Status** | ACTIVE / FROZEN / ARCHIVED / EXPERIMENTAL / PRODUCTION / DEPRECATED / BLOCKED |
| **Branch** | `feature/xxx` or `main` |
| **Last Commit** | `[hash] [message]` |
| **Phase** | [Current phase name, e.g. "MVP Delivery", "Production Hardening"] |
| **Fact Source** | This GitHub repository is the single source of truth |

## Current Tasks

> Point to TASKS.md for the full list. Summarize only the active P0 here.

- [ ] P0: [Task description] — Assigned to: [Claude Code / Codex / ChatGPT]
- [ ] P0: [Task description] — Assigned to: [Claude Code / Codex / ChatGPT]

## Current Freeze Items

> What should NOT be changed right now.

- [Frozen area]: [Reason]

## Current Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| [Risk description] | High / Medium / Low | [What to do] |

## Last Acceptance

| Date | Result | Verified by | Notes |
|------|--------|-------------|-------|
| YYYY-MM-DD | PASS / PARTIAL PASS / FAIL | [Agent or human] | [Brief note] |

## Next Steps

1. [Next action, who does it, expected output]
2. [Next action, who does it, expected output]

## Prohibited Actions

- [What must NOT be done, e.g. "Do not merge to main without acceptance check"]
- [What must NOT be done]

## Handoff Entry for New Agents

> When a new ChatGPT / Claude Code / Codex session starts, read in this order:

1. This file (`CURRENT.md`) — project state
2. `TASKS.md` — task list
3. `DECISIONS.md` — decision history
4. `AGENTS.md` — role definitions
5. `CLAUDE.md` — Claude Code instructions (if applicable)
6. `CHATGPT_START_HERE.md` — ChatGPT session entry guide
