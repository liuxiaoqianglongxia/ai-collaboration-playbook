# templates

`templates/` 用于存放可复制到业务项目中的任务模板、报告模板、验收模板和项目接入模板。

## V0.2 定位

V0.2 只补可复制模板，不改变 V4 主链路，不接入自动化，不做 Claude Code 能力测试，不处理任何业务项目。

这些模板的作用是减少重复沟通，让 ChatGPT、Codex、Claude Code 和用户围绕同一个任务文件与报告格式协作。

## 使用原则

- 模板必须先适配具体项目，再写入业务仓库。
- 不允许把模板当成项目事实源。
- 不允许把其他项目的路径、端口、密钥、数据库或业务状态复制进新项目。
- 不允许因为有模板就跳过读取 GitHub 事实源。
- 模板应帮助减少重复沟通，而不是制造新的固定教条。

## 当前模板

```text
templates/PROJECT_BOOTSTRAP_TASK.md
templates/CODEX_TASK_PACKAGE.md
templates/CODEX_EXECUTION_REPORT.md
templates/CHATGPT_ACCEPTANCE_REPORT.md
templates/CLAUDE_CODE_READONLY_ANALYSIS_TASK.md
templates/TASK_PACKAGE_REGISTRY_BOOTSTRAP_TASK.md
templates/tasks/
templates/reports/chatgpt/task-packages/
```

## 使用建议

新项目第一轮优先使用 `PROJECT_BOOTSTRAP_TASK.md` 建协作底座。

进入工程执行时，ChatGPT 先用 `CODEX_TASK_PACKAGE.md` 生成任务包；Codex 执行后用 `CODEX_EXECUTION_REPORT.md` 写回报告；ChatGPT 再用 `CHATGPT_ACCEPTANCE_REPORT.md` 验收。

如果项目需要持续多轮 Codex / Claude Code 协作，可以使用 `TASK_PACKAGE_REGISTRY_BOOTSTRAP_TASK.md` 和 `templates/tasks/` 建立项目级任务包注册表。模板必须先适配具体项目，再写入业务仓库。

涉及 Claude Code 时，只能把 `CLAUDE_CODE_READONLY_ANALYSIS_TASK.md` 作为只读分析任务模板，不把它当成能力测试或自动执行入口。
