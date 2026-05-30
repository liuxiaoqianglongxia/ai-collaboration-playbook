# C-A: sub2api-maijian 价值审计

## 1. 审计范围

- 项目: sub2api-maijian 主仓库
- 本地路径: `/home/codex/projects/sub2api`
- 分支: `feature/sub2api-maijian-mvp-v1-delivery-20260528-182302`
- Remote: `https://github.com/liuxiaoqianglongxia/sub2api-maijian.git`
- 含 8 个 worktree (delivery-clean, pr1-docs-ops, pr1-docs-ops-v2, pr2-upstream-integration, qwen-fix, qwen-thinking, upstream-v129-sync, local-dev)
- 读取文件: AGENTS.md, CLAUDE.md, CURRENT.md, TASKS.md, DECISIONS.md, RUNBOOK.md, reports/, orchestration/
- 未读取: .env, auth.json, token, db, node_modules, dist, build

## 2. 读取的安全文件

| 文件 | 路径 |
|------|------|
| AGENTS.md | /home/codex/projects/sub2api/AGENTS.md |
| CLAUDE.md | /home/codex/projects/sub2api/CLAUDE.md |
| CURRENT.md | /home/codex/projects/sub2api/CURRENT.md |
| TASKS.md | /home/codex/projects/sub2api/TASKS.md |
| DECISIONS.md | /home/codex/projects/sub2api/DECISIONS.md |
| RUNBOOK.md | /home/codex/projects/sub2api/RUNBOOK.md |
| CHATGPT_START_HERE.md | /home/codex/projects/sub2api/CHATGPT_START_HERE.md |
| CLAUDE_CODE_HARDENING_V1.md | /home/codex/projects/sub2api/orchestration/CLAUDE_CODE_HARDENING_V1.md |
| reports/claude/latest.md | /home/codex/projects/sub2api/reports/claude/latest.md |
| reports/codex/latest.md | /home/codex/projects/sub2api/reports/codex/latest.md |
| reports/incident/latest.md | /home/codex/projects/sub2api/reports/incident/latest.md |
| reports/incident/wsl-server-guard-closeout.md | /home/codex/projects/sub2api/reports/incident/wsl-server-guard-closeout.md |

## 3. 资产评分表

| 资产 | 路径 | 建议归属 | 复用价值 | 完整度 | 整合难度 | 风险分 | 业务相关度 | 总分 | 分类 | 处理建议 |
|------|------|---------|---------|--------|----------|--------|-----------|------|------|----------|
| AGENTS.md | sub2api/AGENTS.md | sub2api-maijian | 4 | 5 | 5 | 5 | 5 | 24 | **A** | 提炼通用模板入 playbook |
| CLAUDE.md | sub2api/CLAUDE.md | sub2api-maijian | 4 | 5 | 5 | 5 | 5 | 24 | **A** | 提炼为通用 Claude Code 角色定义模板 |
| CURRENT.md | sub2api/CURRENT.md | sub2api-maijian | 5 | 5 | 4 | 5 | 5 | 24 | **A** | CURRENT.md 模式是优秀的事实源协议 |
| TASKS.md | sub2api/TASKS.md | sub2api-maijian | 3 | 4 | 4 | 5 | 5 | 21 | **A** | 保持业务仓，模板化入 playbook |
| DECISIONS.md | sub2api/DECISIONS.md | sub2api-maijian | 4 | 4 | 4 | 5 | 5 | 22 | **A** | ADR 决策模式可提炼为通用模板 |
| RUNBOOK.md | sub2api/RUNBOOK.md | sub2api-maijian | 5 | 5 | 3 | 4 | 5 | 22 | **A** | wsl-server guard runbook 是生产运维范本 |
| CHATGPT_START_HERE.md | sub2api/CHATGPT_START_HERE.md | sub2api-maijian | 4 | 5 | 5 | 5 | 5 | 24 | **A** | 多 Agent 引导入口是最佳实践 |
| CLAUDE_CODE_HARDENING_V1.md | sub2api/orchestration/ | sub2api-maijian | 5 | 4 | 4 | 5 | 5 | 23 | **A** | Claude Code 加固规范是高价值方法论 |
| 生产事故报告 | sub2api/reports/incident/ | sub2api-maijian | 4 | 5 | 3 | 3 | 5 | 20 | **A** | WSL Server Guard 关闭报告是运维范本 |
| Codex 执行报告 | sub2api/reports/codex/ | sub2api-maijian | 3 | 4 | 5 | 4 | 5 | 21 | **A** | 执行报告格式可标准化为模板 |
| sub2api 主工程代码 | sub2api/backend,frontend/ | sub2api-maijian | 5 | 5 | 1 | 4 | 5 | 20 | **A** | 核心业务代码，不动不归仓 |
| sub2api worktree (8个) | sub2api/.git/worktrees/ | sub2api-maijian | 3 | 4 | 3 | 4 | 4 | 18 | **B** | 部分可能已过期，需总控裁决 |
| Character Studio 文档 | sub2api/CHARACTER_STUDIO_HERMES.md | sub2api-maijian | 4 | 3 | 4 | 4 | 5 | 20 | **A** | 形象馆平台资产，明确归属 DreamSoul 线 |

## 4. A 类资产

1. **AGENTS.md** — 多 Agent 协作规范模板 (24分)
2. **CURRENT.md** — 单仓事实源协议 (24分)
3. **CHATGPT_START_HERE.md** — Agent 引导入口 (24分)
4. **CLAUDE_CODE_HARDENING_V1.md** — Claude Code 加固规范 (23分)
5. **DECISIONS.md** — ADR 决策模式 (22分)
6. **RUNBOOK.md** — wsl-server 生产运维范本 (22分)
7. **CLAUDE.md** — Claude Code 角色定义模板 (24分)
8. **TASKS.md** — 任务追踪模式 (21分)
9. **Codex 执行报告** — 执行报告格式标准 (21分)
10. **生产事故报告** — WSL Server Guard 运维范本 (20分)
11. **Character Studio 文档** — 形象馆平台资产 (20分)
12. **sub2api 主工程代码** — 核心业务 (20分)

## 5. B 类资产

1. **sub2api worktree (8个)** — delivery-clean 和 pr1-docs-ops 等可能仍有价值，qwen-fix/qwen-thinking 可能已过期 (18分)

## 6. C/D 类资产

- **legacy docs**: OPERATIONS.md, TODO.md, HANDOFF.md, PROJECT_STATE.md — 已被 V3.1 协作文档替代，但仍有历史参考价值 (12-14分)

## 7. X 类禁止入仓资产

| 类型 | 路径 | 原因 |
|------|------|------|
| .env | sub2api/.env, runtime/sub2api-maijian/.env | 含密钥 |
| auth.json | .hermes/auth.json | 含认证凭据 |
| token 文件 | .config/sub2api-maijian/cloudflare-api-token | Cloudflare Token |
| 生产数据库 | runtime/sub2api-maijian/postgres_data/ | 运行态数据 |
| Redis 数据 | runtime/sub2api-maijian/redis_data/ | 运行态数据 |
| Docker 数据 | runtime/sub2api-maijian/data/ | 运行态数据 |
| 备份 | runtime/sub2api-maijian/backups/ | 备份数据 |
| logs | .claude/telemetry/, .codex/logs_2.sqlite | 运行日志 |

## 8. 分流建议

| 目标 | 资产 |
|------|------|
| **ai-collaboration-playbook** | AGENTS.md/CLAUDE.md/CURRENT.md/TASKS.md/DECISIONS.md/RUNBOOK.md/CHATGPT_START_HERE.md 的**通用模板版本**；CLAUDE_CODE_HARDENING_V1.md；执行报告格式标准 |
| **sub2api-maijian** | 全部 sub2api 工程代码、业务专用协作文档、reports、orchestration、Character Studio 文档 |
| **保持本地** | 运行态数据、.env、token、数据库 |

## 9. 需要总控裁决的问题

1. **sub2api 8 个 worktree 清理** — qwen-fix, qwen-thinking 是否已过期，是否允许 prune
2. **sub2api 是否已成为工程事实源** — CURRENT.md 明确 sub2api-maijian 是唯一事实源，但 dream-soul-control 仍有一些活跃状态追踪
3. **legacy docs 去留** — OPERATIONS.md/TODO.md/HANDOFF.md/PROJECT_STATE.md 是否标记为已弃用

## 10. 下一步建议

1. P0: 提炼 sub2api 全套协作文件 (AGENTS/CLAUDE/CURRENT/TASKS/DECISIONS/RUNBOOK/CHATGPT_START_HERE) 为通用模板入 playbook
2. P0: 确认 worktree 清理策略
3. P1: CLAUDE_CODE_HARDENING_V1.md 提炼为通用加固检查清单入 playbook
4. P1: 生产事故报告格式提炼为通用 incident report 模板
