# C-B: DreamSoul / Character Studio 价值审计

## 1. 审计范围

- 项目: DreamSoul 平台线 + Character Studio / 形象馆
- 本地路径: `/home/codex/projects/dream-soul-control`, `dream-soul-adapter`, `dream-soul-bff`, `dream-soul-sub2api`, `dreamsoul-chat-agent`
- 读取文件: AGENTS.md, README.md, DECISIONS.md, reports/*.md, docs/
- 未读取: .env, auth.json, token, db, worker env, 密钥

## 2. 读取的安全文件

| 文件 | 路径 |
|------|------|
| AGENTS.md | dream-soul-control/docs/agent-handoff/AGENTS.md |
| DECISIONS.md | dream-soul-control/DECISIONS.md (空) |
| DECISIONS.md | dream-soul-control/docs/agent-handoff/DECISIONS.md |
| reports/* (20+份) | dream-soul-control/reports/ |
| README.md | dream-soul-adapter/README.md |
| README.md | dream-soul-bff/README.md |
| README.md, SOUL.md | dreamsoul-chat-agent/ |
| CHARACTER_STUDIO_HERMES.md | sub2api/ (已提交但未推送) |
| PRODUCT_CHARACTER_IMAGE.md | sub2api/ (已提交但未推送) |
| dream-soul-admin-mock-link.md | biaoge-web/docs/ |
| dream-soul-chat-agent/ 报告 | biaoge-web/docs/dreamsoul-chat-agent/reports/ (12份) |

## 3. 资产评分表

| 资产 | 路径 | 建议归属 | 复用价值 | 完整度 | 整合难度 | 风险分 | 业务相关度 | 总分 | 分类 | 处理建议 |
|------|------|---------|---------|--------|----------|--------|-----------|------|------|----------|
| DreamSoul Agent Handoff | dream-soul-control/docs/agent-handoff/AGENTS.md | sub2api-maijian | 5 | 4 | 4 | 5 | 5 | 23 | **A** | 多 Agent 交接规范提炼入 playbook |
| DreamSoul 审计报告集 | dream-soul-control/reports/ (20+份) | sub2api-maijian | 4 | 5 | 4 | 5 | 5 | 23 | **A** | 审计方法论范本，脱敏后入 playbook |
| DreamSoul DECISIONS.md | dream-soul-control/docs/agent-handoff/DECISIONS.md | sub2api-maijian | 4 | 3 | 4 | 5 | 5 | 21 | **A** | DreamSoul 平台决策，保持业务仓 |
| dream-soul-control 仓库 | dream-soul-control/ | sub2api-maijian | 4 | 4 | 3 | 4 | 5 | 20 | **A** | DreamSoul 控制中心，应远程化并入 sub2api-maijian 组织 |
| dream-soul-adapter | dream-soul-adapter/ | sub2api-maijian | 3 | 3 | 4 | 5 | 4 | 19 | **B** | SillyTavern 字段适配适配器，保持本地或入 sub2api-maijian |
| dream-soul-bff | dream-soul-bff/ | sub2api-maijian | 3 | 3 | 4 | 5 | 4 | 19 | **B** | Sub2API Lab mock contract BFF，应并入 DreamSoul 平台线 |
| dream-soul-sub2api | dream-soul-sub2api/ | sub2api-maijian | 2 | 2 | 4 | 4 | 4 | 16 | **B** | origin 指向本地 sub2api，实验态，需确认价值 |
| dreamsoul-chat-agent | dreamsoul-chat-agent/ | sub2api-maijian | 3 | 3 | 4 | 4 | 4 | 18 | **B** | 聊天代理项目，含 SOUL.md、config、12份报告 |
| Character Studio Hermes | sub2api/CHARACTER_STUDIO_HERMES.md | sub2api-maijian | 5 | 3 | 4 | 4 | 5 | 21 | **A** | 形象馆 Hermes 守护文档，明确归 DreamSoul 线 |
| Character Studio Worker | sub2api/CHARACTER_STUDIO_WORKER.md | sub2api-maijian | 4 | 3 | 4 | 4 | 5 | 20 | **A** | 形象馆 Worker 配置文档 |
| Product Character Image | sub2api/PRODUCT_CHARACTER_IMAGE.md | sub2api-maijian | 3 | 2 | 4 | 4 | 5 | 18 | **B** | 角色图片配置文档 |

## 4. A 类资产

1. **DreamSoul Agent Handoff 规范** — 多 Agent 交接规范 (23分)
2. **DreamSoul 审计报告集 (20+份)** — 审计方法论范本 (23分)
3. **DreamSoul DECISIONS.md** — 平台决策 (21分)
4. **Character Studio Hermes** — 形象馆守护文档 (21分)
5. **dream-soul-control 仓库** — DreamSoul 控制中心 (20分)
6. **Character Studio Worker** — 形象馆 Worker 配置 (20分)

## 5. B 类资产

1. **dream-soul-adapter** — SillyTavern 适配器 (19分)
2. **dream-soul-bff** — BFF mock contract (19分)
3. **dreamsoul-chat-agent** — 聊天代理 (18分)
4. **Product Character Image** — 角色图片配置 (18分)
5. **dream-soul-sub2api** — 实验态子项目 (16分)

## 6. C/D 类资产

| 资产 | 路径 | 总分 | 说明 |
|------|------|------|------|
| dream-soul-control DECISIONS.md (根) | dream-soul-control/DECISIONS.md | 10 | 空文件，无内容 |
| dreamsoul-chat-agent import_reports | dreamsoul-chat-agent/import_reports/ | 12 | 导入报告，历史价值 |
| dreamsoul-chat-agent conversations | dreamsoul-chat-agent/conversations/ | 10 | 会话历史 |

## 7. X 类禁止入仓资产

| 类型 | 路径 | 原因 |
|------|------|------|
| .env | dream-soul-email-routing/.env.local | 含密钥 |
| .env.example | dream-soul-email-routing/.env.example | 配置模板，但关联邮件服务 |
| 传输压缩包 | dream-soul-email-routing-transfer.tar.gz | 旧传输包 |
| token 文件 | .config/dreamsoul/agent_gateway_token | Agent Gateway Token |
| API Key | .config/dreamsoul/llm_api_key | LLM API Key |

## 8. 分流建议

| 目标 | 资产 |
|------|------|
| **ai-collaboration-playbook** | DreamSoul Agent Handoff 规范 (脱敏版)、DreamSoul 审计报告集 (方法论部分)、多 Agent 交接模式 |
| **sub2api-maijian** | dream-soul-control, dream-soul-adapter, dream-soul-bff, dreamsoul-chat-agent, Character Studio 全部文档, dream-soul-sub2api |
| **保持本地** | .env, token, API Key, 传输压缩包, 会话历史 |

## 9. 需要总控裁决的问题

1. **DreamSoul 平台线是否应独立于 sub2api-maijian** — 当前 dream-soul-control 有独立 GitHub 仓库 (dream-soul-control.git)，是否应合并到 sub2api-maijian 组织或保持独立
2. **dream-soul-sub2api origin 指向本地 sub2api** — 这是实验性配置，是否应更正为远程 origin
3. **DreamSoul 20+ 份审计报告中哪些可以脱敏入 playbook** — 大部分是 Hermes 系统审计报告，可能含内部架构细节
4. **dreamsoul-chat-agent 的 12 份 reports 是否应迁移到 biaoge-web 仓库** — 这些报告实际是在 biaoge-web 上下文产生的

## 10. 下一步建议

1. P0: 确认 DreamSoul 平台线各仓库的远程化策略 (control, adapter, bff)
2. P1: 脱敏 DreamSoul 审计报告中可提炼的方法论部分
3. P1: 修正 dream-soul-sub2api 的 origin 指向
4. P2: Character Studio 文档整理进入 sub2api-maijian docs/character-studio/
