# AI 协作总规范库

这个仓库用于沉淀可复用的 AI 项目协作规范、任务模板、验收清单与运行记录。

它不是某一个业务项目的源码仓库，也不承载任何生产系统代码。它的职责是作为多个项目共享的“协作操作系统”：让 ChatGPT、GitHub、Codex、Claude Code 围绕同一套事实源、任务文件和验收规则工作。

## 当前稳定版本

```text
PLAYBOOK_OPERATIONAL_BASELINE_V1.1
reports/latest.md: PASS
```

V1.1 已通过 PR #6、Claude Code 只读复审、ChatGPT 独立验收和 merge closeout。当前入口以 `reports/latest.md` 为准。

## 稳定主链路

当前稳定主链路是 `AI_COLLABORATION_MODE_V4.md`，四件套分工不变：

- ChatGPT：总控、架构判断、任务包、验收。
- GitHub：唯一事实源、项目状态机、留痕系统。
- Codex：现场交付负责人、最终集成者、报告提交者。
- Claude Code：本地工程增强工具、深度代码分析、局部修复、复审。

Hermes、Qwen、MCP、自动化、心跳、子代理等能力不是默认四件套成员。只有具体项目事实源或用户明确授权时，才作为项目特化工具进入。

## V1.1 的使用目标

V1.1 不是为了让用户面对更多流程，而是为了把复杂度放到背后：

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

对用户来说，理想使用方式应该像浏览器或微信一样：入口简单、动作短、结果清楚；背后可以复杂，但复杂度应由 ChatGPT、GitHub、Codex、Claude Code 和项目文件承担，而不是让用户每天复制长任务包。

## 默认工作方式

用户只需要给目标，例如：

```text
按 V1.1 给这个项目发一个登录修复任务包。
```

ChatGPT 应该完成背后判断：

```text
1. 读取项目 GitHub 事实源。
2. 判断任务风险、范围、执行者和验收方式。
3. 能直接安全完成的文档、任务包、验收、轻量仓库操作，由 ChatGPT 直接完成。
4. 需要本地环境、代码修改、测试、集成、PR、部署前验证的工作，交给 Codex。
5. 需要深度代码分析、局部修复草案或复审时，由 Codex 编排 Claude Code。
6. Codex 完成后写回 reports/codex/latest.md。
7. ChatGPT 只读验收并输出 PASS / PARTIAL PASS / FAIL / BLOCKED。
```

如果当前 ChatGPT 会话有 GitHub 写权限，任务包应直接落 GitHub；如果没有写权限，必须明确说明，不能声称“已落 GitHub”。

## GitHub 的定位

GitHub 是事实源，不是让用户消耗精力的地方。

正确用法：

```text
GitHub 保存当前状态、任务包、报告、决策和验收证据。
用户只看关键结论和下一句指令。
Agent 负责读写细节。
```

错误用法：

```text
为了流程而流程。
让用户反复复制大段任务包。
把所有注意力都耗在 GitHub 文件维护上。
把简单任务搞成复杂仪式。
```

## V1.1 任务包注册表

V1.1 在 V4 基线上新增项目级任务包注册表：

```text
tasks/codex/latest.md
tasks/claude/latest.md
reports/chatgpt/task-packages/
```

它的作用是减少聊天复制，让 Codex 和 Claude Code 从稳定 GitHub 文件接任务。

它不接入自动化，不改变 V4，不新增默认协作成员，也不替代 `CURRENT.md`、`TASKS.md`、`DECISIONS.md`、`reports/latest.md` 等项目事实源。

V1.1 追加两条稳定执行规则：

- 一个阶段只保留一个 active execution lane。默认同一阶段只有一个 active Codex task。
- Claude Code 由 Codex 在当前 Codex task 内编排；Claude Code 不替代 Codex 做最终集成。

面向用户的任务公告应保持短格式，详见 `templates/USER_FACING_TASK_ANNOUNCEMENT.md`。用户通常只需要把这句发给 Codex：

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```

## 新项目接入

新项目第一轮只搭协作底座，不做业务开发。详见：

- `NEW_PROJECT_BOOTSTRAP.md`
- `AI_AGENT_ONBOARDING.md`

项目侧应创建自己的适配层，例如：

```text
CHATGPT_START_HERE.md
AGENTS.md
CLAUDE.md
CURRENT.md
TASKS.md
DECISIONS.md
reports/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/codex/latest.md
```

## 模板 / 清单

`templates/` 和 `checklists/` 保存可复制到具体项目的任务模板、报告模板与验收清单。模板必须先适配具体项目，再写入业务仓库，不能替代项目事实源。

## archive

`archive/` 用于保存迁移、误写抢救、历史版本与原始材料。归档内容只作为证据和素材，不直接代表当前最新规范。

当前归档入口：

- `archive/recovered-from-sub2api-misroute/2026-05-30/`

## whitepapers

`whitepapers/` 用于保存长版研究成果、白皮书草稿和可公开文章候选稿。它不替代 README、onboarding、modules、templates、checklists。

## 实验室

`lab/` 用于只读实验和方法验证。实验室内容默认不进入稳定主链路，必须先证明有效，再升级为稳定模块。

## 禁止边界

本仓库不做业务开发，不存放密钥，不承载生产自动化，不替代具体项目仓库的事实源。任何具体项目执行任务必须落到对应项目的 GitHub 仓库，而不是只停留在聊天记录里。
