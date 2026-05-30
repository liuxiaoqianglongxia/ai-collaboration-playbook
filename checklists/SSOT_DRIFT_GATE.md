# SSOT Drift Gate Checklist

> **Purpose**: Detect and prevent drift from the Single Source of Truth (SSOT).
> **Applies to**: Any project using GitHub as the fact source.
> **Run before**: Starting any new agent session, before merging branches, before declaring a task complete.

---

## What Is SSOT Drift?

SSOT drift occurs when the actual state of a project diverges from what the fact source (GitHub) records. Common causes:
- Local changes not committed or pushed
- Chat history contains decisions not recorded in `DECISIONS.md`
- `CURRENT.md` is outdated relative to actual project phase
- Multiple working copies on different branches without synchronization
- Cross-environment conflicts (e.g., same project on two different WSL instances)

## Common Drift Types

| Type | Symptom | Severity |
|------|---------|----------|
| **Uncommitted drift** | `git status` shows modified files | Medium |
| **Unpushed drift** | `git log @{upstream}..HEAD` shows commits not on remote | Medium |
| **Branch drift** | Local branch is behind or ahead of remote | High |
| **Documentation drift** | `CURRENT.md` / `TASKS.md` don't match reality | Medium |
| **Cross-environment drift** | Same project on two machines with different states | Critical |
| **Secret exposure drift** | Sensitive files accidentally tracked in git | Critical |

## GitHub Fact Source Check

- [ ] Repository exists and is accessible
- [ ] Default branch matches expected branch name
- [ ] `CURRENT.md` exists on the remote branch
- [ ] `TASKS.md` exists on the remote branch
- [ ] Most recent commit on remote matches expected state
- [ ] No open PRs that conflict with current work
- [ ] `.gitignore` covers sensitive patterns (`.env`, `*.db`, `auth.json`)

## Local Workspace Check

- [ ] `git status` is clean (or changes are intentional and tracked)
- [ ] Current branch is the expected branch
- [ ] No untracked files that should be committed
- [ ] No sensitive files in the working tree are tracked by git

## Branch Check

- [ ] Local branch is not behind remote (`git pull --ff-only` succeeds or you know why it doesn't)
- [ ] Local commits have descriptive messages
- [ ] No merge commits that weren't intentional

## Uncommitted / Unpushed Check

| Check | Command | Pass Criteria |
|-------|---------|--------------|
| Uncommitted changes | `git status --porcelain` | Empty or intentional |
| Unpushed commits | `git log @{upstream}..HEAD --oneline` | Empty or intentional |
| Untracked files | `git status --porcelain \| grep '^??'` | Only expected untracked files |

## Cross-WSL Conflict Check

When the same project exists on multiple machines (e.g., WSL-hermes and WSL-codex):

- [ ] Both machines are on the same branch
- [ ] Both machines have pulled latest from remote
- [ ] No conflicting uncommitted changes on either machine
- [ ] If different branches: clear understanding of which is the active line

## Decision Gate

Answer these questions to determine if it's safe to proceed:

| Question | Yes → | No → |
|----------|-------|------|
| Is the remote branch accessible? | Proceed to next check | **BLOCKED** |
| Is local workspace clean (or intentionally dirty)? | Proceed | Commit or stash first |
| Are CURRENT.md and TASKS.md up to date? | Proceed | Update them before proceeding |
| Are there cross-environment conflicts? | Resolve before proceeding | Proceed |
| Is the expected branch checked out? | Proceed | Switch branch |

### Final Verdict

| Condition | Verdict |
|-----------|---------|
| All checks pass | **SAFE TO PROCEED** |
| Minor issues (uncommitted intentional changes, documentation slightly stale) | **PROCEED WITH NOTES** — update docs as first task |
| Major issues (branch drift, cross-environment conflicts, unpushed critical commits) | **STOP** — resolve drift before proceeding |
| Critical issues (secret exposure, production database in repo) | **EMERGENCY** — remove sensitive files immediately, rotate credentials |
