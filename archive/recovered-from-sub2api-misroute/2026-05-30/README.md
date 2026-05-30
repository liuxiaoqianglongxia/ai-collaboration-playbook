# AI 协作总规范库

仓库英文名：`ai-collaboration-playbook`  
定位：AI 项目协作总规范库 / AI Agent 入职手册 / 新项目接入模板 / 实验室事实源

---

## 1. 这个仓库是什么

这个仓库不是某一个业务项目的源码仓库。

它是给 ChatGPT、Codex、Claude Code，以及未来可能接入的其他 AI Agent 使用的“协作总规范库”。

它负责回答：

```text
AI 项目协作应该怎么分工？
ChatGPT、GitHub、Codex、Claude Code 各自做什么？
新项目如何接入这套协作模式？
什么时候可以进入执行？
任务如何落到 GitHub？
Claude Code 什么时候该被 Codex 调用？
哪些实验能力可以放进 lab，哪些能力才能升级成稳定模块？
```

---

## 2. 当前稳定主链路

当前稳定主链路继续保持“四件套”：

```text
ChatGPT：总控 / 架构判断 / 任务包 / 验收
GitHub：唯一事实源 / 项目状态机 / 留痕系统
Codex：现场交付负责人 / 最终集成者 / 报告提交者
Claude Code：本地工程增强工具 / 深度代码分析 / 局部修复 / 复审
```

一句话：

```text
ChatGPT 管判断，GitHub 管事实，Claude Code 管工程探索，Codex 管交付收口。
```

---

## 3. 当前扩展策略

V4 继续保持四件套稳定主链路。

总规范库新增 `lab/` 实验室。

把过去讨论的 `Codex-Hermes Fusion` 改名为：

```text
Codex Agentic Workbench Lab
```

核心原则：

```text
Hermes 是组织哲学参考，不是 V4 默认执行组件。
Codex Agentic Workbench Lab 是实验轨，不是稳定生产主链路。
先做只读实验：heartbeat、skill、subagent、memory-distill、MCP。
证明有效后，再升级成稳定模块。
```

---

## 4. 必读顺序

新 ChatGPT / Codex / Claude Code 会话，应按顺序读取：

```text
1. README.md
2. AI_AGENT_ONBOARDING.md
3. AI_COLLABORATION_MODE_V4.md
4. NEW_PROJECT_BOOTSTRAP.md
5. lab/CODEX_AGENTIC_WORKBENCH_V0_1.md
6. lab/CODEX_HERMES_TRANSLATION_NOTES.md
```

如果要研究实验能力，再读取：

```text
lab/experiments/001-heartbeat-readonly.md
lab/experiments/002-skill-start-here-audit.md
lab/experiments/003-subagent-readonly-scout.md
lab/experiments/004-memory-distillation.md
lab/experiments/005-mcp-docs-context.md
```

---

## 5. 稳定模块和实验模块的区别

稳定模块：

```text
已经验证，可以进入项目默认协作流程。
```

实验模块：

```text
只放在 lab/ 中，用于研究、测试、验证。
不得默认进入业务项目主链路。
不得自动部署、自动改数据库、自动改 .env、自动提交。
```

---

## 6. 当前目录建议

```text
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
NEW_PROJECT_BOOTSTRAP.md

lab/
  CODEX_AGENTIC_WORKBENCH_V0_1.md
  CODEX_HERMES_TRANSLATION_NOTES.md
  experiments/
    001-heartbeat-readonly.md
    002-skill-start-here-audit.md
    003-subagent-readonly-scout.md
    004-memory-distillation.md
    005-mcp-docs-context.md

modules/
  README.md

templates/
  README.md

checklists/
  README.md
```

---

## 7. 当前状态

状态：`PLAYBOOK_BOOTSTRAP_V0_1`

当前目标：

```text
先把 V4 稳定主链路和 Codex Agentic Workbench Lab 的事实文件落地。
完成后，再开展 Codex 调用 Claude Code 能力边界测试。
```

当前禁止：

```text
不做业务开发。
不动任何业务项目代码。
不做 Claude Code 能力测试。
不写生产自动化。
不做自动部署。
不把 lab 实验直接升级成稳定模块。
```
