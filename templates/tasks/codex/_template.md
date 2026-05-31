# Codex Task Package Template

## 1. Task Name

```text
<task-id>
```

## 2. Goal

Describe the concrete, verifiable outcome for Codex.

## 3. Repository

```text
repository_full_name: <owner/name>
branch: <branch-name>
base_commit: <sha-or-unknown>
```

## 4. Current Project State

List the GitHub fact-source files that define the current state.

## 5. Allowed Scope

List files, directories, commands, or environments Codex may use.

## 6. Forbidden Scope

List files, directories, commands, environments, and actions Codex must not touch.

## 7. Required Work

1. Verify repository identity and branch.
2. Read required fact-source files.
3. Complete the allowed work.
4. Validate the result.
5. Write a report.
6. Prepare a PR if requested.

## 8. Validation

List required checks, tests, inspections, or read-only verifications.

## 9. Report Format

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Repository:
Branch:
Files changed:
Validation:
Forbidden scope confirmation:
Next step:
```

## 10. Stop Conditions

Stop and report `BLOCKED` when repository identity, branch, fact source, allowed scope, or safety boundary cannot be verified.

## 11. Next Step

State what should happen after PASS, PARTIAL PASS, FAIL, or BLOCKED.
