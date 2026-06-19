# Claude Code Hardening Checklist

> **Purpose**: Ensure Claude Code operates safely within defined boundaries on any project.
> **Applies to**: All Claude Code sessions, especially read-only audits and local engineering tasks.
> **Place at**: Project `checklists/CLAUDE_CODE_HARDENING.md` or include in `CLAUDE.md`.

---

## Before Execution

- [ ] Read `CLAUDE.md` for project-specific rules
- [ ] Read `AGENTS.md` for role boundaries
- [ ] Read `CURRENT.md` for project state
- [ ] Identify the task scope: what files are in-bounds, what is out-of-bounds
- [ ] Confirm current git branch and workspace state
- [ ] Confirm whether this Claude Code task is bounded support inside an active Codex task
- [ ] Confirm Codex remains final integrator

## Safe Path Check

| Path Pattern | Allowed | Reason |
|-------------|---------|--------|
| `*.md` files | Yes | Documentation, reports, templates |
| Source code (`*.py`, `*.ts`, `*.js`) | Yes (within task scope) | Engineering tasks |
| `docs/`, `reports/`, `templates/` | Yes | Documentation directories |
| `.env`, `.env.*`, `*.env` | **NO** | Contains secrets |
| `auth.json`, `auth.json.bak*` | **NO** | Authentication credentials |
| `*token*`, `*key*`, `*secret*`, `*cred*` | **NO** | Tokens and keys |
| `*.db`, `*.sqlite`, `*.sqlite3` | **NO** | Database contents |
| `logs/`, `backups/`, `sessions/`, `pastes/` | **NO** | Runtime data |
| `node_modules/`, `dist/`, `build/`, `venv/` | **NO** | Generated directories |
| `.git/` (internal) | **NO** | Git internals |

## Shell Command Safety

| Command Category | Allowed | Notes |
|-----------------|---------|-------|
| Read-only (`cat`, `head`, `grep`, `find`, `ls`) | Yes | Standard exploration |
| Git read (`git status`, `git log`, `git diff`) | Yes | Always safe |
| Git write (`git add`, `git commit`, `git push`) | Only if task requires | Verify diff first |
| Package install (`npm install`, `pip install`) | Only with authorization | Can introduce dependencies |
| Destructive (`rm`, `mv`, `git reset`) | **NO without explicit authorization** | Always confirm with user first |
| Network (`curl`, `wget`) | Only if task requires | May expose tokens in URLs |

## Sub-Agent Boundaries

When launching sub-agents:
- [ ] Sub-agent must receive the same prohibited-file rules
- [ ] Sub-agent scope must be narrower than parent task
- [ ] Do not delegate understanding — synthesize findings yourself
- [ ] Report sub-agent results concisely; do not dump raw output
- [ ] Verify sub-agent didn't modify files outside its scope

## Backup Before Modification

Before modifying any file that isn't clearly a draft or temp file:
- [ ] Note the original content in the report
- [ ] Use `git diff` to verify changes before committing
- [ ] For critical files, recommend the user review before applying

## Diff Check

Before any commit:
- [ ] Run `git diff` and review every changed line
- [ ] Verify no sensitive paths are included
- [ ] Verify the diff matches the task scope
- [ ] Check for accidentally staged files: `git diff --cached --name-only`

## Pre-Commit Check

- [ ] Only files related to the task are staged
- [ ] No `.env`, `*.db`, `auth.json`, `node_modules/`, `logs/`, `backups/`
- [ ] No `*.tar.gz`, `*.zip`, or other archives
- [ ] Commit message is clear and describes the "why" not just the "what"
- [ ] Commit message contains no secrets or sensitive information

## Stop Conditions

Stop immediately and report if:
1. A prohibited file must be read to continue the task.
2. Project source code must be modified outside the task scope.
3. Sensitive content will be committed (detected in diff check).
4. Git workspace is in an unexpected dirty state.
5. Uncertain which file is the single source of truth.
6. The task requires production environment changes.
7. The task asks Claude Code to replace Codex as final integrator.
7. A security vulnerability or exposed secret is discovered.
