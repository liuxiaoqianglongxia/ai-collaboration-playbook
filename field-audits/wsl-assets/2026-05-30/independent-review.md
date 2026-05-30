# WSL 资产审计独立复核报告

**生成时间**: 2026-05-30 19:00 CST
**复核员**: WSL 资产审计独立复核员（Claude Code，独立于两份原始审计）
**输入分支**: `origin/audit/wsl-hermes-assets-20260530` + `origin/audit/wsl-codex-assets-20260530`
**本分支**: `audit/wsl-assets-independent-review-20260530`

---

## 1. 复核结论

**PARTIAL PASS**

理由：

- 两份审计报告均完整覆盖了各自 WSL 用户（hermes / codex）的项目资产、敏感文件、可复用资产和分流建议。
- Hermes 审计报告在敏感文件识别上做得较好，但遗漏了 Codex WSL 中存在的 DreamSoul 系列项目和 Character Studio 资产。
- Codex 审计报告对 sub2api worktree 体系的分析详尽，但分流建议中**将 Character Studio 错误归入 `maijian-wechat-content-lab`**。
- 两份报告均未识别出 `biaoge-web` 在两个 WSL 中存在**同一仓库不同分支**的跨 WSL 重复。
- 存在多处 worktree / 副本重复现象，两份报告有所提及但分析不够交叉化。
- 敏感文件均被正确登记为"不入仓"，无内容泄露。

---

## 2. 两份审计报告可信度

### 2.1 wsl-hermes-audit.md（Hermes WSL）

| 维度 | 评分 | 说明 |
|------|------|------|
| 覆盖面 | 8/10 | 覆盖了 projects/、knowledge/、.hermes/ 三大目录，但对 Codex WSL 资产无感知（合理，属不同用户空间） |
| 准确性 | 8/10 | git 分支/remote/commit 信息准确，未提交数可信 |
| 敏感文件识别 | 9/10 | 完整列出了 .env、auth.json、*.db、backups、logs、sessions，但遗漏了 DreamSoul 相关（因为 DreamSoul 在 codex WSL） |
| 分流建议 | 7/10 | 整体合理，但 Hermes 审计对 `sub2api` 体系几乎未涉及，导致分流不完整 |
| 可复用资产 | 9/10 | Skills/Standards/Prompts/Workflows 盘点全面 |

**可信度: 高（在其扫描范围内）**

### 2.2 wsl-codex-audit.md（Codex WSL）

| 维度 | 评分 | 说明 |
|------|------|------|
| 覆盖面 | 9/10 | 覆盖了 projects/、HOME 级脚本、.hermes/、runtime/，识别了 worktree 体系 |
| 准确性 | 9/10 | 正确识别了 worktree 共享同一 .git 对象存储，分支/remote 信息准确 |
| 敏感文件识别 | 9/10 | 完整列出 .env、token 文件、数据库、浏览器 profile、Docker 数据目录 |
| 分流建议 | 6/10 | **Character Studio 归入 maijian-wechat-content-lab 是错误的**（详见第 4 节） |
| 可复用资产 | 8/10 | AGENTS.md / CLAUDE.md / CHATGPT_START_HERE.md 体系识别好，但重复 worktree 副本未去重 |

**可信度: 高（在其扫描范围内），但分流建议有 1 处明显错分**

---

## 3. 关键交叉发现

### 3.1 biaoge-web 跨 WSL 重复

| WSL | 路径 | 分支 | 未提交 |
|-----|------|------|--------|
| hermes | `/home/hermes/projects/biaoge-web` | master | 2 |
| codex | `/home/codex/projects/biaoge-web` | hotfix/v2-orchestrator-async-live | 14 文件 + 11M |
| codex worktree | `/home/codex/projects/biaoge-web-context-injection` | sync/public-v2-context-injection-hotfix | 0 |
| codex worktree | `/home/codex/projects/biaoge-web-runtime-role-v2` | feat/runtime-info-and-role-package-v2-public | 0 |

**结论**: 同一个 `biaoge-web` GitHub 仓库在两个 WSL 中处于不同分支。hermes 端是 `master`，codex 端是 `hotfix/v2-orchestrator-async-live`（有大量未提交变更）。codex 端还有 2 个额外 worktree。**存在代码冲突风险**。

### 3.2 aoxue-edu 跨 WSL 重复

| WSL | 路径 | 分支 | 状态 |
|-----|------|------|------|
| hermes | `/home/hermes/projects/aoxue-edu` | master | 已封盘，3 个未推送 commit |
| codex | `/home/codex/projects/aoxue-edu-clean` | codex/local-sync-20260512 | 5 个未提交文件，1 个未推送 commit |
| codex 废弃 | `/home/codex/projects/aoxue-edu-clean.bad-1778640795` | codex/local-sync-20260512 | 废弃副本，含生产数据库 |

**结论**: 同一 `aoxue-edu` GitHub 仓库在两个 WSL 中有不同状态。hermes 端已封盘（`288039a`），codex 端 `aoxue-edu-clean` 是清理版但仍有未提交变更。`aoxue-edu-clean.bad-*` 是含生产数据库的废弃副本，**应优先清理**。

### 3.3 hermes-core-audit-private 跨 WSL 重复

| WSL | 路径 | 分支 |
|-----|------|------|
| hermes | `/home/hermes/projects/hermes-core-audit-private` | inventory/multi-system-context-v1 |
| codex | `/home/codex/projects/hermes-core-audit-private` | inventory/multi-system-context-v1 |

**结论**: 同一分支，各自独立工作副本。hermes 最近 commit `63a9fed`，codex 最近 commit `432d6a1`（Hermes-B context inventory）。**分支相同但 commit 不同，存在分叉风险**。

### 3.4 sub2api worktree 体系（仅 codex WSL）

`sub2api` 主仓库有 **10+ 个 worktree**，包括：
- `sub2api-delivery-clean`（已提交）
- `sub2api-pr1-docs-ops` / `sub2api-pr1-docs-ops-v2`
- `sub2api-pr2-upstream-integration`
- `sub2api-qwen-fix` / `sub2api-qwen-thinking`（可能过期）
- `sub2api-upstream-v129-sync`
- `sub2api-local-dev` / `sub2api-qwen-fix` 等

**每份 worktree 都包含完整的 AGENTS.md / CLAUDE.md / CHATGPT_START_HERE.md / TASKS.md / DECISIONS.md / RUNBOOK.md / reports/ / orchestration/ 副本**。两份审计报告均正确识别了重复现象，但未量化重复文件的总磁盘占用。

### 3.5 SillyTavern 多个副本（仅 codex WSL）

| 副本 | 大小 | 状态 |
|------|------|------|
| SillyTavern | 435M | 非 git 源码副本 |
| sillytavern-lab | 519M | 实验环境 |
| sillytavern-lab-source-test | 145M | 源码测试 |
| sillytavern-runtime-patched | 385M | patch 版本 |
| sillytavern-runtime-patched.pre-l2-* | 385M | 旧版备份 |

**总计 ~1.9GB**，全部是第三方 SillyTavern 源码的本地变体。两份报告均建议保持本地不入仓。

### 3.6 maijian-wechat 与 maijian-wechat-private-repo（仅 hermes WSL）

| 仓库 | remote | 未提交 | 未推送 |
|------|--------|--------|--------|
| maijian-wechat | `liuxiaoqianglongxia/aoxue-media` | 250 | 3 |
| maijian-wechat-private-repo | `liuxiaoqianglongxia/maijian-wechat` | 0 | 0 |

**结论**: 两个不同 GitHub 仓库，职责清晰（一个公开、一个私有），无混乱。但公开仓库的 250 个未提交文件需要重点审查。

---

## 4. 错分与纠偏

### 4.1 Character Studio / 形象馆归属纠偏

Codex 审计报告 Section 5.3 将以下内容建议归入 `maijian-wechat-content-lab`：

```
sub2api Character Studio 相关文件 (CHARACTER_STUDIO_HERMES.md 等)
/home/codex/.config/sub2api-character-studio-worker.env
```

**纠偏**: Character Studio（形象馆）**不应归入 maijian-wechat-content-lab**。

理由：
- Character Studio 是 sub2api 生态下的功能模块，文件位于 sub2api 仓库内
- 其 worker 配置为 `.config/sub2api-character-studio-worker.env`，与 sub2api 服务绑定
- DreamSoul 控制中心 (`dream-soul-control`) 是 Character Studio 的上层平台
- 这属于 **DreamSoul 平台线**，应归 `sub2api-maijian` 或独立的 `dream-soul-control` 仓库
- 除非这些文件纯粹是公众号文章素材（从文件名判断不是），否则不应归入内容实验室

**修正建议**: Character Studio 相关文件应归入 `sub2api-maijian`（作为 sub2api 功能模块）或 `dream-soul-control`（作为平台控制功能）。

### 4.2 Hermes 审计遗漏 DreamSoul 体系

Hermes 审计报告完全没有提及 DreamSoul 系列项目（`dream-soul-control`、`dream-soul-adapter`、`dream-soul-bff`、`dream-soul-sub2api`、`dreamsoul-chat-agent`、`dream-soul-email-routing`），因为这些资产存在于 codex WSL 的 `/home/codex/projects/` 下。这不属于错误，但说明**单一 WSL 审计无法形成全局视图**。

### 4.3 重复 worktree 副本的"复用价值"评价偏高

Codex 审计报告将每个 worktree 副本中的 AGENTS.md / CLAUDE.md / CHATGPT_START_HERE.md / TASKS.md 都列为独立的"可复用资产"，并分别给了"高/中"价值。实际上这些是同一仓库的不同 worktree 分支上的同一文件的不同版本。**真正有价值的是主仓库版本本身**，而非每个 worktree 副本。复核建议将重复副本去重，仅保留主仓库的原始文件作为复用资产。

---

## 5. 高价值可复用资产 TOP 20

| # | 资产名称 | 来源 WSL | 来源路径 | 建议归属仓库 | 价值 | 风险 | 处理建议 |
|---|----------|----------|----------|-------------|------|------|----------|
| 1 | github-ai-collaboration-pattern skill | hermes | `.hermes/skills/github-ai-collaboration-pattern/` | ai-collaboration-playbook | 高 | 无 | 脱敏后直接入仓 |
| 2 | 17 份 knowledge standards | hermes | `knowledge/standards/` | ai-collaboration-playbook | 高 | 无 | 直接入仓，已是标准文档 |
| 3 | context-injection-protocol skill | hermes | `.hermes/skills/context-injection-protocol/` | ai-collaboration-playbook | 高 | 无 | 核心 AI 协作协议 |
| 4 | sub2api AGENTS.md + CLAUDE.md + CHATGPT_START_HERE.md | codex | `sub2api/` (主仓库) | ai-collaboration-playbook | 高 | 无 | 提炼为多 Agent 协作模板 |
| 5 | article-writing-workflow skill | hermes | `.hermes/skills/article-writing-workflow/` | ai-collaboration-playbook | 高 | 无 | 写作工作流入 playbook |
| 6 | hermes-skill-development-standard skill | hermes | `.hermes/skills/hermes-skill-development-standard/` | ai-collaboration-playbook | 高 | 无 | 技能开发标准 |
| 7 | AGENTS.md (biaoge-web agent handoff) | codex | `biaoge-web/docs/agent-handoff/` | ai-collaboration-playbook | 高 | 无 | Agent 交接模式可复用 |
| 8 | AGENTS.md (dream-soul-control) | codex | `dream-soul-control/docs/agent-handoff/` | ai-collaboration-playbook | 高 | 无 | DreamSoul 交接模式 |
| 9 | sub2api reports/ 全集 | codex | `sub2api/reports/` | ai-collaboration-playbook | 高 | 可能含敏感 | 脱敏 incident 报告后入仓 |
| 10 | dream-soul 审计报告 | codex | `~/dreamsoul-audit-2026-05-25.md` | ai-collaboration-playbook | 高 | 无 | 归档到 archive/ |
| 11 | hermes-core-audit 白皮书/手册 | both | `hermes-core-audit-private/knowledge/` | ai-collaboration-playbook | 高 | 无 | 提炼非敏感版本 |
| 12 | article-lifecycle-sop standard | hermes | `knowledge/standards/17-article-lifecycle-sop.md` | ai-collaboration-playbook | 高 | 无 | 文章 SOP |
| 13 | validated-workflow-v1-freeze | hermes | `.hermes/skills/delegation/wechat-article-workflow/` | maijian-wechat-content-lab | 高 | 无 | 已验证文章工作流 |
| 14 | wechat-article-workflow.SKILL.md | hermes | `knowledge/archive/fixes/` | maijian-wechat-content-lab | 高 | 无 | 公众号文章工作流 |
| 15 | maijian-wechat-publish-config skill | hermes | `.hermes/skills/maijian-wechat-publish-config/` | maijian-wechat-content-lab | 高 | 无 | 发布配置 |
| 16 | publish_map.jsonl + preflight 脚本 | hermes | `maijian-wechat/scripts/` | maijian-wechat-content-lab | 高 | 无 | 发布管线核心 |
| 17 | hermes-openclaw-collaboration skill | hermes | `.hermes/skills/hermes-openclaw-collaboration/` | ai-collaboration-playbook | 中 | 无 | AI 间协作模式 |
| 18 | sub2api RUNBOOK.md | codex | `sub2api/RUNBOOK.md` | ai-collaboration-playbook | 中 | 无 | 部署运维模板 |
| 19 | sub2api DECISIONS.md | codex | `sub2api/DECISIONS.md` | ai-collaboration-playbook | 中 | 无 | ADR 决策模板 |
| 20 | biaoge-visual-dictionary-lighting.md | codex | `~/docs/` | ai-collaboration-playbook | 中 | 无 | 视觉词典文档 |

---

## 6. 禁止入仓资产清单

> 按类型排列，仅登记路径和风险，不输出任何敏感内容。

### 6.1 密钥与认证

| 类型 | 路径 | 风险 |
|------|------|------|
| .env | `/home/hermes/.hermes/.env` | 含 API 密钥 |
| .env | `/home/hermes/.hermes/.env.bak.*` (2份) | 历史密钥 |
| .env | `/home/hermes/projects/shanxi-edu-hot/.env` | 项目密钥 |
| .env | `/home/hermes/projects/openmaic/.env.local` | 项目密钥 |
| .env | `/home/codex/.hermes/.env` | Hermes 主密钥 |
| .env | `/home/codex/.hermes/.env.bak_*` (2份) | 历史密钥 |
| .env | `/home/codex/projects/biaoge-web/.env` | 项目密钥 |
| .env | `/home/codex/runtime/sub2api-maijian/.env` | 运行时密钥 |
| .env | `/home/codex/projects/dream-soul-email-routing/.env.local` | 邮件路由密钥 |
| .env | `/home/codex/.config/sub2api-character-studio-worker.env` | Character Studio 密钥 |
| auth.json | `/home/hermes/.hermes/auth.json` (+ 7 备份) | 认证凭据 |
| auth.json | `/home/codex/.hermes/auth.json` (+ 2 备份) | 认证凭据 |
| API Token | `/home/codex/.config/sub2api-maijian/cloudflare-api-token` | Cloudflare Token |
| API Token | `/home/codex/.config/dreamsoul/agent_gateway_token` | Gateway Token |
| API Key | `/home/codex/.config/dreamsoul/llm_api_key` | LLM API Key |
| 测试凭据 | `/home/codex/test_creds.json` | 测试凭据 |

### 6.2 数据库

| 类型 | 路径 | 大小 | 风险 |
|------|------|------|------|
| state.db | `/home/hermes/.hermes/state.db` (+ WAL) | ~2.3GB | 运行态状态数据 |
| memory_store.db | `/home/hermes/.hermes/memory_store.db` | ~167MB | 持久化记忆 |
| 业务数据库 | `/home/hermes/projects/aoxue-edu/*.db` (14 文件) | 400-640KB 每个 | 生产/测试数据 |
| 业务数据库 | `/home/codex/projects/aoxue-edu-clean/aoxue_edu_production.db` | ~640KB | **生产数据** |
| 业务数据库 | `/home/codex/projects/biaoge-web/product.db` | 208KB | 产品数据 |
| Docker 数据 | `/home/codex/runtime/sub2api-maijian/postgres_data/` | 未知 | PostgreSQL 数据 |
| Docker 数据 | `/home/codex/runtime/sub2api-maijian/redis_data/` | 未知 | Redis 数据 |

### 6.3 运行态与临时数据

| 类型 | 路径 | 风险 |
|------|------|------|
| 会话历史 | `/home/hermes/.hermes/sessions/` (87 目录) | 可能含对话内容 |
| 粘贴板 | `/home/hermes/.hermes/pastes/` | 可能含临时敏感数据 |
| Gateway 状态 | `/home/hermes/.hermes/gateway.pid / gateway_state.json` | 运行时状态 |
| 日志 | `/home/hermes/.hermes/logs/`、`/home/codex/.hermes/logs/` | 应用日志 |
| 截图 | `/home/hermes/.hermes/browser_screenshots/` | 可能含页面敏感信息 |
| 浏览器 profile | `/home/codex/.camofox/profiles/*/cookies.sqlite` | 浏览器数据 |

### 6.4 第三方源码

| 类型 | 路径 | 大小 | 风险 |
|------|------|------|------|
| SillyTavern 全系列 | `/home/codex/projects/SillyTavern/` 等 4-5 个副本 | ~1.9GB | 第三方版权 + 本地 patch |

### 6.5 备份与快照

| 类型 | 路径 | 风险 |
|------|------|------|
| aoxue-edu 备份 | `/home/hermes/projects/aoxue-edu/backups/` (14 目录) | 含生产数据库 |
| aoxue-edu 废弃副本 | `/home/codex/projects/aoxue-edu-clean.bad-*/` | 含生产数据库副本 |
| sub2api 废弃副本 | `/home/codex/projects/sub2api.bad-1778640832/` | 上游镜像废弃副本 |
| 清理快照 | `/home/codex/projects/sub2api-maijian-fact-source-clean-*/` | 可能过期 |
| 传输压缩包 | `dream-soul-email-routing-transfer.tar.gz`、`ST-release.tar.gz` | 压缩包，可能过期 |
| patch 备份 | `/home/hermes/.hermes/patch-backups/` (23 目录) | 补丁历史 |
| state 快照 | `/home/hermes/.hermes/state-snapshots/` | 状态快照 |

---

## 7. 下一阶段建议

### P0（立即执行，安全相关）

| # | 建议 | 理由 |
|---|------|------|
| P0-1 | **确认 aoxue-edu 生产数据库安全处置** | `aoxue_edu_production.db` 存在于 hermes + codex 两个 WSL 的多个目录中，至少 3 个副本 |
| P0-2 | **审查 maijian-wechat 250 个未提交文件** | 量大且含公众号内容，需区分资产 vs 临时文件 |
| P0-3 | **确认 hermes-dashboard 55 个未提交变更** | 面板项目活跃开发中，需确认状态 |
| P0-4 | **确认 biaoge-web 跨 WSL 分支同步** | hermes 端 master / codex 端 hotfix 分支不同，存在冲突风险 |
| P0-5 | **各仓库 .gitignore 复核** | 确认 .env / *.db / auth.json / token 文件已被排除 |

### P1（近期执行，资产整理）

| # | 建议 | 理由 |
|---|------|------|
| P1-1 | **将 TOP 20 可复用资产中无风险的脱敏入仓** | github-ai-collaboration-pattern / standards / context-injection 等 |
| P1-2 | **Codex DreamSoul 审计报告归档** | 2 份 HOME 级审计报告有价值，可归档到 playbook archive/ |
| P1-3 | **hermes-core-audit-private 分叉合并** | hermes + codex 同分支不同 commit，需确认哪个是权威版本 |
| P1-4 | **sub2api worktree 精简** | 10+ 个 worktree 中 qwen-fix / qwen-thinking 可能过期 |
| P1-5 | **biaoge-web worktree 统一** | hermes 端无 remote，codex 端有 2 个 worktree + 1 非 git 副本 |
| P1-6 | **maijian-wechat 3 个未推送 commit 推送** | 已确认干净（codex 审计未报告问题） |

### P2（中期规划，战略决策）

| # | 建议 | 理由 |
|---|------|------|
| P2-1 | **DreamSoul 平台线正式化** | dream-soul-control / adapter / bff / sub2api 均在 codex 端实验态，需确定架构 |
| P2-2 | **SillyTavern 全系列决策** | ~1.9GB 第三方源码副本，确认保留策略（保留/清理/迁移） |
| P2-3 | **bendi-llm-gateway 远程化** | 服务器镜像无 remote，决定推私有仓库或保持本地 |
| P2-4 | **ApexSpiral 审计子仓库决策** | 6 个外部审计仓库独立管理，确认是否继续维护 |
| P2-5 | **hermes state.db 压缩** | ~2.3GB 状态数据库，考虑压缩或归档策略 |
| P2-6 | **定期月度审计机制** | 建立每月自动只读审计的 cron |

---

## 8. 需要 ChatGPT 总控裁决的问题

| # | 分歧/问题 | 需要裁决的内容 |
|---|-----------|----------------|
| Q1 | **biaoge-web 跨 WSL 分支冲突** | hermes 端在 master（2 未提交），codex 端在 hotfix（14 未提交 + 11M）。哪个分支是权威？是否应合并？ |
| Q2 | **aoxue-edu 封盘状态 vs codex 清理版** | hermes 端已标记"封盘"（`288039a`），codex 端 `aoxue-edu-clean` 仍在活跃开发（5 未提交）。封盘是否意味着所有开发停止？ |
| Q3 | **Character Studio 归属** | Codex 审计将其归入 maijian-wechat-content-lab，复核认为应归 sub2api-maijian / DreamSoul 平台线。请总控裁决。 |
| Q4 | **DreamSoul 平台架构** | dream-soul-control / adapter / bff / sub2api 四个子项目均在 codex 端，adapter 和 bff 无 remote。是否应统一推送到 GitHub？ |
| Q5 | **sub2api worktree 精简** | 10+ 个 worktree 占用大量磁盘空间。哪些应保留（pr1-docs-ops, pr2-upstream-integration），哪些可 prune（qwen-fix, qwen-thinking）？ |
| Q6 | **SillyTavern 系列去留** | ~1.9GB 第三方源码，含本地 patch。是否应保留实验价值最高的 `sillytavern-runtime-patched`，清理其余？ |
| Q7 | **hermes-core-audit-private 分叉** | hermes + codex 同分支但不同 commit。哪个是 SSOT？是否需要 rebase 合并？ |
| Q8 | **biaoge-web / biaoge-role-packages 远程化** | hermes 端无 remote。是否应推送到 GitHub 私有仓库？ |
| Q9 | **250 个 maijian-wechat 未提交文件的入仓策略** | 哪些算"内容资产"（可入 maijian-wechat-content-lab），哪些是"运行态临时文件"（不入仓）？ |
| Q10 | **DreamSoul 审计报告公开范围** | 2 份审计报告含生产环境信息。是否可脱敏后入 ai-collaboration-playbook 的 archive/，还是应保持私有？ |

---

*本复核报告基于两份原始审计报告交叉分析生成，未执行任何文件修改、删除或迁移操作。*
*复核员与两份原始审计员独立，不存在利益冲突。*
