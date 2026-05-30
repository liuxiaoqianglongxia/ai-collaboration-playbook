# WSL Codex 资产审计报告

> 生成时间: 2026-05-30T10:48 UTC
> 审计员: wsl-codex (只读盘点, 未修改任何项目代码或配置)
> 审计范围: `/home/codex/projects`, `/home/codex`, `/home/codex/Documents`
> 排除: `/mnt/c`, `/mnt/d`, `/mnt/e` 未扫描(仅注明存在)

---

## 1. 环境摘要

| 字段 | 值 |
|------|------|
| 主机名 | DESKTOP-RO91D2M |
| WSL 内核 | Linux 6.6.87.2-microsoft-standard-WSL2 (WSL2) |
| 当前用户 | codex |
| HOME | /home/codex |
| 审计时间 | 2026-05-30 10:48 UTC |
| 主要项目根目录 | /home/codex/projects |
| Node | /usr/local/bin/node (v20.19.0) |
| Python | /usr/bin/python3 (3.12.3) |
| Go | 未安装 |
| npm | /usr/local/bin/npm (10.8.2) |
| Claude Code | /usr/local/bin/claude |
| Codex CLI | /usr/local/bin/codex |
| GitHub CLI | /usr/bin/gh (已认证: liuxiaoqianglongxia) |
| WSL 互通 | enabled (appendWindowsPath=false) |
| WSL 启动命令 | hermes-gateway-autostart-boot |

---

## 2. Git 仓库清单

> 注: 多个 `sub2api-*` 目录是 `sub2api` 主仓库的 **git worktree**, 共享同一 `.git` 对象存储, 各自位于不同分支。

| 项目名 | 本地路径 | 当前分支 | Remote URL | 最近一次 commit | 未提交 | 未推送 | 分类 | 说明 |
|--------|----------|----------|------------|-----------------|--------|--------|------|------|
| sub2api | /home/codex/projects/sub2api | feature/sub2api-maijian-mvp-v1-delivery-20260528-182302 | https://github.com/liuxiaoqianglongxia/sub2api-maijian.git (origin) + Wei-Shaw/sub2api.git (upstream) | 51b307e docs: consolidate single-repo authority | 2 文件 + 7 新增 | 有 | **生产相关** | 主仓库, 含多个 worktree |
| sub2api.bad-1778640832 | /home/codex/projects/sub2api.bad-1778640832 | main | https://github.com/Wei-Shaw/sub2api.git | 1879038 fix(deploy): 移除数据库与 Redis 宿主机端口映射 | 2 | 无 | 废弃 | 上游镜像, 疑似早期废弃分支 |
| aoxue-edu-clean | /home/codex/projects/aoxue-edu-clean | codex/local-sync-20260512 | https://github.com/liuxiaoqianglongxia/aoxue-edu.git | b64f3e0 fix: gate aoxue domains | 5 文件 | 有(1 commit) | **生产相关** | 学热项目清理版 |
| aoxue-edu-clean.bad-1778640795 | /home/codex/projects/aoxue-edu-clean.bad-1778640795 | codex/local-sync-20260512 | https://github.com/liuxiaoqianglongxia/aoxue-edu.git | ce3e76b docs: codify Windows handoff and product map | 1 | 无 | 废弃 | aoxue 早期副本 |
| biaoge-web | /home/codex/projects/biaoge-web | hotfix/v2-orchestrator-async-live | https://github.com/liuxiaoqianglongxia/biaoge-web.git | bb7680d fix: typing beat always LLM-generated | 11M + 14 新增 | 有(1 commit) | **生产相关** | 表格 Web 主仓库 |
| biaoge-web-context-injection | /home/codex/projects/biaoge-web-context-injection | sync/public-v2-context-injection-hotfix | git@github.com:liuxiaoqianglongxia/biaoge-web.git | 2d3e6b8 fix: inject public v2 context | 0 | 无 | 活跃 | biaoge-web worktree |
| biaoge-web-runtime-role-v2 | /home/codex/projects/biaoge-web-runtime-role-v2 | feat/runtime-info-and-role-package-v2-public | git@github.com:liuxiaoqianglongxia/biaoge-web.git | ca9c3af feat: import public role package v2 | 0 | 无 | 活跃 | biaoge-web worktree |
| biaoge-web-role-studio-pr | /home/codex/projects/biaoge-web-role-studio-pr | (N/A — 非 git repo) | 无 | N/A | 未知 | 未知 | 非 git 目录, 内容不明 |
| dream-soul-control | /home/codex/projects/dream-soul-control | main | https://github.com/liuxiaoqianglongxia/dream-soul-control.git | e4c8708 close out mac snapshot restore | 4 新增 | 有(1 commit) | 活跃 | DreamSoul 控制中心 |
| dream-soul-adapter | /home/codex/projects/dream-soul-adapter | main | 无 origin | 4ae841d align adapter dry-run outputs | 2 新增 | N/A | 实验 | 本地实验 |
| dream-soul-bff | /home/codex/projects/dream-soul-bff | main | 无 origin | ea1c4bc feat: expose Sub2API Lab mock contract | 0 | N/A | 实验 | 本地 BFF |
| dream-soul-sub2api | /home/codex/projects/dream-soul-sub2api | dream-soul/lab-base | /home/codex/projects/sub2api (本地路径) | efe2b82 chore: | 0 | N/A | 实验 | origin 指向本地 sub2api |
| hermes-core-audit-private | /home/codex/projects/hermes-core-audit-private | inventory/multi-system-context-v1 | https://github.com/liuxiaoqianglongxia/hermes-core-audit-private.git | 432d6a1 docs: add Hermes-B context inventory | 0 | 无 | **危险敏感** | Private repo, 含系统审计 |
| bendi-llm-gateway | /home/codex/projects/bendi-llm-gateway | main | 无 origin | 006665b init: mirror from server | 0 | N/A | **生产相关** | 服务器 /opt 镜像, 无远程 |
| sillytavern-runtime-patched | /home/codex/projects/sillytavern-runtime-patched | dream-soul/runtime-patched-local | /home/codex/projects/sillytavern-lab/SillyTavern (本地路径) | a580ffc Add basic auth max attempts config | 0 | N/A | 实验 | origin 指向本地 SillyTavern |
| codex-smoke-test | /home/codex/projects/codex-smoke-test | master | 无 origin | 无 commits | 0 | N/A | 实验 | 空仓库 |

### 非 Git 项目目录 (无 `.git`)

| 目录名 | 路径 | 体积 | 初步判断 |
|--------|------|------|----------|
| SillyTavern | /home/codex/projects/SillyTavern | 435M | SillyTavern 源码副本, 非 git |
| sillytavern-lab | /home/codex/projects/sillytavern-lab | 519M | SillyTavern 实验环境 |
| sillytavern-lab-source-test | /home/codex/projects/sillytavern-lab-source-test | 145M | SillyTavern 源码测试 |
| sillytavern-runtime-patched.pre-l2-20260517145531 | /home/codex/projects/sillytavern-runtime-patched.pre-l2-20260517145531 | 385M | 旧版本备份 (时间戳名) |
| dreamsoul-chat-agent | /home/codex/projects/dreamsoul-chat-agent | ~76K | 聊天代理项目, 含 SOUL.md/config.yaml.example |
| dream-soul-email-routing | /home/codex/projects/dream-soul-email-routing | ~60K | 邮件路由脚本, 含 .env.local |
| feishu_docs_tool | /home/codex/projects/feishu_docs_tool | ~24K | 飞书文档工具 (Python 单文件) |
| sub2api-delivery-clean | /home/codex/projects/sub2api-delivery-clean | 42M | sub2api worktree |
| sub2api-local-dev | /home/codex/projects/sub2api-local-dev | 无 | sub2api worktree |
| sub2api-qwen-fix | /home/codex/projects/sub2api-qwen-fix | ~196K | sub2api worktree |
| sub2api-qwen-thinking | /home/codex/projects/sub2api-qwen-thinking | ~196K | sub2api worktree |
| sub2api-upstream-v129-sync | /home/codex/projects/sub2api-upstream-v129-sync | 149M | sub2api worktree |
| sub2api-pr1-docs-ops | /home/codex/projects/sub2api-pr1-docs-ops | 34M | sub2api worktree |
| sub2api-pr1-docs-ops-v2 | /home/codex/projects/sub2api-pr1-docs-ops-v2 | 256K | sub2api worktree |
| sub2api-pr2-upstream-integration | /home/codex/projects/sub2api-pr2-upstream-integration | 151M | sub2api worktree |
| sub2api-maijian-fact-source-clean-20260521-173934 | /home/codex/projects/sub2api-maijian-fact-source-clean-20260521-173934 | 无 | 清理快照 (时间戳名) |
| sub2api-maijian-fact-source-clean-wsl-20260521-174744 | /home/codex/projects/sub2api-maijian-fact-source-clean-wsl-20260521-174744 | 无 | 清理快照 (时间戳名) |
| home | /home/codex/projects/home | 无 | 内容不明 |

---

## 3. 可复用资产清单

### 3.1 AI Agent 协作文件 (AGENTS.md / CLAUDE.md / etc.)

| 资产名称 | 路径 | 类型 | 可能归属仓库 | 复用价值 | 风险 | 说明 |
|----------|------|------|-------------|---------|------|------|
| AGENTS.md | /home/codex/projects/sub2api/AGENTS.md | Agent 指令 | sub2api-maijian | 高 | 无 | 主仓库 Agent 协作规范 |
| AGENTS.md | /home/codex/projects/sub2api-delivery-clean/AGENTS.md | Agent 指令 | sub2api-maijian | 中 | 无 | delivery worktree 副本 |
| AGENTS.md | /home/codex/projects/sub2api-pr1-docs-ops/AGENTS.md | Agent 指令 | sub2api-maijian | 中 | 无 | worktree 副本 |
| AGENTS.md | /home/codex/projects/sub2api-pr1-docs-ops-v2/AGENTS.md | Agent 指令 | sub2api-maijian | 中 | 无 | worktree 副本 |
| AGENTS.md | /home/codex/projects/aoxue-edu-clean/AGENTS.md | Agent 指令 | aoxue-edu | 高 | 无 | 学热项目 Agent 规范 |
| AGENTS.md | /home/codex/projects/sub2api.bad-1778640832/AGENTS.md | Agent 指令 | upstream/sub2api | 低 | 无 | 废弃副本 |
| AGENTS.md | /home/codex/.hermes/hermes-agent/AGENTS.md | Agent 指令 | hermes | 高 | 无 | Hermes agent 主规范 |
| AGENTS.md | /home/codex/projects/biaoge-web/docs/agent-handoff/AGENTS.md | Agent 指令 | biaoge-web | 高 | 无 | biaoge-web 交接规范 |
| AGENTS.md | /home/codex/projects/biaoge-web-context-injection/docs/agent-handoff/AGENTS.md | Agent 指令 | biaoge-web | 中 | 无 | worktree 副本 |
| AGENTS.md | /home/codex/projects/biaoge-web-runtime-role-v2/docs/agent-handoff/AGENTS.md | Agent 指令 | biaoge-web | 中 | 无 | worktree 副本 |
| AGENTS.md | /home/codex/projects/biaoge-web-role-studio-pr/docs/agent-handoff/AGENTS.md | Agent 指令 | biaoge-web | 中 | 无 | 非 git 副本 |
| AGENTS.md | /home/codex/projects/dream-soul-control/docs/agent-handoff/AGENTS.md | Agent 指令 | dream-soul-control | 高 | 无 | DreamSoul 交接规范 |
| CLAUDE.md | /home/codex/projects/sub2api/CLAUDE.md | Claude 配置 | sub2api-maijian | 高 | 无 | 主仓库 Claude 配置 |
| CLAUDE.md | /home/codex/projects/sub2api-delivery-clean/CLAUDE.md | Claude 配置 | sub2api-maijian | 中 | 无 | worktree 副本 |
| CLAUDE.md | /home/codex/projects/sub2api-pr1-docs-ops/CLAUDE.md | Claude 配置 | sub2api-maijian | 中 | 无 | worktree 副本 |
| CLAUDE.md | /home/codex/projects/sub2api-pr1-docs-ops-v2/CLAUDE.md | Claude 配置 | sub2api-maijian | 中 | 无 | worktree 副本 |
| CHATGPT_START_HERE.md | /home/codex/projects/sub2api/CHATGPT_START_HERE.md | 引导文档 | sub2api-maijian | 高 | 无 | 多 Agent 引导入口 |
| CHATGPT_START_HERE.md | /home/codex/projects/sub2api-delivery-clean/CHATGPT_START_HERE.md | 引导文档 | sub2api-maijian | 中 | 无 | worktree 副本 |
| CHATGPT_START_HERE.md | /home/codex/projects/sub2api-pr1-docs-ops/CHATGPT_START_HERE.md | 引导文档 | sub2api-maijian | 中 | 无 | worktree 副本 |
| CHATGPT_START_HERE.md | /home/codex/projects/sub2api-pr1-docs-ops-v2/CHATGPT_START_HERE.md | 引导文档 | sub2api-maijian | 中 | 无 | worktree 副本 |
| CURRENT.md | /home/codex/projects/sub2api/CURRENT.md | 状态文件 | sub2api-maijian | 高 | 无 | 当前状态追踪 |
| CURRENT.md | /home/codex/projects/sub2api-delivery-clean/CURRENT.md | 状态文件 | sub2api-maijian | 中 | 无 | worktree 副本 |
| CURRENT.md | /home/codex/projects/sub2api-pr1-docs-ops/CURRENT.md | 状态文件 | sub2api-maijian | 中 | 无 | worktree 副本 |
| TASKS.md | /home/codex/projects/sub2api/TASKS.md | 任务列表 | sub2api-maijian | 高 | 无 | 任务追踪 |
| TASKS.md | /home/codex/projects/sub2api-delivery-clean/TASKS.md | 任务列表 | sub2api-maijian | 中 | 无 | worktree 副本 |
| TASKS.md | /home/codex/projects/sub2api-pr1-docs-ops/TASKS.md | 任务列表 | sub2api-maijian | 中 | 无 | worktree 副本 |
| DECISIONS.md | /home/codex/projects/sub2api/DECISIONS.md | 决策记录 | sub2api-maijian | 高 | 无 | ADR 决策日志 |
| DECISIONS.md | /home/codex/projects/hermes-core-audit-private/DECISIONS.md | 决策记录 | hermes-core-audit-private | 高 | 无 | Hermes 决策日志 |
| DECISIONS.md | /home/codex/projects/aoxue-edu-clean/DECISIONS.md | 决策记录 | aoxue-edu | 高 | 无 | 学热决策日志 |
| DECISIONS.md | /home/codex/projects/dream-soul-sub2api/DECISIONS.md | 决策记录 | dream-soul | 中 | 无 | DreamSoul 决策 |
| DECISIONS.md | /home/codex/projects/biaoge-web/docs/agent-handoff/DECISIONS.md | 决策记录 | biaoge-web | 高 | 无 | biaoge-web 决策 |
| RUNBOOK.md | /home/codex/projects/sub2api/RUNBOOK.md | 运维手册 | sub2api-maijian | 高 | 无 | 部署运维指南 |
| RUNBOOK.md | /home/codex/projects/sub2api-delivery-clean/RUNBOOK.md | 运维手册 | sub2api-maijian | 中 | 无 | worktree 副本 |
| RUNBOOK.md | /home/codex/projects/sub2api-pr1-docs-ops/RUNBOOK.md | 运维手册 | sub2api-maijian | 中 | 无 | worktree 副本 |
| RUNBOOK.md | /home/codex/projects/sub2api-pr1-docs-ops-v2/RUNBOOK.md | 运维手册 | sub2api-maijian | 中 | 无 | worktree 副本 |

### 3.2 Reports 目录

| 资产名称 | 路径 | 类型 | 可能归属仓库 | 复用价值 | 风险 | 说明 |
|----------|------|------|-------------|---------|------|------|
| sub2api reports | /home/codex/projects/sub2api/reports/ | 报告集合 | sub2api-maijian | 高 | 无 | 含 claude/, codex/, incident/ 子目录 |
| sub2api incident report | /home/codex/projects/sub2api/reports/incident/latest.md | 生产事件报告 | sub2api-maijian | 高 | 可能含敏感 | ~19K, 生产事件 |
| sub2api incident closeout | /home/codex/projects/sub2api/reports/incident/wsl-server-guard-closeout.md | 生产事件关闭报告 | sub2api-maijian | 高 | 无 | WSL 服务器守卫关闭 |
| dream-soul-control reports | /home/codex/projects/dream-soul-control/reports/ | 报告集合 | dream-soul-control | 高 | 无 | ~572K, 20+ 审计/交接报告 |
| biaoge-web reports (dreamsoul) | /home/codex/projects/biaoge-web/docs/dreamsoul-chat-agent/reports/ | 报告集合 | biaoge-web | 中 | 无 | 角色工作室相关报告 |
| biaoge-web reports (deploy) | /home/codex/projects/biaoge-web/runtime/local-deploy/reports/ | 部署报告 | biaoge-web | 低 | 无 | 仅 1 文件 cloudflare tunnel |
| hermes reports (nightly) | /home/codex/.hermes/profiles/*/reports/nightly/ | 夜巡报告 | hermes | 中 | 无 | 多个 profile 各有 nighty 报告 |
| hermes-core-audit reports | /home/codex/projects/hermes-core-audit-private/knowledge/archive/reports/ | 体系白皮书 | hermes-core-audit-private | 高 | 无 | Hermes 白皮书/手册多版本 |

### 3.3 Orchestration 目录

| 资产名称 | 路径 | 类型 | 可能归属仓库 | 复用价值 | 风险 | 说明 |
|----------|------|------|-------------|---------|------|------|
| orchestration | /home/codex/projects/sub2api/orchestration | 编排脚本 | sub2api-maijian | 高 | 无 | 主仓库编排 |
| orchestration | /home/codex/projects/sub2api-delivery-clean/orchestration | 编排脚本 | sub2api-maijian | 中 | 无 | worktree 副本 |
| orchestration | /home/codex/projects/sub2api-pr1-docs-ops/orchestration | 编排脚本 | sub2api-maijian | 中 | 无 | worktree 副本 |
| orchestration | /home/codex/projects/sub2api-pr1-docs-ops-v2/orchestration | 编排脚本 | sub2api-maijian | 中 | 无 | worktree 副本 |

### 3.4 本地脚本和工具

| 资产名称 | 路径 | 类型 | 复用价值 | 风险 | 说明 |
|----------|------|------|---------|------|------|
| start-biaoge-web.sh | /home/codex/scripts/start-biaoge-web.sh | 启动脚本 | 中 | 无 | biaoge-web 本地启动 |
| hermes-token-api.py | /home/codex/hermes-token-api.py | Python 脚本 | 低 | 可能含敏感 | Token API |
| hermes-token-export.py | /home/codex/hermes-token-export.py | Python 脚本 | 低 | 可能含敏感 | Token 导出 |
| start-token-api.sh | /home/codex/start-token-api.sh | 启动脚本 | 低 | 无 | Token API 启动 |
| update_blocked.py | /home/codex/update_blocked.py | Python 脚本 | 低 | 无 | QA 更新脚本 |
| update_dashboard.py | /home/codex/update_dashboard.py | Python 脚本 | 低 | 无 | QA 仪表板 |
| update_qa_dashboard.py | /home/codex/update_qa_dashboard.py | Python 脚本 | 低 | 无 | QA 仪表板 |
| qa_test.py | /home/codex/qa_test.py | Python 脚本 | 低 | 无 | QA 测试脚本 |
| qa_results.json | /home/codex/qa_results.json | JSON 数据 | 低 | 无 | QA 结果 |

### 3.5 审计/报告文档 (HOME 级别)

| 资产名称 | 路径 | 类型 | 复用价值 | 风险 | 说明 |
|----------|------|------|---------|------|------|
| DreamSoul 审计报告 | /home/codex/dreamsoul-audit-2026-05-25.md | 审计报告 | 高 | 无 | 2026-05-25 完成 |
| DreamSoul 审计报告 | /home/codex/dreamsoul_audit_20260524.md | 审计报告 | 高 | 无 | 2026-05-24 完成 |
| biaoge 视觉词典 | /home/codex/docs/biaoge-visual-dictionary-lighting.md | 文档 | 中 | 无 | 11K, 灯光视觉词典 |

### 3.6 ai-collaboration-playbook 现有结构

| 目录/文件 | 说明 |
|-----------|------|
| AI_AGENT_ONBOARDING.md | Agent 入职指南 |
| AI_COLLABORATION_MODE_V4.md | 协作模式 v4 |
| NEW_PROJECT_BOOTSTRAP.md | 新项目启动模板 |
| README.md | 仓库说明 |
| archive/ | 归档目录 |
| checklists/ | 检查清单目录 |

---

## 4. 敏感风险清单

> 仅列路径和风险说明, 不输出任何内容。

| 风险类型 | 路径 | 说明 |
|----------|------|------|
| `.env` 文件 | /home/codex/.hermes/.env | **Hermes 主环境配置, 含密钥** |
| `.env` 备份 | /home/codex/.hermes/.env.bak_maijian_gpt_20260515_* | 历史环境配置备份 (2份) |
| `.env` 文件 | /home/codex/.config/sub2api-character-studio-worker.env | Character Studio 环境变量 |
| `.env` 文件 | /home/codex/projects/biaoge-web/.env | biaoge-web 环境配置 |
| `.env` 文件 | /home/codex/runtime/sub2api-maijian/.env | 运行时环境配置 |
| `.env.local` | /home/codex/projects/dream-soul-email-routing/.env.local | 邮件路由本地配置 |
| Token 文件 | /home/codex/.config/sub2api-maijian/cloudflare-api-token | Cloudflare API Token |
| Token 文件 | /home/codex/.config/dreamsoul/agent_gateway_token | Agent Gateway Token |
| API Key 文件 | /home/codex/.config/dreamsoul/llm_api_key | LLM API Key |
| 认证文件 | /home/codex/.hermes/auth.json | Hermes 认证凭据 |
| 认证文件 | /home/codex/.hermes/auth.json.bak_* | 认证凭据备份 (2份) |
| 数据库 | /home/codex/projects/aoxue-edu-clean/aoxue_edu_production.db | 生产数据库 |
| 数据库 | /home/codex/projects/aoxue-edu-clean/aoxue_edu.db | 开发数据库 |
| 数据库 | /home/codex/projects/aoxue-edu-clean.bad-1778640795/aoxue_edu_production.db | 生产数据库副本 |
| 数据库 | /home/codex/projects/aoxue-edu-clean.bad-1778640795/aoxue_edu.db | 开发数据库副本 |
| 数据库 | /home/codex/projects/biaoge-web/product.db | 产品数据库 |
| 数据库 | /home/codex/.hermes/state.db / response_store.db / kanban.db | Hermes 内部数据库 |
| 数据库 | /home/codex/.codex/*.sqlite | Codex 内部状态数据库 |
| 浏览器数据库 | /home/codex/.camofox/profiles/*/cookies.sqlite 等 | 浏览器 profile 数据库 |
| 测试凭据 | /home/codex/test_creds.json | 测试凭据 |
| 备份目录 | /home/codex/projects/biaoge-web/backups/ | biaoge-web 备份 |
| 备份目录 | /home/codex/projects/biaoge-web/data/backups/ | biaoge-web 数据备份 |
| 备份目录 | /home/codex/runtime/sub2api-maijian/backups/ | 运行时备份 |
| 备份目录 | /home/codex/.hermes/profiles/*/backups/ | Hermes profile 备份 |
| 备份目录 | /home/codex/projects/SillyTavern/backups/ | SillyTavern 备份 |
| 压缩包 | /home/codex/projects/dream-soul-email-routing-transfer.tar.gz | 邮件路由传输包 |
| 压缩包 | /home/codex/projects/sillytavern-lab-source-test/ST-release.tar.gz | SillyTavern 发布包 |
| Docker 运行数据 | /home/codex/runtime/sub2api-maijian/postgres_data/ | PostgreSQL 数据目录 |
| Docker 运行数据 | /home/codex/runtime/sub2api-maijian/redis_data/ | Redis 数据目录 |
| Docker 运行数据 | /home/codex/runtime/sub2api-maijian/data/ | 应用数据目录 |
| PID / 锁文件 | /home/codex/.hermes/gateway.pid / gateway.lock / gateway_state.json | Hermes Gateway 运行时状态 |

---

## 5. 建议分流

### 5.1 → sub2api-maijian

| 资产 | 说明 |
|------|------|
| sub2api 主仓库 (当前工作目录) | 已经是该仓库的工作副本 |
| sub2api worktree 系列 (delivery-clean, pr1-docs-ops, pr2-upstream-integration 等) | 共享同一仓库, 已在仓库管理下 |
| sub2api reports/ | 已在仓库内 |
| sub2api orchestration/ | 已在仓库内 |
| sub2api 全套 Agent 协作文件 (AGENTS.md, CLAUDE.md, etc.) | 已在仓库内 |

### 5.2 → ai-collaboration-playbook

| 资产 | 说明 |
|------|------|
| 本审计报告 | 本次创建 |
| /home/codex/dreamsoul-audit-2026-05-25.md | DreamSoul 审计报告, 可归档 |
| /home/codex/dreamsoul_audit_20260524.md | DreamSoul 审计报告, 可归档 |
| /home/codex/docs/biaoge-visual-dictionary-lighting.md | 视觉词典文档 |
| hermes-core-audit-private/knowledge/archive/reports/ 中的通用方法论文档 | 非敏感部分可提炼 |

### 5.3 → maijian-wechat-content-lab

| 资产 | 说明 |
|------|------|
| sub2api Character Studio 相关文件 (CHARACTER_STUDIO_HERMES.md 等) | 未提交的 Character Studio 资产 |
| /home/codex/.config/sub2api-character-studio-worker.env | 需在人工确认后决定是否提炼模板 |

### 5.4 → shanxi-edu-hot / aoxue-edu

| 资产 | 说明 |
|------|------|
| aoxue-edu-clean 仓库 | 已在 aoxue-edu GitHub 仓库 |
| aoxue-edu-clean.bad-1778640795 | 可清理的副本 |
| aoxue 生产数据库 | **不应入仓, 需安全处理** |

### 5.5 暂不入仓 / 仅本地保留

| 资产 | 说明 |
|------|------|
| bendi-llm-gateway | 服务器镜像, 无远程, 建议保持本地 |
| dream-soul-adapter, dream-soul-bff | 实验性质, 建议确认价值后再决定 |
| dream-soul-sub2api | origin 指向本地, 实验性 |
| SillyTavern 全系列 (lab, runtime-patched, source-test) | 第三方源码 + 本地 patch, 建议保持本地 |
| feishu_docs_tool | 单文件工具, 价值低 |
| codex-smoke-test | 空仓库 |
| hermes 全系统 (.hermes/, hermes-agent/) | 运行中系统, 不建议入仓 |
| camofox-browser / .camofox/ | 浏览器工具, 不建议入仓 |

### 5.6 应隔离 / 删除前需人工确认

| 资产 | 原因 |
|------|------|
| aoxue-edu-clean.bad-1778640795 | 含生产数据库副本, 时间戳名暗示是废弃副本 |
| sub2api.bad-1778640832 | 同上, 含上游镜像的废弃工作副本 |
| sub2api-maijian-fact-source-clean-* (2个) | 清理快照目录, 可能已过期 |
| dream-soul-email-routing-transfer.tar.gz | 传输包, 可能已过期 |
| /home/codex/.hermes/.env.bak_maijian_gpt_* | 含密钥的旧备份 |
| /home/codex/.hermes/auth.json.bak_* | 含认证凭据的旧备份 |
| sub2api-qwen-fix, sub2api-qwen-thinking | 早期实验 worktree, 可能已过期 |

---

## 6. 下一步建议

> 以下为建议, 本轮未执行任何迁移操作。

1. **生产数据库安全处置**: aoxue-edu 生产数据库 (`aoxue_edu_production.db`) 存在于两个目录中, 应从版本控制和审计入仓中永久排除
2. **废弃副本清理**: 带 `.bad-` 前缀和时间戳的目录 (5+ 个) 建议人工确认后清理, 减少磁盘占用 (~700M+)
3. **Agent 协作文件标准化**: sub2api 各 worktree 上的 AGENTS.md / CLAUDE.md / CHATGPT_START_HERE.md 存在重复, 建议统一到主仓库 `docs/agent-collab/` 目录
4. **Hermes 审计文档提炼**: hermes-core-audit-private 中的白皮书/手册可提炼非敏感版本入 ai-collaboration-playbook
5. **DreamSoul 审计报告归档**: 两份 HOME 级审计报告可归档到 ai-collaboration-playbook 的 `archive/` 目录
6. **敏感文件 .gitignore 复核**: 确认各仓库 `.gitignore` 已覆盖所有 `.env`, `*.db`, `*.sqlite`, `auth.json`, token 文件
7. **worktree 清理**: sub2api 有 8 个 worktree, 部分可能已过期 (qwen-fix, qwen-thinking), 建议 `git worktree prune` 前人工确认
8. **biaoge-web worktree 状态**: biaoge-web 有 2 个 worktree + 1 个非 git 副本 (role-studio-pr), 建议统一
9. **bendi-llm-gateway**: 无远程的服务器镜像, 建议决定是推送到私有仓库还是保持本地
10. **定期审计**: 建议每月运行一次类似的只读审计, 追踪资产增长和敏感文件暴露风险

---

## 附录: 未扫描范围

| 路径 | 说明 |
|------|------|
| /mnt/c, /mnt/d, /mnt/e | Windows 文件系统, 本轮未扫描 |
| /home/codex/.hermes/ (大部分内容) | 运行中 Hermes 系统, 仅做了路径级盘点 |
| /home/codex/.camofox/ | 浏览器 profile 和缓存, 仅做了路径级盘点 |
| /home/codex/runtime/sub2api-maijian/ (Docker 数据) | 运行中容器数据, 仅做了路径级盘点 |
| node_modules, venv, dist, build 等 | 按排除规则跳过 |
