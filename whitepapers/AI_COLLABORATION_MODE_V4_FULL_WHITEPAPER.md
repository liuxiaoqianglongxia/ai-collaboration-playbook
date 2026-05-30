# AI 协作模式 V4 完整白皮书

版本：V0.2.6 Full Whitepaper Recovery  
状态：长版归档稿  
适用范围：项目级 AI 协作、GitHub 事实源、Codex 交付、Claude Code 工程探索、ChatGPT 总控验收

---

## 1. 核心判断

V4 的目标不是把更多 AI 塞进项目，也不是让每个工具都去做所有事。V4 的目标是把项目协作拆成稳定岗位，让每个工具只做自己最擅长、最可验证、最不容易越界的工作。

一句话版本：

```text
ChatGPT 管判断。
GitHub 管事实。
Claude Code 管工程探索。
Codex 管交付收口。
```

四件套不是为了显得复杂，而是为了降低复杂项目里的混乱成本。过去的问题通常不是 AI 不够强，而是项目状态散在聊天记录、临时记忆、本地目录、执行报告和口头承诺里。一旦上下文变长，就会出现误判、误写、跨项目污染、重复劳动和生产风险。

V4 解决的不是“模型智商”问题，而是“协作制度”问题。

---

## 2. 四件套职责

### 2.1 ChatGPT：总控 / 架构判断 / 任务包 / 验收

ChatGPT 是总控，不是现场施工队。它负责：

```text
理解用户真实目标
读取 GitHub 事实源
判断项目阶段
识别风险和边界
拆分任务
生成任务文件
验收执行报告
决定下一步
```

ChatGPT 不应该：

```text
不读事实源就判断项目状态
只凭聊天记忆派任务
直接承诺已经完成文件写入
把多个执行线同时派去改同一批文件
绕过 GitHub 事实源验收
```

ChatGPT 的价值在于做架构判断、风险收敛、任务组织和最终验收，而不是替代 Codex 去跑命令。

### 2.2 GitHub：唯一事实源 / 项目状态机 / 留痕系统

GitHub 是唯一事实源。项目状态不以聊天记录、模型记忆、执行者口头描述为准。每个项目都应有最小事实源文件：

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

如果这些文件不存在，第一轮任务不是开发功能，而是建立协作底座。

### 2.3 Codex：现场交付负责人 / 最终集成者 / 报告提交者

Codex 是交付线。它负责读任务文件、改代码、运行检查、整合结果、写报告、提交 PR。Codex 可以借助 Claude Code 做工程探索，但最终责任仍在 Codex。

Codex 负责：

```text
读取任务文件
确认分支和工作区
组织执行
必要时生成 Claude Code task-file
复核 Claude Code 输出
执行最终修改
跑测试
检查 diff
写 reports/codex/latest.md
给出提交和合并建议
```

Codex 不应该：

```text
没有任务文件就直接改代码
把 Claude Code 输出原样当最终结论
擅自部署
擅自改数据库
擅自改 .env / secrets
擅自 force push
擅自扩大任务范围
```

### 2.4 Claude Code：本地工程增强工具 / 深度代码分析 / 局部修复 / 复审

Claude Code 是工程探索工具，不是项目总控。适合它的任务包括：

```text
只读代码路径侦察
调用链分析
测试失败定位
错误栈解释
diff review
回归风险检查
局部修复草案
测试补充草案
```

Claude Code 不负责：

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

## 3. 核心流程

V4 的核心流程是：

```text
用户说进入执行
→ ChatGPT 读取 GitHub 事实源
→ ChatGPT 生成任务文件
→ 任务文件落 GitHub
→ Codex 按任务文件执行
→ Codex 必要时调用 Claude Code
→ Codex 复核 Claude Code 输出
→ Codex 完成修改和测试
→ Codex 写执行报告
→ ChatGPT 按 GitHub 事实源验收
→ 进入下一轮任务或收口
```

重要原则：

```text
讨论可以在聊天里。
执行必须落 GitHub。
报告必须写回 GitHub。
验收必须以 GitHub 为准。
```

如果报告只在聊天里，不能算完整交付。如果任务只在聊天里，不能算正式执行依据。

---

## 4. Codex 任务包模板

````markdown
# Codex Task Package｜<task-name>

## 1. 背景

说明当前项目状态来自哪些 GitHub 文件，为什么要做本轮任务。

## 2. 目标

列出可验收目标。不要写“优化一下”，要写清楚完成后如何判断。

## 3. 范围

允许修改：

```text
<path>
<path>
```

只读范围：

```text
<path>
```

禁止范围：

```text
.env
secrets
生产数据库
部署配置
其他项目仓库
```

## 4. 执行步骤

1. 读取任务文件。
2. 读取 CURRENT / TASKS / DECISIONS / AGENTS。
3. 检查分支和工作区。
4. 必要时生成 Claude Code task-file。
5. 修改允许范围内的文件。
6. 运行测试或检查。
7. 检查 diff。
8. 写 reports/codex/latest.md。

## 5. 验收标准

- 指定文件存在。
- 指定测试通过。
- 未触碰禁止范围。
- 报告写回 GitHub。
- 可回滚。

## 6. 停止条件

- 仓库或分支不匹配。
- 任务和事实源冲突。
- 需要生产权限但未授权。
- 发现密钥或数据库风险。
- 需要跨项目写入。
````

---

## 5. Claude Code task-file 模板

````markdown
# Claude Code Readonly / Local Analysis Task｜<topic>

## 1. 角色

你是本地工程增强工具，只做工程分析或局部修复草案。最终集成由 Codex 负责。

## 2. 输入

```text
任务文件：<path>
分析范围：<path>
相关日志：<path>
输出报告：reports/claude/latest.md
```

## 3. 允许行为

```text
读取文件
搜索代码
分析调用链
解释错误
提出修复建议
生成局部补丁草案
```

## 4. 禁止行为

```text
不部署
不改数据库
不改 .env / secrets
不 force push
不改生产服务
不跨项目写入
不替代 Codex 最终提交
```

## 5. 输出格式

```text
结论：PASS / PARTIAL PASS / FAIL / BLOCKED
读取范围
关键发现
证据路径
建议修改
风险
需要 Codex 复核的点
```
````

---

## 6. Claude Code timeout 分级

Claude Code 不应该默认用一个固定 300 秒上限。推荐分级：

```text
30 秒：可用性检查
120–180 秒：小型 smoke test
300 秒：单文件分析 / 小范围问题定位
600–900 秒：多文件调用链分析 / diff review / 测试失败分析
900–1200 秒：局部修复草案 / 测试补充草案
1200–1800 秒：大范围架构侦察，但必须拆阶段，不允许无限扫全仓
```

推荐调用方式：

```bash
timeout 900 claude --bare -p < task-file.md > reports/claude/latest.md
```

Codex 必须复核 Claude Code 输出。Claude Code 的报告不是最终交付，只是工程输入。

---

## 7. Windows / WSL / Shell 命令安全

很多 AI 工程事故不是模型推理错，而是命令细节错。Windows、WSL、PowerShell、Git Bash、Linux shell 的路径、引号、管道和通配符行为不同。

默认规则：

```text
优先使用项目相对路径
不要写死本机绝对路径
正则表达式加引号
rg / grep 优先用 -e
不要裸写包含 | 的正则
命令失败必须留痕
报告中说明运行环境
```

推荐：

```bash
rg -n -e 'foo|bar|baz' -- .
```

避免：

```bash
rg -n foo|bar|baz .
```

涉及 Windows / WSL 时，任务文件必须写清运行环境、项目路径、禁止路径、是否允许访问 Windows 用户目录。

---

## 8. wsl-server 本机生产保护

当本机有专门的 `wsl-server` 承担生产环境时，它必须按生产环境处理，而不是当作开发 WSL。

默认禁止：

```text
直接开发
随意杀端口
改生产 .env
改生产数据库
docker prune
reset --hard / clean -fd
跳过备份直接部署
```

任何生产变更必须有：

```text
DEPLOYMENT_PLAN
ROLLBACK_PLAN
HEALTHCHECK_PLAN
BACKUP_RECORD
```

---

## 9. 部署任务包模板

````markdown
# Deployment Task Package｜<service>

## 1. 背景

说明部署原因、目标版本、影响范围。

## 2. 生产环境确认

```text
server:
service:
domain:
port:
systemd/docker:
current version:
target version:
```

## 3. 备份计划

```text
code backup:
db backup:
env backup:
config backup:
```

## 4. 部署步骤

1. 只读检查当前状态。
2. 创建备份。
3. 拉取指定 commit / tag。
4. 安装或构建。
5. 切换服务。
6. 健康检查。
7. 写部署报告。

## 5. 回滚计划

```text
rollback command:
rollback version:
db restore:
config restore:
```

## 6. 禁止事项

```text
不改无关服务
不清理全局 Docker
不删除备份
不改未授权端口
不跳过健康检查
```

## 7. 验收标准

- 服务可启动。
- 健康检查通过。
- 关键接口可访问。
- 日志无明显错误。
- 回滚路径仍可用。
````

---

## 10. PASS / PARTIAL PASS / FAIL / BLOCKED

ChatGPT 验收必须输出四选一：

```text
PASS
PARTIAL PASS
FAIL
BLOCKED
```

定义：

```text
PASS：目标完成，证据充分，测试通过，未触碰禁止范围。
PARTIAL PASS：主要目标完成，但存在明确剩余项或未覆盖验证。
FAIL：目标未完成、证据不足、测试失败或触碰禁止范围。
BLOCKED：因权限、凭证、环境、事实源不足或安全边界无法继续。
```

验收依据必须来自任务文件、commit / PR diff、reports/codex/latest.md、reports/claude/latest.md、测试结果、CURRENT.md、TASKS.md、DECISIONS.md。

---

## 11. 分阶段策略

```text
阶段 A：协作底座，只建事实源，不做业务开发。
阶段 B：只读诊断，理解项目、风险和当前状态。
阶段 C：受控开发，Codex 按任务文件修改允许范围。
阶段 D：复审和验收，Claude Code 可做 diff review，ChatGPT 验收。
阶段 E：生产变更，必须有部署计划、备份、回滚和健康检查。
阶段 F：复盘沉淀，把经验写入 DECISIONS / CURRENT / templates / checklists。
```

---

## 12. 禁止事项总表

```text
不读事实源不得判断项目状态
不落任务文件不得进入执行
不写报告不得算完成
不把聊天记录当事实源
不把 Claude Code 输出当最终结论
不让多个 agent 抢改同一批文件
不自动部署
不自动改数据库
不自动改 .env / secrets
不跨项目写入
不把 lab 实验直接升级为稳定模块
```

---

## 13. 一句话总结

V4 不是一套口号，而是一套交付纪律。

```text
ChatGPT 做判断。
GitHub 做事实。
Claude Code 做探索。
Codex 做交付。
报告写回仓库。
验收看证据。
```
