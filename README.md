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
