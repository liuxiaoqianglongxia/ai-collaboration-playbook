# 用户使用说明 V1

> 适用版本：`PLAYBOOK_OPERATIONAL_BASELINE_V2`
> 目标读者：用户、ChatGPT 新会话、Codex 执行会话、接入本 playbook 的项目维护者

## 1. 这套 playbook 是什么

它是一套项目协作操作规范，不是业务项目源码。

它解决的问题是：

- 项目状态不散落在聊天记录里。
- ChatGPT、GitHub、Codex、Claude Code 各自职责清楚。
- 用户不用每天复制长任务包。
- 执行、报告、验收都能回到同一个事实源。

默认日常事实源是 Drive。GitHub 承载稳定成果、版本管理、release、rollback 和可复用文档。用户不需要每天维护 GitHub 细节，Agent 负责读写和同步关键事实。

## 2. 日常你怎么用

你通常只需要说目标。

示例：

```text
按 V2 给这个项目发一个登录修复任务包，并安排 Codex 执行。
```

如果项目明确启用 GitHub-backed registry 兼容入口，也可以说：

```text
按该项目的 GitHub-backed registry 兼容入口执行当前 Codex 任务。
```

ChatGPT 应该在背后完成判断：

```text
读 Drive 日常上下文和 GitHub 稳定事实
判断风险和执行者
能自己安全完成就直接写 Drive 或稳定 GitHub 文档
需要本地执行就写 Drive task package 并指向 Codex
需要 first-pass 工程支持就由 Codex 编排 Claude Code
完成后只读验收
```

V2 的日常分工：

```text
Drive 管日常任务、报告、截图、材料、交接、临时验收、决策记录、daily log。
WSL/local Git 管真实代码编辑、测试、集成。
GitHub main 管稳定代码和稳定文档。
GitHub tags 管版本锚点、release 和 rollback。
Codex 负责最终集成、验证、push main、tag、必要时 PR、报告。
```

## 3. 四个稳定角色

```text
ChatGPT：总控、判断、任务包、验收、轻量 Drive/GitHub 写入
Drive：日常事实源、任务、报告、材料、交接、临时验收、决策记录
GitHub：稳定成果、版本、release、rollback、可复用文档
Codex：本地执行、集成、测试、PR、执行报告
Claude Code：由 Codex 编排的 first-pass 工程支持、深度代码阅读、局部草案、失败分析、复审
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
你发给 Codex：任务已写入 Drive：tasks/codex/YYYYMMDD/<task-name>.md；请读取该任务包执行，完成后写 Drive 报告。
详情：任务包已在 Drive。
```

前提是项目明确启用了 GitHub-backed registry，且任务包确实已经写入 GitHub。V2 默认使用 Drive task package。

## 6. 怎么判断任务状态

看这些文件：

```text
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

如果项目启用 GitHub-backed registry，再看 `tasks/codex/latest.md` 和 `tasks/claude/latest.md`。

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
ChatGPT 读取 Drive 日常上下文和 GitHub 稳定事实
  |
  +-- 日常任务/报告/验收 ----> ChatGPT 直接写 Drive
  |
  +-- 稳定文档/release/rollback --> ChatGPT 或 Codex 同步 GitHub
  |
  +-- 需要本地执行 ---------> 写 Drive task package
                                  |
                                  v
                                Codex 执行
                                  |
                                  +-- 需要 first-pass 支持 --> Codex 编排 Claude Code
                                  |
                                  v
                                Codex 在 WSL/local Git 集成、验证、push main/tag
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
- 不把 Drive 当生产部署源。
- 不把 GitHub-backed registry 当默认日常派工入口。
- 不把 branch 当版本记录；版本锚点应是 main 上的 tag。
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
reports/codex/latest.md
reports/claude/latest.md
```

V2 默认还应建立项目 Drive workbench。若项目启用 GitHub-backed registry，再补 `tasks/codex/latest.md` 和 `tasks/claude/latest.md`。通用规范在本仓库。项目事实在项目自己的 Drive/GitHub 空间。不要混用。
