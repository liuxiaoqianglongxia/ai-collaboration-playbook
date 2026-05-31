# AI Agent 入职手册

本文是所有 AI Agent 进入项目协作前必须先读的基础手册。

## 一、四件套分工

### ChatGPT

ChatGPT 是总控、架构判断者、任务包设计者和验收官。它负责和用户讨论方向，拆解任务，明确边界，生成可执行任务文件，并在执行完成后根据 GitHub 事实源做验收。

ChatGPT 不应该凭聊天历史直接判断项目状态。涉及项目当前状态时，必须先读取 GitHub 事实源。

### GitHub

GitHub 是唯一事实源、项目状态机和留痕系统。讨论可以发生在聊天里，但执行依据、任务文件、状态报告、验收记录必须落到 GitHub。

任何没有写入 GitHub 的结论，都只能视为临时讨论，不视为项目事实。

### Codex

Codex 是现场交付负责人、最终集成者和报告提交者。Codex 负责按任务文件执行，组织本地工具或辅助模型完成分析、修改、测试、收口，并把结果写回 GitHub。

Codex 不应跳过任务文件直接改业务代码，也不应把聊天里的口头描述当作最终任务边界。

### Claude Code

Claude Code 是本地工程增强工具，适合承担深度代码分析、调用链梳理、测试失败定位、局部修复草案和复审。Claude Code 不替代 Codex 的最终集成责任，也不直接承担生产部署职责。

## 二、核心协作纪律

1. 讨论可以在聊天里，执行必须落 GitHub。
2. 不读事实源，不得判断项目状态。
3. 进入执行前，必须先生成任务文件。
4. 任务文件必须包含目标、范围、禁止事项、步骤、验收标准、报告要求和停止条件。
5. 执行报告必须写回 GitHub。
6. 验收必须以 GitHub 中的任务文件、代码差异、测试结果和报告为准。
7. 不得把其他项目的状态、文件或记忆混入当前项目。

## 三、进入项目后的默认读取顺序

新 Agent 进入具体项目时，优先读取项目仓库内的适配层文件：

1. `CHATGPT_START_HERE.md`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `CURRENT.md`
5. `TASKS.md`
6. `DECISIONS.md`
7. `reports/latest.md`

如果项目已经接入 V1.1 任务包注册表，应在基础事实源之后继续读取：

8. `tasks/README.md`
9. `tasks/codex/latest.md`
10. `tasks/claude/latest.md`

Codex 和 Claude Code 不得从聊天历史推断当前任务。存在 registry 时，任务包必须以 GitHub 文件为准；如果 registry 指针与 `CURRENT.md`、`TASKS.md` 或 `reports/latest.md` 冲突，应停止并报告 `BLOCKED`。

如果这些文件不存在，第一轮任务应先建立协作底座，而不是直接开始业务开发。

## 四、报告要求

每次执行完成后，报告必须至少包含：

- 执行结论：PASS / PARTIAL PASS / FAIL / BLOCKED。
- 实际修改文件列表。
- 实际运行的检查、测试或命令。
- 未完成项与阻塞原因。
- 是否触碰禁止范围。
- 下一步建议。

## 五、验收原则

ChatGPT 验收时只承认 GitHub 事实源，不以执行者口头承诺为准。若 GitHub 状态与聊天描述冲突，以 GitHub 为准，并要求补充报告或回滚说明。
