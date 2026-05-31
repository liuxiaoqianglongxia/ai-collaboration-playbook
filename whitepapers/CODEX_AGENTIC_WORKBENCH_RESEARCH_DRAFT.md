# Codex Agentic Workbench Research Draft

版本：V0.2.6 Full Whitepaper Recovery  
状态：研究草稿  
定位：把 Hermes 的组织哲学翻译成 Codex 可执行的工程工作台，而不是把 Hermes 原样搬进 Codex

---

## 1. 核心判断

不要把 Hermes 原样搬进 Codex。

更准确的方向是：

```text
Hermes 提供组织哲学。
Codex 提供工程执行能力。
GitHub 提供唯一事实源。
ChatGPT 提供总控判断和验收。
Claude Code 提供局部工程增强。
```

Hermes 的价值在于它长期沉淀出来的“组织方式”：角色、记忆、技能、团队、心跳、复盘、上下文注入、失败经验和边界意识。Codex 的价值在于它能真实读取仓库、改文件、跑命令、生成 diff、提交 PR。两者的结合不应该是运行时拼接，而应该是方法论翻译。

所以本研究稿使用名称：

```text
Codex Agentic Workbench Lab
```

它是实验室，不是 V4 默认主链路。

---

## 2. 为什么不能直接搬 Hermes

直接搬 Hermes 会导致三个问题。

第一，运行时边界不同。Hermes 是本地长期组织系统，强调 team、role、memory、skill、soul；Codex 是工程执行系统，强调仓库、diff、命令、测试、PR。把 Hermes 的结构原样塞进 Codex，会让 Codex 背负过多状态和角色负担。

第二，事实源边界不同。V4 已经确定 GitHub 是唯一事实源。Hermes 的记忆可以提供经验，但不能替代 GitHub 中的 CURRENT、TASKS、DECISIONS、reports。否则项目状态会再次散落到多个系统里。

第三，安全边界不同。Hermes 的长期记忆和本地能力可能包含私有路径、个人偏好、项目隐含状态；Codex 的输出会进入仓库和 PR。任何混入都可能变成跨项目污染。

因此结论是：

```text
复制运行时是错误方向。
翻译组织哲学才是正确方向。
```

---

## 3. 七层结构

Codex Agentic Workbench Lab 暂定七层：

```text
Soul Layer        灵魂层
State Layer       状态层
Memory Layer      记忆层
Skill Layer       技能层
Agent Layer       子代理层
Tool Layer        工具层 / MCP
Heartbeat Layer   心跳层
```

这七层不是一次性启用，也不是默认进入业务项目。它们是研究方向，需要逐层做只读实验，证明有效后再升级。

### 3.1 Soul Layer：灵魂层

Soul 不是人格扮演，而是项目使命、价值观、禁区和执行哲学。

在 Codex 体系中，它可以落到：

```text
PROJECT_CARD.md
DECISIONS.md
AGENTS.md
CHATGPT_START_HERE.md
```

它回答：

```text
这个项目为什么存在？
哪些事情永远不做？
哪些边界不能碰？
什么算成功？
什么算危险？
```

Soul Layer 的风险是写胖。AGENTS.md 不能变成百科全书，AI_COLLABORATION_MODE_V4.md 不能无限变胖。长期内容应拆到 modules、templates、checklists、whitepapers、archive。

### 3.2 State Layer：状态层

State 是当前事实，不是历史记忆。

推荐文件：

```text
CURRENT.md
TASKS.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

State Layer 的目标是让任何新会话都能知道：当前阶段是什么、最近一次报告是什么、下一步是什么、哪些事情禁止做。

### 3.3 Memory Layer：记忆层

Memory 是经验，不是事实。

它可以从执行报告、失败记录、复盘中蒸馏出候选经验，但不能自动覆盖当前事实源。

推荐流程：

```text
reports → memory candidates → ChatGPT / 人工验收 → DECISIONS 或 templates/checklists
```

禁止：

```text
把 memory 当 CURRENT.md
把失败日志直接变成强制规则
把个人路径、密钥、生产配置写入记忆
```

### 3.4 Skill Layer：技能层

Skill 是可复用流程，不是神秘能力。它适合封装：

```text
进入项目先读事实源
执行前检查
提交前检查
PR 复审
生产变更 preflight
```

Skill 的原则：短、明确、可触发、可审计、有停止条件。Skill 不应绕过任务文件和报告系统。

### 3.5 Agent Layer：子代理层

Subagent 适合只读侦察，不适合一开始就并行写代码。

可选子代理：

```text
backend-route-scout
frontend-flow-scout
test-failure-scout
docs-state-scout
ops-risk-scout
```

主 Codex 仍然负责综合判断和最终收口。子代理输出必须带证据路径，不能直接成为最终结论。

### 3.6 Tool Layer：工具层 / MCP

工具层用于连接官方文档、只读 GitHub、浏览器资料、Context7/docs MCP 等低风险来源。

第一阶段不建议接入：

```text
生产数据库
密钥管理
云控制台
DNS / Cloudflare
支付后台
真实用户数据
可写入的生产工具
```

外部文档是参考，不是项目事实源。

### 3.7 Heartbeat Layer：心跳层

心跳不是自动修复。第一阶段只允许：

```text
读取状态
发现冲突
输出报告
建议下一步
```

不允许：

```text
自动提交
自动修复
自动部署
自动改任务状态
```

---

## 4. 五个只读实验

V0.2.6 以前已经恢复了五个实验方向，本节整理为研究路线。

### 4.1 Experiment 001：heartbeat readonly

目标：验证 Codex / automation 能否承担项目状态心跳巡检。

输入：

```text
CHATGPT_START_HERE.md
CURRENT.md
TASKS.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

输出：

```text
结论：PASS / ATTENTION / BLOCKED
检查时间
读取文件
发现的问题
风险等级
建议下一步
是否需要人工介入
```

升级条件：连续多次稳定只读 PASS，且没有诱发自动修复或生产操作。

### 4.2 Experiment 002：skill start-here audit

目标：把“进入项目先读事实源”封装成可复用 skill / workflow。

必须输出：

```text
当前项目
当前分支
当前阶段
当前任务
启用模块
允许修改范围
禁止修改范围
风险 flags
是否允许 coding
建议下一步
```

失败条件：未读事实源就给建议、直接进入代码修改、忽略禁止事项、输出没有证据路径。

### 4.3 Experiment 003：subagent readonly scout

目标：验证子代理是否能承担只读侦察任务，减少主执行线程上下文污染。

允许：读取指定文件、搜索指定路径、输出摘要、列出证据、提出风险。  
禁止：修改文件、运行迁移、访问 .env、改数据库、部署、创建 commit、创建 PR。

主 Codex 职责：分派、过滤、要求证据、综合判断、最终集成、写报告。

### 4.4 Experiment 004：memory distillation

目标：从执行报告、失败记录和项目复盘中提取可复用经验，形成 memory candidates。

候选记忆格式：

```text
Source
Observation
Reusable Lesson
Applies When
Does Not Apply When
Evidence
Risk
Recommended Destination
```

核心原则：

```text
Memory 是经验，不是事实。
CURRENT.md 才是当前事实。
reports/latest.md 才是最新报告。
任务文件才是执行依据。
```

### 4.5 Experiment 005：MCP docs context

目标：验证 Codex / Claude Code 能否通过低风险 MCP 或外部文档上下文获取官方信息，并且不把外部信息误当成项目事实。

输出必须区分：

```text
官方文档信息
当前仓库事实
推断
不确定项
```

第一阶段只允许低风险文档上下文，不接入可写生产工具。

---

## 5. 实验升级为稳定模块的条件

实验能力只有满足以下条件，才能从 lab 升级到 modules：

```text
有明确输入
有明确输出
有适用场景
有禁止事项
有停止条件
有报告格式
能连续稳定通过测试
不破坏 V4 四件套主链路
不增加 Codex / Claude Code 抢改同一批文件的风险
不绕过 GitHub 事实源
不绕过 Codex 最终收口
不绕过 ChatGPT 验收
```

升级后也要保持最小权限原则。比如子代理即使升级，第一阶段也应只读；MCP 即使升级，也应先从文档型 MCP 开始。

---

## 6. 安全边界

Codex Agentic Workbench Lab 当前禁止：

```text
自动部署
自动提交
自动 PR
自动修生产故障
自动改数据库
自动改 .env
自动写正式 memory
多个 subagent 并行写代码
hooks 自动修改文件
把 Hermes 接入默认执行链路
```

涉及生产、密钥、数据库、支付、DNS、Cloudflare、用户数据时，实验必须停止并转入受控任务包。

---

## 7. 与 V4 主链路的关系

V4 是稳定主链路。Lab 是探索轨。

稳定主链路只强制：

```text
State
Handoff
Report
Review
Acceptance
```

Soul、Memory、Skill、Agent、Tool、Heartbeat 都是增强层。它们可以进入研究、归档和实验，但不能自动变成默认项目规则。

---

## 8. 最终目标

成熟后的 Codex Agentic Workbench 可以拥有：

```text
灵魂
事实源
记忆
技能
子代理
外部工具
安全反射
心跳
报告
验收
```

但当前阶段的原则是：

```text
先低风险只读。
先证明有效。
先报告和验收。
再升级稳定模块。
```

---

## 9. 一句话总结

Codex Agentic Workbench 不是把 Hermes 复制到 Codex，而是把 Hermes 的组织哲学翻译成 GitHub 可审计、Codex 可执行、ChatGPT 可验收的工程协作系统。
