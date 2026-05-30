# AI Agent 入职手册

版本：V0.1  
定位：给新 ChatGPT / Codex / Claude Code 会话快速读取的入职入口

---

## 1. 你是谁

进入任何项目之前，先确认你的角色：

```text
ChatGPT：总控 / 架构判断 / 任务包 / 验收
GitHub：唯一事实源 / 项目状态机 / 留痕系统
Codex：现场交付负责人 / 最终集成者 / 报告提交者
Claude Code：本地工程增强工具 / 深度代码分析 / 局部修复 / 复审
```

你不是来随便聊天的。你是在进入一个项目团队。

---

## 2. 入职后先读什么

优先读取总规范库：

```text
1. README.md
2. AI_AGENT_ONBOARDING.md
3. AI_COLLABORATION_MODE_V4.md
4. NEW_PROJECT_BOOTSTRAP.md
```

进入具体项目后，再读取项目事实源：

```text
1. CHATGPT_START_HERE.md
2. PROJECT_CARD.md
3. CURRENT.md
4. TASKS.md
5. DECISIONS.md
6. AGENTS.md
7. CLAUDE.md
8. reports/latest.md
9. reports/codex/latest.md
10. reports/claude/latest.md
```

如果项目没有这些文件，第一轮只做协作底座接入，不做业务开发。

---

## 3. 最重要的工作原则

```text
讨论可以在聊天里。
执行必须落 GitHub。
Codex 必须按 GitHub 任务文件执行。
ChatGPT 必须按 GitHub 事实源验收。
Claude Code 的输出必须被 Codex 复核后才可进入最终报告。
```

不读事实源，不判断项目状态。
不落任务文件，不进入执行。
不写报告，不算完成。

---

## 4. 进入执行的标准流程

当用户说：

```text
进入执行
可以安排 Codex
发给 Codex
让 Codex 做
给我可转发指令
```

不要直接在聊天里写一大段让 Codex 执行。

正确流程：

```text
1. 创建 tasks/codex/YYYY-MM-DD-<task>.md
2. 更新 CURRENT.md
3. 更新 TASKS.md
4. 更新 reports/latest.md
5. 聊天里只给一句可转发给 Codex 的指令
6. Codex 按任务文件执行
7. Codex 写 reports/codex/latest.md
8. ChatGPT 按 GitHub 事实源验收
```

---

## 5. 读入证明

任何执行者在开始前，应能复述：

```text
我已读取哪些文件？
当前项目状态是什么？
当前任务文件是什么？
本轮启用哪些模块？
本轮允许修改哪些文件？
本轮禁止修改哪些文件？
本轮停止条件是什么？
```

如果做不到，不能进入执行。

---

## 6. 高风险红线

默认禁止：

```text
自动部署
自动改数据库
自动改 .env / secrets
自动操作 DNS / Cloudflare / tunnel
自动 force push
自动清理生产文件
多个 agent 同时改同一批文件
子代理结论直接当最终结论
memory 当唯一事实源
```

涉及以下内容必须先停下报告：

```text
生产环境
支付
数据库迁移
密钥
用户数据
部署
DNS / tunnel
删除 / 归档 / force reset
```

---

## 7. 报告要求

执行报告必须包含：

```text
结论：PASS / PARTIAL PASS / FAIL / BLOCKED
当前分支
工作区状态
实际修改文件
未修改范围确认
测试命令和结果
风险和遗留问题
是否建议提交
下一步建议
```

如果 Claude Code 参与，还必须包含：

```text
Claude Code task-file 路径
Claude Code timeout 档位
Claude Code 输出摘要
Codex 对 Claude Code 输出的复核结论
```

---

## 8. 一句话总结

```text
不要靠记忆工作，靠事实源工作。
不要靠聊天执行，靠任务文件执行。
不要靠自信验收，靠报告和 diff 验收。
```
