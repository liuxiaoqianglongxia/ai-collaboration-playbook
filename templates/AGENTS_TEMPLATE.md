# AGENTS Template — Multi-Agent Collaboration Rules

> **Purpose**: Define role boundaries, responsibilities, and working rules for AI agents on this project.
> **Applies to**: Any project using AI collaboration (2-role, 3-role, or 4-piece pattern).
> **Place at**: Project root as `AGENTS.md`.

## How to use

- Choose the role configuration that matches your team size (2-role or 3-role).
- All agents must read this file before taking any action.
- Do not modify another agent's files without explicit authorization.

---

## Project Boundaries

| Field | Value |
|-------|-------|
| **Project** | [Project name] |
| **Repository** | [GitHub URL] |
| **Primary Language** | [Python / TypeScript / etc.] |
| **Deployment** | [WSL / Server / Docker / Local] |

## Role Configuration

### Option A: Two-Role Pattern (Small Project)

| Role | Agent | Responsibilities |
|------|-------|------------------|
| Total Control / Architect | ChatGPT | Task decomposition, architecture judgment, acceptance criteria, task packages |
| Engineering Executor | Claude Code | Code exploration, draft implementation, analysis, local fixes |

### Option B: Three-Role Pattern (Standard Project)

| Role | Agent | Responsibilities |
|------|-------|------------------|
| Total Control / Architect | ChatGPT | Task decomposition, architecture, acceptance, task packages |
| Local Engineering | Claude Code | Code exploration, draft, analysis, local fixes, audit |
| Integration / Delivery | Codex | Task scheduling, integration, PR creation, testing, delivery reports |

### Option C: Four-Piece Pattern (Full Collaboration)

| Role | Agent | Metaphor | Responsibilities |
|------|-------|----------|------------------|
| Total Control | ChatGPT | Brain | Communication, judgment, task packages, acceptance |
| Memory | GitHub | Memory | Save facts, tasks, reports, decisions, code — the single source of truth |
| Delivery Lead | Codex | Hands | Task scheduling, integration, PR, delivery reports |
| Engineering Muscle | Claude Code | Muscle | Code exploration, draft, failure analysis, review |

## Iron Laws

1. **GitHub is the single source of truth** — Chat history does not count.
2. **Do not act without reading GitHub first** — Always read `CURRENT.md`, `TASKS.md`, `DECISIONS.md` before starting.
3. **One file, one editor at a time** — Never have two agents modifying the same file simultaneously.
4. **Read-only before write** — Always audit the current state before making changes.

## What Each Agent CAN Do

### ChatGPT (Total Control)
- [ ] Read all files and assess project state
- [ ] Create task packages in TASKS.md
- [ ] Define acceptance criteria
- [ ] Review reports and make decisions
- [ ] Direct Claude Code and Codex to specific tasks

### Claude Code (Local Engineering)
- [ ] Read and analyze code without modification
- [ ] Draft fixes and patches (clearly marked as drafts)
- [ ] Run tests and report results
- [ ] Create audit reports
- [ ] Review changes for correctness and safety

### Codex (Integration / Delivery)
- [ ] Execute task packages from ChatGPT
- [ ] Run tests and verify fixes
- [ ] Create PRs with proper descriptions
- [ ] Write delivery reports
- [ ] Integrate changes from multiple sources

## What Each Agent MUST NOT Do

### All Agents
- Must NOT read `.env`, `auth.json`, token files, database contents
- Must NOT modify files outside the task scope
- Must NOT force push or bypass safety checks
- Must NOT merge to main without acceptance verification

### Claude Code
- Must NOT run destructive commands (`rm -rf`, `git reset --hard`) without explicit authorization
- Must NOT expose secrets in commit messages or reports

### Codex
- Must NOT push to protected branches without review
- Must NOT deploy without rollback plan

## File Modification Rules

1. Before modifying any file, read it first and understand its purpose.
2. Before committing, run `git diff` to verify changes.
3. Before pushing, ensure all acceptance criteria are met.
4. Never commit without a clear, descriptive message.

## Testing Requirements

| Project Type | Minimum Requirement |
|-------------|---------------------|
| Library | All existing tests pass; new code has tests |
| Web App | Smoke test passes; no regressions in main flows |
| Infrastructure | Dry-run succeeds; rollback plan documented |

## Commit Requirements

- Clear, descriptive commit message (imperative mood)
- Only include files related to the task
- No `.env`, `*.db`, `auth.json`, `node_modules/`, `logs/`, `backups/`
- Follow existing commit message conventions

## Production Environment Boundaries

| Rule | Description |
|------|-------------|
| No direct production modification | All changes go through staging first |
| Rollback plan required | Every production change must have a documented rollback |
| Production health check | Verify after deployment: [Health check URL] |
| Production data is read-only | Never modify production data directly |

## Report Format

When an agent completes a task, produce a report in this format:

```markdown
# [Task Name] Execution Report

**Status**: PASS / PARTIAL PASS / FAIL / BLOCKED
**Branch**: [branch name]
**Commit**: [hash]
**Files Modified**: [list]
**Test Results**: [summary]
**Safety Confirmation**: [confirmed items]
**Unresolved Items**: [if any]
**Next Steps**: [recommendations]
```
