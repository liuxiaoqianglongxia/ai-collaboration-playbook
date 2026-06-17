# Playbook Codex Task Package Template

## 1. Task Name

```text
<task-id>
```

## 2. Goal

Describe the concrete playbook maintenance outcome for Codex.

## 3. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
branch: <branch-name>
base_commit: <sha-or-unknown>
```

## 4. Current Project State

List the playbook fact-source files that define the current state.

## 5. Allowed Scope

List the playbook files Codex may read or modify.

## 6. Forbidden Scope

List files, directories, projects, commands, environments, and actions Codex must not touch.

## 7. Required Work

1. Verify repository identity and branch.
2. Read required fact-source files.
3. Complete only the allowed playbook maintenance work.
4. Validate the result.
5. Write a Codex report.
6. Prepare or update a PR if requested.

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
