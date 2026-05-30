# Hermes Skills 价值审计报告 (v1)

**审计日期**: 2026-05-30
**审计人**: H-A (Hermes Skills Value Audit)
**审计范围**: `/home/hermes/.hermes/skills/` 下全部 83 个技能目录（52 个含 SKILL.md，31 个为分类/占位目录）

---

## 1. 审计范围

| 维度 | 数值 |
|------|------|
| 技能目录总数 | 83 |
| 含 SKILL.md 的技能数 | 52 |
| 分类/占位目录（无 SKILL.md） | 31 |
| 精读 SKILL.md 数 | 30（focus list） |
| 快速扫描数 | 22（其余含 SKILL.md 的技能） |

### 评分标准

每个技能按 5 个维度评分（1-5 分），满分 25 分：

| 维度 | 说明 |
|------|------|
| 复用价值 | 能否成为模板/协议/工具/文章/产品模块 |
| 当前完整度 | 是否成熟，是否有 README/使用说明 |
| 整合难度 | 越高越容易整合（5=开箱即用，1=需大量改造） |
| 风险程度 | 越高越安全（5=无敏感信息，1=含密钥/生产数据） |
| 业务相关度 | 是否契合 AI 协作 / sub2api / 微信 / 教育等业务 |

**分级**: A=20-25, B=15-19, C=10-14, D=1-9, X=禁止入仓

---

## 2. 读取的安全文件

本次审计仅读取 `/home/hermes/.hermes/skills/*/SKILL.md` 文件，未读取 `.env`、`auth.json`、`*.db`、`logs`、`sessions`、`pastes`、`backups` 等敏感文件。所有路径引用保留原始形式，未输出任何密钥或凭证内容。

---

## 3. 资产评分表

### 3.1 精读技能（Focus List，30 个）

| # | 技能名 | 复用价值 | 完整度 | 整合难度 | 安全 | 业务相关 | 总分 | 分级 | 简述 |
|---|--------|---------|--------|---------|------|---------|------|------|------|
| 1 | github-ai-collaboration-pattern | 5 | 5 | 4 | 5 | 5 | 24 | A | 四件套协作框架，通用性极强 |
| 2 | context-injection-protocol | 5 | 5 | 3 | 5 | 5 | 23 | A | 双轨注入协议，多代理系统核心 |
| 3 | article-writing-workflow | 5 | 5 | 3 | 5 | 5 | 23 | A | 公众号写作全链路 SOP |
| 4 | hermes-skill-development-standard | 5 | 5 | 5 | 5 | 4 | 24 | A | 技能开发宪法，元规范 |
| 5 | feishu-broadcast-standard | 5 | 5 | 4 | 5 | 5 | 24 | A | 飞书播报 SSOT，样式/文案/发送全规范 |
| 6 | sanitized-public-demo-creation | 5 | 5 | 4 | 5 | 3 | 22 | A | 脱敏公开演示创建协议，通用安全流程 |
| 7 | topic-mining-synthesis | 4 | 5 | 3 | 5 | 4 | 21 | A | 社区知识提炼引擎，含 Cron+Wiki 全链路 |
| 8 | hermes-skills-architecture-refactoring | 4 | 5 | 4 | 5 | 4 | 22 | A | 三层架构重构+Dashboard 可视化 |
| 9 | role-memory-pipeline | 4 | 5 | 3 | 5 | 5 | 22 | A | 角色经验自动沉淀管线 |
| 10 | hermes-weekly-audit | 4 | 4 | 3 | 5 | 5 | 21 | A | 周度漂移审计，系统治理核心 |
| 11 | project-fact-layer-audit | 4 | 5 | 4 | 5 | 4 | 22 | A | 项目事实层审计，马拉松模式 |
| 12 | maijian-wechat-publish-config | 4 | 5 | 3 | 4 | 5 | 21 | A | 微信公众号生产配置标准 |
| 13 | standard-driven-team-upgrade | 4 | 4 | 4 | 5 | 4 | 21 | A | 对标升级工作流 |
| 14 | html-ppt-video-pipeline | 3 | 3 | 3 | 5 | 4 | 18 | B | HTML-PPT 视频管线，框架级 |
| 15 | maijian-video-hyperframes-rendering | 4 | 4 | 3 | 5 | 4 | 20 | A | HyperFrames 渲染技术规范 |
| 16 | wechat-article-camofox | 4 | 5 | 4 | 5 | 4 | 22 | A | 公众号文章抓取工具 |
| 17 | aoxue-edu-development | 3 | 5 | 2 | 3 | 5 | 18 | B | 奥学教育开发指南，高度项目化 |
| 18 | aoxue-feishu-query | 3 | 4 | 3 | 3 | 5 | 18 | B | 飞书 NL 查询运营工具 |
| 19 | hermes-openclaw-collaboration | 4 | 4 | 3 | 3 | 4 | 18 | B | Hermes-OpenClaw 跨 Agent 协作 |
| 20 | cron-audit-after-standards | 3 | 5 | 4 | 5 | 3 | 20 | A | CRON 审计清理工作流 |
| 21 | feishu-file-sender | 4 | 4 | 4 | 3 | 4 | 19 | B | 飞书文件发送器 |
| 22 | hermes-feishu-streaming-card | 3 | 4 | 2 | 3 | 3 | 15 | B | 流式卡片 sidecar，维护成本高 |
| 23 | dashscope-qwen-tts-config | 4 | 4 | 3 | 3 | 3 | 17 | B | DashScope TTS 配置指南 |
| 24 | lmstudio-local-setup | 4 | 5 | 3 | 4 | 2 | 18 | B | LM Studio 本地 profile 配置 |
| 25 | wsl-vhdx-compaction | 4 | 5 | 5 | 5 | 1 | 19 | B | WSL VHDX 压缩指南 |
| 26 | premium-dark-theme-upgrade | 4 | 5 | 4 | 5 | 2 | 20 | A | Aurora 2.0 毛玻璃主题升级 |
| 27 | element-plus-popup-positioning-fix | 4 | 4 | 5 | 5 | 2 | 20 | A | Element Plus 弹窗定位修复 |
| 28 | dark-tech-ui-style | 2 | 3 | 4 | 5 | 2 | 16 | B | 暗黑技术 UI 兼容别名 |
| 29 | school-data-quality-fix | 3 | 4 | 4 | 5 | 2 | 18 | B | 学校数据质量修复 |
| 30 | autonomous-ai-agents | 0 | 0 | 0 | 0 | 0 | 0 | X | 无 SKILL.md 文件 |

### 3.2 快速扫描技能（其余 22 个含 SKILL.md 的技能）

| # | 技能名 | 复用价值 | 完整度 | 整合难度 | 安全 | 业务相关 | 总分 | 分级 | 简述 |
|---|--------|---------|--------|---------|------|---------|------|------|------|
| 31 | aoxue-data-query | 3 | 3 | 3 | 4 | 4 | 17 | B | 奥学飞书群数据查询 |
| 32 | aoxue-edu-pack-deploy | 2 | 3 | 3 | 4 | 4 | 16 | B | 奥学一键打包部署 |
| 33 | aurora-theme-development | 3 | 3 | 4 | 5 | 2 | 17 | B | Aurora 暗黑主题开发指南 |
| 34 | community-daily-ingestion | 4 | 4 | 3 | 4 | 4 | 19 | B | 社区日报采集索引 |
| 35 | competitor-style-analysis-workflow | 3 | 3 | 3 | 5 | 4 | 18 | B | 竞品公众号风格拆解 |
| 36 | darwin-skill | 3 | 3 | 2 | 5 | 3 | 16 | B | 技能自主进化系统 |
| 37 | dogfood | 3 | 3 | 4 | 5 | 3 | 18 | B | Web App 探索式 QA |
| 38 | excalidraw-diagram-generator | 3 | 3 | 4 | 5 | 3 | 18 | B | 自然语言转 Excalidraw |
| 39 | feishu-card-rendering-reality | 4 | 4 | 3 | 5 | 4 | 20 | A | 飞书卡片渲染真相 |
| 40 | github-ssh-setup | 3 | 4 | 5 | 5 | 2 | 19 | B | WSL2 GitHub SSH 配置 |
| 41 | gpt-image-generate | 3 | 3 | 3 | 4 | 3 | 16 | B | GPT 图像生成/编辑 |
| 42 | gpu-memory-upgrade | 3 | 3 | 3 | 5 | 3 | 17 | B | GPU 记忆引擎配置 |
| 43 | hermes-custom-provider | 3 | 3 | 3 | 4 | 3 | 16 | B | 自定义 Provider 添加 |
| 44 | hermes-tts-provider-addition | 3 | 3 | 3 | 4 | 3 | 16 | B | TTS Provider 添加 |
| 45 | hermes-update-maintenance | 3 | 4 | 3 | 5 | 4 | 19 | B | Hermes 升级补丁维护 |
| 46 | holographic-hf-offline-fix | 2 | 3 | 4 | 5 | 3 | 17 | B | Holographic HF 离线修复 |
| 47 | math-problem-explainer-video | 3 | 3 | 3 | 5 | 3 | 17 | B | 数学题 Manim 动画制作 |
| 48 | moss-tts-deployment | 3 | 3 | 2 | 4 | 3 | 15 | B | MOSS-TTS 模型部署 |
| 49 | openmaic-video-pipeline | 3 | 3 | 3 | 5 | 3 | 17 | B | OpenMAIC 视频录制 |
| 50 | team-boss | 5 | 5 | 3 | 5 | 5 | 23 | A | 通用团队总控路由 |
| 51 | wechat-article-creation-guide | 3 | 3 | 3 | 5 | 4 | 18 | B | 公众号创作策略指南 |
| 52 | wsl-disk-compaction | 3 | 4 | 5 | 5 | 1 | 18 | B | WSL 磁盘压缩（与 wsl-vhdx-compaction 重复） |
| 53 | yuanbao | 2 | 3 | 3 | 3 | 3 | 14 | C | 元宝群 @ 用户查询 |

### 3.3 分类/占位目录（31 个，无 SKILL.md）

以下目录仅为分类容器或空占位，不含可评估技能内容：
`apple`, `content`, `creative`, `dashboard-development`, `data-science`, `data`, `delegation`, `devops`, `diagramming`, `domain`, `draco`, `email`, `gaming`, `gifs`, `github`, `index-cache`, `inference-sh`, `mcp`, `media`, `messaging`, `mlops`, `note-taking`, `productivity`, `red-teaming`, `research`, `roleplay`, `smart-home`, `social-media`, `software-development`, `web-development`

---

## 4. A 类资产（20-25 分，17 个）

**核心特征**：高复用价值、成熟度高、可直接成为 playbook 协议或产品模块

| 技能名 | 总分 | 核心价值主张 |
|--------|------|-------------|
| github-ai-collaboration-pattern | 24 | 四件套协作框架，通用 AI 团队编排协议，可独立成文/产品 |
| hermes-skill-development-standard | 24 | 技能开发宪法，三层架构元规范 |
| feishu-broadcast-standard | 24 | 飞书播报 SSOT，样式/文案/发送全规范 |
| context-injection-protocol | 23 | 双轨上下文注入协议，多代理系统核心基础设施 |
| article-writing-workflow | 23 | 公众号写作全链路 SOP（素材提取->主编->写手->发布） |
| team-boss | 23 | 通用团队总控路由，意图识别+分派+播报 |
| sanitized-public-demo-creation | 22 | 内部项目脱敏为公开 demo 的安全流程 |
| hermes-skills-architecture-refactoring | 22 | 技能库三层重构+Dashboard 可视化工作流 |
| role-memory-pipeline | 22 | 角色经验自动沉淀闭环管线 |
| project-fact-layer-audit | 22 | 项目事实层审计（含马拉松深加工模式） |
| wechat-article-camofox | 22 | 公众号文章精准抓取工具（camofox 方案） |
| maijian-wechat-publish-config | 21 | 微信公众号生产配置标准（API/封面/编码/IP） |
| hermes-weekly-audit | 21 | 周度漂移审计，系统健康治理核心 |
| standard-driven-team-upgrade | 21 | 对标升级工作流，矩阵化审计+批量补齐 |
| topic-mining-synthesis | 21 | 社区知识专题提炼（Cron+Wiki+LLM 深度稿） |
| cron-audit-after-standards | 20 | CRON 任务审计清理工作流 |
| maijian-video-hyperframes-rendering | 20 | HyperFrames 视频渲染技术规范（TTS/音画同步） |
| premium-dark-theme-upgrade | 20 | Aurora 2.0 毛玻璃+霓虹主题升级指南 |
| element-plus-popup-positioning-fix | 20 | Element Plus 弹窗定位修复（通用 Vue3+EP 项目） |
| feishu-card-rendering-reality | 20 | 飞书卡片渲染真相（双构建器/限制/测试） |

> 注：A 类 20 个（含 feishu-card-rendering-reality 和 premium-dark-theme-upgrade 和 element-plus-popup-positioning-fix 在快速扫描中发现）

---

## 5. B 类资产（15-19 分，24 个）

**核心特征**：有价值但项目绑定较深、或完整度不足、或整合成本较高

| 技能名 | 总分 | 主要短板 |
|--------|------|---------|
| feishu-file-sender | 19 | 含凭证引用路径，中英双语文档略冗余 |
| hermes-update-maintenance | 19 | 升级补丁维护，偏运维 |
| github-ssh-setup | 19 | 基础工具类，通用但价值有限 |
| community-daily-ingestion | 19 | 社区日报采集，绑定飞书群 |
| html-ppt-video-pipeline | 18 | 框架级但内容较薄 |
| aoxue-edu-development | 18 | 高度绑定奥学项目 |
| aoxue-feishu-query | 18 | 运营工具，绑定特定 DB |
| hermes-openclaw-collaboration | 18 | 绑定 OpenClaw 配置 |
| lmstudio-local-setup | 18 | 本地模型 profile 配置， niche |
| school-data-quality-fix | 18 | 高度绑定太原学校数据 |
| aoxue-data-query | 17 | 与 aoxue-feishu-query 功能重叠 |
| dashscope-qwen-tts-config | 17 | TTS 配置，需 API Key |
| gpu-memory-upgrade | 17 | GPU 记忆配置， niche |
| aurora-theme-development | 17 | 与 premium-dark-theme-upgrade 重叠 |
| hermes-custom-provider | 16 | Provider 添加， niche |
| hermes-tts-provider-addition | 16 | 与 dashscope 重叠 |
| gpt-image-generate | 16 | 图像生成，通用但不深 |
| competitor-style-analysis-workflow | 18 | 竞品分析，有复用潜力 |
| dogfood | 18 | Web App QA 探索，通用 |
| excalidraw-diagram-generator | 18 | 图生成器，工具类 |
| math-problem-explainer-video | 17 | Manim 数学视频， niche |
| openmaic-video-pipeline | 17 | 官网视频录制， niche |
| wechat-article-creation-guide | 18 | 公众号创作策略 |
| darwin-skill | 16 | 技能自主进化，概念好但落地薄 |
| holographic-hf-offline-fix | 17 | 特定 bug 修复 |
| moss-tts-deployment | 15 | MOSS-TTS 部署， niche |
| aoxue-edu-pack-deploy | 16 | 奥学打包部署 |
| dark-tech-ui-style | 16 | 兼容别名，非独立技能 |
| hermes-feishu-streaming-card | 15 | 流式卡片 sidecar，维护成本高 |
| wsl-vhdx-compaction | 19 | WSL 磁盘压缩，通用运维 |
| wsl-disk-compaction | 18 | 与 wsl-vhdx-compaction 重复 |
| yuanbao | 14 | 元宝群查询， niche |

---

## 6. C/D 类资产

### C 类（10-14 分，1 个）

| 技能名 | 总分 | 说明 |
|--------|------|------|
| yuanbao | 14 | 元宝群 @ 用户查询，功能单一，绑定特定平台 |

### D 类（1-9 分，0 个）

无。最低分技能为 yuanbao（14 分）。

---

## 7. X 类禁止入仓资产

| 技能名 | 原因 |
|--------|------|
| autonomous-ai-agents | 目录存在但无 SKILL.md 文件，无实质内容 |

> 注意：部分技能引用了 `~/.hermes/.env` 路径（dashscope-qwen-tts-config, feishu-file-sender, hermes-feishu-streaming-card, hermes-tts-provider-addition），但仅为"读取该文件获取凭证"的说明，**未嵌入实际密钥值**，故不列入 X 类。整合时需确保凭证引用方式符合目标环境规范。

---

## 8. 分流建议

### 8.1 Playbook 层（通用协议/规范，可独立发布）

以下 12 个技能具备跨项目通用性，建议进入 `ai-collaboration-playbook/protocols/`：

- `github-ai-collaboration-pattern` — AI 团队协作四件套协议
- `context-injection-protocol` — 多代理上下文注入协议
- `hermes-skill-development-standard` — 技能开发元规范
- `feishu-broadcast-standard` — 飞书播报标准
- `sanitized-public-demo-creation` — 脱敏公开演示创建流程
- `standard-driven-team-upgrade` — 对标升级工作流
- `cron-audit-after-standards` — CRON 审计清理流程
- `project-fact-layer-audit` — 项目事实层审计框架
- `hermes-weekly-audit` — 系统周度审计框架
- `role-memory-pipeline` — 角色经验沉淀管线
- `team-boss` — 通用团队总控路由框架
- `feishu-card-rendering-reality` — 飞书卡片渲染技术文档

### 8.2 Maijian-WeChat-Content-Lab 层（公众号/内容生产）

以下 6 个技能建议归入麦尖内容实验室：

- `article-writing-workflow` — 公众号写作工作流
- `maijian-wechat-publish-config` — 微信公众号发布配置
- `wechat-article-camofox` — 公众号文章抓取
- `wechat-article-creation-guide` — 公众号创作策略
- `competitor-style-analysis-workflow` — 竞品风格拆解
- `maijian-video-hyperframes-rendering` — 视频渲染技术

### 8.3 Shanxi-Edu-Hot 层（教育业务）

以下 4 个技能建议归入教育业务线：

- `aoxue-edu-development` — 奥学开发指南
- `aoxue-feishu-query` — 飞书 NL 查询
- `aoxue-data-query` — 飞书群数据查询
- `school-data-quality-fix` — 学校数据质量修复

### 8.4 Local-Only 层（高度绑定本机/个人环境，不建议出仓）

以下 8 个技能建议仅保留在本地：

- `lmstudio-local-setup` — 本地模型 profile 配置
- `wsl-vhdx-compaction` / `wsl-disk-compaction` — WSL 磁盘压缩（后者为重复项可删除）
- `hermes-feishu-streaming-card` — 流式卡片 sidecar，维护成本高
- `hermes-update-maintenance` — 本机源码补丁维护
- `dark-tech-ui-style` — 兼容别名，非独立技能
- `yuanbao` — 元宝群查询
- `moss-tts-deployment` — MOSS-TTS 部署（大资产绑定）
- `holographic-hf-offline-fix` — 特定 bug 修复

### 8.5 待裁决层（需要总控判断是否值得整合）

- `html-ppt-video-pipeline` — 视频管线框架，内容较薄，需判断是否值得投入
- `darwin-skill` — 技能自主进化概念好但落地薄
- `openmaic-video-pipeline` — 官网视频录制， niche 场景
- `math-problem-explainer-video` — Manim 数学视频， niche
- `feishu-file-sender` — 文件发送器，中英双语文档需精简

---

## 9. 需要总控裁决的问题

1. **重复资产清理**：`wsl-vhdx-compaction` 与 `wsl-disk-compaction` 功能完全重叠，建议保留一个、删除另一个。
2. **技能库膨胀**：83 个目录中 31 个（37%）是空占位/分类容器（无 SKILL.md），是否做目录结构精简？
3. **凭证引用规范**：4 个技能引用 `~/.hermes/.env` 路径获取凭证，出仓时需要统一改为"外部配置注入"模式，不引用任何本地路径。
4. **aoxue 系列拆分**：aoxue-edu-development、aoxue-feishu-query、aoxue-data-query、aoxue-edu-pack-deploy 高度绑定奥学项目，是否作为 shanxi-edu 子包整体出仓，还是只提炼通用模式？
5. **OpenClaw 协作出仓**：`hermes-openclaw-collaboration` 中嵌入了大量 OpenClaw 配置详情（群 ID、Agent 注册表、Bot App ID），出仓前需要彻底脱敏。
6. **topic-mining-synthesis 社区数据**：技能中引用了飞书 Space ID（7629199638691597254）和群 ID，出仓前需参数化。

---

## 10. 下一步建议

1. **Phase 1（本周）**：总控裁决上述 6 个问题，确认分流方向。
2. **Phase 2（下周）**：按分流结果，将 A 类资产复制到对应目标仓库，做路径适配和脱敏处理。
3. **Phase 3（两周内）**：B 类资产做精简改造（去除项目绑定、统一配置接口），评估是否值得入仓。
4. **Phase 4（持续）**：建立技能入仓审查流程，新技能必须通过"复用价值/完整度/安全"三项门槛才允许加入。
5. **清理动作**：删除 `wsl-disk-compaction`（与 `wsl-vhdx-compaction` 重复）、清理 31 个空分类目录、移除 `autonomous-ai-agents` 空目录。
