# Claude Bounded Implementation Task

> Use only when Codex coordinates Claude Code inside an active Codex task.

## Parent Codex Task

```text
task:
repository:
branch:
final_integrator: Codex
```

## Goal

Describe the narrow first-pass implementation Claude Code should attempt.

## Allowed Scope

- `<file-or-directory>`

## Forbidden Scope

- secrets, credentials, cookies, `.env`
- production deployment
- database writes or migrations
- force push, commit, tag, PR, merge
- unrelated files

## Required Work

1. Verify repository and branch.
2. Read the parent task and allowed files.
3. Make only the bounded first-pass change.
4. Summarize changed files and reasoning.
5. Stop before commit, push, PR, tag, deploy, or final status.

## Output

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Files changed:
Validation run:
Risks:
What Codex must verify:
```

Claude Code output is evidence. Codex owns the final diff and report.
