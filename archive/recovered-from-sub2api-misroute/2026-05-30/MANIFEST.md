# MANIFEST｜sub2api-maijian misroute recovery｜2026-05-30

## 1. 误写原因

另一个 ChatGPT / GitHub connector 会话原计划初始化：

```text
liuxiaoqianglongxia/ai-collaboration-playbook
```

但 GitHub connector 路由错误，把 AI 协作总规范库文件写入了业务仓库：

```text
liuxiaoqianglongxia/sub2api-maijian
```

这些文件属于 AI 协作总规范库，不属于 `sub2api-maijian` 业务仓库。本 manifest 只记录素材抢救状态，不清理来源仓库。

## 2. 来源与目标

```text
source_repository: liuxiaoqianglongxia/sub2api-maijian
source_commit: f542c0101f2a44396ee07b9f466a99607789eda5
target_repository: liuxiaoqianglongxia/ai-collaboration-playbook
target_branch: main
recovery_date: 2026-05-30
archive_root: archive/recovered-from-sub2api-misroute/2026-05-30/
```

## 3. 状态说明

```text
recovered: 已在目标 archive 中保存恢复副本。
missing_at_source_commit: 在 source commit 中读取不到，无法归档。
skipped_with_reason: 本轮未归档，有明确原因。
```

## 4. 文件清单

| source_path | archive_path | status | notes |
|---|---|---|---|
| `README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/README.md` | recovered | 来源为 `liuxiaoqianglongxia/sub2api-maijian@f542c0101f2a44396ee07b9f466a99607789eda5`；与当前正式 README 不同，归档内容不代表最新规范。 |
| `AI_AGENT_ONBOARDING.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/AI_AGENT_ONBOARDING.md` | recovered | 来源 commit 固定为 `f542c0101f2a44396ee07b9f466a99607789eda5`；归档内容作为误写素材保留。 |
| `AI_COLLABORATION_MODE_V4.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/AI_COLLABORATION_MODE_V4.md` | recovered | 来源版本为长版/白皮书化素材；不覆盖当前 V4 主链路。 |
| `NEW_PROJECT_BOOTSTRAP.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/NEW_PROJECT_BOOTSTRAP.md` | recovered | 已按来源误写原文归档；不覆盖当前正式版本。 |
| `modules/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/modules/README.md` | recovered | 已按来源误写原文归档；不覆盖当前正式 `modules/README.md`。 |
| `templates/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/templates/README.md` | recovered | 已按来源误写原文归档；不覆盖 V0.2 templates。 |
| `checklists/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/checklists/README.md` | recovered | 已按来源误写原文归档；不覆盖 V0.2 checklists。 |
| `lab/CODEX_AGENTIC_WORKBENCH_V0_1.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/CODEX_AGENTIC_WORKBENCH_V0_1.md` | recovered | 已按来源误写原文归档；不覆盖当前 lab 正式版本。 |
| `lab/CODEX_HERMES_TRANSLATION_NOTES.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/CODEX_HERMES_TRANSLATION_NOTES.md` | recovered | 已按来源误写原文归档；不覆盖当前 lab 正式版本。 |
| `lab/experiments/001-heartbeat-readonly.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/001-heartbeat-readonly.md` | recovered | 已按来源误写原文归档。 |
| `lab/experiments/002-skill-start-here-audit.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/002-skill-start-here-audit.md` | recovered | 已按来源误写原文归档。 |
| `lab/experiments/003-subagent-readonly-scout.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/003-subagent-readonly-scout.md` | recovered | 已按来源误写原文归档。 |
| `lab/experiments/004-memory-distillation.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/004-memory-distillation.md` | recovered | 已按来源误写原文归档，修复提交见本轮 recovery repair。 |
| `lab/experiments/005-mcp-docs-context.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/005-mcp-docs-context.md` | recovered | 已按来源误写原文归档，修复提交见本轮 recovery repair。 |
| `reports/latest.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md` | skipped_with_reason | 本轮只允许处理 MANIFEST、recovery report、reports/latest、whitepapers/README.md 四个收口文件；该 archive 目标仍未写入。后续若要完全 PASS，需要单独授权补写该归档文件。 |

## 5. 当前结论

PARTIAL PASS。

15 个目标归档项中，14 个已 recovered；`archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md` 因本轮写入范围限制未补写，状态为 `skipped_with_reason`。

## 6. 后续清理许可

不建议现在清理 `sub2api-maijian`。

建议先单独授权补齐 `archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md`，或明确确认该项不可恢复/不需要恢复；之后再由 `sub2api-maijian` 项目总控单独执行污染治理。
