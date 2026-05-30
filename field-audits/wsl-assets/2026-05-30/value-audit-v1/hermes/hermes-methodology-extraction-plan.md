# Hermes 方法论资产提取计划

**审计日期**: 2026-05-30
**审计人**: Hermes Methodology Extraction (H-E)
**输出路径**: `value-audit-v1/hermes/hermes-methodology-extraction-plan.md`

---

## 1. 审计范围

| # | 扫描路径 | 文件数 | 说明 |
|---|---------|--------|------|
| 1 | `/home/hermes/knowledge/standards/` | 17 | 系统规范（事实层/导航层/展示层治理、上下文注入、团队能力框架、SSOT 漂移门控、记忆纯度、文章生命周期 SOP 等） |
| 2 | `/home/hermes/knowledge/archive/reports/` | ~15 | 白皮书、系统状态报告、管道交付文档、多团队架构设计 |
| 3 | `/home/hermes/.hermes/skills/` | ~80 | 技能库，从中筛选含方法论内容的（非纯工具型） |
| 4 | `/home/hermes/.hermes/prompts/` | 1 | role_prompts.md |
| 5 | `/home/hermes/projects/hermes-core-audit-private/` | ~10 | EXPORT_MANIFEST, SECURITY_REDACTION_REPORT, ROADMAP |
| 6 | `/home/hermes/projects/hermes-system-spec-public/` | ~10 | 公开系统规范、白皮书、示例配置 |
| 7 | `/home/hermes/projects/hermes_overview_v*.md` | 9 | 系统各版本总览（v3 ~ v7.0） |

**未读取的安全敏感路径**: `.db` 文件、`.env`、`auth.json`、`config.yaml` 中的真实凭证、`state.db`、`memory_store.db`、日志、备份文件。

---

## 2. 读取的安全文件

本次审计仅读取以下类型文件的前 40-60 行，用于判断方法论价值：

- `knowledge/standards/*.md` (17 份规范)
- `knowledge/archive/reports/` 中的白皮书和架构报告
- `.hermes/skills/*/SKILL.md` 中具方法论属性的技能
- `.hermes/prompts/role_prompts.md`
- `hermes-core-audit-private/` 中的 EXPORT_MANIFEST、SECURITY_REDACTION_REPORT、ROADMAP
- `hermes-system-spec-public/README.md` + `docs/` 下的公开规范
- `hermes_overview_v*.md` 各版本

---

## 3. 资产评分表

评分维度：复用价值 / 当前完整度 / 整合难度 / 风险程度(越高越好) / 业务相关度，各 1-5，满分 25。

| ID | 资产名称 | 来源路径 | 复用 | 完整 | 整合 | 风险 | 业务 | 总分 | 等级 |
|----|---------|---------|------|------|------|------|------|------|------|
| M01 | SSOT 与漂移校验规范 | `knowledge/standards/10-ssot-drift-gate.md` | 5 | 5 | 2 | 5 | 5 | 22 | A |
| M02 | 上下文注入协议 | `knowledge/standards/13-context-injection.md` + `.hermes/skills/context-injection-protocol/` | 5 | 5 | 3 | 5 | 5 | 23 | A |
| M03 | 团队能力框架 (五层模型) | `knowledge/standards/14-team-capability-framework.md` | 5 | 4 | 2 | 5 | 4 | 20 | A |
| M04 | 团队注册与边界规范 | `knowledge/standards/15-team-registry-and-boundaries.md` | 4 | 4 | 2 | 5 | 4 | 19 | B |
| M05 | 记忆纯度与边界规范 | `knowledge/standards/16-memory-purity-and-boundary.md` | 4 | 4 | 2 | 5 | 4 | 19 | B |
| M06 | 文章生命周期 SOP | `knowledge/standards/17-article-lifecycle-sop.md` | 4 | 4 | 3 | 4 | 4 | 19 | B |
| M07 | 系统架构总览 (分层+团队矩阵) | `knowledge/standards/00-system-overview.md` | 4 | 4 | 3 | 3 | 4 | 18 | B |
| M08 | GitHub AI 协作模式 (四件套) | `.hermes/skills/github-ai-collaboration-pattern/` | 5 | 4 | 2 | 5 | 5 | 21 | A |
| M09 | 对标升级工作流 | `.hermes/skills/standard-driven-team-upgrade/` | 4 | 4 | 2 | 5 | 4 | 19 | B |
| M10 | 达尔文技能 (棘轮自主优化) | `.hermes/skills/darwin-skill/` | 5 | 4 | 3 | 5 | 4 | 21 | A |
| M11 | 脱敏公开演示创建流程 | `.hermes/skills/sanitized-public-demo-creation/` | 4 | 4 | 2 | 5 | 3 | 18 | B |
| M12 | 角色记忆管线 (经验沉淀闭环) | `.hermes/skills/role-memory-pipeline/` | 4 | 4 | 3 | 4 | 4 | 19 | B |
| M13 | 技能开发规范 (宪法) | `.hermes/skills/hermes-skill-development-standard/` | 4 | 5 | 2 | 5 | 3 | 19 | B |
| M14 | Hermes Weekly Audit 审计协议 | `.hermes/skills/hermes-weekly-audit/` | 4 | 4 | 2 | 5 | 3 | 18 | B |
| M15 | 专题知识提炼工作流 | `.hermes/skills/topic-mining-synthesis/` | 3 | 4 | 3 | 4 | 3 | 17 | B |
| M16 | 飞书播报标准 (样式与业务解耦) | `.hermes/skills/feishu-broadcast-standard/` | 3 | 5 | 3 | 5 | 3 | 19 | B |
| M17 | team-boss (通用总控路由) | `.hermes/skills/team-boss/` | 5 | 4 | 3 | 3 | 4 | 19 | B |
| M18 | 系统白皮书 v8 (真相版) | `knowledge/archive/reports/2026-04-18-hermes-system-whitepaper-v8.md` | 4 | 4 | 4 | 3 | 4 | 19 | B |
| M19 | 三层架构治理理念 | `hermes-system-spec-public/docs/wechat-article.md` | 5 | 4 | 2 | 5 | 5 | 21 | A |
| M20 | 系统术语表 | `knowledge/standards/01-terminology.md` | 3 | 4 | 1 | 5 | 3 | 16 | B |
| M21 | 项目结构规范 | `knowledge/standards/02-structure.md` | 3 | 4 | 2 | 5 | 3 | 17 | B |
| M22 | 命名规范 | `knowledge/standards/05-naming.md` | 2 | 4 | 2 | 5 | 2 | 15 | B |
| M23 | 状态文件规范 | `knowledge/standards/06-state-md.md` | 3 | 4 | 2 | 5 | 3 | 17 | B |
| M24 | 项目备份规范 | `knowledge/standards/07-project-backup.md` | 2 | 3 | 2 | 5 | 2 | 14 | C |
| M25 | 模型调用基石规范 | `knowledge/standards/11-model-foundation.md` | 3 | 4 | 4 | 2 | 3 | 16 | B |
| M26 | EXPORT_MANIFEST (导出清单) | `hermes-core-audit-private/EXPORT_MANIFEST.md` | 2 | 5 | 1 | 4 | 2 | 14 | C |
| M27 | SECURITY_REDACTION_REPORT | `hermes-core-audit-private/SECURITY_REDACTION_REPORT.md` | 2 | 5 | 1 | 4 | 2 | 14 | C |
| M28 | hermes_overview v3-v6 (历史版) | `projects/hermes_overview_v[3-6]*.md` | 2 | 3 | 4 | 3 | 2 | 14 | C |
| M29 | role_prompts.md | `.hermes/prompts/role_prompts.md` | 3 | 3 | 3 | 2 | 3 | 14 | C |
| M30 | Pipeline 交付文档 (Dashboard) | `knowledge/archive/reports/2026-04-19-hermes-pipeline-final.md` | 2 | 3 | 4 | 3 | 2 | 14 | C |
| M31 | ROADMAP | `hermes-core-audit-private/ROADMAP.md` | 1 | 3 | 2 | 4 | 2 | 12 | C |
| M32 | HTML-PPT-Video 流水线 | `.hermes/skills/html-ppt-video-pipeline/` | 2 | 3 | 3 | 4 | 3 | 15 | B |
| M33 | Hermes-OpenClaw 跨 Agent 协作 | `.hermes/skills/hermes-openclaw-collaboration/` | 3 | 3 | 4 | 2 | 3 | 15 | B |
| M34 | 系统规范入口 (public spec README) | `hermes-system-spec-public/README.md` | 4 | 4 | 2 | 5 | 4 | 19 | B |

---

## 4. A 类资产 (20-25 分：可直接提炼的方法论)

### A-1: SSOT 与漂移校验规范 (M01, 22 分)
- **核心价值**: 定义"事实层-导航层-展示层"三层文档治理体系，以及漂移检测和修复流程
- **可产出**: 《AI 协作文档治理协议》模板，含漂移校验 checklist
- **风险**: 无敏感信息，概念通用
- **建议**: 直接改写为通用 playbook 章节，去掉具体路径和工具名

### A-2: 上下文注入协议 (M02, 23 分)
- **核心价值**: 主代理向子代理动态组装"事实包"的协议，包含角色档案独立化、注入脚本、组装公式
- **可产出**: 《AI Agent 上下文注入协议》标准模板 + 事实包组装模式库
- **风险**: 涉及具体脚本路径和数据库表名
- **建议**: 提取协议框架和组装公式，用伪代码替代具体实现

### A-3: GitHub AI 协作模式四件套 (M08, 21 分)
- **核心价值**: ChatGPT(脑) + GitHub(记忆) + Codex(手脚) + Claude Code(肌肉) 的角色分工模型
- **可产出**: 《多模型 AI 协作框架》产品模块，含角色定义、铁律、工作流
- **风险**: 极低，本身就是通用方法论
- **建议**: 最适合作为 playbook 的开篇案例，几乎可直接使用

### A-4: 达尔文棘轮自主优化 (M10, 21 分)
- **核心价值**: 受 Karpathy autoresearch 启发的"实验-评估-保留"棘轮机制，同时评估结构质量和真实执行效果
- **可产出**: 《AI 技能自主进化协议》方法论文章
- **风险**: 涉及具体脚本路径
- **建议**: 提取棘轮概念和评估框架，改写为通用模式

### A-5: 三层架构治理理念 (M19, 21 分)
- **核心价值**: 面向普通读者的 Hermes 问题定义和解决思路，四层典型痛点 + 分层治理框架
- **可产出**: 《AI 协作为什么需要规范体系》品牌文章
- **风险**: 无，已公开发布
- **建议**: 作为 playbook 的引言/序章，适当扩写

### A-6: 团队能力框架五层模型 (M03, 20 分)
- **核心价值**: L1目标层 → L2边界层 → L3产出层 → L4记忆层 → L5进化层的团队能力成熟度模型
- **可产出**: 《AI 团队能力成熟度框架》评估工具
- **风险**: 涉及具体团队名称和路径
- **建议**: 保留五层结构，用通用角色替换具体实例

---

## 5. B 类资产 (15-19 分：需脱敏/改造后提炼)

### B-1: 团队注册与边界规范 (M04, 19 分)
- 可产出：《多 Agent 系统边界管理指南》
- 需脱敏：团队 ID、飞书群 ID、具体项目名
- 建议：提取"唯一事实源"概念和 ID 规范框架

### B-2: 记忆纯度与边界规范 (M05, 19 分)
- 可产出：《AI Agent 记忆治理 SOP》
- 需脱敏：具体路径和 bucket 名
- 建议：抽象为"什么该记、什么不该记"的决策树

### B-3: 对标升级工作流 (M09, 19 分)
- 可产出：《标准驱动的能力升级流程》模板
- 需脱敏：飞书工具名、具体团队名
- 建议：保留四步法（获取标准→审计→差距矩阵→系统性补齐）

### B-4: 文章生命周期 SOP (M06, 19 分)
- 可产出：《内容生产流水线 SOP》模板
- 需脱敏：具体项目路径、飞书群 ID
- 建议：抽象为"素材→提纲→草稿→审核→发布→归档"通用流程

### B-5: 飞书播报标准 (M16, 19 分)
- 可产出：《AI 团队播报规范》模板
- 需脱敏：飞书特定 JSON 结构
- 建议：保留"样式与业务解耦"原则，适配通用通知格式

### B-6: team-boss 通用总控路由 (M17, 19 分)
- 可产出：《AI 任务路由与分派协议》
- 需脱敏：具体团队注册表
- 建议：提取"意图识别→关键词匹配→加载技能→监督执行→播报"链路

### B-7: 系统白皮书 v8 (M18, 19 分)
- 可产出：方法论素材库（漂移分析、边界污染、扩展风险评估）
- 需脱敏：大量具体路径、数据库、配置
- 建议：只提取分析框架和判断标准，不搬运具体数字

### B-8: 角色记忆管线 (M12, 19 分)
- 可产出：《Agent 经验自动沉淀管线》
- 需脱敏：脚本路径、数据库名
- 建议：抽象为"注入→捕获→回填→审计"四步闭环

### B-9: 技能开发规范 (M13, 19 分)
- 可产出：《AI 技能开发宪法》
- 需脱敏：Hermes 特定元数据结构
- 建议：提取三层分层原则（标准/组件/业务）和依赖声明规范

### B-10: 系统规范入口 (M34, 19 分)
- 可产出：已脱敏的公开规范，可直接复用
- 风险：低，已是公开仓库
- 建议：扩写为完整的 playbook 章节

### B-11: 系统架构总览 (M07, 18 分)
- 可产出：《多团队 AI 系统架构模式》
- 需脱敏：团队名、群 ID、项目名

### B-12: 脱敏公开演示创建流程 (M11, 18 分)
- 可产出：《内部工具脱敏发布 SOP》
- 需脱敏：具体替换规则中的内部标识

### B-13: Weekly Audit 审计协议 (M14, 18 分)
- 可产出：《AI 系统周度审计协议》模板
- 建议：提取 drift 分类（hard/soft/snapshot）和审计检查清单

### B-14: 专题知识提炼工作流 (M15, 17 分)
- 可产出：《社区知识提炼流水线》
- 需脱敏：飞书 Wiki、具体脚本路径

### B-15: 项目结构规范 (M21, 17 分)
- 可产出：《AI 项目目录结构规范》

### B-16: 状态文件规范 (M23, 17 分)
- 可产出：《项目状态文件编写规范》

### B-17: 系统术语表 (M20, 16 分)
- 可产出：术语附录

### B-18: 模型调用基石规范 (M25, 16 分)
- 可产出：《多模型路由策略》
- 需脱敏：具体模型名称和 provider
- 建议：抽象为"默认/轻量/高阶"三层路由模型

### B-19: 命名规范 (M22, 15 分)
- 可产出：命名约定附录

### B-20: HTML-PPT-Video 流水线 (M32, 15 分)
- 可产出：《Agent 驱动的内容生产流水线》

### B-21: Hermes-OpenClaw 跨 Agent 协作 (M33, 15 分)
- 可产出：《跨 Agent 通信模式》
- 需脱敏：具体平台配置

---

## 6. C/D 类资产 (10-14 分)

### C-1: 项目备份规范 (M24, 14 分)
- 价值有限，偏运维细节
- 建议：如 playbook 涉及备份章节可简要引用

### C-2: EXPORT_MANIFEST (M26, 14 分)
- 纯统计报表，非方法论
- 建议：仅作为资产规模参考数据

### C-3: SECURITY_REDACTION_REPORT (M27, 14 分)
- 安全审计报告，非方法论
- 建议：提取"导出前安全扫描"原则作为附录

### C-4: hermes_overview v3-v6 (M28, 14 分)
- 历史版本，已被 v7/v7.0 替代
- 建议：不提炼，仅存档

### C-5: role_prompts.md (M29, 14 分)
- 角色提示词模板，偏具体实现
- 建议：提取"角色提示词结构模式"作为参考

### C-6: Pipeline 交付文档 (M30, 14 分)
- 特定产品的交付验证报告
- 建议：不提炼

### C-7: ROADMAP (M31, 12 分)
- 项目规划，非方法论
- 建议：不提炼

---

## 7. X 类禁止入仓

| 资产 | 原因 |
|------|------|
| 任何 `.db` 文件 (state.db, memory_store.db) | 含真实会话数据和凭证 |
| `.env` / `auth.json` / `config.yaml` 中的真实值 | 含 API 密钥、密码等 |
| `.hermes/hermes-agent/` 源码 | 核心系统代码，非方法论资产 |
| `.hermes/scripts/*.py` | 实现细节，含具体路径和凭证 |
| 各团队 `memory/` 目录 | 含用户私人经验和项目数据 |
| 飞书群 ID / chat_id | 个人隐私 |
| 奥学教育相关业务数据 | 商业机密 |
| 具体项目 STATE.md / progress.md | 项目状态，非通用方法论 |

---

## 8. 提炼建议 (按优先级)

### 第一批 (直接改写，高复用)
1. **三层架构治理理念** (M19) → playbook 序章/引言
2. **GitHub AI 协作四件套** (M08) → 核心方法论章节
3. **SSOT 与漂移校验** (M01) → 文档治理协议模板
4. **上下文注入协议** (M02) → Agent 上下文组装标准

### 第二批 (脱敏后改写)
5. **团队能力五层模型** (M03) → 能力成熟度评估工具
6. **达尔文棘轮优化** (M10) → 自主进化方法论
7. **对标升级工作流** (M09) → 标准驱动升级模板
8. **记忆纯度规范** (M05) → 记忆治理 SOP

### 第三批 (选择性提取)
9. **播报标准解耦原则** (M16) → 样式/业务分离模式
10. **路由分派链路** (M17) → 任务路由协议
11. **文章生命周期 SOP** (M06) → 内容生产流水线模板
12. **周度审计协议** (M14) → 系统健康检查模板

---

## 9. 需要总控裁决的问题

1. **业务关联度**: 奥学教育(Aoxue Edu)相关的技能和工作流是否纳入 playbook？当前判定为"高度领域特定"，建议排除，但需确认。

2. **脱敏级别**: M02 上下文注入协议涉及具体的脚本实现，playbook 应保留协议框架还是也需要示例代码？需裁决粒度。

3. **品牌关联**: 当前方法论是否保留 "Hermes" 品牌名，还是用通用名称（如 "AI Agent Governance Framework"）？这影响 M19 等公开文章的直接复用。

4. **版本选择**: hermes_overview 有 v3 到 v7.0 共 9 个版本，是否只需参考最新的 v7.0，历史版本完全忽略？

5. **公开边界**: hermes-system-spec-public 已是公开仓库，但其中的规范是否与内部 standards/ 同步？如不同步，以哪个为准？

6. **模型特定内容**: M25 模型调用规范中涉及具体的模型名称和 provider（阿里云百炼等），playbook 中是保留具体名称还是抽象为"模型层级"概念？

---

## 10. 下一步建议

1. **总控裁决**: 先解决第 9 节的 6 个问题，明确脱敏级别和品牌策略。

2. **A 类优先提炼**: 按第一批顺序，逐个将 A 类资产改写为 playbook 章节草稿。每个 A 类资产预计产出 1-2 页通用方法论文档。

3. **B 类分批处理**: 按脱敏难度排序，先处理低难度（M34 公开规范入口、M09 对标升级），再处理中难度（M04 团队边界、M05 记忆纯度），最后处理高难度（M18 白皮书、M02 上下文注入）。

4. **建立映射表**: 为每个 playbook 章节建立"源资产 → 提炼产物"的追溯映射表，方便后续版本更新时回溯。

5. **C/D 类归档**: 将 C/D 类资产标记为"参考素材"，不进入正式提炼流程，但保留索引以便将来需要时回溯。

6. **安全复查**: 所有提炼产物在入库前，需执行一次类似 SECURITY_REDACTION_REPORT 的安全扫描，确保无残留敏感信息。
