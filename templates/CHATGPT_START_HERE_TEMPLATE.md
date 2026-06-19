# CHATGPT Start Here — New Session Entry Point

> **Purpose**: The first file ChatGPT should read when starting a new session on this project.
> **Applies to**: Any ChatGPT session (GPT-4o, o1, o3) entering this project.
> **Place at**: Project root as `CHATGPT_START_HERE.md` or link to it from a pinned comment.

> **Template Authority**: This file is an upstream template from `ai-collaboration-playbook`. When copied into a project repository, remove the `_TEMPLATE` suffix and customize the project card, read order, and task delegation examples. The project-local copy becomes the execution authority for that project, while this template remains the upstream baseline.

## How to use

- Pin this file in the ChatGPT conversation or project instructions.
- ChatGPT reads this FIRST, then follows the pointers to other files.
- Never rely on chat history for project state — always read files from GitHub.

---

## New Session Read Order

When you enter this project, read files in this exact order:

1. `CHATGPT_START_HERE.md` — This file. Understand the project context.
2. `CURRENT.md` — What is the project doing RIGHT NOW? What phase? What risks?
3. `TASKS.md` — What tasks are open? What is P0?
4. `AGENTS.md` — What are your role boundaries? What can/can't you do?
5. `DECISIONS.md` — What decisions have been made? Why?
6. `CLAUDE.md` — If Claude Code is active, what are its rules?

## Current Project Card

| Field | Value |
|-------|-------|
| **Project** | [Project name] |
| **Repository** | [GitHub URL] |
| **Current Branch** | [branch name] |
| **Current Phase** | [phase name] |
| **Status** | ACTIVE / FROZEN / ARCHIVED / EXPERIMENTAL / PRODUCTION / DEPRECATED / BLOCKED |
| **Fact Source** | This GitHub repository — chat history is NOT the fact source |

## How to Judge Results

| Status | When |
|--------|------|
| **PASS** | All acceptance criteria met, tests pass, no risks introduced, push succeeded |
| **PARTIAL PASS** | Core task done but some items need follow-up, or minor issues found |
| **FAIL** | Acceptance criteria not met, tests fail, or introduced regressions |
| **BLOCKED** | Cannot proceed due to missing context, access issues, or risks detected |

## How to Give Tasks to Claude Code / Codex

### To Claude Code
- Give specific file paths and clear questions.
- Ask for read-only analysis first, then draft fixes.
- Do NOT delegate architecture — you own that.
- Example: "Read `src/auth.py` lines 45-120. Check if the token validation handles expired tokens. Report findings with line numbers."

### To Codex
- Give complete task packages: goal, acceptance criteria, constraints.
- Codex is the integration lead — it runs tests and creates PRs.
- Example: "Apply the fix from Claude Code's audit at `reports/claude/latest.md`. Run all tests. Create a PR if tests pass. Write a delivery report."

## How to Avoid Relying on Chat History

1. **Always read files from GitHub** before making judgments.
2. **Never assume** the project state from a previous conversation.
3. **Update `CURRENT.md`** every time the project phase changes.
4. **Update `TASKS.md`** every time tasks are completed or created.
5. **Use `DECISIONS.md`** to record why decisions were made.
6. **Chat history is for communication only** — not for facts, code, or state.
