# 资产价值审计 V1 — H 线总报告

**生成时间**: 2026-05-30 19:45 CST
**执行线**: H 线（wsl-hermes）
**审计范围**: Hermes skills / knowledge standards / 公众号资产 / 教培资产 / 方法论
**子报告**: H-A（skills）/ H-B（standards）/ H-C（maijian-wechat）/ H-D（edu）/ H-E（methodology）

---

## 1. 结论

**PARTIAL PASS**

- 5 份子报告全部完成，评分体系一致应用
- 所有资产已按 A/B/C/D/X 分类，分流建议明确
- 部分资产因含项目绑定/脱敏需求需总控裁决后才能入仓
- 未发现需要读取敏感文件才能继续的情况
- 未修改任何业务项目源码或配置

---

## 2. 当前执行线

**H 线 — wsl-hermes**

审计覆盖：
- `/home/hermes/.hermes/skills/` — 86 个 skills（52 个含 SKILL.md，30 个精读 + 22 个快速扫描）
- `/home/hermes/knowledge/standards/` — 18 份标准文档
- `/home/hermes/projects/maijian-wechat/` + `maijian-wechat-private-repo/`
- `/home/hermes/projects/aoxue-edu/` + `shanxi-edu-hot/` + `taiyuan-schools-map/`
- `/home/hermes/knowledge/archive/reports/`
- `/home/hermes/projects/hermes-core-audit-private/`
- `/home/hermes/projects/hermes-system-spec-public/`
- `hermes_overview_v*.md` 系列

---

## 3. Top 30 高价值资产

按总分降序排列，跨 5 份子报告统一排名：

| 排名 | 资产 | 来源报告 | 总分 | 建议归属 |
|------|------|----------|------|----------|
| 1 | 01-terminology.md（三层文档架构） | H-B | 25 | ai-collaboration-playbook |
| 2 | 06-state-md.md（11 字段状态模板） | H-B | 25 | ai-collaboration-playbook |
| 3 | 10-ssot-drift-gate.md（漂移校验） | H-B | 25 | ai-collaboration-playbook |
| 4 | github-ai-collaboration-pattern | H-A | 24 | ai-collaboration-playbook |
| 5 | hermes-skill-development-standard | H-A | 24 | ai-collaboration-playbook |
| 6 | feishu-broadcast-standard | H-A | 24 | sub2api-maijian |
| 7 | 02-structure.md（目录结构规范） | H-B | 24 | ai-collaboration-playbook |
| 8 | context-injection-protocol | H-A | 23 | ai-collaboration-playbook |
| 9 | article-writing-workflow | H-A | 23 | maijian-wechat-content-lab |
| 10 | team-boss（团队总控路由） | H-A | 23 | ai-collaboration-playbook |
| 11 | 05-naming.md（命名规范） | H-B | 23 | ai-collaboration-playbook |
| 12 | 13-context-injection.md | H-B | 23 | ai-collaboration-playbook |
| 13 | 14-team-capability-framework.md | H-B | 23 | ai-collaboration-playbook |
| 14 | sanitized-public-demo-creation | H-A | 22 | ai-collaboration-playbook |
| 15 | hermes-skills-architecture-refactoring | H-A | 22 | ai-collaboration-playbook |
| 16 | role-memory-pipeline | H-A | 22 | ai-collaboration-playbook |
| 17 | project-fact-layer-audit | H-A | 22 | ai-collaboration-playbook |
| 18 | wechat-article-camofox | H-A | 22 | maijian-wechat-content-lab |
| 19 | SSOT 漂移校验方法论 (M01) | H-E | 22 | ai-collaboration-playbook |
| 20 | 上下文注入方法论 (M02) | H-E | 23 | ai-collaboration-playbook |
| 21 | GitHub 协作四件套方法论 (M08) | H-E | 21 | ai-collaboration-playbook |
| 22 | 03-projects.md（项目规范） | H-B | 21 | ai-collaboration-playbook |
| 23 | maijian-wechat-publish-config | H-A | 21 | maijian-wechat-content-lab |
| 24 | hermes-weekly-audit | H-A | 21 | ai-collaboration-playbook |
| 25 | standard-driven-team-upgrade | H-A | 21 | ai-collaboration-playbook |
| 26 | topic-mining-synthesis | H-A | 21 | ai-collaboration-playbook |
| 27 | 15-team-registry-and-boundaries.md | H-B | 21 | ai-collaboration-playbook |
| 28 | 16-memory-purity-and-boundary.md | H-B | 21 | ai-collaboration-playbook |
| 29 | aoxue-edu 代码库 | H-D | 21 | aoxue-edu |
| 30 | publish_map.jsonl（发布真值源） | H-C | 20 | maijian-wechat-content-lab（脱敏后） |

---

## 4. 推荐优先整合 Top 10

以下 10 个资产建议下一阶段优先整合进 `ai-collaboration-playbook`：

| 优先级 | 资产 | 整合形式 | 预估工作量 |
|--------|------|----------|------------|
| 1 | 01-terminology.md | 直接入仓 → `standards/TERMINOLOGY.md` | 30 分钟 |
| 2 | 06-state-md.md | 改写为模板 → `templates/PROJECT_STATE_TEMPLATE.md` | 30 分钟 |
| 3 | 10-ssot-drift-gate.md | 改写为检查清单 → `checklists/SSOT_DRIFT_GATE.md` | 30 分钟 |
| 4 | github-ai-collaboration-pattern | 脱敏后入仓 → `protocols/GITHUB_AI_COLLAB.md` | 1 小时 |
| 5 | 02-structure.md | 改写为模板 → `templates/PROJECT_STRUCTURE_TEMPLATE.md` | 30 分钟 |
| 6 | context-injection-protocol | 提取协议框架 → `protocols/CONTEXT_INJECTION.md` | 1 小时 |
| 7 | team-boss | 通用化后入仓 → `protocols/TEAM_BOSS_ROUTING.md` | 1 小时 |
| 8 | sanitized-public-demo-creation | 脱敏后入仓 → `workflows/SANITIZED_DEMO.md` | 1 小时 |
| 9 | article-writing-workflow | 项目绑定剥离后入仓 → `workflows/ARTICLE_WRITING.md` | 1 小时 |
| 10 | 14-team-capability-framework.md | 直接入仓 → `standards/TEAM_CAPABILITY.md` | 30 分钟 |

---

## 5. 仓库分流建议

### 5.1 → ai-collaboration-playbook

| 资产类别 | 数量 | 代表资产 |
|----------|------|----------|
| A 类 skills | 12 | github-ai-collaboration-pattern, context-injection-protocol, article-writing-workflow, team-boss, sanitized-public-demo-creation, role-memory-pipeline, project-fact-layer-audit, hermes-weekly-audit, standard-driven-team-upgrade, hermes-skill-development-standard, hermes-skills-architecture-refactoring, topic-mining-synthesis |
| A 类 standards | 12 | 01-terminology, 02-structure, 03-projects, 05-naming, 06-state-md, 10-ssot-drift-gate, 13-context-injection, 14-team-capability, 15-team-registry, 16-memory-purity, 17-article-lifecycle-sop |
| 方法论资产 | 6 | M01 SSOT, M02 Context Injection, M08 GitHub 协作四件套, Darwin Ratchet, 三层治理哲学, 团队能力 5 层模型 |
| 报告/白皮书 | 3 | hermes-system-whitepaper (脱敏版), EXPORT_MANIFEST, SECURITY_REDACTION_REPORT |

### 5.2 → maijian-wechat-content-lab

| 资产类别 | 数量 | 代表资产 |
|----------|------|----------|
| 文章资产 | ~40 | maijian-wechat/articles/ 正式稿 |
| 发布脚本 | 21 | preflight_*.py, validate_*.py |
| 封面 Prompt | ~13 | visuals/*.md 系列 |
| 生产规则 | 3 | PRODUCTION_CONSTITUTION.md, HANDOFF_CONTRACT.md, WECHAT_LAYOUT_STANDARD.md |
| 发布真值源 | 1 | publish_map.jsonl（脱敏后） |
| Skills | 3 | article-writing-workflow, wechat-article-camofox, maijian-wechat-publish-config |

### 5.3 → shanxi-edu-hot / aoxue-edu

| 资产类别 | 数量 | 代表资产 |
|----------|------|----------|
| aoxue-edu 代码库 | 1 | 完整项目（已封盘，产品级 ERP） |
| 教育 skills | 4 | aoxue-edu-development, aoxue-feishu-query, aoxue-data-query, school-data-quality-fix |
| shanxi-edu-hot 代码 | 1 | 完整项目（升学情报 + 自动化） |
| 教育 runbooks | 4 | automation/maintenance/search/wechat-account-pool |
| taiyuan-schools-map | 1 | 学校地图 + 67 所学校数据 |

### 5.4 → sub2api-maijian

| 资产类别 | 数量 | 代表资产 |
|----------|------|----------|
| feishu-broadcast-standard | 1 | 飞书播报 SSOT |
| feishu-file-sender | 1 | 飞书文件发送 |
| hermes-feishu-streaming-card | 1 | 飞书流式卡片（sidecar 架构） |
| feishu-card-rendering-reality | 1 | 飞书卡片渲染真相 |

### 5.5 仅本地保留

| 资产类别 | 数量 | 原因 |
|----------|------|------|
| WSL 运维 skills | 2 | wsl-vhdx-compaction, wsl-disk-compaction（仅运维用） |
| 本地工具 skills | 5 | lmstudio-local-setup, gpu-memory-upgrade, moss-tts-deployment, hermes-tts-provider-addition, dashscope-qwen-tts-config |
| 主题/UI skills | 3 | dark-tech-ui-style, premium-dark-theme-upgrade, element-plus-popup-positioning-fix |
| 实验性 assets | ~10 | browser-automation, brain-graph, market-insight, maijian-video 等 |
| 运行态 .hermes/ | 全量 | 含密钥和状态数据库 |

---

## 6. 不入仓资产

### 6.1 X 类禁止入仓

| 类型 | 路径/说明 | 原因 |
|------|-----------|------|
| 密钥文件 | `.env`, `.env.*`, `*.env` (9+ 路径) | 含 API 密钥 |
| 认证凭据 | `auth.json` + 9 个备份 | 含 provider 认证信息 |
| Token 文件 | `cloudflare-api-token`, `agent_gateway_token`, `llm_api_key` | 生产令牌 |
| 运行态数据库 | `state.db` (~1.5GB + 797MB WAL), `memory_store.db` (~167MB), `response_store.db`, `trace.db`, `kanban.db` | Hermes 运行态数据 |
| 生产数据库 | `aoxue_edu_production.db` (多副本), `product.db` | 真实业务数据 |
| 备份目录 | aoxue-edu/backups/ (14 目录), biaoge-web/backups/, maijian-wechat/backups/, hermes/backups/ | 含完整数据库副本 |
| 会话历史 | `.hermes/sessions/` (87 目录) | 交互记录，无复用价值 |
| 粘贴板 | `.hermes/pastes/` | 临时数据 |
| 日志 | `.hermes/logs/`, `aoxue-edu/logs/`, 等 | 无复用价值 |
| 补丁备份 | `.hermes/patch-backups/` (23 目录) | 历史补丁，无复用价值 |
| 状态快照 | `.hermes/state-snapshots/` | 运行态快照 |
| 浏览器数据 | `.camofox/profiles/`, `browser_screenshots/` | 浏览器 profile |

---

## 7. 风险与冻结项

| 风险项 | 描述 | 建议 |
|--------|------|------|
| maijian-wechat 250 个未提交文件 | 量大，需区分文章资产 vs 临时文件 | P0 审计 |
| aoxue-edu 封盘状态 | 已标记"封盘"但有 3 个未推送 commit | 总控决定是否解封 |
| aoxue-edu 生产数据库多副本 | hermes + codex 各有多份 | 安全处置，不入仓 |
| hermes-core-audit-private 分叉 | hermes + codex 同分支不同 commit | 确认 SSOT |
| biaoge-web 跨 WSL 不同分支 | hermes master vs codex hotfix | 总控裁决合并策略 |
| skills 库膨胀 | 83 目录中 31 个（37%）为空 | 精简 |
| wsl-vhix-compaction 重复 | wsl-vhix-compaction 与 wsl-disk-compaction 功能重叠 | 保留一个 |
| knowledge standards 编号冲突 | 07 号有两个文件，缺失 12 号 | 重新编号 |

---

## 8. 需要 ChatGPT 总控裁决的问题

| # | 问题 | 涉及资产 | 紧迫度 |
|---|------|----------|--------|
| Q1 | **aoxue-edu 是否解封重启？** 已封盘但产品完成度 100%，是否作为"培训机构老板自用系统"继续开发？ | aoxue-edu 代码库 | P0 |
| Q2 | **aoxue 系列 skills 出仓策略** — 作为 shanxi-edu 子包整体出仓，还是只提炼通用模式？ | aoxue-edu-development 等 4 skills | P1 |
| Q3 | **publish_map.jsonl 脱敏规则** — 哪些字段必须脱敏后才能入公开仓？ | publish_map.jsonl | P0 |
| Q4 | **maijian-wechat backups/ 去留** — 28 个备份快照是全部保留、只保留 N 个、还是完全不入仓？ | maijian-wechat/backups/ | P1 |
| Q5 | **reviews/daily-style 系列处理** — 25+ 天每日风格报告是全部入仓还是只保留精华？ | maijian-wechat/reviews/daily-style/ | P2 |
| Q6 | **Hermes 品牌名策略** — playbook 中保留"Hermes"还是用通用名称？影响所有方法论资产 | 全部方法论 | P0 |
| Q7 | **skills 库精简** — 31 个空目录 + autonomous-ai-agents 空目录是否删除？ | .hermes/skills/ | P2 |
| Q8 | **knowledge standards 编号修正** — 07 号重复、缺失 12 号，如何重新编号？ | knowledge/standards/ | P1 |
| Q9 | **00-system-overview 脱敏深度** — 完全保留架构但删实体名，还是只保留"三层定义"概念？ | 00-system-overview.md | P1 |
| Q10 | **taiyuan-schools-map 是否整合进 shanxi-edu-hot？** | taiyuan-schools-map | P2 |
| Q11 | **OpenClaw 协作出仓脱敏** — hermes-openclaw-collaboration 含群 ID/Bot App ID，需彻底脱敏 | hermes-openclaw-collaboration | P1 |
| Q12 | **11-model-foundation 是否值得重写** — 当前版本价值极低，但"模型策略"概念可能有通用价值 | 11-model-foundation.md | P2 |

---

## 9. 下一阶段任务包建议

### P0 — 立刻执行（本周）

1. **Top 10 资产入仓** — 将 Top 10 高价值资产按整合形式写入 playbook
2. **maijian-wechat 250 文件分类审计** — 区分文章/脚本/临时/缓存
3. **publish_map.jsonl 脱敏** — 生成脱敏副本后入仓
4. **PRODUCTION_CONSTITUTION + HANDOFF_CONTRACT + WECHAT_LAYOUT_STANDARD 入仓**

### P1 — 近期执行（两周内）

5. **12 个 A 类 standards 入仓** — 修正编号冲突后直接复制
6. **B 类 skills 改造** — 去除项目绑定，统一配置接口
7. **aoxue-edu 解封决策** — 确认后执行
8. **maijian-wechat 文章资产批量迁移** — 排除 draft/.bak/.new

### P2 — 中期规划（一个月内）

9. **21 个 B 类方法论资产分批处理** — 按脱敏难度排序
10. **skills 库精简** — 删除空目录和重复技能
11. **建立技能入仓审查流程** — 新技能必须通过三项门槛
12. **maijian-wechat backups/ 决策** — 确认后执行

---

## 10. 安全确认

- [x] 未读取任何 `.env` / `auth.json` / `*.db` / `*.sqlite` 内容
- [x] 未提交任何密钥、数据库、日志、备份、node_modules
- [x] 未修改任何业务项目源码
- [x] 未删除/移动/清理任何本地项目
- [x] 未操作 wsl-server
- [x] 未 force push
- [x] 仅提交 `value-audit-v1/hermes/` 目录下 Markdown 文件
- [x] 所有评分基于文档/README/SKILL.md 等安全文件

---

*本报告由 wsl-hermes 资产价值审计员（Claude Code）于 2026-05-30 自动生成。*
*H 线 5 份子报告全部完成，等待 ChatGPT 总控读取后统一裁决。*
