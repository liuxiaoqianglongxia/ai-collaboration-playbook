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
source_branch: main
source_head_at_read: f542c0101f2a44396ee07b9f466a99607789eda5
target_repository: liuxiaoqianglongxia/ai-collaboration-playbook
target_branch: main
archive_root: archive/recovered-from-sub2api-misroute/2026-05-30/
```

## 3. 状态说明

```text
recovered: 已在目标 archive 中保存恢复副本。
missing: 来源疑似存在或曾经存在，但本轮未能确认目标 archive 中已有原样恢复副本。
skipped_existing_project_file: 目标正式目录已有独立版本，本轮不把归档内容覆盖正式规范。
recovered_differs_from_current: 已归档，但与当前正式目录版本不同，不能直接作为最新规范。
```

## 4. 文件清单

| 来源路径 | 目标归档路径 | 来源 commit / 证据 | 状态 | 是否已提炼到正式目录 | 后续是否允许清理 sub2api-maijian |
|---|---|---|---|---|---|
| `README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/README.md` | current source head `f542c0101f2a44396ee07b9f466a99607789eda5`; fetched from source branch | recovered_differs_from_current | partially: target `README.md` has independent current index | yes, after B-line confirms restore/cleanup plan |
| `AI_AGENT_ONBOARDING.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/AI_AGENT_ONBOARDING.md` | `7911d8f027e3d998f0df37d69e3886fc3e34ff2f` | recovered_differs_from_current | partially: target has independent onboarding file | yes, after B-line confirms restore/cleanup plan |
| `AI_COLLABORATION_MODE_V4.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/AI_COLLABORATION_MODE_V4.md` | `d79e92b32886fe80ca68b835329b5e968e961bf5` | recovered_differs_from_current | yes, but archive version is long-form / whitepaper-like source, not current short spec | yes, after B-line confirms restore/cleanup plan |
| `NEW_PROJECT_BOOTSTRAP.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/NEW_PROJECT_BOOTSTRAP.md` | `3908b73a7e10e5f2a96eabcd4e8a3e8ed9d6ffa7` | missing | target has independent formal version | not yet; recover original first |
| `modules/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/modules/README.md` | `06ce5fd1a4acb5456272fb10f019229522db6f39` | missing | target has independent formal version | not yet; recover original first |
| `templates/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/templates/README.md` | `455b28e24acf2708cf34098f9fdebc5a5033c60d` | missing | target V0.2 has expanded version | not yet; recover original first |
| `checklists/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/checklists/README.md` | `982272c68307e1a62baf266cbe685460ab1bb0ae` | missing | target V0.2 has expanded version | not yet; recover original first |
| `lab/CODEX_AGENTIC_WORKBENCH_V0_1.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/CODEX_AGENTIC_WORKBENCH_V0_1.md` | `3548135be51e79e46cdce855a853ee8b30818e3a` | missing | target has independent formal version | not yet; recover original first |
| `lab/CODEX_HERMES_TRANSLATION_NOTES.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/CODEX_HERMES_TRANSLATION_NOTES.md` | `272154b66fbbf55c42d87fad704e8bff146cb1c3` | missing | target has independent formal version | not yet; recover original first |
| `lab/experiments/001-heartbeat-readonly.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/001-heartbeat-readonly.md` | `b950416b6360a603f7cc9bed75995b606c7b1445` | missing | target has independent formal version | not yet; recover original first |
| `lab/experiments/002-skill-start-here-audit.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/002-skill-start-here-audit.md` | `2f2955f0388090fff963734ed793e2d5e1f3bf7e` | missing | target has independent formal version | not yet; recover original first |
| `lab/experiments/003-subagent-readonly-scout.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/003-subagent-readonly-scout.md` | `8f0d6b55ab5e99ab1d4913a279d0fcd404e8601b` | missing | target has independent formal version | not yet; recover original first |
| `lab/experiments/004-memory-distillation.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/004-memory-distillation.md` | `3dd694d2ef99bba69ba2d2fc72967edc1ef479e9` | missing | target has independent formal version | not yet; recover original first |
| `lab/experiments/005-mcp-docs-context.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/005-mcp-docs-context.md` | `cb9574f47378bd8857e7f66a368318a457e72aba` | missing | target has independent formal version | not yet; recover original first |
| `reports/latest.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md` | initial `eed31a170acd85b81ed2f4015850e8eefc4362fb`; current source head `f542c0101f2a44396ee07b9f466a99607789eda5` | missing | target `reports/latest.md` will be updated to recovery status | not yet; recover original first |

## 5. 当前结论

PARTIAL PASS。

已确认 misroute 来源、来源仓库、来源分支、来源 head、关键误写提交链，并且目标仓库已有 3 个核心恢复文件与 `whitepapers/README.md`。但并非全部疑似误写文件都已原样归档，因此不能给 PASS。

## 6. 后续清理许可

不建议立即清理 `sub2api-maijian`。

建议下一步先进入：

```text
Full Misroute Archive Completion
```

补齐所有 `missing` 项的原样归档后，再由 `sub2api-maijian` 项目总控单独执行污染治理。
