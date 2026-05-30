# Hermes 组织哲学到 Codex 工程执行的翻译笔记

版本：V0.1  
状态：实验室参考笔记  
参考来源：Hermes Genesis Season 1 public pack

参考仓库：

```text
https://github.com/liuxiaoqianglongxia/hermes-genesis-season1-pack
```

---

## 1. 核心判断

```text
不要把 Hermes 原样搬进 Codex。
应该把 Hermes 的组织哲学，翻译成 Codex 的工程执行系统。
```

Hermes 是方法论来源，不是 V4 默认执行组件。

V4 默认执行组件仍然只有：

```text
ChatGPT
GitHub
Codex
Claude Code
```

---

## 2. Hermes 和 Codex 的差异

Hermes 更像组织工作台，擅长：

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

Codex 更像工程执行体，擅长：

```text
读取仓库
修改代码
运行命令
跑测试
生成 diff
处理 PR
调用工具
使用 skills / subagents / automations / hooks / MCP
```

所以融合方式不是复制，而是翻译。

---

## 3. 概念映射

| Hermes 概念 | Codex 侧对应物 | 融合方式 |
|---|---|---|
| Soul / 人格内核 | SOUL.md + AGENTS.md + DECISIONS.md | 写成项目使命、价值观、禁区、执行哲学 |
| Skill / 技能 | .agents/skills/<skill>/SKILL.md | 把重复流程封装成可触发技能 |
| 记忆 | Codex memory + repo memory | 本地 memory 存偏好，仓库 memory 存可审计经验 |
| 心跳 | Automations + GitHub Actions | 定期检查任务、PR、报告、风险、状态冲突 |
| Agent / 角色 | roles + subagent prompt + agent config | 每个角色有 profile、experience、failure |
| 子代理 | Subagents | 并行侦察、测试、审计、总结，不抢主线程 |
| MCP | MCP servers | 连接 GitHub、文档、浏览器、Figma、Sentry、Hermes |
| Hooks / 反射 | .codex/hooks 或 Claude hooks | 执行前拦截危险命令，执行后生成报告候选 |
| Dashboard / 可观测 | reports/ + GitHub Issues/PR | 先文件化，后产品化 |

---

## 4. 继承的原则

从 Hermes 继承的最重要原则：

```text
boss 不能写胖。
```

翻译到 Codex 协作体系里就是：

```text
AGENTS.md 不能写胖。
AI_COLLABORATION_MODE_V4.md 不能无限变胖。
总规范库应该模块化。
项目适配层应该薄。
每轮任务文件应该具体。
```

正确拆法：

```text
README.md：总入口
AI_AGENT_ONBOARDING.md：AI 入职手册
AI_COLLABORATION_MODE_V4.md：完整白皮书
NEW_PROJECT_BOOTSTRAP.md：新项目接入
modules/：稳定模块
templates/：模板
checklists/：验收清单
lab/：实验室
```

---

## 5. 什么能进入主链路

可以进入 V4 主链路的能力，必须满足：

```text
稳定
可验证
可回滚
可报告
不会破坏 GitHub 事实源
不会让多个 agent 抢同一批文件
不会绕过 Codex 最终收口
不会绕过 ChatGPT 验收
```

当前已经进入主链路：

```text
四件套职责
GitHub 事实源
任务文件执行
Claude Code task-file 调用
Codex 最终收口
ChatGPT 验收
Windows / WSL 命令安全
wsl-server 生产保护
```

---

## 6. 什么只能放在实验室

以下能力先放在 `lab/`：

```text
Soul Layer
Role Memory
Skill Library
Subagents
MCP Context Bridge
Heartbeat Automations
Hooks Safety
Memory Distillation
```

这些能力需要先证明：

```text
是否稳定触发
是否真的减少人工和 token 成本
是否不会污染事实源
是否不会越权
是否能被报告和验收
```

---

## 7. Hermes 的最终位置

Hermes 在本体系中的位置：

```text
组织哲学来源
公开资料参考
角色 / 记忆 / team-boss / registry 的设计灵感
未来 MCP 知识源候选
实验室研究对象
```

Hermes 不是：

```text
默认第五角色
默认开发执行者
默认审计员
默认事实源
```

一句话：

```text
Hermes 是方法论来源，不是 V4 默认执行组件。
```

---

## 8. 当前建议

当前只做：

```text
把 V4 稳定主链路落地。
把 lab/ 实验事实文件落地。
先做只读实验。
证明有效后再升级成稳定模块。
```

不要做：

```text
大系统化
自动生产修复
自动部署
多 agent 并行写代码
把 memory 当事实源
把 Hermes 接入默认执行链路
```
