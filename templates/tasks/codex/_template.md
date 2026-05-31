# Codex Task Package Template

## 0. User-Facing Summary

```text
任务：<TASK-ID>
能实现：
- <one concrete outcome>
- <one concrete outcome>
- <one concrete outcome>
不做：<key boundary>
你发给 Codex：执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
详情：任务包已在 GitHub。
```

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

## 5. Execution Lane Status

```text
current_codex_lane: ACTIVE_CODEX_TASK / NO_ACTIVE_CODEX_TASK
current_claude_lane: ACTIVE_CLAUDE_TASK / NO_ACTIVE_CLAUDE_TASK
one_active_execution_lane: required
new_findings_policy: record as candidate next steps unless this task explicitly authorizes scope update
```

Stop if another active Codex task already exists for the same stage and is not this task.

## 6. Claude Code Coordination

```text
claude_code_allowed: yes / no
claude_code_required: yes / no
claude_code_forbidden: yes / no
coordination_mode: Codex coordinates inside this active Codex task
final_integrator: Codex
```

Claude Code does not replace Codex as final integrator. Claude Code output is evidence, not direct merge, deploy, or final-status authority.

## 7. Allowed Scope

List files, directories, commands, or environments Codex may use.

## 8. Forbidden Scope

List files, directories, commands, environments, and actions Codex must not touch.

## 9. Required Work

1. Verify repository identity and branch.
2. Read required fact-source files.
3. Complete the allowed work.
4. Validate the result.
5. Write a report.
6. Prepare a PR if requested.

## 10. Validation

List required checks, tests, inspections, or read-only verifications.

## 11. Report Format

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Repository:
Branch:
Files changed:
Validation:
Forbidden scope confirmation:
Next step:
```

## 12. Stop Conditions

Stop and report `BLOCKED` when repository identity, branch, fact source, allowed scope, execution lane state, or safety boundary cannot be verified.

## 13. Next Step

State what should happen after PASS, PARTIAL PASS, FAIL, or BLOCKED.
