# Knowledge Standards Value Audit v1

**日期**: 2026-05-30
**审计范围**: `/home/hermes/knowledge/standards/` 全部 18 个文件
**审计方法**: 逐文件读取，5 维度评分，对比现有 playbook 资产

---

## 1. 审计范围

审计目标为 Hermes 知识库中 18 个现行规范文件，评估其是否具备纳入 AI Collaboration Playbook 的价值。评分维度：

- **复用价值** (1-5): 能否成为通用模板/检查清单/协议
- **当前完整度** (1-5): 是否成熟、结构是否清晰
- **整合难度** (1-5): 分数越高 = 越容易整合进 playbook
- **风险程度** (1-5): 分数越高 = 越安全、无生产机密
- **业务相关度** (1-5): 与 AI 协作/微信/教育场景的契合度

分级：A=20-25, B=15-19, C=10-14, D=1-9, X=禁止入仓

---

## 2. 读取的安全文件

全部 18 个文件均为 `.md` 文本规范文件，不包含 .env、auth.json、数据库、日志或备份。读取安全。

| # | 文件 | 大小 |
|---|------|------|
| 00 | 00-system-overview.md | 307 行 |
| 01 | 01-terminology.md | 183 行 |
| 02 | 02-structure.md | 135 行 |
| 03 | 03-projects.md | 73 行 |
| 04 | 04-ports.md | 108 行 |
| 05 | 05-naming.md | 130 行 |
| 06 | 06-state-md.md | 181 行 |
| 07 | 07-teams.md | 150 行 |
| 07b | 07-project-backup.md | 134 行 |
| 08 | 08-file-cleanup.md | 189 行 |
| 09 | 09-project-sync-skill.md | 70 行 |
| 10 | 10-ssot-drift-gate.md | 112 行 |
| 11 | 11-model-foundation.md | 101 行 |
| 13 | 13-context-injection.md | 195 行 |
| 14 | 14-team-capability-framework.md | 222 行 |
| 15 | 15-team-registry-and-boundaries.md | 288 行 |
| 16 | 16-memory-purity-and-boundary.md | 238 行 |
| 17 | 17-article-lifecycle-sop.md | 152 行 |

注：缺少编号 12，registry.yaml 中也未列出。07 号出现两个文件（07-teams.md 和 07-project-backup.md），属于编号冲突。

---

## 3. 资产评分表

| 编号 | 文件 | 复用 | 完整 | 整合 | 风险 | 相关 | 总分 | 分级 |
|------|------|------|------|------|------|------|------|------|
| 00 | system-overview | 4 | 5 | 2 | 2 | 4 | **17** | B |
| 01 | terminology | 5 | 5 | 5 | 5 | 5 | **25** | A |
| 02 | structure | 5 | 5 | 5 | 5 | 4 | **24** | A |
| 03 | projects | 4 | 4 | 5 | 5 | 4 | **22** | A |
| 04 | ports | 3 | 4 | 2 | 3 | 3 | **15** | B |
| 05 | naming | 5 | 4 | 5 | 5 | 4 | **23** | A |
| 06 | state-md | 5 | 5 | 5 | 5 | 5 | **25** | A |
| 07 | teams | 4 | 4 | 4 | 4 | 4 | **20** | A |
| 07b | project-backup | 4 | 4 | 4 | 5 | 4 | **21** | A |
| 08 | file-cleanup | 4 | 4 | 3 | 3 | 3 | **17** | B |
| 09 | project-sync-skill | 4 | 3 | 3 | 3 | 3 | **16** | B |
| 10 | ssot-drift-gate | 5 | 5 | 5 | 5 | 5 | **25** | A |
| 11 | model-foundation | 2 | 3 | 2 | 4 | 3 | **14** | C |
| 13 | context-injection | 5 | 5 | 4 | 4 | 5 | **23** | A |
| 14 | team-capability-framework | 5 | 5 | 4 | 5 | 4 | **23** | A |
| 15 | team-registry-and-boundaries | 4 | 4 | 4 | 4 | 4 | **20** | A |
| 16 | memory-purity-and-boundary | 5 | 4 | 4 | 5 | 4 | **22** | A |
| 17 | article-lifecycle-sop | 4 | 3 | 3 | 4 | 3 | **17** | B |

**统计**: A=12, B=5, C=1, D=0, X=0

---

## 4. A 类资产 (12 个) - 可直接入 Playbook

### 4.1 01-terminology.md (25/25) -- 事实层/导航层/展示层三分法
**核心贡献**: 三层文档架构（事实层、导航层、展示层）及其冲突处理术语（漂移、纠偏）。
**入仓形式**: 作为 Playbook 的核心认知框架，定义"AI 协作系统中什么是真相"。
**已有对照**: Playbook 中无直接等价物。

### 4.2 06-state-md.md (25/25) -- STATE.md 11 字段规范
**核心贡献**: 项目状态摘要的 11 个必备字段模板，字段解释、常见错误、验证清单。
**入仓形式**: 作为 Playbook 的 `templates/PROJECT_STATE_TEMPLATE.md`。
**已有对照**: 部分概念在 `NEW_PROJECT_BOOTSTRAP.md` 中涉及，但无独立状态模板。

### 4.3 10-ssot-drift-gate.md (25/25) -- 唯一事实源与漂移校验
**核心贡献**: 4 道同步闸门（存在性、结构、一致性、准备），漂移定义，执行顺序。
**入仓形式**: 作为 Playbook 的 `checklists/SSOT_DRIFT_GATE.md`。
**已有对照**: Playbook 无等价物。

### 4.4 02-structure.md (24/24) -- 目录结构规范
**核心贡献**: 系统层/知识层/项目层三层职责划分，项目最小结构，查找顺序。
**入仓形式**: 作为 Playbook 的 `templates/PROJECT_STRUCTURE_TEMPLATE.md`。
**已有对照**: `NEW_PROJECT_BOOTSTRAP.md` 有类似内容但不够结构化。

### 4.5 05-naming.md (23/23) -- 命名规范
**核心贡献**: 短横线/全小写/英文规则，日期版本写法，验证脚本。
**入仓形式**: 作为 Playbook 的 `standards/NAMING.md` 或整合进项目规范。
**已有对照**: 无。

### 4.6 13-context-injection.md (23/23) -- 上下文注入规范
**核心贡献**: 三类事实包（项目型/团队型/系统型），system prompt 最小内容，主代理分派规则。
**入仓形式**: 作为 Playbook 的 `modules/CONTEXT_INJECTION_PROTOCOL.md`。
**已有对照**: Playbook 无等价物。

### 4.7 14-team-capability-framework.md (23/23) -- 五层团队能力模型
**核心贡献**: L1-L5 团队能力模型（目标/边界/产出/记忆/进化），6 种团队风格差异分析。
**入仓形式**: 作为 Playbook 的 `modules/TEAM_CAPABILITY_FRAMEWORK.md`。
**已有对照**: 无。

### 4.8 03-projects.md (22/22) -- 项目规范
**核心贡献**: 项目位置、结构、创建规则、判断规则、验证方法。
**入仓形式**: 与 02-structure 合并或独立为 `modules/PROJECT_STANDARD.md`。
**已有对照**: `NEW_PROJECT_BOOTSTRAP.md` 部分重叠。

### 4.9 16-memory-purity-and-boundary.md (22/22) -- 记忆纯度规范
**核心贡献**: 记忆层 vs 事实层分工，4 类允许内容，4 类禁止内容，归档建议。
**入仓形式**: 作为 Playbook 的 `modules/MEMORY_GOVERNANCE.md`。
**已有对照**: 无。

### 4.10 07-project-backup.md (21/21) -- 项目备份规范
**核心贡献**: 项目级 `backups/` 目录规范，命名规则，排除列表，清理策略。
**入仓形式**: 作为 Playbook 的 `checklists/BACKUP_STANDARD.md`。
**已有对照**: 无。

### 4.11 07-teams.md (20/20) -- 团队记忆规范
**核心贡献**: 团队目录职责边界，team-registry 与目录关系，验收标准。
**入仓形式**: 与 15-team-registry 合并为 `modules/TEAM_MEMORY_STANDARD.md`。
**已有对照**: 无。

### 4.12 15-team-registry-and-boundaries.md (20/20) -- 团队注册与边界
**核心贡献**: canonical team id 规范，team-registry 字段职责，漂移定义。
**入仓形式**: 与 07-teams 合并，作为 `modules/TEAM_REGISTRY_STANDARD.md`。
**已有对照**: 无。

---

## 5. B 类资产 (5 个) - 需脱敏/改造后入仓

### 5.1 00-system-overview.md (17/25)
**问题**: 包含 5 个飞书群 ID (`oc_xxxx`)、具体团队名称、具体项目进度等敏感信息。
**改造建议**: 提取架构图和分层结构作为通用模板，移除所有飞书群 ID、团队名、项目名。保留"总调度室 -> 多团队"架构模式。
**入仓形式**: 模板化后作为 `templates/MULTI_AGENT_ARCHITECTURE.md`。

### 5.2 08-file-cleanup.md (17/25)
**问题**: 提及 `.env`、`auth.json`、`auth.lock`、`channel_directory.json` 等系统文件。
**改造建议**: 抽象为通用文件治理原则（白名单模式、散落文件分类标签、先审计后治理），移除 Hermes 特定文件名。
**入仓形式**: `checklists/FILE_GOVERNANCE_STANDARD.md`。

### 5.3 17-article-lifecycle-sop.md (17/25)
**问题**: 包含具体项目路径 (`/home/liuxiaoqiang/projects/maijian-wechat/`)、具体技能名、17-article-lifecycle-sop.md 自身有 6 个"待确认项"未完成。
**改造建议**: 抽象为通用"内容生产 SOP"（素材 -> 大纲 -> 草稿 -> 审核 -> 发布 -> 锁定），移除具体路径，解决待确认项。
**入仓形式**: `templates/CONTENT_LIFECYCLE_SOP.md`。

### 5.4 09-project-sync-skill.md (16/25)
**问题**: 强依赖飞书同步流程，7 步工作流中多步涉及飞书文档。
**改造建议**: 将飞书替换为"展示层"抽象概念，保留"现场审计 -> 验证 -> 报告 -> 更新 -> 总览 -> 同步详情 -> 同步总览"流程逻辑。
**入仓形式**: `checklists/PROJECT_SYNC_PROTOCOL.md`。

### 5.5 04-ports.md (15/25)
**问题**: 端口编码规则 `XYZZ` 有用但高度系统特定（具体端口号、systemd 服务文件、Hermes Gateway）。
**改造建议**: 提取端口编码方案（类型/环境/序号）作为通用模板，移除具体端口号和 systemd 配置。
**入仓形式**: `templates/PORT_ALLOCATION_TEMPLATE.md`。

---

## 6. C/D 类资产 (1 个)

### 6.1 11-model-foundation.md (14/25) -- C 类
**问题**: 核心内容几乎全部绑定 `qwen3.6-plus`、`alibaba` provider、`hermes-gpt` 终端命令等系统特定配置。"续接口令"部分也是自然语言指令，不具备通用价值。
**改造建议**: 提取"模型调用策略"概念（默认模型、备用轻量模型、高阶判断隔离、跨 provider fallback 规则），重写为通用模板。当前版本不建议入仓。
**入仓形式**: 仅提取抽象层后可作为 `modules/MODEL_STRATEGY_STANDARD.md`。

---

## 7. X 类禁止入仓 (0 个)

无。全部 18 个文件均不涉及生产密码、API key、数据库凭证等绝对禁止共享的内容。

---

## 8. 分流建议

| 分流路径 | 文件 | 行动 |
|----------|------|------|
| **直接复制入仓** | 01, 02, 03, 05, 06, 10, 13, 14, 16 | 创建 playbook `standards/` 目录，直接放入 |
| **合并后入仓** | 07 + 15 (团队相关) | 合并为单一团队标准文档 |
| **脱敏后入仓** | 00, 08, 17 | 移除/泛化敏感信息，放入 `templates/` |
| **抽象后入仓** | 04, 09 | 提取通用逻辑，移除平台绑定 |
| **暂缓** | 11 | 重写后重新评估 |

### 与现有 Playbook 的重叠分析

| 现有 Playbook 文件 | 可能重叠的 standards | 结论 |
|---|---|---|
| `NEW_PROJECT_BOOTSTRAP.md` | 02-structure, 03-projects, 06-state-md | 可互补：现有侧重流程，standards 侧重规范 |
| `checklists/PRODUCTION_SAFETY_CHECK.md` | 07-project-backup, 08-file-cleanup | 可互补：安全 vs 治理不同维度 |
| `templates/CODEX_TASK_PACKAGE.md` | 13-context-injection | 可互补：任务打包 vs 上下文注入 |
| `checklists/*` 全部 | 10-ssot-drift-gate | 无重叠，新增 checklist |

---

## 9. 需要总控裁决的问题

1. **编号冲突**: 07 号同时存在 `07-teams.md` 和 `07-project-backup.md`，需要重新编号（建议 backup 改为 07b 或 12）。
2. **缺失编号 12**: registry.yaml 和文件列表中均无 12 号文件，确认是否已删除或遗漏。
3. **Playbook 目录结构**: 建议新增 `standards/` 子目录来收纳这些规范，与现有 `modules/`、`checklists/`、`templates/` 并列。
4. **00-system-overview 脱敏深度**: 该文件包含团队架构图。需要裁决：(a) 完全保留架构模式但删除所有实体名称，还是 (b) 仅保留"三层定义"概念作为 01-terminology 的补充？
5. **11-model-foundation 是否值得重写**: 当前版本价值极低，但"模型策略"概念（默认模型/轻量备用/高阶隔离/fallback 关闭）在其他多模型系统中可能有用。需要总控判断投入产出比。
6. **09-project-sync-skill 的飞书依赖**: 如果 Playbook 的定位是平台无关的 AI 协作规范，则该文件的"同步到飞书文档"步骤需要抽象化。

---

## 10. 下一步建议

1. **Phase 1 (立即)**: 将 12 个 A 类资产直接复制到 `playbook/standards/`，修正编号冲突。
2. **Phase 2 (本周)**: 对 5 个 B 类资产进行脱敏/抽象改造，完成后入仓。
3. **Phase 3 (视需要)**: 对 11-model-foundation 重写评估，决定是否投入。
4. **Phase 4 (持续)**: 建立 standards -> playbook 的同步机制，避免未来漂移。
5. **编号修正**: 建议重新编号序列为 00-17 无冲突、无缺失。

---

*审计完成: 18/18 文件已读取, 安全评分通过, 无禁止文件被访问*
