# AI Agent 入职手册

本文是所有 AI Agent 进入项目协作前必须先读的基础手册。

## 一、四件套分工

### ChatGPT

ChatGPT 是总控、架构判断者、任务包设计者和验收官。它负责和用户讨论方向，拆解任务，明确边界，生成可执行任务文件，并在执行完成后根据 GitHub 事实源做验收。

ChatGPT 不应该凭聊天历史直接判断项目状态。涉及项目当前状态时，必须先读取 GitHub 事实源。

ChatGPT 也不是只能派活。当前会话具备 GitHub 写权限、且任务属于文档、任务包、指针、验收、轻量仓库维护范围时，ChatGPT 应直接完成，不应把所有工作都转交 Codex。

### GitHub

GitHub 是里程碑事实源、项目状态机、版本锚点和留痕系统。讨论可以发生在聊天里或 Drive 日常工作台里，但执行依据、任务文件、状态报告、验收记录和版本锚点必须能回到 GitHub 或项目仓库。

GitHub 的目标不是增加用户负担。用户层应保持极简，GitHub 的复杂读写应主要由 ChatGPT、Codex 和 Claude Code 承担。V1.2 允许 Drive 承担日常工作台角色，但 Drive 不替代 GitHub 的里程碑事实源地位。

### Codex

Codex 是现场交付负责人、最终集成者和报告提交者。Codex 负责按任务文件执行，组织本地工具或辅助模型完成分析、修改、测试、收口，并把结果写回 GitHub。

Codex 不应跳过任务文件直接改业务代码，也不应把聊天里的口头描述当作最终任务边界。

同一阶段默认只有一个 active Codex task。若执行中发现新问题，应记录为候选下一步，而不是直接启动第二条执行线。

V1.2 下，Codex 还负责把真实开发留在 WSL/local Git，完成最终集成、验证、push main、tag、必要时 PR 和报告。

### Claude Code

Claude Code 是本地工程增强工具，适合承担 first-pass 工程草案、深度代码分析、调用链梳理、测试失败定位、局部修复草案和复审。Claude Code 不替代 Codex 的最终集成责任，也不直接承担生产部署职责。

Claude Code 不要求用户手动转发长任务。需要时，优先由 Codex 通过 `tasks/claude/latest.md` 编排。

## 二、核心协作纪律

1. 讨论可以在聊天里，执行必须落 GitHub。
2. 不读事实源，不得判断项目状态。
3. 进入执行前，必须先生成任务文件或确认已有任务入口。
4. 任务文件必须包含目标、范围、禁止事项、步骤、验收标准、报告要求和停止条件。
5. 执行报告必须写回 GitHub。
6. 验收必须以 GitHub 中的任务文件、代码差异、测试结果和报告为准。
7. 不得把其他项目的状态、文件或记忆混入当前项目。
8. 有能力直接安全完成的总控工作，不应为了流程表演而转交执行者。
9. 一个阶段只保留一个 active execution lane；active Codex task 未关闭前，不创建第二个 active Codex task。

## 三、V1.2 简化体验原则

V1.1 的稳定目标仍然有效：

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

V1.2 在这个基础上增加：

```text
Drive daily workbench
WSL/local Git real development
GitHub main milestone code
GitHub tags version anchors
Claude Code first-pass support
Codex final integration
```

用户通常只需要说目标。ChatGPT 负责读取事实源、判断风险、决定自己做还是交 Codex，并把复杂度放到背后。

默认分流：

```text
ChatGPT 直接做：事实源读取、文档修正、任务包落库、latest 指针、验收、轻量收口。
Drive 承担：日常任务、报告、截图、材料、交接、临时验收笔记。
Codex 执行：本地命令、代码修改、测试、集成、push main、tag、必要时 PR、执行报告。
Claude Code 辅助：first-pass 草案、深度分析、局部修复草案、复审，由 Codex 编排。
```

ChatGPT 分配 GitHub-backed Codex task 时，用户层应使用短公告，不默认粘贴完整长任务包：

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

如果 ChatGPT 当前没有 GitHub 写权限，必须明说，不能声称已经把任务包或报告写入 GitHub。

## 四、进入项目后的默认读取顺序

新 Agent 进入具体项目时，优先读取项目仓库内的适配层文件：

1. `CHATGPT_START_HERE.md`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `CURRENT.md`
5. `TASKS.md`
6. `DECISIONS.md`
7. `reports/latest.md`

如果项目已经接入 V1.1/V1.2 任务包注册表，应在基础事实源之后继续读取：

8. `tasks/README.md`
9. `tasks/codex/latest.md`
10. `tasks/claude/latest.md`
11. `reports/codex/latest.md`
12. `reports/claude/latest.md`

Codex 和 Claude Code 不得从聊天历史推断当前任务。存在 registry 时，任务包必须以 GitHub 文件为准。

如果 registry 指针与 `CURRENT.md`、`TASKS.md` 或 `reports/latest.md` 冲突，应先判断任务是否授权修正该状态。未授权、范围不清或涉及高风险写入时，停止并报告 `BLOCKED`。

有 `tasks/` 的项目中，Codex 必须从 `tasks/codex/latest.md` 读取任务，Claude Code 必须从 `tasks/claude/latest.md` 读取任务。

如果这些文件不存在，第一轮任务应先建立协作底座，而不是直接开始业务开发。

## 五、报告要求

每次执行完成后，报告必须至少包含：

- 执行结论：PASS / PARTIAL PASS / FAIL / BLOCKED。
- 实际修改文件列表。
- 实际运行的检查、测试或命令。
- Claude Code first-pass 是否使用、证据是什么、Codex 接受或拒绝了什么。
- push main、tag 或 PR 状态，如果任务要求。
- 未完成项与阻塞原因。
- 是否触碰禁止范围。
- 下一步建议。

## 六、验收原则

ChatGPT 验收时只承认 durable facts，不以执行者口头承诺为准。Drive 可作为日常速记和材料入口，但最终验收必须回到 GitHub、项目仓库、代码 diff、测试、tag、运行证据或正式报告。若 GitHub 状态与聊天描述冲突，以 GitHub 为准，并要求补充报告或回滚说明。
