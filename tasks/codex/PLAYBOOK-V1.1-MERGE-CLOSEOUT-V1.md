# PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1

## 1. Task Name

```text
PLAYBOOK-V1.1-MERGE-CLOSEOUT-V1
```

## 2. Goal

- Merge PR #6 only after ChatGPT independent acceptance returns `PASS`.
- After merge, update `reports/latest.md` from `PLAYBOOK_OPERATIONAL_BASELINE_V1.1_CANDIDATE / PARTIAL PASS` to `PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS`.
- Write a merge closeout report.
- Do not modify business projects.
- Do not modify `AI_COLLABORATION_MODE_V4.md`.
- Do not add automation.

## 3. Repository

```text
repository_full_name: liuxiaoqianglongxia/ai-collaboration-playbook
target_pr: #6
base: main
head: docs/task-package-registry-v1-1
```

## 4. Current Project State

Read before execution:

```text
README.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
tasks/codex/latest.md
tasks/claude/latest.md
```

## 5. Allowed Scope

Only after ChatGPT acceptance `PASS`:

```text
PR #6 merge
reports/latest.md
reports/codex/
```

## 6. Forbidden Scope

```text
business projects
AI_COLLABORATION_MODE_V4.md
lab/
archive/
whitepapers/
deployment
database
secrets
automation
force push
```

## 7. Required Work

1. Verify ChatGPT has explicitly accepted PR #6 with `PASS`.
2. Verify PR #6 base, head, clean mergeability, and head SHA.
3. Merge PR #6 using a normal merge commit unless the controller specifies otherwise.
4. Fetch and read `origin/main`.
5. Update closeout status only in the explicitly authorized files.
6. Write the closeout report.
7. Do not delete branches unless explicitly authorized.

## 8. Validation

```text
gh pr view 6 --json state,mergeable,mergeStateStatus,headRefName,baseRefName,headRefOid,baseRefOid
git fetch origin main --prune
git rev-parse origin/main
git show origin/main:reports/latest.md
```

## 9. Report Format

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Merge method:
PR:
Merge commit:
main HEAD:
Files read:
Files changed:
Forbidden scope confirmation:
Next step:
```

## 10. Stop Conditions

Stop and report `BLOCKED` when:

- ChatGPT has not explicitly accepted PR #6 with `PASS`.
- PR #6 is not clean or mergeable.
- PR #6 head SHA changed and has not been re-reviewed.
- Work would require modifying a business project, production environment, database, secret, deployment path, or automation.
- Work would require modifying `AI_COLLABORATION_MODE_V4.md`.

## 11. Next Step

After a successful closeout, ChatGPT may declare `PLAYBOOK_OPERATIONAL_BASELINE_V1.1 / PASS`.
