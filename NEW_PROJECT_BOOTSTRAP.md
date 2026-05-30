# 新项目接入手册

新项目接入 V4 协作模式时，第一轮只做协作底座，不做业务开发。

## 一、第一轮目标

第一轮不是写功能，也不是修 bug，而是让项目具备可接力、可验收、可追踪的协作结构。

第一轮应完成：

- 建立项目级事实源入口。
- 明确 AI 角色边界。
- 明确当前项目状态。
- 建立任务与决策记录。
- 建立报告目录。
- 建立禁止范围与安全边界。

## 二、建议创建的项目适配层

每个业务项目应根据自身情况创建以下文件：

```text
CHATGPT_START_HERE.md
AGENTS.md
CLAUDE.md
CURRENT.md
TASKS.md
DECISIONS.md
reports/latest.md
```

可选增强：

```text
PROJECT_CARD.md
REPO_LINEAGE.md
RUNBOOK.md
reports/codex/latest.md
reports/claude/latest.md
orchestration/
```

## 三、各文件职责

### CHATGPT_START_HERE.md

给 ChatGPT 新会话使用的入口文件，说明项目背景、当前状态、读取顺序、协作规则和下一步建议。

### AGENTS.md

给 Codex 或其他执行 Agent 使用的工程规则，说明仓库结构、禁止事项、测试命令、提交规范和安全边界。

### CLAUDE.md

给 Claude Code 使用的本地工程增强说明，限定它适合做什么、不适合做什么、输出报告格式和停止条件。

### CURRENT.md

记录项目当前状态，包括当前阶段、最新结论、已知问题、正在进行的任务和禁止误判的旧信息。

### TASKS.md

记录待办任务、优先级、执行状态、任务文件链接和验收状态。

### DECISIONS.md

记录关键架构决策、取舍原因、日期和影响范围，避免后续 Agent 反复推翻已定边界。

### reports/latest.md

记录最近一次执行报告或验收报告，作为新会话快速接力入口。

## 四、第一轮禁止事项

- 不做业务开发。
- 不重构项目。
- 不部署。
- 不改数据库。
- 不改密钥。
- 不清理生产文件。
- 不把其他项目模板未经适配直接复制进来。

## 五、第一轮验收标准

第一轮完成后，应满足：

- 新 ChatGPT 会话能从 `CHATGPT_START_HERE.md` 读懂项目状态。
- Codex 能从 `AGENTS.md` 明确执行边界。
- Claude Code 能从 `CLAUDE.md` 明确辅助角色。
- `CURRENT.md`、`TASKS.md`、`DECISIONS.md`、`reports/latest.md` 能形成最小事实源闭环。
- 没有触碰业务代码、生产配置、密钥、数据库或部署链路。

只有协作底座通过验收后，才进入业务任务包阶段。
