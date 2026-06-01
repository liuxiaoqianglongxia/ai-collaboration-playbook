# AI 协作总规范库

这个仓库用于沉淀可复用的 AI 项目协作规范、任务模板、验收清单与运行记录。

它不是某一个业务项目的源码仓库，也不承载任何生产系统代码。它的职责是作为多个项目共享的“协作操作系统”：让 ChatGPT、GitHub、Codex、Claude Code 围绕同一套事实源、任务文件和验收规则工作。

## 当前状态

```text
stable: PLAYBOOK_OPERATIONAL_BASELINE_V1.2
candidate: DRIVE_NATIVE_V2_CANDIDATE
reports/latest.md: PARTIAL PASS on the V2 candidate branch
```

V1.1 已通过 PR #6、Claude Code 只读复审、ChatGPT 独立验收和 merge closeout。V1.2 在 V1.1 上新增并冻结 Drive-first 日常工作台、main+tag 版本锚点、Claude-first-pass / Codex-final 执行层。

Drive-native V2 候选层把日常任务、报告、材料、截图、交接、临时验收、决策记录放到 Drive 工作台；GitHub 收口为稳定成果、版本管理、release、rollback 和其他项目复用入口。V1.2 仍是历史稳定基线，V2 候选层在验收前不得标记为 `PLAYBOOK_OPERATIONAL_BASELINE_V2`。

当前入口以 `reports/latest.md` 为准。

日常使用先读：

- `guides/USER_OPERATING_GUIDE_V1.md`
- `CHATGPT_START_HERE.md`
- `reports/latest.md`
- `standards/DRIVE_FIRST_WORKFLOW_V1.md`
- `standards/MAIN_ONLY_TAG_VERSIONING_V1.md`
- `standards/CLAUDE_FIRST_CODEX_FINAL_V1.md`
- `standards/DRIVE_NATIVE_WORKFLOW_V2.md`
- `standards/GITHUB_RELEASE_AND_VERSION_POLICY_V2.md`
- `guides/DRIVE_NATIVE_V2_USER_GUIDE.md`

## 稳定主链路

当前稳定主链路是 `AI_COLLABORATION_MODE_V4.md`，四件套分工不变：

- ChatGPT：总控、架构判断、任务包、验收。
- GitHub：唯一事实源、项目状态机、留痕系统。
- Codex：现场交付负责人、最终集成者、报告提交者。
- Claude Code：本地工程增强工具、深度代码分析、局部修复、复审。

Hermes、Qwen、MCP、自动化、心跳、子代理等能力不是默认四件套成员。只有具体项目事实源或用户明确授权时，才作为项目特化工具进入。

## V1.2 的使用目标

V1.2 不是为了让用户面对更多流程，而是为了把日常操作从 GitHub 机械维护中释放出来，同时保留 GitHub 的里程碑事实源地位：

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

理想使用方式应该像浏览器或微信一样：入口简单、动作短、结果清楚。复杂度由 Agent 层、GitHub 事实源和项目文件承担。

日常分工：

```text
Drive：日常任务、报告、截图、材料、交接、临时验收笔记。
WSL/local Git：真实代码编辑、测试、集成。
GitHub main：里程碑代码和协作事实。
GitHub tags：版本锚点、生产依据、回滚点。
Claude Code：由 Codex 编排的 first-pass 工程支持。
Codex：最终集成、验证、提交、push、tag、必要时 PR、报告。
```

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
4. 日常上下文可先落在 Drive 工作台；关键执行事实必须同步回 GitHub 或项目仓库。
5. 需要本地环境、代码修改、测试、集成、PR、tag 或部署前验证的工作，交给 Codex。
6. 需要深度代码分析、局部修复草案、first-pass patch 或复审时，由 Codex 编排 Claude Code。
7. Codex 完成后写回 reports/codex/latest.md。
8. ChatGPT 只读验收并输出 PASS / PARTIAL PASS / FAIL / BLOCKED。
```

如果当前 ChatGPT 会话有 GitHub 写权限，任务包应直接落 GitHub；如果没有写权限，必须明确说明，不能声称“已落 GitHub”。

## Drive 与 GitHub 的定位

Drive 是日常工作台和日常事实源。GitHub 是稳定成果、版本锚点、release、rollback 和最终可复用文档承载。

正确用法：

```text
Drive 保存日常任务、报告、截图、材料、交接、daily log、临时验收和决策记录。
GitHub 保存稳定成果、main/tag、release notes、rollback anchors、milestone summaries 和最终可复用规范。
用户侧只看关键结论和下一句指令。
Agent 负责读写细节。
```

错误用法：

```text
为了流程而流程。
让用户反复复制大段任务包。
把所有注意力都耗在 GitHub 文件维护上。
把简单任务搞成复杂仪式。
把 Drive 当成生产部署源。
把 GitHub daily task pointer 恢复为默认派工方式。
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

跨项目路由和扩展规则见 `standards/ROUTING_AND_EXTENSIBILITY_V1.md`。项目接入时可从 `templates/PROJECT_ROUTING_PROFILE.md` 生成项目自己的路由配置。

V1.2 稳定层：

- `standards/DRIVE_FIRST_WORKFLOW_V1.md`
- `standards/MAIN_ONLY_TAG_VERSIONING_V1.md`
- `standards/CLAUDE_FIRST_CODEX_FINAL_V1.md`
- `standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md`
- `templates/drive-project-workbench/`
- `templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md`
- `templates/CLAUDE_PATCH_WORKER_TASK.md`
- `templates/CODEX_CLAUDE_ORCHESTRATION.md`

ChatGPT Pro 深度复核入口见 `reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md`。最终个性化内容见 `reports/chatgpt/personalization/PERSONALIZATION_FINAL_V1_2.md`。

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
