# 用户使用说明 V1

> 适用版本：`PLAYBOOK_OPERATIONAL_BASELINE_V1.1`
> 目标读者：用户、ChatGPT 新会话、Codex 执行会话、接入本 playbook 的项目维护者

## 1. 这套 playbook 是什么

它是一套项目协作操作规范，不是业务项目源码。

它解决的问题是：

- 项目状态不散落在聊天记录里。
- ChatGPT、GitHub、Codex、Claude Code 各自职责清楚。
- 用户不用每天复制长任务包。
- 执行、报告、验收都能回到同一个事实源。

默认事实源是 GitHub。用户不需要每天维护 GitHub 细节，Agent 负责读写。

## 2. 日常你怎么用

你通常只需要说目标。

示例：

```text
按 V1.1 给这个项目发一个登录修复任务包。
```

或者：

```text
执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
```

ChatGPT 应该在背后完成判断：

```text
读 GitHub 事实源
判断风险和执行者
能自己安全完成就直接写 GitHub
需要本地执行就写任务包并指向 Codex
需要深度分析就让 Codex 编排 Claude Code
完成后只读验收
```

## 3. 四个稳定角色

```text
ChatGPT：总控、判断、任务包、验收、轻量 GitHub 写入
GitHub：唯一事实源、状态机、留痕
Codex：本地执行、集成、测试、PR、执行报告
Claude Code：深度代码阅读、局部草案、失败分析、复审
```

Hermes、Qwen、MCP、automation、heartbeat、subagent 不是默认成员。只有项目事实源或用户明确授权时，才作为项目特化工具进入。

## 4. 一条执行通道

V1.1 的关键规则：

```text
One stage has one active execution lane.
Default: one active Codex task at a time.
```

意思是：

- 同一个阶段默认只开一个活跃 Codex 任务。
- 新发现先记为候选下一步，不直接开第二条执行线。
- Claude Code 可以参与，但由 Codex 在当前任务里编排。
- Codex 仍是最终集成者。

## 5. 标准任务公告长什么样

ChatGPT 给用户的任务公告应短，不默认粘贴长任务包：

```text
任务：<TASK-ID>
能实现：
- <one concrete outcome>
- <one concrete outcome>
- <one concrete outcome>
不做：<key boundary>
你发给 Codex：执行 tasks/codex/latest.md，完成后更新 reports/codex/latest.md。
详情：任务包已在 GitHub。
```

前提是任务包确实已经写入 GitHub。

## 6. 怎么判断任务状态

看这些文件：

```text
reports/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

状态含义：

```text
ACTIVE_CODEX_TASK：Codex 有活跃任务。
NO_ACTIVE_CODEX_TASK：Codex 当前无活跃任务。
ACTIVE_CLAUDE_TASK：Claude Code 有活跃分析或复审任务。
NO_ACTIVE_CLAUDE_TASK：Claude Code 当前无活跃任务。
PASS：目标完成。
PARTIAL PASS：主体完成但有明确剩余项。
FAIL：目标未完成或关键检查失败。
BLOCKED：事实源、权限、环境或安全边界阻塞。
```

## 7. Codex 报告应包含什么

Codex 完成后应写 `reports/codex/latest.md`，并指向命名报告。

报告至少要说明：

- 结论：PASS / PARTIAL PASS / FAIL / BLOCKED。
- 当前仓库和分支。
- 实际修改文件。
- 实际运行命令或检查。
- 是否触碰禁止范围。
- 未完成项。
- 下一步建议。

## 8. 简单流程图

```text
用户给目标
  |
  v
ChatGPT 读取 GitHub 事实源
  |
  +-- 安全文档/任务包/验收 --> ChatGPT 直接写 GitHub
  |
  +-- 需要本地执行 ---------> 写 tasks/codex/latest.md
                                  |
                                  v
                                Codex 执行
                                  |
                                  +-- 需要深度分析 --> Codex 编排 Claude Code
                                  |
                                  v
                                Codex 写 reports/codex/latest.md
                                  |
                                  v
                                ChatGPT 只读验收
```

## 9. 不要做什么

- 不凭聊天历史判断项目当前状态。
- 不把其他项目的文件、记忆、配置混进当前项目。
- 不让用户反复复制长任务包。
- 不在一个阶段同时启动多条写入执行线。
- 不把 Claude Code 输出当作最终合并或部署授权。
- 不把 Hermes、Qwen、MCP、automation、heartbeat、subagent 变成默认成员。
- 不未经授权部署、改数据库、改密钥、改生产配置或 force push。

## 10. 项目接入时怎么用

每个业务项目必须有自己的事实源，不继承本仓库的临时状态。

项目侧至少应建立：

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
reports/claude/latest.md
```

通用规范在本仓库。项目事实在项目仓库。不要混用。
