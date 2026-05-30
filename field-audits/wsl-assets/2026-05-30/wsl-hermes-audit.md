# WSL Hermes 资产审计报告

**生成时间**: 2026-05-30 18:47 CST
**审计范围**: 只读盘点，未修改任何源码、配置或数据
**审计员**: wsl-hermes 本地资产审计员（Claude Code）

---

## 1. 环境摘要

| 字段 | 值 |
|------|------|
| WSL 主机名 | DESKTOP-RO91D2M |
| 内核 | Linux 6.6.87.2-microsoft-standard-WSL2 (x86_64) |
| 当前用户 | hermes |
| 当前时间 | 2026-05-30 18:47 CST |
| 主要项目根目录 | `/home/hermes/projects/` |
| Knowledge 根目录 | `/home/hermes/knowledge/` |
| Hermes 主目录 | `/home/hermes/.hermes/` |
| Claude Code 路径 | `/home/hermes/.local/bin/claude` |
| Codex 路径 | `/mnt/c/Users/liuxiaoqiang/AppData/Roaming/npm/codex` |
| Hermes 命令路径 | `/home/hermes/.local/bin/hermes` |
| Claude Code skills 数量 | 40+ (gstack 系列 + 通用) |
| Hermes skills 数量 | 86 |
| Hermes plugins 数量 | 20+ |
| Hermes roles 数量 | 8 |

---

## 2. Git 仓库清单

### 2.1 主项目仓库（/home/hermes/projects/）

| 项目名 | 当前分支 | Remote | 最近一次 commit | 未提交 | 未推送 | 分类 | 说明 |
|--------|----------|--------|-----------------|--------|--------|------|------|
| **aoxue-edu** | master | `liuxiaoqianglongxia/aoxue-edu` | `288039a` 项目封盘保存 - 2026-04-29 | 0 | 3 | 生产相关（已封盘） | 在线教育平台，有 3 个未推送 commit，已标记封盘 |
| **shanxi-edu-hot** | main | `liuxiaoqianglongxia/shanxi-edu-hot` | `7c94ac9` fix:bind-preflight-auth-key | 0 | 0 | 活跃/生产 | 山西教育热点项目 |
| **hermes-dashboard** | master | `liuxiaoqianglongxia/hermes-dashboard` | `5335255` chore: 移除 node_modules 追踪 | 55 | 0 | 活跃 | Hermes 监控面板，有大量未提交变更 |
| **hermes-core-audit-private** | inventory/multi-system-context-v1 | `liuxiaoqianglongxia/hermes-core-audit-private` | `63a9fed` docs: add Hermes-A context inventory | 0 | 0 | 活跃（私有审计） | 多系统上下文审计仓库 |
| **hermes-genesis-codebook** | main | `liuxiaoqianglongxia/hermes-genesis-codebook` | `fb26956` fix: 最终 Bundle 发布前整理 | 2 | 0 | 活跃 | Hermes 创世代码本 |
| **hermes-genesis-season1-pack** | main | `liuxiaoqianglongxia/hermes-genesis-season1-pack` | `224f0a6` fix: add console-v31.css | 1 | 0 | 活跃 | 第一季实践包，公开演示用 |
| **hermes-system-spec-public** | main | `liuxiaoqianglongxia/hermes-system-spec-public` (SSH) | `5343131` Add wechat article | 5 | 1 | 活跃/公开 | 系统规范文档，含公众号文章 |
| **maijian-wechat** | master | `liuxiaoqianglongxia/aoxue-media` | `f67f485` polish: refresh dashboard lite visuals | 250 | 3 | 活跃 | 迈减公众号内容仓库（250 个未提交文件！） |
| **maijian-wechat-private-repo** | main | `liuxiaoqianglongxia/maijian-wechat` | `7bef7c7` polish: remove reward-related wording | 0 | 0 | 活跃（私有） | 迈减公众号私有仓库 |
| **openmaic** | main | `THU-MAIC/OpenMAIC` | `a95aa87` support recent model providers (#481) | 15 | 0 | 活跃（上游贡献） | 清华 MAIC 开源项目，有 15 个未提交变更 |
| **biaoge-web** | master | (无 remote) | `3a85c33` feat: import simple v1 role packages | 2 | N/A | 实验/本地 | 表格 Web 项目，无 remote |
| **biaoge-role-packages** | master | (无 remote) | `1a7a763` docs: add public role runtime v1 | 7 | N/A | 实验/本地 | 角色包项目，无 remote |
| **taiyuan-schools-map** | master | `liuxiaoqianglongxia/taiyuan-schools-map` | `4f55537` Initial commit | 28 | 0 | 实验 | 太原学校地图，大量未提交变更 |
| **apexspiral-audit** | (DETACHED) | (无 remote) | (非 git 仓库) | 0 | N/A | 不确定 | 仅包含子目录仓库 |

### 2.2 ApexSpiral 审计子仓库（/home/hermes/projects/apexspiral-audit/）

| 项目名 | 当前分支 | Remote | 最近一次 commit | 未提交 | 分类 | 说明 |
|--------|----------|--------|-----------------|--------|------|------|
| apex-spiral-fork | main | `ApexSpiral/apex-spiral-fork` | `b0c0526` docs: update README | 2 | 实验 | APEX V10.3 公式分叉 |
| GeneNexus | main | `ApexSpiral/GeneNexus` | `7606c74` v1.1: 修复导入bug | 3 | 实验 | 基因系项目 |
| CodeGenesis | main | `ApexSpiral/CodeGenesis` | `e3d1577` feat: add APEX V10.3 | 0 | 实验 | 代码创世纪 |
| apex-spiral | main | `ApexSpiral/apex-spiral` | `715fb97` docs: add APEX V10.3 CHANGELOG | 2 | 实验 | APEX 主项目 |
| LLM-Pangu | main | `ApexSpiral/LLM-Pangu` | `899c5c3` feat: add APEX V10.3 | 3 | 实验 | LLM 盘古项目 |
| XuanjiQuant | main | `ApexSpiral/XuanjiQuant` | `4635e78` feat: add APEX V10.3 quant | 0 | 实验 | 玄机量化项目 |

### 2.3 无 Git 或空仓库目录

| 目录名 | 状态 | 分类 | 说明 |
|--------|------|------|------|
| hermes-genesis-season1-pack-export-dryrun | DETACHED, 无 commits | 废弃 | 导出试运行目录 |
| hermes-a-context-index-private | DETACHED, 无 commits | 不确定 | Hermes-A 上下文索引（私有） |
| browser-automation | DETACHED, 无 commits | 实验 | 浏览器自动化实验 |
| brain-graph | DETACHED, 无 commits | 实验 | 脑图/图谱实验 |
| market-insight | DETACHED, 无 commits | 废弃 | 市场洞察（有 report.md） |
| maijian-video | DETACHED, 无 commits | 实验 | 迈减视频项目 |
| maijian-wechat-previews | DETACHED, 无 commits | 实验 | 公众号预览 |
| backups/ | 目录 | 仅备份 | 通用备份目录 |

---

## 3. 可复用资产清单

### 3.1 Skills（/home/hermes/.hermes/skills/，86 个）

| 资产名称 | 类型 | 复用价值 | 风险 | 说明 |
|----------|------|----------|------|------|
| article-writing-workflow | SKILL | 高 | 无 | 文章写作工作流，可入 playbook |
| context-injection-protocol | SKILL | 高 | 无 | 上下文注入协议，AI 协作核心 |
| feishu-broadcast-standard | SKILL | 高 | 无 | 飞书广播标准 |
| hermes-feishu-streaming-card | SKILL | 高 | 无 | 飞书流式卡片技能 |
| hermes-weekly-audit | SKILL | 中 | 无 | 每周审计技能 |
| maijian-wechat-publish-config | SKILL | 高 | 无 | 公众号发布配置，含 workflow 引用 |
| openmaic-video-pipeline | SKILL | 中 | 无 | OpenMAIC 视频管线 |
| aoxue-edu-development | SKILL | 中 | 无 | 傲学开发技能 |
| aoxue-feishu-query | SKILL | 中 | 无 | 傲学飞书查询 |
| feishu-file-sender | SKILL | 中 | 无 | 飞书文件发送 |
| moss-tts-deployment | SKILL | 低 | 无 | Moss TTS 部署 |
| html-ppt-video-pipeline | SKILL | 中 | 无 | HTML/PPT/视频管线 |
| topic-mining-synthesis | SKILL | 中 | 无 | 主题挖掘综合 |
| standard-driven-team-upgrade | SKILL | 高 | 无 | 标准驱动团队升级 |
| cron-audit-after-standards | SKILL | 中 | 无 | Cron 审计 |
| github-ai-collaboration-pattern | SKILL | 高 | 无 | GitHub AI 协作模式，直接相关 |
| hermes-openclaw-collaboration | SKILL | 中 | 无 | Hermes-OpenClaw 协作 |
| wechat-article-camofox | SKILL | 中 | 无 | 公众号文章 CamoFox |
| sanitized-public-demo-creation | SKILL | 高 | 无 | 公开演示创建（脱敏） |
| role-memory-pipeline | SKILL | 中 | 无 | 角色记忆管线 |
| hermes-skill-development-standard | SKILL | 高 | 无 | 技能开发标准 |
| wsl-vhdx-compaction | SKILL | 低 | 无 | WSL VHDX 压缩 |
| hermes-skills-architecture-refactoring | SKILL | 中 | 无 | 技能架构重构 |
| project-fact-layer-audit | SKILL | 中 | 无 | 项目事实层审计 |
| autonomous-ai-agents | SKILL | 高 | 无 | 自主 AI Agent（optional） |
| 其余 60+ skills | SKILL | 中-低 | 需人工复核 | 涵盖 content/data/research/devops 等领域 |

### 3.2 Prompts

| 资产名称 | 路径 | 类型 | 复用价值 | 说明 |
|----------|------|------|----------|------|
| role_prompts.md | `.hermes/prompts/` | PROMPT | 高 | Hermes 角色提示汇总 |
| system_prompt.py | `.hermes/agent/` | PROMPT-CODE | 高 | 系统提示构建器 |
| claude-team-templates-prompt.md | `.hermes/tmp/` | PROMPT | 中 | Claude 团队模板提示词 |
| claude-aoxue-roadmap-prompt.md | `.hermes/tmp/` | PROMPT | 中 | 傲学路线规划提示词 |
| 2026-05-agent-series-prompts.md | `maijian-wechat/visuals/` | PROMPT | 中 | Agent 系列提示词 |
| season1-cover-prompts*.md | `maijian-wechat/` | PROMPT | 中 | 第一季封面提示词批次 |
| history-thickening-cron-prompts.md | `maijian-wechat/docs/` | PROMPT | 低 | 历史增强 Cron 提示 |
| claude-night-audit.prompt.txt | `shanxi-edu-hot/.codex-run/` | PROMPT | 低 | Codex 夜间审计提示 |

### 3.3 Agent 定义

| 资产名称 | 路径 | 类型 | 复用价值 | 说明 |
|----------|------|------|----------|------|
| hermes-agent/ | `.hermes/hermes-agent/` | AGENT | 高 | Hermes Agent 核心模块 |
| agent_init.py | `.hermes/agent/` | AGENT-CODE | 高 | Agent 初始化 |
| agent_runtime_helpers.py | `.hermes/agent/` | AGENT-CODE | 高 | Agent 运行时辅助 |
| codex_runtime.py | `.hermes/agent/` | AGENT-CODE | 高 | Codex 运行时适配器 |
| background_review.py | `.hermes/agent/` | AGENT-CODE | 中 | 后台审查 |
| acp_registry/agent.json | `.hermes/acp_registry/` | AGENT-CONFIG | 高 | Agent 配置注册 |

### 3.4 Workflows & Runbooks

| 资产名称 | 路径 | 类型 | 复用价值 | 说明 |
|----------|------|------|----------|------|
| automation-runbook.md | `shanxi-edu-hot/docs/` | RUNBOOK | 高 | 自动化运维手册 |
| maintenance-runbook.md | `shanxi-edu-hot/docs/` | RUNBOOK | 中 | 维护手册 |
| search-api-benchmark-runbook-v1.md | `shanxi-edu-hot/docs/` | RUNBOOK | 中 | 搜索 API 基准测试手册 |
| wechat-account-pool-runbook-v1.md | `shanxi-edu-hot/docs/` | RUNBOOK | 高 | 微信公众号账号池手册 |
| article-lifecycle-sop.md | `knowledge/standards/` | WORKFLOW | 高 | 文章生命周期 SOP |
| pm-first-workflow.md | `hermes-genesis-season1-pack/` | WORKFLOW | 中 | PM 首次工作流 |
| validated-workflow-v1-freeze.md | `.hermes/skills/delegation/` | WORKFLOW | 高 | 已验证文章工作流 V1 |
| new-media-workflow.SKILL.md | `knowledge/archive/fixes/` | WORKFLOW | 中 | 新媒体工作流 |
| wechat-article-workflow.SKILL.md | `knowledge/archive/fixes/` | WORKFLOW | 高 | 公众号文章工作流 |

### 3.5 知识库 Standards（/home/hermes/knowledge/standards/）

| 资产名称 | 类型 | 复用价值 | 说明 |
|----------|------|----------|------|
| 00-system-overview.md | STANDARD | 高 | 系统总览 |
| 01-terminology.md | STANDARD | 高 | 术语定义 |
| 02-structure.md | STANDARD | 高 | 目录结构规范 |
| 03-projects.md | STANDARD | 高 | 项目规范 |
| 04-ports.md | STANDARD | 中 | 端口规范 |
| 05-naming.md | STANDARD | 中 | 命名规范 |
| 06-state-md.md | STANDARD | 中 | 状态文件规范 |
| 07-project-backup.md | STANDARD | 中 | 项目备份规范 |
| 07-teams.md | STANDARD | 中 | 团队规范 |
| 08-file-cleanup.md | STANDARD | 中 | 文件清理规范 |
| 09-project-sync-skill.md | STANDARD | 中 | 项目同步技能 |
| 10-ssot-drift-gate.md | STANDARD | 高 | SSOT 漂移门禁 |
| 11-model-foundation.md | STANDARD | 中 | 模型基础规范 |
| 13-context-injection.md | STANDARD | 高 | 上下文注入规范 |
| 14-team-capability-framework.md | STANDARD | 高 | 团队能力框架 |
| 15-team-registry-and-boundaries.md | STANDARD | 高 | 团队注册与边界 |
| 16-memory-purity-and-boundary.md | STANDARD | 高 | 记忆纯度与边界 |
| 17-article-lifecycle-sop.md | STANDARD | 高 | 文章生命周期 SOP |

### 3.6 报告与审计文件

| 资产名称 | 路径 | 类型 | 复用价值 | 说明 |
|----------|------|------|----------|------|
| hermes-system-whitepaper-v8.md | `knowledge/archive/reports/` | REPORT | 高 | Hermes 系统白皮书 V8 |
| system-spec-audit-2026-04-14.md | `knowledge/archive/reports/` | REPORT | 中 | 系统规范审计报告 |
| single-instance-team-baseline.md | `knowledge/archive/reports/` | REPORT | 中 | 单实例团队基线 |
| EXPORT_MANIFEST.md | `hermes-core-audit-private/` | REPORT | 高 | 导出清单 |
| SECURITY_REDACTION_REPORT.md | `hermes-core-audit-private/` | REPORT | 高 | 安全脱敏报告 |
| HERMES_A_SKILLS_INVENTORY.md | `hermes-a-context-index-private/` | REPORT | 高 | Hermes-A 技能清单 |
| full audit reports (aoxue-edu) | `aoxue-edu/` | REPORT | 中 | 多个审计报告 |

### 3.7 发布与文章管线

| 资产名称 | 路径 | 类型 | 复用价值 | 说明 |
|----------|------|------|----------|------|
| publish_map.jsonl | `maijian-wechat/data/` | DATA | 高 | 发布映射数据 |
| preflight_article_publish.py | `maijian-wechat/scripts/` | SCRIPT | 高 | 发布前检查脚本 |
| preflight_publish_bundle.py | `maijian-wechat/scripts/` | SCRIPT | 高 | 发布包预检 |
| publish-results.json | `maijian-wechat/wechat-drafts/` | DATA | 中 | 发布结果记录 |
| feishu-broadcast-standard-article.md | `.hermes/` | ARTICLE | 中 | 飞书广播标准文章 |
| 20+ agent-truth 系列文章 | `maijian-wechat/articles/` | ARTICLE | 中 | Agent 真相系列 |

### 3.8 Claude/Codex/Hermes 协作经验

| 资产名称 | 路径 | 类型 | 复用价值 | 说明 |
|----------|------|------|----------|------|
| .hermes_history | `.hermes/` | HISTORY | 高 | 79KB 交互历史 |
| AGENTS.md | `.hermes/` | AGENT-DOC | 高 | 53KB Agent 定义文档 |
| CONTRIBUTING.md | `.hermes/` | DOC | 高 | 44KB 贡献指南 |
| hermes_overview_v{3-7}.md | `projects/` | DOC | 高 | 多版本系统概述文档 |
| .hermes_stable_release.json | `.hermes/` | CONFIG | 中 | 稳定发布版本标记 |
| registry.yaml | `projects/` | CONFIG | 高 | 项目注册表 |
| PORTS.md | `projects/` | DOC | 中 | 端口分配文档 |
| PORT_MIGRATION_PLAN.md | `projects/` | DOC | 中 | 端口迁移计划 |

---

## 4. 敏感风险清单

> 以下仅列路径和风险类型，不输出任何内容。

### 4.1 环境变量/密钥文件

| 路径 | 风险类型 | 说明 |
|------|----------|------|
| `/home/hermes/.hermes/.env` | 环境变量（含密钥） | 19KB，存在 API key/token 配置 |
| `/home/hermes/.hermes/.env.bak.codex-switch` | 环境变量备份 | 含历史密钥配置 |
| `/home/hermes/.hermes/.env.bak_20260515_134243` | 环境变量备份 | 含历史密钥配置 |
| `/home/hermes/.hermes/.env.example` | 环境变量示例 | 可能含密钥结构信息 |
| `/home/hermes/projects/shanxi-edu-hot/.env` | 环境变量 | 项目级密钥 |
| `/home/hermes/projects/shanxi-edu-hot/.env.example` | 环境变量示例 | 项目级密钥结构 |
| `/home/hermes/projects/openmaic/.env.local` | 环境变量 | OpenMAIC 本地密钥 |
| `/home/hermes/projects/openmaic/.env.example` | 环境变量示例 | OpenMAIC 密钥结构 |
| `/home/hermes/.hermes/auth.json` | 认证凭据 | 11KB，含 provider 认证信息 |
| `/home/hermes/.hermes/auth.json.bak.*` (7 个文件) | 认证凭据备份 | 历史认证信息 |

### 4.2 数据库文件

| 路径 | 大小 | 风险类型 | 说明 |
|------|------|----------|------|
| `/home/hermes/.hermes/state.db` | ~1.5GB | 状态数据库 | Hermes 核心状态 |
| `/home/hermes/.hermes/state.db-wal` | ~797MB | 状态数据库 WAL | 可能含未刷新敏感数据 |
| `/home/hermes/.hermes/memory_store.db` | ~167MB | 记忆数据库 | Hermes 持久化记忆 |
| `/home/hermes/.hermes/response_store.db` | 20KB | 响应存储 | 历史响应数据 |
| `/home/hermes/.hermes/trace.db` | ~15MB | 追踪数据库 | 调用追踪 |
| `/home/hermes/.hermes/kanban.db` | 104KB | 看板数据库 | 任务管理 |
| `/home/hermes/projects/aoxue-edu/*.db` (14 个文件) | 400-640KB 每个 | 业务数据库 | 傲学教育生产/测试数据 |
| `/home/hermes/projects/biaoge-web/data/*.db` | 20-208KB | 业务数据库 | 产品/联系人数据 |

### 4.3 备份与历史数据

| 路径 | 风险类型 | 说明 |
|------|----------|------|
| `/home/hermes/projects/backups/` | 备份目录 | 通用备份，内容未详查 |
| `/home/hermes/projects/aoxue-edu/backups/` (14 个备份子目录) | 数据库备份 | 含完整生产数据库副本 |
| `/home/hermes/projects/maijian-wechat/backups/` | 备份目录 | 公众号内容备份 |
| `/home/hermes/projects/hermes-dashboard/backups/` | 备份目录 | 面板备份 |
| `/home/hermes/projects/biaoge-web/backups/` | 备份目录 | 表格项目备份 |
| `/home/hermes/projects/shanxi-edu-hot/backups/` | 备份目录 | 教育项目备份 |
| `/home/hermes/.hermes/backups/` | 备份目录 | Hermes 系统备份 |
| `/home/hermes/.hermes/sessions/` (87 个子目录) | 会话历史 | 可能含对话敏感内容 |
| `/home/hermes/.hermes/pastes/` | 粘贴板 | 可能含临时敏感数据 |
| `/home/hermes/.hermes/patch-backups/` (23 个子目录) | 补丁备份 | 代码补丁历史 |
| `/home/hermes/.hermes/state-snapshots/` | 状态快照 | 系统状态快照 |

### 4.4 日志文件

| 路径 | 风险类型 | 说明 |
|------|----------|------|
| `/home/hermes/.hermes/logs/` | 系统日志 | 含 agent.log 等 |
| `/home/hermes/projects/aoxue-edu/logs/` | 应用日志 | 傲学日志 |
| `/home/hermes/projects/taiyuan-schools-map/logs/` | 应用日志 | 学校地图日志 |
| `/home/hermes/projects/hermes-dashboard/logs/` | 应用日志 | 面板日志 |
| `/home/hermes/.hermes/browser_screenshots/` | 截图 | 可能含页面敏感信息 |
| `/home/hermes/.hermes/interrupt_debug.log` | 调试日志 | 中断调试日志 |

### 4.5 其他

| 路径 | 风险类型 | 说明 |
|------|----------|------|
| `/home/hermes/.hermes/.models_dev_cache_fgh134y_.tmp` | 临时缓存 | 344KB，可能含模型缓存 |
| `/home/hermes/.hermes/image_cache/` | 图片缓存 | 可能含 API 密钥图片 |
| `/home/hermes/.hermes/cache/` | 缓存 | 模型/API 缓存 |
| `/home/hermes/.hermes/models_dev_cache.json` | 缓存 | 2MB 模型缓存 |

---

## 5. 建议分流

### 5.1 → ai-collaboration-playbook

以下资产建议归入 `ai-collaboration-playbook` 仓库：

| 资产 | 理由 |
|------|------|
| github-ai-collaboration-pattern skill | 核心 AI 协作模式 |
| context-injection-protocol skill + standard | AI 协作上下文协议 |
| article-writing-workflow skill | AI 写作工作流 |
| hermes-openclaw-collaboration skill | AI 间协作模式 |
| hermes-skill-development-standard skill | 技能开发标准 |
| 17 份 knowledge/standards/ 标准文档 | 系统级协作标准 |
| team capability/framework/registry standards | 团队协作框架 |
| article-lifecycle-sop standard | 文章生命周期 SOP |
| github-ai-collaboration-pattern SKILL.md | GitHub AI 协作最佳实践 |
| autonomous-ai-agents (optional skill) | 自主 AI Agent 模式 |
| hermes-weekly-audit skill | AI 协作审计流程 |

### 5.2 → maijian-wechat-content-lab

| 资产 | 理由 |
|------|------|
| maijian-wechat-publish-config skill | 公众号发布配置 |
| maijian-video-hyperframes-rendering skill | 视频超帧渲染 |
| wechat-article-camofox skill | 公众号 CamoFox 流程 |
| 公众号文章（maijian-wechat/articles/） | 公众号内容 |
| publish_map.jsonl + preflight 脚本 | 发布管线 |
| feishu-broadcast-standard skill + article | 飞书广播标准 |
| agent-truth 系列文章 | 公众号系列内容 |
| visuals/*.md (cover prompts) | 封面提示词资产 |

### 5.3 → shanxi-edu-hot / aoxue-edu

| 资产 | 理由 |
|------|------|
| aoxue-edu-development skill | 傲学开发技能 → aoxue-edu |
| aoxue-feishu-query skill | 傲学飞书查询 → aoxue-edu |
| aoxue-data-query skill | 傲学数据查询 → aoxue-edu |
| school-data-quality-fix skill | 学校数据修复 → shanxi-edu-hot |
| automation/maintenance/search runbooks | 运维手册 → shanxi-edu-hot |
| wechat-account-pool-runbook | 公众号池手册 → shanxi-edu-hot |
| 14 个 aoxue-edu 审计报告/数据库 | → aoxue-edu（需人工清理） |

### 5.4 → sub2api-maijian

| 资产 | 理由 |
|------|------|
| hermes-feishu-streaming-card skill | 飞书卡片 → sub2api |
| feishu-file-sender skill | 飞书发送 → sub2api |
| feishu-card-rendering-reality skill | 飞书渲染 → sub2api |
| feishu-streaming-card plugin | 飞书插件 → sub2api |

### 5.5 暂不入仓（仅本地保留）

| 资产 | 理由 |
|------|------|
| ApexSpiral 审计子仓库 (6 个) | 外部审计项目，独立管理 |
| ApexSpiral 相关 skills | 与 ApexSpiral 生态绑定 |
| browser-automation / brain-graph | 早期实验，未成型 |
| market-insight | 仅有 report.md，价值低 |
| hermes-genesis-season1-pack-export-dryrun | 试运行目录，可删除 |
| hermes-a-context-index-private | 私有索引，暂不入仓 |
| .hermes/sessions/ | 会话历史，含大量交互记录 |
| .hermes/pastes/ | 临时粘贴板 |
| .hermes/state-snapshots/ | 状态快照 |
| .hermes/patch-backups/ | 补丁备份 |
| .hermes/quarantine/ | 隔离区 |

### 5.6 应隔离/删除前需人工确认

| 资产 | 理由 |
|------|------|
| aoxue-edu/backups/ (14 个备份目录 + 数据库) | 含生产数据库，需确认保留策略 |
| .hermes/state.db (1.5GB + 797MB WAL) | 超大状态数据库，需确认是否压缩 |
| .hermes/memory_store.db (167MB) | 记忆数据库，需确认是否导出 |
| .hermes/.env + auth.json + 7 个备份 | 含 API 密钥，需人工审查后决定是否脱敏入仓 |
| maijian-wechat 的 250 个未提交文件 | 需确认哪些是新增文章/资产，哪些是临时文件 |
| hermes-dashboard 的 55 个未提交变更 | 需确认开发状态 |
| taiyuan-schools-map 的 28 个未提交变更 | 需确认项目状态 |
| biaoge-web / biaoge-role-packages（无 remote） | 需确认是否应推送到远程仓库 |
| openmaic 的 15 个未提交变更 | 上游贡献项目，需确认是否应提交 PR |

---

## 6. 下一步建议

> 以下仅为建议，不执行迁移操作。

### 6.1 高优先级

1. **maiJian-wechat 250 个未提交文件审查**: 区分新增文章资产、临时文件、缓存文件，然后提交
2. **.env / auth.json 安全审查**: 人工审查密钥文件，确认哪些可以脱敏入仓，哪些必须保持私有
3. **aoxue-edu 备份目录清理**: 14 个备份目录含完整数据库，建议保留最新 2 个，其余归档到安全存储
4. **hermes-dashboard 55 个未提交变更**: 确认开发状态，提交或回滚
5. **ai-collaboration-playbook 入仓**: 将 3.1 中建议分流的 skills/standards 整理并提交

### 6.2 中优先级

6. **hermes-system-spec-public 未推送 1 commit**: 推送到远程
7. **aoxue-edu 未推送 3 commits**: 确认是否应推送（已封盘状态）
8. **maijian-wechat 未推送 3 commits**: 推送到远程
9. **biaoge-web / biaoge-role-packages 添加 remote**: 确认是否应推送到 GitHub
10. **ApexSpiral 子仓库未提交变更**: 各仓库有 2-3 个未提交变更，需审查后提交

### 6.3 低优先级

11. **磁盘空间优化**: state.db + WAL 已达 2.3GB，考虑压缩/归档
12. **sessions 目录清理**: 87 个会话目录可能含过期交互，建议保留最近 N 天
13. **无 Git 目录处理**: 7 个 DETACHED/无 commits 目录，确认是否应初始化仓库或删除
14. **maijian-video 正式化**: 有 skill 和 team 定义但无 git 仓库，建议正式初始化
15. **knowledge/standards 入仓**: 17 份标准文档是高价值可复用资产，建议提交到 playbook

---

*本报告由 wsl-hermes 本地资产审计员于 2026-05-30 自动生成。审计过程未修改任何文件。*
