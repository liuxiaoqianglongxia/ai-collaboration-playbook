# Latest Report｜PLAYBOOK_OPERATIONAL_BASELINE_V1

## 状态

PLAYBOOK_OPERATIONAL_BASELINE_V1

## 结论

PASS

## 当前主线成果

`ai-collaboration-playbook` 已具备可投入项目运行的协作规范基线：

```text
V0.1 Bootstrap: PASS
V0.2 Templates & Checklists: PASS
V0.2.5 Misroute Recovery: PASS
V0.2.6 Full Whitepaper Recovery: PASS
Collaboration Template Pack V1: PASS
Execution Environment Ownership: PASS
```

## 已包含内容

```text
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
NEW_PROJECT_BOOTSTRAP.md
modules/
templates/
checklists/
lab/
archive/recovered-from-sub2api-misroute/2026-05-30/
whitepapers/
standards/
protocols/
reports/
```

## 执行环境分工

```text
Mac Codex:
- ai-collaboration-playbook 总规范库
- 协议规范
- 模板 / 清单 / whitepaper
- 分支合并预检
- PR 复核

Windows Codex:
- 业务项目
- 本地 WSL
- 生产环境
- 数据库
- 服务、端口、部署
- 运行态问题

Historical audit / content ingest:
- 按源仓库位置、风险等级和本地依赖选择 Mac 或 Windows
- 必须先核验 repository_full_name、branch、README 标题和允许写入范围
```

## 当前禁止事项

```text
不直接改业务项目。
不直接部署。
不改数据库。
不改密钥。
不清理 sub2api-maijian。
不进入 V0.3 examples。
不做 Claude Code 委派边界测试。
不接入自动化。
```

## 下一步建议

```text
1. 合并本 PR 到 main 后，只读复验 main。
2. 通知大审计恢复。
3. 开始让真实业务项目按项目接入包建立协作底座。
4. sub2api-maijian 污染清理仍由该项目总控单独处理。
5. V0.3 examples 和 Claude Code 委派边界测试后置，不阻塞当前投入运行。
```
