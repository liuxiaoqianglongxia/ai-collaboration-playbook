# 新项目接入手册

版本：V0.1  
定位：把任意新项目接入 AI 协作模式 V4 的标准流程

---

## 1. 目标

新项目接入不是直接开始开发。

第一轮只做协作底座，不做业务代码。

目标是在目标项目仓库中建立最小事实源，使 ChatGPT、Codex、Claude Code 都能按同一套状态和规则协作。

---

## 2. 新项目接入原则

```text
先建事实源，再做开发。
先建任务状态，再派 Codex。
先声明边界，再允许修改。
先读总规范库，再读项目适配层。
```

禁止第一轮直接：

```text
开发业务功能
重构代码
部署
改数据库
改 .env / secrets
创建自动化生产流程
```

---

## 3. 新项目必须创建的文件

最小项目适配层：

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
tasks/codex/
tasks/claude/
```

如果涉及部署或 wsl-server，再创建：

```text
ENVIRONMENTS.md
DEPLOYMENT.md
PORTS.md
RUNBOOK.md
reports/deploy/latest.md
```

---

## 4. CHATGPT_START_HERE.md 应包含

```text
项目一句话说明
当前仓库
当前分支
事实源读取顺序
当前阶段
当前最重要任务
启用模块
禁止事项
最新报告位置
```

示例读取顺序：

```text
1. README.md / AI_COLLABORATION_MODE_V4.md from ai-collaboration-playbook
2. CHATGPT_START_HERE.md
3. PROJECT_CARD.md
4. CURRENT.md
5. TASKS.md
6. DECISIONS.md
7. AGENTS.md
8. CLAUDE.md
9. reports/latest.md
10. reports/codex/latest.md
11. reports/claude/latest.md
```

---

## 5. AGENTS.md 应包含

```text
本项目采用 AI 协作模式 V4。
总规范库：liuxiaoqianglongxia/ai-collaboration-playbook

ACTIVE_MODULES:
- CORE_FOUR_PIECE_V4: enabled
- CORE_EXECUTION_HANDOFF_V1: enabled
- CLAUDE_CODE_HARDENING_V1: enabled when Claude Code is used
- ENV_COMMAND_SAFETY_V1: enabled when local shell is involved
- WSL_SERVER_PROD_GUARD_V1: enabled / not needed

本项目特殊边界：
- xxx 文件禁止修改
- xxx 目录是运行数据
- xxx 命令是测试命令
- xxx 环境是生产环境
```

---

## 6. CLAUDE.md 应包含

```text
项目运行方式
测试命令
构建命令
禁止修改范围
常见坑
Claude Code 可承担任务
Claude Code 不得承担任务
默认 task-file 格式
报告格式
```

Claude Code 默认定位：

```text
本地工程增强工具 / 深度代码分析 / 局部修复 / 复审。
```

不是：

```text
项目总控
最终交付负责人
部署负责人
生产修复执行者
```

---

## 7. CURRENT.md 初始格式

```markdown
# CURRENT

## Status

BOOTSTRAP_READY

## Current Phase

Project collaboration bootstrap.

## Current Goal

建立 AI 协作模式 V4 项目适配层。

## Active Modules

```text
CORE_FOUR_PIECE_V4: enabled
CORE_EXECUTION_HANDOFF_V1: enabled
CLAUDE_CODE_HARDENING_V1: enabled when Claude Code is used
ENV_COMMAND_SAFETY_V1: enabled if local shell is involved
WSL_SERVER_PROD_GUARD_V1: not needed / enabled
```

## Next Action

等待 ChatGPT 根据事实源判断是否进入第一个 Codex 任务。
```

---

## 8. TASKS.md 初始格式

```markdown
# TASKS

## READY_FOR_CODEX

空

## IN_PROGRESS

空

## WAITING_FOR_VALIDATION

空

## DONE

- project-ai-collaboration-bootstrap-v1

## BLOCKED

空
```

---

## 9. reports/latest.md 初始格式

```markdown
# Latest Report｜BOOTSTRAP_READY

## Conclusion

BOOTSTRAP_READY

## Summary

已建立 AI 协作模式 V4 项目适配层。

## Active Modules

```text
CORE_FOUR_PIECE_V4: enabled
CORE_EXECUTION_HANDOFF_V1: enabled
CLAUDE_CODE_HARDENING_V1: enabled when Claude Code is used
ENV_COMMAND_SAFETY_V1: enabled if local shell is involved
WSL_SERVER_PROD_GUARD_V1: not needed / enabled
```

## Next Step

等待 ChatGPT / 用户确认第一个正式任务。
```

---

## 10. 新项目接入任务包建议

给 Codex 的第一轮任务应是：

```text
project-ai-collaboration-bootstrap-v1
```

目标：

```text
读取 ai-collaboration-playbook 总规范库。
创建项目适配层。
不做业务开发。
不改 .env。
不改数据库。
不部署。
输出 reports/codex/latest.md。
```

---

## 11. 验收标准

PASS 必须满足：

```text
CHATGPT_START_HERE.md 已创建
PROJECT_CARD.md 已创建
CURRENT.md 已创建
TASKS.md 已创建
DECISIONS.md 已创建
AGENTS.md 已创建
CLAUDE.md 已创建
reports/latest.md 已创建
reports/codex/latest.md 已创建
reports/claude/latest.md 已创建
tasks/codex/ 与 tasks/claude/ 已创建
没有业务代码修改
没有 .env / secrets / 数据库修改
没有部署
```

---

## 12. 新会话提示词

```text
请读取 GitHub 仓库 liuxiaoqianglongxia/ai-collaboration-playbook，先读 README.md、AI_AGENT_ONBOARDING.md、AI_COLLABORATION_MODE_V4.md、NEW_PROJECT_BOOTSTRAP.md。

然后在当前项目中建立 AI 协作模式 V4 的项目适配层。本轮只做协作底座，不做业务开发、不部署、不改 .env、不改数据库。
```
