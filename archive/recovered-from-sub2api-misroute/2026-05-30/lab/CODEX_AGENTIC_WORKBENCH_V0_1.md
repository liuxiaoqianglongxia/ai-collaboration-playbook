# Codex Agentic Workbench Lab V0.1

版本：V0.1  
状态：实验室总纲  
定位：V4 稳定主链路之上的研究扩展轨

---

## 1. 定位

Codex Agentic Workbench Lab 不是 V4 默认主链路。

它是一个实验室，用来研究如何把 Hermes 的组织哲学翻译成 Codex / Claude Code / GitHub 可执行的工程系统。

V4 主链路继续保持：

```text
ChatGPT：总控 / 架构判断 / 任务包 / 验收
GitHub：唯一事实源 / 项目状态机 / 留痕系统
Codex：现场交付负责人 / 最终集成者 / 报告提交者
Claude Code：本地工程增强工具 / 深度代码分析 / 局部修复 / 复审
```

Lab 只做实验，不直接进入业务项目默认流程。

---

## 2. 核心判断

```text
不要把 Hermes 原样搬进 Codex。
应该把 Hermes 的组织哲学，翻译成 Codex 的工程执行系统。
```

Hermes 更像组织工作台：

```text
角色
记忆
团队
技能
soul
心跳
上下文注入
长期项目治理
```

Codex 更像工程执行体：

```text
读取仓库
修改代码
运行命令
跑测试
生成 diff
处理 PR
调用工具
接入 skills / subagents / automations / hooks / MCP
```

融合方向不是让 Hermes 重新成为默认第五角色，而是：

```text
Hermes 提供组织哲学
Codex 提供工程执行能力
GitHub 提供唯一事实源
ChatGPT 提供总控判断和架构验收
Claude Code 提供局部工程增强
```

---

## 3. 七个实验方向

Codex Agentic Workbench Lab 暂定七层实验方向：

```text
Soul Layer        灵魂层
State Layer       状态层
Memory Layer      记忆层
Skill Layer       技能层
Agent Layer       子代理层
Tool Layer        MCP 工具层
Heartbeat Layer   心跳层
```

重要边界：

```text
V4 主链路只强制 State + Handoff + Report。
Soul / Memory / Skill / Agent / Tool / Heartbeat 都是可选增强层。
```

---

## 4. 当前优先实验

V0.1 只做五个只读实验：

```text
001-heartbeat-readonly.md
002-skill-start-here-audit.md
003-subagent-readonly-scout.md
004-memory-distillation.md
005-mcp-docs-context.md
```

这些实验共同原则：

```text
默认只读。
不自动修改业务代码。
不自动提交。
不自动部署。
不改数据库。
不碰 .env / secrets。
不触碰生产环境。
```

---

## 5. 稳定模块升级条件

实验能力只有满足以下条件，才能升级到 `modules/`：

```text
有明确输入。
有明确输出。
有适用场景。
有禁止事项。
有停止条件。
有报告格式。
能连续稳定通过测试。
不会破坏 V4 四件套主链路。
不会增加 Codex / Claude Code 争抢同一批文件的风险。
```

---

## 6. 当前不做什么

V0.1 不做：

```text
自动部署
自动提交
自动 PR
自动修生产故障
自动改数据库
自动改 .env
自动写正式 memory
Hermes as MCP Server 实接生产项目
多个 subagent 并行写代码
hooks 自动修改文件
```

---

## 7. 实验报告要求

每个实验完成后，应输出：

```text
实验名称
实验目标
输入文件
执行方式
输出文件
是否只读
是否越界
是否节省人工 / Codex 成本
是否建议继续
是否建议升级稳定模块
```

---

## 8. 最终目标

长期成熟后，Codex Agentic Workbench 可以拥有：

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

但当前阶段只追求：

```text
先把实验事实文件落地。
先做低风险只读验证。
先证明有用，再升级为稳定模块。
```
