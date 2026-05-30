# Recovery Report｜sub2api-maijian misroute｜2026-05-30

## 1. 结论

PARTIAL PASS

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

目标分支：

```text
main
```

## 5. 实际归档文件列表

已 recovered：

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
```

## 6. missing_at_source_commit 文件列表

无。

```text
missing_at_source_commit_count: 0
```

## 7. skipped_with_reason 文件列表

```text
archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md
```

原因：本轮用户明确限定只允许处理以下 4 个收口文件：

```text
archive/recovered-from-sub2api-misroute/2026-05-30/MANIFEST.md
reports/recovery/sub2api-misroute-20260530.md
reports/latest.md
whitepapers/README.md
```

因此本轮未补写 archive 下的 `reports/latest.md`。如需让 V0.2.5 Recovery Repair 达到完整 PASS，需要单独授权补写该归档文件，或明确确认该项不需要恢复。

## 8. MANIFEST 路径

```text
archive/recovered-from-sub2api-misroute/2026-05-30/MANIFEST.md
```

## 9. whitepapers/README.md 是否存在

存在。

```text
whitepapers/README.md
```

## 10. 是否允许进入 sub2api-maijian 清理

不建议现在清理。

理由：archive 目标中仍有 1 项 `skipped_with_reason`。建议先补齐或明确确认该项不需要恢复，再由 `sub2api-maijian` 项目总控单独处理污染清理。

## 11. 是否允许进入 Full Whitepaper Recovery

暂不建议立即进入。

建议先完成 archive 完整性收口，尤其是 `archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md` 的处置决定。之后可进入 Full Whitepaper Recovery。

## 12. 本轮 commit hash

本报告创建前最近一次收口提交：

```text
3d954029a8faa9a13d1cb06d3261a6dafae68c7b
```

最终 HEAD 以本轮最终只读复验结果为准。

## 13. 是否 push

是。通过 GitHub connector 直接写入 `main`。

## 14. 禁止范围确认

```text
未进入 V0.3。
未创建 examples/。
未做 Claude Code 能力测试。
未改 AI_COLLABORATION_MODE_V4.md 主链路。
未改 templates/。
未改 checklists/。
未写 sub2api-maijian。
未清理 sub2api-maijian。
未处理微信公众号仓库。
未接入自动化。
未改业务代码。
```
