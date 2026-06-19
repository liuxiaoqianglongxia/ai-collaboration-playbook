# Codex Task Package Template

task_id: <TASK-ID>
mode: DRIVE_NATIVE_V2
owner: Codex
daily_fact_source: Google Drive
github_role: stable version / release / rollback / final reusable docs

## Goal

- <verifiable outcome>

## Allowed Scope

- <Drive path or repo path>

## Forbidden Scope

- production
- databases
- secrets
- unrelated repositories
- force push
- main, tags, protected branches, and unmerged branches

## Steps

1. Read Drive current state and task files.
2. Read GitHub facts when branch, PR, tag, or release work is required.
3. Make scoped changes.
4. Run checks.
5. Write a named report in Drive.
6. Sync reusable stable output to GitHub only when needed.

## Acceptance

Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
