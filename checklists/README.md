# checklists

`checklists/` 用于存放执行前、提交前、部署前、验收前的检查清单。

## V0.2 定位

V0.2 只补可复制验收清单，不改变 V4 主链路，不接入自动化，不做 Claude Code 能力测试，不处理任何业务项目。

检查清单不是替代判断的机械表格，而是防止 AI 协作中常见错误：

- 没读事实源就判断。
- 没任务文件就执行。
- 把实验能力当稳定模块。
- 跨项目误写。
- 未授权部署或改生产环境。
- 报告没有写回 GitHub。

## 当前清单

```text
checklists/GITHUB_CONNECTOR_ROUTE_CHECK.md
checklists/CODEX_BEFORE_EXECUTION_CHECK.md
checklists/CODEX_BEFORE_COMMIT_CHECK.md
checklists/CHATGPT_ACCEPTANCE_CHECK.md
checklists/PRODUCTION_SAFETY_CHECK.md
checklists/TASK_PACKAGE_REGISTRY_REVIEW.md
```

## 使用建议

进入任何仓库写操作前，先使用 `GITHUB_CONNECTOR_ROUTE_CHECK.md`。

Codex 执行前使用 `CODEX_BEFORE_EXECUTION_CHECK.md`，提交前使用 `CODEX_BEFORE_COMMIT_CHECK.md`。

ChatGPT 验收时使用 `CHATGPT_ACCEPTANCE_CHECK.md`。

涉及生产、部署、数据库、密钥、端口、服务重启时，必须额外使用 `PRODUCTION_SAFETY_CHECK.md`。

验收项目级任务包注册表和 latest 指针时，使用 `TASK_PACKAGE_REGISTRY_REVIEW.md`。
