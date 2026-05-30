# C-C: biaoge-web 跨 WSL 冻结后只读对账

## 1. 审计范围

- 项目: biaoge-web 主仓库 + 2 个 worktree
- 本地路径: `/home/codex/projects/biaoge-web`, `biaoge-web-context-injection`, `biaoge-web-runtime-role-v2`
- 额外: `biaoge-web-role-studio-pr` (非 git 副本)
- 读取文件: AGENTS.md, docs/*.md, reports/, DECISIONS.md
- 未读取: .env, db, node_modules, 生产配置

## 2. 读取的安全文件

| 文件 | 路径 |
|------|------|
| AGENTS.md | biaoge-web/docs/agent-handoff/AGENTS.md |
| DECISIONS.md | biaoge-web/docs/agent-handoff/DECISIONS.md |
| biaoge-web-main-asset-map-v1.md | biaoge-web/docs/ |
| cloud-deployment.md | biaoge-web/docs/ |
| deploy-scripts.md | biaoge-web/docs/ |
| dream-soul-admin-mock-link.md | biaoge-web/docs/ |
| invite-system-design.md | biaoge-web/docs/ |
| visual_assets_plan.md | biaoge-web/docs/ |
| local-runtime-migration-report-2026-05-25.md | biaoge-web/docs/ |
| local-runtime-tunnel-ops.md | biaoge-web/docs/ |
| reports/* (12份) | biaoge-web/docs/dreamsoul-chat-agent/reports/ |
| reports/* (1份) | biaoge-web/runtime/local-deploy/reports/ |

## 3. 跨 WSL 状态对比

| 维度 | wsl-codex | wsl-hermes |
|------|-----------|------------|
| 路径 | /home/codex/projects/biaoge-web | /home/hermes/projects/biaoge-web |
| 分支 | hotfix/v2-orchestrator-async-live | master |
| 未提交 | 14 文件 + 11 修改 | 2 文件 |
| Worktree | context-injection, runtime-role-v2 | 无 |
| 非 git 副本 | role-studio-pr (存在) | 未知 |
| 最近 commit | bb7680d (typing beat fix) | 未知 |
| 分支类型 | hotfix | master |

## 4. 资产评分表

| 资产 | 路径 | 建议归属 | 复用价值 | 完整度 | 整合难度 | 风险分 | 业务相关度 | 总分 | 分类 | 处理建议 |
|------|------|---------|---------|--------|----------|--------|-----------|------|------|----------|
| AGENTS.md (agent-handoff) | biaoge-web/docs/agent-handoff/AGENTS.md | sub2api-maijian/playbook | 5 | 5 | 4 | 5 | 4 | 23 | **A** | GPT/Codex/Hermes 三方交接范本 |
| DreamSoul Chat Agent Reports (12份) | biaoge-web/docs/dreamsoul-chat-agent/reports/ | sub2api-maijian | 4 | 5 | 4 | 5 | 4 | 22 | **A** | 角色工作室流水线报告集 |
| local-runtime-migration-report | biaoge-web/docs/local-runtime-migration-report-2026-05-25.md | sub2api-maijian | 4 | 4 | 4 | 4 | 4 | 20 | **A** | 本地运行时迁移报告 |
| local-runtime-tunnel-ops | biaoge-web/docs/local-runtime-tunnel-ops.md | sub2api-maijian | 3 | 4 | 4 | 4 | 4 | 19 | **B** | Tunnel 运维操作指南 |
| biaoge-web-main-asset-map-v1.md | biaoge-web/docs/ | sub2api-maijian | 3 | 3 | 4 | 5 | 4 | 19 | **B** | 资产地图，文档导航价值 |
| cloud-deployment.md | biaoge-web/docs/ | sub2api-maijian | 3 | 3 | 4 | 4 | 4 | 18 | **B** | 云部署文档 |
| DECISIONS.md (agent-handoff) | biaoge-web/docs/agent-handoff/DECISIONS.md | sub2api-maijian | 3 | 3 | 4 | 5 | 4 | 19 | **B** | biaoge-web 决策记录 |
| codex worktree: context-injection | biaoge-web-context-injection/ | sub2api-maijian | 3 | 4 | 3 | 4 | 4 | 18 | **B** | 上下文注入 hotfix，可能有价值 |
| codex worktree: runtime-role-v2 | biaoge-web-runtime-role-v2/ | sub2api-maijian | 3 | 4 | 3 | 4 | 4 | 18 | **B** | Role Package v2 特性分支 |
| codex worktree: role-studio-pr | biaoge-web-role-studio-pr/ | sub2api-maijian | 2 | 2 | 3 | 3 | 3 | 13 | **C** | 非 git 副本，状态不明 |

## 5. A 类资产

1. **AGENTS.md (agent-handoff)** — GPT/Codex/Hermes 三方交接范本 (23分)
2. **DreamSoul Chat Agent Reports (12份)** — 角色工作室流水线报告集 (22分)
3. **local-runtime-migration-report** — 本地运行时迁移报告 (20分)

## 6. B 类资产

1. **local-runtime-tunnel-ops** — Tunnel 运维指南 (19分)
2. **biaoge-web-main-asset-map-v1.md** — 资产地图 (19分)
3. **DECISIONS.md (agent-handoff)** — biaoge-web 决策 (19分)
4. **cloud-deployment.md** — 云部署文档 (18分)
5. **context-injection worktree** — hotfix 分支 (18分)
6. **runtime-role-v2 worktree** — 特性分支 (18分)

## 7. C/D 类资产

1. **biaoge-web-role-studio-pr** — 非 git 副本，状态不明 (13分)

## 8. X 类禁止入仓资产

| 类型 | 路径 | 原因 |
|------|------|------|
| .env | biaoge-web/.env | 含密钥 |
| product.db | biaoge-web/product.db | 生产数据库 |
| backups/ | biaoge-web/backups/, biaoge-web/data/backups/ | 备份目录 |
| reports/cloudflare-tunnel-cutover.json | biaoge-web/runtime/local-deploy/reports/ | 部署配置 JSON |

## 9. 分流建议

| 目标 | 资产 |
|------|------|
| **ai-collaboration-playbook** | AGENTS.md (agent-handoff) 通用模板版、DreamSoul Chat Agent 报告的方法论部分 |
| **sub2api-maijian** | biaoge-web 全部 docs/、reports/、worktree 资产 |
| **保持本地** | .env, product.db, backups/, 部署配置 |
| **冻结** | 主仓库直到总控裁决分支合并策略 |

## 10. 需要总控裁决的问题

1. **分支冲突**: wsl-hermes 的 `master` vs wsl-codex 的 `hotfix/v2-orchestrator-async-live` — 哪个是当前主线？codex 端 14 个未提交文件是否应提交？
2. **worktree 保留**: context-injection 和 runtime-role-v2 两个 worktree 是否仍有活跃开发价值？
3. **role-studio-pr**: 非 git 副本是否应被吸收回主仓库或清理？
4. **biaoge-web 是否应纳入 sub2api-maijian 组织** — 目前是独立仓库

## 11. 下一步建议

1. P0: **总控裁决 biaoge-web 分支合并策略** — 这是最高优先级问题
2. P1: 脱敏 AGENTS.md agent-handoff 模板入 playbook
3. P1: DreamSoul Chat Agent 报告方法论提炼
4. P2: worktree 清理前确认各分支价值
