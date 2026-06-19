# templates

**Default V3 template**: `templates/task-hall-v3/` — use this for new projects.

`templates/` 根目录下的旧模板保留为 **history / reference**，供历史项目回滚和适配参考。

## V0.2 定位（历史）

V0.2 只补可复制模板，不改变 V4 主链路，不接入自动化，不做 Claude Code 能力测试，不处理任何业务项目。

这些模板的作用是减少重复沟通，让 ChatGPT、Codex、Claude Code 和用户围绕同一个任务文件与报告格式协作。

## 使用原则

- 模板必须先适配具体项目，再写入业务仓库。
- 不允许把模板当成项目事实源。
- 不允许把其他项目的路径、端口、密钥、数据库或业务状态复制进新项目。
- 不允许因为有模板就跳过读取 GitHub 事实源。
- 模板应帮助减少重复沟通，而不是制造新的固定教条。

## 历史模板（history / reference）

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

## V3 默认模板

```text
templates/task-hall-v3/README.md
templates/task-hall-v3/00_HOME.md
templates/task-hall-v3/01_CURRENT.md
templates/task-hall-v3/02_INDEX.md
templates/task-hall-v3/task-hall/  — complete workbench skeleton
```

新项目第一轮优先使用 `templates/task-hall-v3/` 建协作底座。
