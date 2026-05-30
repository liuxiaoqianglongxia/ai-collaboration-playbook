# 资产价值审计 V1 — C 线总报告

> 执行员: wsl-codex
> 执行时间: 2026-05-30
> 执行线: **C 线** — 工程 / sub2api / DreamSoul / biaoge / 协作文件资产价值审计
> 输入报告: summary.md, wsl-codex-audit.md, independent-review.md
> 严格只读: 未修改任何项目代码、配置、密钥、数据库

---

## 1. 结论

**PASS** ✅

- 6 份子报告全部完成
- 覆盖 sub2api-maijian、DreamSoul、biaoge-web、sub2api worktree、协作文件模板、第三方实验资产
- 全部报告含评分表、分类、分流建议
- 未提交任何敏感文件

---

## 2. 当前执行线

**C 线** — wsl-codex 工程资产价值审计

| 子代理 | 状态 | 输出文件 |
|--------|------|----------|
| C-A: sub2api-maijian | ✅ 完成 | sub2api-value-audit.md |
| C-B: DreamSoul / Character Studio | ✅ 完成 | dreamsoul-character-studio-value-audit.md |
| C-C: biaoge-web 跨 WSL 对账 | ✅ 完成 | biaoge-web-value-audit.md |
| C-D: sub2api worktree | ✅ 完成 | sub2api-worktree-value-audit.md |
| C-E: 协作文件模板 | ✅ 完成 | agent-collaboration-files-value-audit.md |
| C-F: 第三方实验资产 | ✅ 完成 | third-party-local-experiments-value-audit.md |

---

## 3. Top 30 高价值资产

按总分降序排列：

| 排名 | 资产 | 来源 | 总分 | 分类 | 建议归属 |
|------|------|------|------|------|----------|
| 1 | CURRENT.md 事实源协议 | sub2api | 25 | **A** | playbook 模板 |
| 2 | AGENTS.md (sub2api) | sub2api | 24 | **A** | playbook 模板 + sub2api-maijian |
| 3 | CLAUDE.md (sub2api) | sub2api | 24 | **A** | playbook 模板 |
| 4 | CHATGPT_START_HERE.md | sub2api | 24 | **A** | playbook 模板 |
| 5 | sub2api-pr1-docs-ops worktree | sub2api | 24 | **A** | sub2api-maijian |
| 6 | sub2api-delivery-clean worktree | sub2api | 24 | **A** | sub2api-maijian |
| 7 | AGENTS.md 三角色规范 | dream-soul-control | 24 | **A** | playbook 模板 |
| 8 | DreamSoul Agent Handoff | dream-soul-control | 23 | **A** | playbook 模板 + sub2api-maijian |
| 9 | DreamSoul 审计报告集 (20+份) | dream-soul-control | 23 | **A** | playbook 方法论 + sub2api-maijian |
| 10 | CLAUDE_CODE_HARDENING_V1.md | sub2api/orchestration | 23 | **A** | playbook 检查清单 |
| 11 | DECISIONS.md ADR 模式 | sub2api + hermes | 23 | **A** | playbook 模板 |
| 12 | AGENTS.md (biaoge-web) | biaoge-web | 23 | **A** | playbook 模板 |
| 13 | DreamSoul DECISIONS.md | dream-soul-control | 21 | **A** | sub2api-maijian |
| 14 | TASKS.md 任务追踪 | sub2api | 21 | **A** | playbook 模板 |
| 15 | Codex 执行报告格式 | sub2api/reports/codex | 21 | **A** | playbook 模板 |
| 16 | Character Studio Hermes | sub2api | 21 | **A** | sub2api-maijian |
| 17 | RUNBOOK.md 运维范本 | sub2api | 22 | **A** | playbook 模板 |
| 18 | DreamSoul Chat Agent Reports (12份) | biaoge-web | 22 | **A** | sub2api-maijian |
| 19 | 生产事故报告 | sub2api/reports/incident | 20 | **A** | playbook 模板 |
| 20 | local-runtime-migration-report | biaoge-web | 20 | **A** | sub2api-maijian |
| 21 | dream-soul-control 仓库 | dream-soul-control | 20 | **A** | sub2api-maijian 组织 |
| 22 | Character Studio Worker | sub2api | 20 | **A** | sub2api-maijian |
| 23 | sub2api 主工程代码 | sub2api | 20 | **A** | sub2api-maijian |
| 24 | sub2api-pr1-docs-ops-v2 worktree | sub2api | 21 | **A** | sub2api-maijian |
| 25 | biaoge-web AGENTS.md | biaoge-web | 22 | **A** | playbook 模板 |
| 26 | dream-soul-adapter | dream-soul-adapter | 19 | **B** | sub2api-maijian |
| 27 | dream-soul-bff | dream-soul-bff | 19 | **B** | sub2api-maijian |
| 28 | local-runtime-tunnel-ops | biaoge-web | 19 | **B** | sub2api-maijian |
| 29 | sillytavern-runtime-patched | sillytavern-runtime-patched | 19 | **B** | 仅本地保留 |
| 30 | dreamsoul-chat-agent | dreamsoul-chat-agent | 18 | **B** | sub2api-maijian |

---

## 4. 推荐优先整合 Top 10

按"提炼进 ai-collaboration-playbook"的优先级排序：

| 优先级 | 整合内容 | 目标位置 | 说明 |
|--------|---------|----------|------|
| 1 | **CURRENT.md 事实源协议模板** | playbook/templates/ | 最高价值协作协议 (25分) |
| 2 | **AGENTS.md 多角色模板 (2角色 + 3角色)** | playbook/templates/ | GPT/Codex 和 GPT/Codex/Hermes 两种变体 (24分) |
| 3 | **CLAUDE.md 定位-允许-禁止模板** | playbook/templates/ | Claude Code 角色定义最佳实践 (24分) |
| 4 | **CHATGPT_START_HERE.md 引导入口模板** | playbook/templates/ | 多 Agent 引导标准 (24分) |
| 5 | **DECISIONS.md ADR 决策日志模板** | playbook/templates/ | 通用决策记录格式 (23分) |
| 6 | **CLAUDE_CODE_HARDENING_V1.md 加固检查清单** | playbook/checklists/ | Claude Code 安全加固标准 (23分) |
| 7 | **RUNBOOK.md 运维手册模板** | playbook/templates/ | 生产运维手册 + 检查清单 (22分) |
| 8 | **TASKS.md 任务追踪模板** | playbook/templates/ | 配套 CURRENT.md (21分) |
| 9 | **Codex 执行报告格式标准** | playbook/templates/ | 执行报告模板 (21分) |
| 10 | **生产事故报告格式标准** | playbook/templates/ | Incident report 模板 (20分) |

---

## 5. 仓库分流建议

| 目标仓库 | 应入仓资产 | 数量 |
|----------|-----------|------|
| **ai-collaboration-playbook** | 10 个通用协作模板 (脱敏版) | 10 |
| **sub2api-maijian** | sub2api 主工程、DreamSoul 全部项目、Character Studio、biaoge-web 文档 | 全部 |
| **maijian-wechat-content-lab** | 仅公众号文章素材，不含 Character Studio | 0 (本轮 C 线无发现) |
| **shanxi-edu-hot / aoxue-edu** | 仅教培相关资产 | 0 (本轮 C 线无发现) |
| **仅本地保留** | SillyTavern patched 版、bendi-llm-gateway、feishu_docs_tool | 3 |
| **仅登记，不入仓** | SillyTavern 全部副本 (~1.5GB)、运行态数据、数据库 | 全部 |

---

## 6. 不入仓资产

| 类别 | 说明 | 规模 |
|------|------|------|
| SillyTavern 源码 | 4 个副本含 node_modules，总计 ~1.5GB | 不入仓 |
| 运行态 .hermes/ | 含密钥、状态、会话 | 不入仓 |
| state.db / SQLite | 运行态数据库 | 不入仓 |
| 生产数据库 | aoxue_edu_production.db, product.db | 不入仓 |
| .env / auth.json / token | 密钥和认证文件 | 不入仓 |
| Docker 数据 | postgres_data, redis_data | 不入仓 |
| 浏览器 profile | .camofox/ | 不入仓 |
| 备份目录 | 各 backups/ | 不入仓 |
| 传输压缩包 | *.tar.gz, *.zip | 不入仓 |

---

## 7. 风险与冻结项

### 7.1 必须冻结

| 项目 | 风险 | 建议 |
|------|------|------|
| **biaoge-web** | 两个 WSL 中不同分支，codex 端有大量未提交变更 | 冻结，不合并不清理 |
| **aoxue-edu** | 两个 WSL 中不同状态，含生产数据库副本 | 冻结，先制定数据库策略 |
| **hermes-core-audit-private** | 两 WSL 同一分支但 commit 不同，分叉风险 | 以 GitHub 最新为事实源，不 force push |
| **sub2api worktree (qwen-fix, qwen-thinking)** | 可能已过期的实验分支 | 确认上游合并状态后 prune |

### 7.2 总控裁决问题

| 问题 | 描述 | 紧急度 |
|------|------|--------|
| 1 | **biaoge-web 分支合并策略** — hermes master vs codex hotfix | P0 |
| 2 | **DreamSoul 仓库远程化** — control/adapter/bff 是否独立或归入 sub2api-maijian 组织 | P1 |
| 3 | **sub2api worktree 清理** — 8 个 worktree 中 3 个可能已过期 | P1 |
| 4 | **协作文件模板版本控制** — playbook 权威模板 vs 各项目副本 | P1 |
| 5 | **bendi-llm-gateway 远程化** — 是否创建私有仓库 | P2 |
| 6 | **SillyTavern 保留策略** — 1.5GB 是否可缩减为 74M | P2 |

---

## 8. 需要 ChatGPT 总控裁决的问题

1. **biaoge-web 跨 WSL 分支冲突** — hermes (master, 2 未提交) vs codex (hotfix, 14 未提交) — 哪个是当前主线？
2. **DreamSoul 平台线仓库策略** — dream-soul-control 有独立 GitHub，是否应归入 sub2api-maijian 组织？
3. **协作文件模板权威源** — playbook 维护权威模板还是各项目仓库自行维护？
4. **hermes-core-audit-private 分叉** — 两 WSL 同一分支不同 commit，以哪个为准？
5. **bendi-llm-gateway 远程化** — 是否值得创建私有仓库？

---

## 9. 下一阶段任务包建议

| 优先级 | 任务 | 说明 |
|--------|------|------|
| P0 | **协作文件模板提炼** — 10 个通用模板入 playbook | 本轮 C 线最高价值产出 |
| P0 | **biaoge-web 跨 WSL 解冻** — 总控裁决后合并 | 最高风险项 |
| P1 | **DreamSoul 平台线整合** — 仓库归口 + 远程化策略 | 平台资产统一管理 |
| P1 | **sub2api worktree 清理** — prune 过期分支 | 减少维护负担 |
| P1 | **DreamSoul 审计报告脱敏** — 方法论部分入 playbook | 知识沉淀 |
| P2 | **SillyTavern 保留策略** — 清理到 74M | 释放 1.4GB 磁盘 |
| P2 | **bendi-llm-gateway 远程化** — 创建私有仓库 | 服务器镜像远程化 |

---

## 10. 安全确认

- ✅ 未读取任何 .env / auth.json / token / secret / key 文件内容
- ✅ 未读取任何 .db / .sqlite / .sqlite3 内容
- ✅ 未读取 node_modules / dist / build / logs / backups
- ✅ 未扫描 /mnt/c / /mnt/d / /mnt/e
- ✅ 未修改任何业务项目源码
- ✅ 未删除/移动/清理任何本地项目
- ✅ 未操作 wsl-server
- ✅ 未 force push
- ✅ 未 merge 到 main
- ✅ 未创建新 GitHub 仓库
- ✅ 未改 Git remote
- ✅ 未提交运行态 .hermes/ / sessions / state.db
- ✅ 未提交生产数据库或备份
- ✅ 未提交 SillyTavern 源码
- ✅ 仅提交 field-audits/wsl-assets/2026-05-30/value-audit-v1/codex/ 目录下 Markdown

---

## 附录: C 线输出文件

```
field-audits/wsl-assets/2026-05-30/value-audit-v1/codex/
├── index.md                                    ← 本文件
├── sub2api-value-audit.md                      ← C-A
├── dreamsoul-character-studio-value-audit.md   ← C-B
├── biaoge-web-value-audit.md                   ← C-C
├── sub2api-worktree-value-audit.md             ← C-D
├── agent-collaboration-files-value-audit.md    ← C-E
└── third-party-local-experiments-value-audit.md ← C-F
```
