# 项目级 AI 协作模式 V4｜四件套核心版

版本：V4.0  
状态：稳定主链路规范  
定位：所有项目默认协作模式的总说明

---

## 1. 核心目标

V4 的目标不是让更多 AI 同时参与，而是让每个 AI 只做自己最擅长的事。

```text
ChatGPT 管判断。
GitHub 管事实。
Claude Code 管工程探索和局部分析。
Codex 管集成、测试、报告和最终收口。
```

最高目标：

```text
少角色
清边界
强交付
可验证
可追踪
少烧 Codex 探索额度
充分发挥 Claude Code 工程能力
保护生产环境
避免 Windows / WSL / Shell 命令坑
```

---

## 2. 四件套分工

```text
ChatGPT：总控 / 架构判断 / 任务包 / 验收
GitHub：唯一事实源 / 项目状态机 / 留痕系统
Codex：现场交付负责人 / 最终集成者 / 报告提交者
Claude Code：本地工程增强工具 / 深度代码分析 / 局部修复 / 复审
```

更直白地说：

```text
ChatGPT 负责脑子。
GitHub 负责记忆。
Claude Code 负责工程肌肉。
Codex 负责手脚和收口。
```

---

## 3. 模块体系

V4 使用模块化规则。

```text
CORE_FOUR_PIECE_V4：四件套稳定主链路
CORE_EXECUTION_HANDOFF_V1：执行交接协议
CLAUDE_CODE_HARDENING_V1：Claude Code 性能与调用策略
ENV_COMMAND_SAFETY_V1：Windows / WSL / Shell 命令安全
WSL_SERVER_PROD_GUARD_V1：wsl-server 本机生产保护
```

启用原则：

```text
CORE_FOUR_PIECE_V4：所有项目默认启用
CORE_EXECUTION_HANDOFF_V1：所有项目默认启用
CLAUDE_CODE_HARDENING_V1：使用 Claude Code 时启用
ENV_COMMAND_SAFETY_V1：涉及 Windows / WSL / PowerShell / Git Bash / 本机 shell 时启用
WSL_SERVER_PROD_GUARD_V1：涉及 wsl-server / 部署 / 端口 / .env / 数据库 / uploads / logs 时启用
```

---

## 4. GitHub 是唯一事实源

项目状态不以聊天记录、口头描述、AI 记忆、旧报告为准。

项目状态以仓库文件为准：

```text
CHATGPT_START_HERE.md
PROJECT_CARD.md
CURRENT.md
TASKS.md
DECISIONS.md
AGENTS.md
CLAUDE.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

如果这些文件不存在，第一轮应先建立项目适配层，不应直接开发。

---

## 5. ChatGPT 职责

ChatGPT 负责：

```text
理解用户真实目标
读取 GitHub 事实源
判断项目阶段
判断启用模块
识别风险和边界
设计任务拆分
写 Codex 任务文件
验收 Codex / Claude Code 报告
决定下一步
```

ChatGPT 不应该：

```text
不读事实源就判断项目状态
一上来就派 Codex 干活
同时安排 Codex 和 Claude Code 修改同一批文件
在没有验收标准时进入执行
把聊天记录当事实源
```

---

## 6. Codex 职责

Codex 是现场交付负责人。

Codex 负责：

```text
读取任务文件
检查分支和工作区状态
判断是否需要 Claude Code
生成 Claude Code task-file
复核 Claude Code 输出
执行最终修改
跑测试
检查 git diff
写 reports/codex/latest.md
给出是否建议提交
```

Codex 不应该：

```text
擅自部署
擅自改数据库
擅自改 .env / secrets
擅自 force push
擅自扩大任务范围
把 Claude Code 输出原样当最终结论
把所有工作甩给 Claude Code
```

---

## 7. Claude Code 职责

Claude Code 是工程增强工具。

适合做：

```text
只读代码路径侦察
调用链分析
测试失败定位
错误栈解释
diff review
回归风险检查
局部修复草案
测试补充草案
小范围受限修改
```

不负责：

```text
项目方向判断
产品路线判断
是否部署
是否提交
替代 Codex 最终收口
替代 GitHub 成为事实源
直接操作生产环境
```

---

## 8. 执行交接协议

当用户说“进入执行 / 可以安排 Codex / 发给 Codex”时，不应直接把一大段任务包只放在聊天里。

正确流程：

```text
用户说进入执行
→ ChatGPT 创建 tasks/codex/YYYY-MM-DD-<task>.md
→ 更新 CURRENT.md
→ 更新 TASKS.md
→ 更新 reports/latest.md
→ 聊天里只给一句可转发给 Codex 的指令
→ Codex 按 GitHub 任务文件执行
→ Codex 写 reports/codex/latest.md
→ ChatGPT 按 GitHub 事实源验收
```

一句话：

```text
讨论可以在聊天里，执行必须落 GitHub。
```

---

## 9. Claude Code 调用策略

默认用 task-file 调用 Claude Code。

推荐命令：

```bash
timeout 900 claude --bare -p < /tmp/claude-task-xxx.md > reports/claude/latest.md
```

timeout 分级：

```text
30 秒：可用性检查
120–180 秒：smoke test
300 秒：单文件分析 / 小范围问题定位
600–900 秒：多文件调用链分析 / diff review / 测试失败分析
900–1200 秒：局部修复草案 / 测试补充草案
1200–1800 秒：大范围架构侦察，但必须拆阶段，不允许无限扫全仓
```

Claude Code 输出必须被 Codex 复核，不能直接作为项目最终结论。

---

## 10. 环境安全

涉及 shell 命令时必须遵守：

```text
用相对路径
正则加引号
rg / grep 优先用 -e
不裸写 |
不写死本机绝对路径
报告中说明运行环境
命令失败必须留痕
```
