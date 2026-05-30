# WSL 资产审计总账 — 2026-05-30

> 汇总审计员: wsl-codex (只读汇总, 未修改任何项目代码或配置)
> 输入报告: `wsl-hermes-audit.md`, `wsl-codex-audit.md`
> 审计范围: `wsl-hermes` (/home/hermes), `wsl-codex` (/home/codex)
> 排除: `wsl-server` (生产环境, 仅建立只读边界)

---

## 1. 总结论

- **wsl-hermes 审计 PASS** ✅ — 只读盘点完成, 报告已入仓
- **wsl-codex 审计 PASS** ✅ — 只读盘点完成, 报告已入仓
- 两份报告均为**只读审计**, 未修改任何项目代码、配置或密钥
- **未提交**: 密钥、数据库、日志、node_modules、备份、源码大文件
- **wsl-server 暂缓审计**, 仅建立只读边界 (见 `wsl-server-readonly-boundary.md`)

---

## 2. 三个 WSL 的定位

| WSL 身份 | 定位 | 核心内容 |
|----------|------|----------|
| **wsl-hermes** | 知识 / 内容 / Hermes 方法资产库 | Hermes Agent 运行环境、86 skills、知识标准、公众号内容生产链路、AI 协作方法论 |
| **wsl-codex** | 工程 / 执行 / 平台项目资产库 | sub2api/maijian 平台、DreamSoul、biaoge-web 前端、SillyTavern 实验、多 worktree 协作 |
| **wsl-server** | 生产环境, 暂不参与资产清理 | 服务部署、数据库、Docker 容器、Cloudflare 隧道 — 仅允许只读健康摘要 |

---

## 3. 关键发现

### 3.1 wsl-hermes

| 指标 | 数量 |
|------|------|
| Git 仓库 | 19 个 (含 ApexSpiral 审计子仓库) |
| Hermes Skills | 86 个 |
| Knowledge Standards | 17 份 |
| Hermes Plugins | 20+ |
| Hermes Roles | 8 |
| 大型运行态数据库 | ~2.3GB (state.db / memory_store.db 等) |
| 重大风险 | maijian-wechat 有 **250 个未提交文件** 需要单独审计 |

关键资产:

- 86 个 Hermes Skills 覆盖文章写作、上下文注入、团队协作、飞书广播、Cron 审计等
- 17 份 Knowledge Standards 为系统级协作标准 (术语、结构、端口、命名、状态文件、备份、团队、同步)
- 大量 prompt / workflow / runbook / report 资产
- 多个 `.env`、`auth.json`、数据库、备份需要安全处置
- hermes-core-audit-private 含多系统上下文审计报告

### 3.2 wsl-codex

| 指标 | 数量 |
|------|------|
| Git 仓库 | 17 个 (含 8 个 sub2api worktree) |
| Worktree (sub2api) | 8 个 (delivery-clean, pr1-docs-ops, pr2-upstream-integration, qwen-fix, qwen-thinking, upstream-v129-sync, local-dev, pr1-docs-ops-v2) |
| 非 Git 项目 | 10 个 (SillyTavern 系列、dreamsoul-chat-agent、feishu_docs_tool 等) |
| AGENTS.md | 12 份 |
| CLAUDE.md | 4 份 |
| CHATGPT_START_HERE.md | 4 份 |
| DECISIONS.md | 10+ 份 |
| RUNBOOK.md | 4 份 |
| reports/ 目录 | 8 个, 含 30+ 份报告 |
| orchestration/ 目录 | 4 个 |
| 敏感文件发现 | 30+ 路径 (.env, auth.json, token, *.db, backups) |
| 生产数据库 | 4 个 (aoxue_edu_production.db × 2, product.db, hermes *.db) |

关键资产:

- sub2api-maijian 主工程 + 8 个 worktree, 是平台化核心
- biaoge-web 前端 + 2 个 worktree + 1 个非 git 副本
- DreamSoul 适配器、BFF、控制中心
- 全套 Agent 协作文件 (AGENTS.md / CLAUDE.md / CHATGPT_START_HERE.md / DECISIONS.md / RUNBOOK.md)
- 两份 DreamSoul 审计报告 (HOME 级别)

### 3.3 共同敏感资产

两个 WSL 环境均存在:

- `.env` 文件 (Hermes 主环境 20K、sub2api 运行时、biaoge-web 等)
- `auth.json` 认证凭据 + 备份
- 运行态数据库 (state.db, memory_store.db, SQLite 等)
- 生产数据库及备份 (aoxue_edu_production.db, product.db)
- 备份目录 (SillyTavern backups, biaoge-web backups, hermes profile backups)
- 传输压缩包 (dream-soul-email-routing-transfer.tar.gz, ST-release.tar.gz)
- 浏览器 profile 数据库 (camofox cookies/places/cert)

**以上全部仅登记路径, 未输出内容, 不应入仓。**

---

## 4. 仓库分流原则

### ai-collaboration-playbook

| 应入仓内容 | 说明 |
|------------|------|
| 通用 AI 协作协议 | AGENTS.md / CLAUDE.md 模板、协作规范 |
| 任务包模板 | 标准 task package 结构 |
| 验收标准 | Definition of Done 模板 |
| 审计总账 | 本汇总 + 各子审计 |
| 脱敏后的通用 standards / skills | Hermes 17 份 standards 中可公开部分 |
| Claude / Codex / Hermes 协作方法论 | 上下文注入、多 Agent 编排、Agent 交接 |

### sub2api-maijian

| 应入仓内容 | 说明 |
|------------|------|
| sub2api 主工程 | 已在此仓库 |
| DreamSoul 平台化资产 | dream-soul-adapter, dream-soul-bff, dream-soul-control |
| Character Studio / 形象馆 | Character Studio Hermes、Worker、Worker Env |
| wsl-server 守护文档 | 边界说明、健康检查、部署配置 |
| reports / orchestration / AGENTS / CLAUDE / CHATGPT_START_HERE | 已在此仓库 |

### maijian-wechat-content-lab

| 应入仓内容 | 说明 |
|------------|------|
| 公众号文章 | maijian-wechat 仓库中的文章 |
| 写作流程 | article-writing-workflow, article-lifecycle-sop |
| OpenWrite / WeChat / Draco 发布链路 | 发布 SOP |
| 封面 prompt | 封面生成提示词 |
| 内容实验 | 内容生产实验文档 |
| 发布 preflight | 发布前检查清单 |

### shanxi-edu-hot / aoxue-edu

| 应入仓内容 | 说明 |
|------------|------|
| 山西教育情报系统 | shanxi-edu-hot 相关资产 |
| 奥学教育老板自用后台 | aoxue-edu 项目 |
| 教培业务资料 | 教育业务文档 |
| 教育项目 runbook | 教育项目运维手册 |
| 学校数据相关资料 | 学校数据审计等 |

### 仅本地保留, 不入仓

| 内容 | 原因 |
|------|------|
| Hermes 运行态 `.hermes/` | 运行中系统, 含密钥和状态 |
| state.db / memory_store.db | 运行态数据库 |
| sessions / pastes / logs | 会话历史, 无复用价值 |
| SillyTavern 实验副本 | 第三方源码 + 本地 patch |
| Docker 数据目录 | postgres_data / redis_data |
| 浏览器 profile | camofox profile |
| `.bad-*` 副本 | 废弃/失败的工作副本 |
| 时间戳清理快照 | sub2api-maijian-fact-source-clean-* |
| 传输压缩包 | *-transfer.tar.gz, *-release.tar.gz |
| 生产数据库和备份 | aoxue_edu_production.db, product.db 等 |

---

## 5. 总控纠偏

> **Character Studio / 形象馆属于 sub2api-maijian / DreamSoul 平台线, 不应归入 maijian-wechat-content-lab, 除非只是公众号文章素材。**

Character Studio (角色工作室) 是平台功能模块, 涉及:

- 角色生成流水线
- 角色包打包与分发
- 角色与 Chat Agent 的绑定
- Character Studio Worker (Hermes 守护进程)

这些都是 sub2api-maijian 的平台功能, 与公众号内容生产 (maijian-wechat-content-lab) 是不同业务线, 不应混淆。

仅当内容是"介绍 Character Studio 的公众号文章"时, 才可归入 maijian-wechat-content-lab。

---

## 6. 下一阶段建议

### P0 — 立刻执行

1. **合并审计报告分支, 形成统一资产总账** ← 本分支即为此目标
2. **复核各仓库 `.gitignore`** 是否覆盖以下模式:
   - `.env`, `.env.*`, `*.env`
   - `*.db`, `*.sqlite`, `*.sqlite3`
   - `auth.json`, `auth.json.bak*`
   - `*token*`, `*key*`, `*secret*`, `*cred*` (非代码文件)
   - `logs/`, `backups/`, `node_modules/`
   - `*.tar.gz`, `*.zip`

### P1 — 近期执行

3. **maijian-wechat 250 个未提交文件单独审计** — 这是最大的未提交堆积, 需确认是新增内容、实验文件、还是应清理的临时文件
4. **sub2api / biaoge-web worktree 清理前审计** — 8 + 2 个 worktree 中部分可能已过期 (qwen-fix, qwen-thinking), 需确认后再 prune
5. **aoxue 生产数据库和备份保留策略** — `aoxue_edu_production.db` 存在于两个目录, 需决定归档或删除

### P2 — 中长期规划

6. **Hermes skills / standards 脱敏提炼进入 playbook** — 86 skills + 17 standards 中高价值部分, 脱敏后入 ai-collaboration-playbook
7. **DreamSoul / biaoge / Character Studio 资产归入 sub2api-maijian** — 平台化资产统一归口
8. **教培相关资产归入 shanxi-edu-hot / aoxue-edu** — 教育业务资产独立仓库管理

---

## 附录: 审计报告索引

| 文件 | 来源 WSL | 大小 | 说明 |
|------|----------|------|------|
| [wsl-hermes-audit.md](./wsl-hermes-audit.md) | wsl-hermes | ~23KB | Hermes 环境完整审计 |
| [wsl-codex-audit.md](./wsl-codex-audit.md) | wsl-codex | ~24KB | Codex 环境完整审计 |
| [wsl-server-readonly-boundary.md](./wsl-server-readonly-boundary.md) | — | ~1KB | wsl-server 只读边界说明 |
| [summary.md](./summary.md) | 汇总 | — | 本文件 |
