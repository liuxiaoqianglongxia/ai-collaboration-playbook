# 新项目接入手册

新项目接入 `PLAYBOOK_OPERATIONAL_BASELINE_V2` 时，第一轮只做协作底座，不做业务开发。

## 一、第一轮目标

第一轮不是写功能，也不是修 bug，而是让项目具备可接力、可验收、可追踪的协作结构。

第一轮应完成：

- 建立项目级事实源入口。
- 明确 AI 角色边界。
- 明确当前项目状态。
- 建立任务与决策记录。
- 建立报告目录。
- 建立禁止范围与安全边界。
- 建立 Drive workbench 作为日常事实源。
- 明确 GitHub stable sync 点。

## 二、建议创建的 Drive workbench

每个项目应先建立 Drive 日常工作台：

```text
00_HOME.md
01_CURRENT.md
02_INDEX.md
03_ROUTING.md
04_DECISIONS_LATEST.md
05_RELEASE_POLICY.md
tasks/
reports/
daily/
decisions/
acceptance/
handoffs/
materials/
screenshots/
```

Drive workbench 管日常任务、报告、材料、截图、交接、临时验收、决策记录和 daily log。

## 三、建议创建的 GitHub 稳定适配层

每个项目应根据自身情况创建以下 GitHub 文件：

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

GitHub-backed registry 兼容增强结构：

```text
tasks/README.md
tasks/codex/_template.md
tasks/codex/latest.md
tasks/claude/_template.md
tasks/claude/latest.md
reports/chatgpt/task-packages/README.md
```

第一轮仍只建协作底座，不做业务开发。如果项目准备进入持续 Codex / Claude Code 协作，可以在第一轮作为兼容增强补齐 registry，也可以在 bootstrap PASS 后单独补齐。V2 默认日常派工仍使用 Drive task package。

bootstrap PASS 后，可追加独立接入任务：

```text
PROJECT-TASK-PACKAGE-REGISTRY-ADOPTION-V1
```

## 四、各文件职责

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

## 五、第一轮禁止事项

- 不做业务开发。
- 不重构项目。
- 不部署。
- 不改数据库。
- 不改密钥。
- 不清理生产文件。
- 不把其他项目模板未经适配直接复制进来。

## 六、第一轮验收标准

第一轮完成后，应满足：

- 新 ChatGPT 会话能从 `CHATGPT_START_HERE.md` 读懂项目状态。
- Codex 能从 `AGENTS.md` 明确执行边界。
- Claude Code 能从 `CLAUDE.md` 明确辅助角色。
- `CURRENT.md`、`TASKS.md`、`DECISIONS.md`、`reports/latest.md` 能形成最小事实源闭环。
- Drive workbench 能承载日常任务、报告、材料、交接、临时验收和决策记录。
- GitHub 只承载稳定成果、版本、release、rollback 和可复用文档。
- 没有触碰业务代码、生产配置、密钥、数据库或部署链路。

只有协作底座通过验收后，才进入业务任务包阶段。
