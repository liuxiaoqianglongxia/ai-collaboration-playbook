# Claude Code Task Package Template

## 1. Task Name

```text
<task-id>
```

## 2. Review / Analysis Goal

Describe the concrete read, review, analysis, or local engineering support goal.

## 3. Repository

```text
repository_full_name: <owner/name>
branch: <branch-name>
base_commit: <sha-or-unknown>
```

## 4. Current Project State

List the GitHub fact-source files that define the current state.

## 5. Allowed Scope

List files, directories, commands, or local checks Claude Code may use.

## 6. Forbidden Scope

List files, directories, commands, environments, and actions Claude Code must not touch.

## 7. Required Work

1. Verify repository identity and branch.
2. Read required fact-source files.
3. Perform only the requested review or analysis.
4. Validate findings against the fact source.
5. Write a report or return findings in the requested format.

## 8. Validation

List required read-only checks, local inspections, or evidence requirements.

## 9. Report Format

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Repository:
Branch:
Files inspected:
Findings:
Validation:
Forbidden scope confirmation:
Next step:
```

## 10. Stop Conditions

Stop and report `BLOCKED` when repository identity, branch, fact source, allowed scope, or safety boundary cannot be verified.

## 11. Next Step

State what should happen after PASS, PARTIAL PASS, FAIL, or BLOCKED.
