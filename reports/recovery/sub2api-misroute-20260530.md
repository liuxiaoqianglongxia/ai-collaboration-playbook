# Recovery Report｜sub2api-maijian misroute｜2026-05-30

## 1. 结论

PASS

## 2. 来源仓库

```text
liuxiaoqianglongxia/sub2api-maijian
```

## 3. 来源 commit

```text
f542c0101f2a44396ee07b9f466a99607789eda5
```

## 4. 目标仓库

```text
liuxiaoqianglongxia/ai-collaboration-playbook
```

## 5. 目标分支

```text
recovery/sub2api-misroute-20260530
```

## 6. 归档目录

```text
archive/recovered-from-sub2api-misroute/2026-05-30/
```

## 7. recovered 文件列表

```text
archive/recovered-from-sub2api-misroute/2026-05-30/README.md
archive/recovered-from-sub2api-misroute/2026-05-30/AI_AGENT_ONBOARDING.md
archive/recovered-from-sub2api-misroute/2026-05-30/AI_COLLABORATION_MODE_V4.md
archive/recovered-from-sub2api-misroute/2026-05-30/NEW_PROJECT_BOOTSTRAP.md
archive/recovered-from-sub2api-misroute/2026-05-30/modules/README.md
archive/recovered-from-sub2api-misroute/2026-05-30/templates/README.md
archive/recovered-from-sub2api-misroute/2026-05-30/checklists/README.md
archive/recovered-from-sub2api-misroute/2026-05-30/lab/CODEX_AGENTIC_WORKBENCH_V0_1.md
archive/recovered-from-sub2api-misroute/2026-05-30/lab/CODEX_HERMES_TRANSLATION_NOTES.md
archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/001-heartbeat-readonly.md
archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/002-skill-start-here-audit.md
archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/003-subagent-readonly-scout.md
archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/004-memory-distillation.md
archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/005-mcp-docs-context.md
archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md
```

```text
recovered_count: 15
```

## 8. missing_at_source_commit 文件列表

无。

```text
missing_at_source_commit_count: 0
```

## 9. MANIFEST 路径

```text
archive/recovered-from-sub2api-misroute/2026-05-30/MANIFEST.md
```

## 10. whitepapers/README.md 是否存在

存在。

```text
whitepapers/README.md
```

## 11. 是否建议进入 Full Whitepaper Recovery

建议进入。

理由：误写素材已经完整归档到 recovery 分支，长版白皮书恢复可以基于 archive 内容继续推进。

## 12. 是否建议现在清理 sub2api-maijian

不建议现在清理。

`sub2api-maijian` 污染治理必须由该项目总控单独处理。本 PR 只处理 `ai-collaboration-playbook` 的 V0.2.5 Recovery，不删除、不恢复、不修改 `sub2api-maijian`。

## 13. 本轮 commit hash

本报告随 PR head commit 一起提交；准确 commit hash 见 PR head 与最终回报。

## 14. 是否 push

是。通过 GitHub connector 推送到分支：

```text
recovery/sub2api-misroute-20260530
```

## 15. 禁止范围确认

```text
未直接写 main。
未进入 V0.3。
未创建 examples/。
未做 Claude Code 测试。
未写 whitepaper 正文。
未接入自动化。
未改业务代码。
未改敏感配置。
未改数据库。
未部署。
未写 sub2api-maijian。
未清理 sub2api-maijian。
未处理微信公众号仓库。
```
