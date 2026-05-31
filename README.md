# AI 协作总规范库

这个仓库用于沉淀可复用的 AI 项目协作规范、任务模板、验收清单与实验记录。

它不是某一个业务项目的源码仓库，也不承载任何生产系统代码。它的职责是作为多个项目共享的“协作操作系统”：让 ChatGPT、GitHub、Codex、Claude Code 围绕同一套事实源、任务文件和验收规则工作。

## 稳定主链路

当前稳定主链路是 `AI_COLLABORATION_MODE_V4.md`：

- ChatGPT：总控、架构判断、任务包、验收。
- GitHub：唯一事实源、项目状态机、留痕系统。
- Codex：现场交付负责人、最终集成者、报告提交者。
- Claude Code：本地工程增强工具、深度代码分析、局部修复、复审。

默认流程：用户明确说进入执行 → 任务落 GitHub → Codex 按任务文件执行 → 报告写回 GitHub → ChatGPT 按 GitHub 事实源验收。

## 新项目接入

新项目第一轮只搭协作底座，不做业务开发。详见：

- `NEW_PROJECT_BOOTSTRAP.md`
- `AI_AGENT_ONBOARDING.md`

项目侧应创建自己的适配层，例如 `CHATGPT_START_HERE.md`、`AGENTS.md`、`CLAUDE.md`、`CURRENT.md`、`TASKS.md`、`DECISIONS.md`、`reports/latest.md`。

## Collaboration Template Pack V1

本次新增的可复用资产（详见 `feature/collaboration-template-pack-v1-20260530` 分支）：

- `templates/` — 项目就绪文件模板：`CURRENT.md`、`AGENTS.md`、`CLAUDE.md`、`CHATGPT_START_HERE.md`、`DECISIONS.md`、`TASKS.md`、`RUNBOOK.md`、执行报告与事故报告模板
- `standards/` — 共享术语表、项目状态标准、推荐仓库结构
- `checklists/` — SSOT 漂移检查、Claude Code 安全加固清单
- `protocols/` — GitHub 中心化 AI 协作协议、上下文注入协议、任务路由协议
- `reports/codex/` — 模板包执行报告与合并前复核报告

模板文件使用 `_TEMPLATE` 后缀。复制到业务项目后去掉后缀并填充项目特定字段。

## PLAYBOOK_OPERATIONAL_BASELINE_V1.1 Candidate

V1 仍是当前稳定主链路，四件套分工不变。

V1.1 候选层只补充项目级任务包注册表，让持续协作项目可以在 GitHub 中维护当前 Codex / Claude Code 任务入口：

- `tasks/codex/latest.md`
- `tasks/claude/latest.md`
- `reports/chatgpt/task-packages/`

它不接入自动化，不改变 V4，不新增默认协作成员，也不替代 `CURRENT.md`、`TASKS.md`、`reports/latest.md` 等项目事实源。

## templates / checklists

`templates/` 和 `checklists/` 保存可复制到具体项目的任务模板、报告模板与验收清单。模板必须先适配具体项目，再写入业务仓库，不能替代项目事实源。

## archive

`archive/` 用于保存迁移、误写抢救、历史版本与原始材料。归档内容只作为证据和素材，不直接代表当前最新规范。

当前归档入口：

- `archive/recovered-from-sub2api-misroute/2026-05-30/`

## whitepapers

`whitepapers/` 用于保存长版研究成果、白皮书草稿和可公开文章候选稿。它不替代 README、onboarding、modules、templates、checklists。

## 实验室

`lab/` 用于只读实验和方法验证。实验室内容默认不进入稳定主链路，必须先证明有效，再升级为 `modules/` 中的稳定模块。

当前实验方向：

- heartbeat 只读心跳
- skill start-here 审计
- subagent 只读侦察
- memory distillation 记忆蒸馏
- MCP docs context 文档上下文

## 禁止边界

本仓库不做业务开发，不存放密钥，不承载生产自动化，不替代具体项目仓库的事实源。任何执行任务必须落到对应项目的 GitHub 仓库，而不是只停留在聊天记录里。
