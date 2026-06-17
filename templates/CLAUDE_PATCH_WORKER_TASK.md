# Claude Patch Worker Task

> Use when Claude Code should propose a patch but not edit the working tree.

## Parent Codex Task

```text
task:
repository:
branch:
final_integrator: Codex
```

## Goal

Describe the patch or implementation approach needed.

## Inputs

- `<file-or-directory>`
- `<log-or-report>`

## Forbidden Actions

- no file edits
- no commits
- no push, tag, PR, merge
- no production, database, credential, or deployment work

## Output Format

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Patch summary:
Suggested diff or file-by-file changes:
Risks:
Validation Codex should run:
```

Codex decides whether to apply, edit, or reject the patch.
