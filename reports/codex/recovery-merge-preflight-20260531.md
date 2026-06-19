# Recovery Merge Preflight — 2026-05-31

> **Task**: `playbook-recovery-merge-preflight-and-env-ownership-v1`
> **Repository**: `liuxiaoqianglongxia/ai-collaboration-playbook`
> **Local path**: `/Users/liuxiaoqiang/code/ai-collaboration-playbook`
> **Generated**: 2026-05-31
> **Executed by**: Mac Codex

---

## 1. Conclusion

**PARTIAL PASS**

The controlled local merge preflight was completed on a temporary branch, and the merge result was clearly determined. The preflight cannot be marked `PASS` because `git merge --no-commit --no-ff origin/recovery/sub2api-misroute-20260530` produced a content conflict in `reports/latest.md`.

No conflict was resolved. The merge was aborted. No merge commit was created.

## 2. Current Repository

```text
liuxiaoqianglongxia/ai-collaboration-playbook
```

Remote:

```text
origin https://github.com/liuxiaoqianglongxia/ai-collaboration-playbook.git
```

README title verified:

```text
# AI 协作总规范库
```

## 3. Current Local Branch

```text
integration/recovery-merge-preflight-20260531
```

This branch was created from:

```text
origin/main
```

## 4. origin/main HEAD

```text
e0679572cdd3cc8fcafd78f902fa10418606b7c2
```

## 5. origin/recovery HEAD

```text
1840a24884e3cac6ce84b799413089514cf12706
```

Branch:

```text
origin/recovery/sub2api-misroute-20260530
```

## 6. merge-base

```text
102784ad7025a153d71153df58f1cabe5576e14d
```

## 7. Diverged

**Yes.**

```text
origin/main unique commits: 5
origin/recovery/sub2api-misroute-20260530 unique commits: 7
```

The branches share the merge-base above and both contain commits not present in the other branch.

## 8. Local `merge --no-commit` Result

Command executed on the temporary branch:

```text
git merge --no-commit --no-ff origin/recovery/sub2api-misroute-20260530
```

Result:

```text
Auto-merging reports/latest.md
CONFLICT (content): Merge conflict in reports/latest.md
Automatic merge failed; fix conflicts and then commit the result.
```

Follow-up action:

```text
git merge --abort
```

Final merge state:

```text
aborted; no merge commit created
```

## 9. Conflict Status

**Conflicts found: yes**

## 10. Conflict File List

```text
reports/latest.md
```

No conflict resolution was attempted.

## 11. Files The Merge Would Affect

From:

```text
git diff --name-status origin/main...origin/recovery/sub2api-misroute-20260530
```

Result:

```text
M	archive/recovered-from-sub2api-misroute/2026-05-30/MANIFEST.md
A	archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md
M	reports/latest.md
M	reports/recovery/sub2api-misroute-20260530.md
A	whitepapers/AI_COLLABORATION_MODE_V4_FULL_WHITEPAPER.md
A	whitepapers/CODEX_AGENTIC_WORKBENCH_RESEARCH_DRAFT.md
A	whitepapers/GPT_SUBSCRIPTION_ENGINEERING_WORKFLOW_ARTICLE.md
```

During the attempted merge, Git also staged or prepared the same recovery-side file changes, with `reports/latest.md` left unmerged.

## 12. Main Audit Content Overwrite Risk

**No direct overwrite of main's existing large audit content was observed in the merge preflight.**

The conflict is limited to `reports/latest.md`, which is a latest-report pointer/status file. Main's existing audit and template-pack files, including `reports/codex/wsl-asset-audit-closeout-20260530.md`, `reports/codex/collaboration-template-pack-v1.md`, `reports/codex/collaboration-template-pack-v1-postfix.md`, `standards/`, `templates/`, `checklists/`, and `protocols/`, were not listed as files modified by the merge preflight.

Risk note: choosing the recovery version of `reports/latest.md` during a future manual resolution would replace main's current latest-report status text. That would not delete the large audit files, but it could make the visible latest report point backward unless reconciled carefully.

## 13. New Execution Environment Ownership Standard

Created:

```text
standards/EXECUTION_ENVIRONMENT_OWNERSHIP.md
```

The draft states:

- `ai-collaboration-playbook` general standards repository work is preferably owned by Mac Codex.
- Business projects, local WSL, production environment, database, and deployment work are preferably owned by Windows Codex.
- Large audits, historical resource archives, and low-risk material migrations may be assigned to Mac Codex or Windows Codex by source repository and risk.
- Before such work begins, the agent must verify `repository_full_name`, `branch`, README title, and allowed write scope.

## 14. PR Recommendation

**Yes, open a PR for this temporary branch if the controller wants to preserve the preflight report and ownership draft.**

Do not directly merge `origin/recovery/sub2api-misroute-20260530` into `main` until `reports/latest.md` is manually reconciled.

## 15. Audit Freeze Recommendation

**Yes. Continue freezing audit/history-resource integration decisions until the `reports/latest.md` conflict is reviewed and resolved by controller-approved policy.**

The recovery branch can still be reviewed, but automatic merge should remain blocked.

## 16. Prohibited Scope Confirmation

Confirmed:

```text
未直接写 main。
未 force push。
未合并 PR。
未处理 sub2api-maijian。
未进入 V0.3。
未创建 examples/。
未做 Claude Code 测试。
未接入自动化。
未改 V4 主链路正文。
未处理微信公众号仓库。
未修改 .env、cookie、auth、数据库或部署配置。
```

## 17. Next Recommendations

1. Review `reports/latest.md` manually and decide the correct latest-report state after recovery plus main audit/template-pack work.
2. If the ownership draft is accepted, open a PR from `integration/recovery-merge-preflight-20260531`.
3. Keep the recovery branch unmerged until the `reports/latest.md` conflict is explicitly resolved.
4. Do not route `sub2api-maijian`, V0.3 examples, Claude Code testing, or WeChat repository work through this task.

## 18. Allowed Files Written In This Task

```text
standards/EXECUTION_ENVIRONMENT_OWNERSHIP.md
reports/codex/recovery-merge-preflight-20260531.md
reports/codex/latest.md
```
