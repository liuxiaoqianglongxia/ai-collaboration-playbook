# Playbook Claude Code Task Package Template

## 1. Task Name

```text
<task-id>
```

## 2. Review / Analysis Goal

Describe the concrete read-only review or analysis goal for the playbook repository.

## 3. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
branch: <branch-name>
base_commit: <sha-or-unknown>
```

## 4. Current Project State

List the playbook fact-source files Claude Code must read before review.

## 5. Allowed Scope

List files, directories, or diffs Claude Code may inspect.

## 6. Forbidden Scope

List files, directories, projects, commands, environments, and actions Claude Code must not touch.

## 7. Required Work

1. Verify repository identity and branch.
2. Read required fact-source files.
3. Perform only the requested read-only review.
4. Validate findings against GitHub facts.
5. Write a report if authorized.

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
