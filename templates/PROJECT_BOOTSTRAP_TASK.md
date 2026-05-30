# 新项目协作底座初始化任务模板

> 用途：复制到具体项目仓库后，作为第一轮协作底座任务。第一轮只建立协作文件，不做业务开发。

## 任务名

`project-bootstrap-collaboration-baseline-v1`

## 背景

本项目准备接入 AI 协作模式 V4。第一轮目标不是开发功能，而是建立 GitHub 事实源、任务记录、决策记录和执行报告入口，让 ChatGPT、Codex、Claude Code 后续能够稳定接力。

## 目标

在当前项目仓库中建立最小协作底座：

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

## 范围

- 只读梳理当前仓库结构。
- 创建或更新协作底座文件。
- 明确项目状态、禁止事项、任务入口和报告入口。
- 不修改业务代码。

## 禁止事项

- 不做业务开发。
- 不重构。
- 不部署。
- 不改数据库。
- 不改密钥。
- 不改生产配置。
- 不 force push。
- 不把其他项目状态复制进来。

## 执行步骤

1. 读取仓库 README、目录结构和现有协作文档。
2. 判断是否已有协作底座，避免覆盖有效内容。
3. 创建或补齐 `CHATGPT_START_HERE.md`、`AGENTS.md`、`CLAUDE.md`、`CURRENT.md`、`TASKS.md`、`DECISIONS.md`、`reports/latest.md`。
4. 在 `CURRENT.md` 中记录当前阶段和已知限制。
5. 在 `TASKS.md` 中列出下一批候选任务，但不进入业务开发。
6. 在 `reports/latest.md` 中写入本轮执行报告。

## 验收标准

- 新 ChatGPT 会话能从 `CHATGPT_START_HERE.md` 理解项目状态。
- Codex 能从 `AGENTS.md` 理解执行边界。
- Claude Code 能从 `CLAUDE.md` 理解只读分析边界。
- `CURRENT.md`、`TASKS.md`、`DECISIONS.md`、`reports/latest.md` 形成最小闭环。
- 没有业务代码、数据库、密钥、部署配置被修改。

## 报告要求

报告必须包含：

- 结论：PASS / PARTIAL PASS / FAIL / BLOCKED。
- 新增或修改文件列表。
- 未完成项。
- 是否触碰禁止范围。
- 下一步建议。

## 停止条件

遇到以下情况必须停止并报告：

- 仓库身份不明确。
- 疑似进入错误项目。
- 发现密钥或生产配置风险。
- 用户要求同时做业务开发。
- 需要删除或覆盖既有重要文件。
