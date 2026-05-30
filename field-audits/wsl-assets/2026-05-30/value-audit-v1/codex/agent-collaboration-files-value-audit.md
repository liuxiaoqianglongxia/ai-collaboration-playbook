# C-E: 协作文件模板价值审计

## 1. 审计范围

- 项目: 所有已识别的 AGENTS.md / CLAUDE.md / CHATGPT_START_HERE.md / CURRENT.md / TASKS.md / DECISIONS.md / RUNBOOK.md
- 读取路径: sub2api, sub2api-delivery-clean, sub2api-pr1-docs-ops, sub2api-pr1-docs-ops-v2, aoxue-edu-clean, aoxue-edu-clean.bad, hermes-agent, biaoge-web, biaoge-web worktrees, dream-soul-control
- 未读取: 含敏感信息的项目特定内容

## 2. 读取的安全文件

| 文件类型 | 出现位置数 | 示例路径 |
|----------|-----------|----------|
| AGENTS.md | 12 份 | sub2api/, biaoge-web/docs/agent-handoff/, hermes-agent/, dream-soul-control/docs/agent-handoff/ |
| CLAUDE.md | 4 份 | sub2api/, sub2api-delivery-clean/, sub2api-pr1-docs-ops/, sub2api-pr1-docs-ops-v2/ |
| CHATGPT_START_HERE.md | 4 份 | sub2api/, sub2api-delivery-clean/, sub2api-pr1-docs-ops/, sub2api-pr1-docs-ops-v2/ |
| CURRENT.md | 3 份 | sub2api/, sub2api-delivery-clean/, sub2api-pr1-docs-ops/ |
| TASKS.md | 3 份 | sub2api/, sub2api-delivery-clean/, sub2api-pr1-docs-ops/ |
| DECISIONS.md | 10+ 份 | sub2api/, aoxue-edu-clean/, hermes-core-audit-private/, biaoge-web/docs/agent-handoff/ |
| RUNBOOK.md | 4 份 | sub2api/, sub2api-delivery-clean/, sub2api-pr1-docs-ops/, sub2api-pr1-docs-ops-v2/ |

## 3. 模板价值评估

### 3.1 AGENTS.md — 多 Agent 协作规范

| 变体 | 项目 | 复用价值 | 通用度 | 说明 |
|------|------|---------|--------|------|
| sub2api AGENTS.md | sub2api-maijian | **高** | 高 | 最完整的工程协作规范，包含工作规则、完成定义、V3.1 协作规则 |
| biaoge-web AGENTS.md | biaoge-web | **高** | 高 | GPT/Codex 两角色分工规范，简洁有效 |
| dream-soul-control AGENTS.md | DreamSoul | **高** | 高 | GPT/Codex/Hermes 三角色规范，含 Hermes 只读审查定位 |
| hermes-agent AGENTS.md | Hermes | **中** | 中 | 开发指南，非协作规范 |
| aoxue-edu-clean AGENTS.md | aoxue-edu | **中** | 中 | 教培项目版 |

**提炼建议**: 从 sub2api + dream-soul-control + biaoge-web 三个变体中提炼通用 AGENTS.md 模板，支持 2-3 角色配置。

### 3.2 CLAUDE.md — Claude Code 角色定义

| 变体 | 项目 | 复用价值 | 通用度 | 说明 |
|------|------|---------|--------|------|
| sub2api CLAUDE.md | sub2api-maijian | **高** | 高 | 清晰的"定位-允许-禁止"结构 |

**提炼建议**: sub2api 的 CLAUDE.md 结构 (定位/允许/禁止) 是最佳实践，可直接模板化。

### 3.3 CHATGPT_START_HERE.md — 多 Agent 引导入口

| 变体 | 项目 | 复用价值 | 通用度 | 说明 |
|------|------|---------|--------|------|
| sub2api CHATGPT_START_HERE.md | sub2api-maijian | **高** | 高 | 多 Agent 引导入口，指向 AGENTS.md, CLAUDE.md, CURRENT.md 等 |

**提炼建议**: 作为 playbook 的"新项目 Agent 协作启动"模板。

### 3.4 CURRENT.md — 事实源状态追踪

| 变体 | 项目 | 复用价值 | 通用度 | 说明 |
|------|------|---------|--------|------|
| sub2api CURRENT.md | sub2api-maijian | **高** | 高 | 单仓事实源协议，含里程碑、当前阶段、唯一事实源声明 |

**提炼建议**: CURRENT.md 是最有价值的协作协议之一，应提炼为 playbook 标准模板。

### 3.5 TASKS.md — 任务追踪

| 变体 | 项目 | 复用价值 | 通用度 | 说明 |
|------|------|---------|--------|------|
| sub2api TASKS.md | sub2api-maijian | **中** | 中 | 任务列表，与 CURRENT.md 配合使用 |

**提炼建议**: 作为 CURRENT.md 模板的配套文件。

### 3.6 DECISIONS.md — ADR 决策日志

| 变体 | 项目 | 复用价值 | 通用度 | 说明 |
|------|------|---------|--------|------|
| sub2api DECISIONS.md | sub2api-maijian | **高** | 高 | 决策记录含日期、状态 |
| hermes-core-audit DECISIONS.md | hermes | **高** | 高 | 已冻结决策，含分层架构决策 |
| biaoge-web DECISIONS.md | biaoge-web | **中** | 中 | 项目特定决策 |

**提炼建议**: 通用 ADR 模板入 playbook。

### 3.7 RUNBOOK.md — 运维手册

| 变体 | 项目 | 复用价值 | 通用度 | 说明 |
|------|------|---------|--------|------|
| sub2api RUNBOOK.md | sub2api-maijian | **高** | 高 | wsl-server guard 运维范本，含多层守护 |
| sub2api-delivery-clean RUNBOOK.md | sub2api-maijian | 中 | 中 | worktree 副本 |
| sub2api-pr1-docs-ops RUNBOOK.md | sub2api-maijian | 中 | 中 | worktree 副本 |

**提炼建议**: 生产运维手册模板入 playbook，含 guard 层结构和健康检查模式。

## 4. 资产评分表

| 资产 | 来源 | 建议归属 | 复用价值 | 完整度 | 整合难度 | 风险分 | 业务相关度 | 总分 | 分类 | 处理建议 |
|------|------|---------|---------|--------|----------|--------|-----------|------|------|----------|
| CURRENT.md 协议 | sub2api | playbook | 5 | 5 | 5 | 5 | 5 | 25 | **A** | **最高优先级** — 提炼为 playbook 标准模板 |
| AGENTS.md 三角色规范 | dream-soul-control | playbook | 5 | 5 | 4 | 5 | 5 | 24 | **A** | 提炼 GPT/Codex/Hermes 通用模板 |
| CLAUDE.md 角色定义 | sub2api | playbook | 5 | 5 | 5 | 5 | 4 | 24 | **A** | 定位-允许-禁止 结构模板化 |
| CHATGPT_START_HERE.md | sub2api | playbook | 5 | 5 | 5 | 5 | 4 | 24 | **A** | 多 Agent 引导入口模板 |
| RUNBOOK.md 运维范本 | sub2api | playbook | 4 | 5 | 4 | 4 | 5 | 22 | **A** | 生产运维手册模板 |
| DECISIONS.md ADR 模式 | sub2api + hermes | playbook | 4 | 5 | 5 | 5 | 4 | 23 | **A** | ADR 决策日志模板 |
| TASKS.md 任务追踪 | sub2api | playbook | 3 | 4 | 5 | 5 | 4 | 21 | **A** | 配套 CURRENT.md |
| AGENTS.md 双角色规范 | biaoge-web | playbook | 4 | 4 | 5 | 5 | 4 | 22 | **A** | 简化版 GPT/Codex 模板 |
| CLAUDE_CODE_HARDENING_V1.md | sub2api/orchestration | playbook | 5 | 4 | 4 | 5 | 5 | 23 | **A** | Claude Code 加固检查清单 |

## 5. A 类资产 (全部 9 项)

以上 9 项全部 A 类，因为协作文件模板是 playbook 的核心价值所在。

## 6. B/C/D/X 类

- **C 类**: 各项目 worktree 副本中的重复协作文档 — 价值在于比较差异，不单独提炼
- **X 类**: 协作文档中可能涉及的内部 URL、端口、API endpoint — 模板化时需替换为占位符

## 7. 项目专属 vs 通用模板判断

### 可抽象为通用模板的内容

| 模式 | 来源 | 说明 |
|------|------|------|
| 定位-允许-禁止 | sub2api/CLAUDE.md | 通用 Claude Code 角色定义 |
| GPT/Codex/Hermes 三角色 | dream-soul-control/AGENTS.md | 通用多 Agent 分工 |
| 事实源声明 | sub2api/CURRENT.md | 通用单仓事实源协议 |
| 完成定义 | sub2api/AGENTS.md | 通用 Done Definition |
| 决策记录格式 | hermes-core-audit/DECISIONS.md | 通用 ADR 格式 |
| 多层守护 | sub2api/RUNBOOK.md | 通用生产运维模式 |
| 工作规则 | sub2api/AGENTS.md | 通用 Agent 工作规则 |
| Agent 引导入口 | sub2api/CHATGPT_START_HERE.md | 通用新项目启动入口 |

### 应保留在业务仓的内容

| 内容 | 原因 |
|------|------|
| 具体端口、URL、域名 | 业务特定 |
| 具体里程碑 hash | 业务特定 |
| 生产事故细节 | 业务特定 |
| 具体部署步骤 | 业务特定 |

### 应提炼进 playbook 的内容

| 内容 | 处理方式 |
|------|---------|
| 所有协作文件模板 | 脱敏占位符替换 |
| AGENTS.md 多角色配置 | 2/3 角色变体 |
| CLAUDE.md 定位-允许-禁止 | 通用结构 |
| CURRENT.md 事实源协议 | 通用模板 |
| DECISIONS.md ADR 格式 | 通用模板 |
| RUNBOOK.md 运维手册 | 通用模板 + 检查清单 |

## 8. 分流建议

| 目标 | 资产 |
|------|------|
| **ai-collaboration-playbook** | 全部 9 个通用协作模板 (脱敏版) |
| **sub2api-maijian** | 业务特定的协作文档 (含具体端口、URL、配置) |
| **biaoge-web** | 业务特定的 biaoge-web 协作文档 |
| **aoxue-edu** | 业务特定的 aoxue-edu 协作文档 |

## 9. 需要总控裁决的问题

1. **协作文件模板的版本控制** — 是否应在 playbook 维护"权威模板"，各项目仓库通过 symlink 或 copy 引用
2. **CLAUDE.md 的 Claude Code 项目级支持** — 如果 Claude Code 自动读取 CLAUDE.md，playbook 模板应如何与业务仓库的 CLAUDE.md 共存
3. **AGENTS.md 的放置位置** — 是放在项目根目录还是 docs/ 子目录

## 10. 下一步建议

1. P0: 提炼 CURRENT.md 模板 — 最高优先级协作协议
2. P0: 提炼 AGENTS.md 模板 (2角色版 + 3角色版)
3. P1: 提炼 CLAUDE.md 定位-允许-禁止模板
4. P1: 提炼 CHATGPT_START_HERE.md 引导入口模板
5. P1: 提炼 DECISIONS.md ADR 模板
6. P2: 提炼 RUNBOOK.md 运维手册模板 + 检查清单
7. P2: 提炼 TASKS.md 任务追踪模板
