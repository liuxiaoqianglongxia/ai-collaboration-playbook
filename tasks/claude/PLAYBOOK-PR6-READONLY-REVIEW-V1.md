# PLAYBOOK-PR6-READONLY-REVIEW-V1

## 1. Task Name

```text
PLAYBOOK-PR6-READONLY-REVIEW-V1
```

## 2. Review / Analysis Goal

Perform a read-only review of PR #6 and its `TASK-PACKAGE-REGISTRY-V1.1` candidate standard.

Review goals:

- Check whether PR #6 breaks the V4 four-piece model.
- Check whether any non-default component is being reintroduced as a default member.
- Check whether Claude Code is described as final integrator.
- Check whether Codex is described as project controller.
- Check whether ChatGPT is described as execution-environment operator.
- Check whether templates contain business-project content.
- Check whether `tasks/codex/latest.md` and `tasks/claude/latest.md` are executable and do not conflict with `reports/latest.md`.
- Check whether the rollout wave avoids direct business project modification.

## 3. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
branch: docs/task-package-registry-v1-1
pr: #6
```

## 4. Current Project State

Read:

```text
README.md
reports/latest.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
tasks/README.md
tasks/codex/latest.md
tasks/claude/latest.md
rollouts/TASK_PACKAGE_REGISTRY_ROLLOUT_WAVE1.md
```

## 5. Allowed Scope

```text
Read current PR #6 diff.
Read this repository's documentation.
Generate a review report at reports/claude/playbook-pr6-readonly-review-v1.md.
Update reports/claude/latest.md only if the task runner is explicitly authorized to write the report.
```

## 6. Forbidden Scope

```text
Do not modify playbook standards or templates.
Do not submit commits.
Do not deploy.
Do not modify databases.
Do not modify secrets.
Do not touch business projects.
Do not handle sub2api-maijian.
Do not promote lab experiments to stable modules.
```

## 7. Required Work

1. Verify repository identity and branch.
2. Read PR #6 diff and the files listed above.
3. Review role boundaries, registry executability, template neutrality, and rollout safety.
4. Write findings to `reports/claude/playbook-pr6-readonly-review-v1.md`.
5. Use only `PASS`, `PARTIAL PASS`, `FAIL`, or `BLOCKED`.

## 8. Validation

Read-only checks should include:

```text
git diff --name-only origin/main...HEAD
git diff --check origin/main...HEAD
grep for prohibited role-boundary drift
grep for business-project content in generic templates
```

## 9. Report Format

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Repository:
Branch:
PR:
Files inspected:
Findings:
Validation:
Forbidden scope confirmation:
Next step:
```

## 10. Stop Conditions

Stop and report `BLOCKED` when:

- repository identity is unclear;
- PR #6 branch is not available;
- review requires modifying standards or templates;
- review requires business project access;
- review requires production, deployment, database, secret, or automation access.

## 11. Next Step

After the Claude Code report exists, ChatGPT should perform independent read-only acceptance of PR #6.
