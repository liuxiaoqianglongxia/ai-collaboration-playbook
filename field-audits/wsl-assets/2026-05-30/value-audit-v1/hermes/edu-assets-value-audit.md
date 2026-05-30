# 教育资产价值审计 v1

**审计日期**: 2026-05-30
**审计范围**: WSL2 环境下教育相关项目资产
**审计方式**: 只读分析，未读取任何 .db/.sqlite/.env/backup 内容
**审计人**: Hermes (AI Agent)

---

## 1. 审计范围

共审计 3 个项目仓库 + 0 个独立技能（预期技能不存在）：

| # | 资产标识 | 路径 | 类型 | 状态 |
|---|---------|------|------|------|
| 1 | aoxue-edu | `/home/hermes/projects/aoxue-edu/` | FastAPI + Vue3 + SQLite 教育管理系统 | 已封盘 (2026-04-29) |
| 2 | shanxi-edu-hot | `/home/hermes/projects/shanxi-edu-hot/` | Nuxt3 升学情报操作系统 | 开发中 (认证 BLOCKED) |
| 3 | taiyuan-schools-map | `/home/hermes/projects/taiyuan-schools-map/` | Flask + 高德地图 学校地图 | 数据维护期 |
| 4 | aoxue-edu-development skill | `~/.claude/skills/aoxue-edu-development/` | 自定义技能 | **不存在** |
| 5 | aoxue-feishu-query skill | `~/.claude/skills/aoxue-feishu-query/` | 自定义技能 | **不存在** |
| 6 | aoxue-data-query skill | `~/.claude/skills/aoxue-data-query/` | 自定义技能 | **不存在** |
| 7 | school-data-quality-fix skill | `~/.claude/skills/school-data-quality-fix/` | 自定义技能 | **不存在** |

注：`~/.claude/skills/` 下无教育相关自定义技能。预期中的 4 个教育技能均未创建。

---

## 2. 读取的安全文件

以下文件已安全读取（均为文档/配置，不含敏感数据）：

| 项目 | 文件 |
|------|------|
| aoxue-edu | `README.md`, `STATE.md` |
| shanxi-edu-hot | `README.md`, `CURRENT.md`, `docs/intelligence-operating-system-blueprint-v1.md` (前50行) |
| taiyuan-schools-map | `README.md`, `STATE.md` |

以下路径已列名但**未读取内容**：
- 所有 `.db` / `.sqlite` 文件（13个）
- 所有 `backups/` 子目录
- 所有 `logs/` 文件
- `aoxue_edu_production.db.bak.*` 备份文件

---

## 3. 资产评分表

评分维度：复用价值、当前完整度、整合难度、风险程度、业务相关度（各1-5分，总分25）

| 资产 | 复用价值 | 完整度 | 整合难度 | 风险程度 | 业务相关度 | 总分 | 级别 |
|------|---------|-------|---------|---------|-----------|------|------|
| aoxue-edu (代码+前端+后端) | 5 | 5 | 3 | 4 | 4 | 21 | **A** |
| aoxue-edu (生产DB+备份) | 2 | 5 | 5 | 5 | 2 | 19 | **B** |
| aoxue-edu (测试DB) | 1 | 3 | 2 | 1 | 1 | 8 | **D** |
| aoxue-edu (docs/ 文档) | 3 | 4 | 3 | 1 | 3 | 14 | **C** |
| aoxue-edu (scripts/ 运维脚本) | 4 | 4 | 3 | 1 | 3 | 15 | **B** |
| shanxi-edu-hot (Nuxt3代码) | 4 | 3 | 3 | 1 | 5 | 16 | **B** |
| shanxi-edu-hot (docs/ 蓝图) | 5 | 4 | 2 | 1 | 5 | 17 | **B** |
| shanxi-edu-hot (local-reports/ alerts) | 2 | 2 | 1 | 1 | 2 | 8 | **D** |
| taiyuan-schools-map (代码+数据) | 3 | 4 | 3 | 2 | 3 | 15 | **B** |
| taiyuan-schools-map (schools.db) | 1 | 3 | 3 | 4 | 1 | 12 | **C** |
| taiyuan-schools-map (reports/) | 2 | 3 | 1 | 1 | 2 | 9 | **D** |

---

## 4. A 类资产 (现实业务可用，总分20-25)

### 4.1 aoxue-edu 完整代码库（21分）

**定位**: 奥学教育管理系统 —— 培训机构内部 ERP

**业务可用性**: 极高。已实现完整闭环：
- 认证系统（API Key 分级、强制认证开关）
- 学员管理（档案、余额动态计算、点名记录）
- 订单/交易/退款流水
- 工资核算与发放
- 排课系统（循环排课）
- NL 自然语言查询（20+ 维度）
- 数据大屏与统计报表
- 双环境（开发/生产）部署
- 打包迁移能力（pack-aoxue.sh）
- 1289 项测试全部通过

**适合场景**: "培训机构老板自用系统" 的核心候选
- 学员管理、收费、排课、工资 —— 正好是教培机构核心运营需求
- 已封盘但未损坏，代码基线稳定

**风险**: 生产数据库 `aoxue_edu_production.db` 可能包含真实业务数据（学员信息、订单、工资），需脱敏后再进入公共仓

---

## 5. B 类资产 (15-19分)

### 5.1 shanxi-edu-hot 代码 + 蓝图（16-17分）

**定位**: 山西升学情报操作系统 —— 教培机构招生情报工作台

**现状**:
- 代码基座基于 wechat-article-exporter 扩展
- Nuxt3 全栈框架，端口 3118
- 已完成老板简报入口、多源采集框架
- 当前认证 BLOCKED（微信公众号采集接口认证失效）
- 39 篇设计文档，蓝图完整

**适合场景**: "培训机构老板自用系统" 的情报侧
- 招生政策监控、竞品动向、升学信息预警
- 与 aoxue-edu 互补：一个管内部运营，一个管外部情报

### 5.2 aoxue-edu scripts/ 运维脚本（15分）

- `start-all.sh` 一键双环境启动
- `pack-aoxue.sh` 打包迁移
- `scripts/bootstrap_local_admin.py` 管理员引导
- `scripts/ensure_core_indexes.py` 索引一致性
- 可直接复用于 shanxi-edu-hot 或新项目

### 5.3 aoxue-edu 生产 DB + 备份（19分）

**警告**: 含真实业务数据，属 X 类风险级别的业务资产
- `aoxue_edu_production.db` —— 生产库
- `aoxue_edu_production.db.bak.20260428_101901` —— 备份
- `backups/db/` 目录下的历史备份
- `backups/` 下 15 个业务修复备份（balance-drift、orphan-clean、salary-clean 等）

### 5.4 taiyuan-schools-map 代码+数据（15分）

**定位**: 太原市学校地图 —— 67 所学校位置可视化

**现状**: 功能完成，进入数据维护期
- Flask + 高德地图
- 67 所学校数据（初中31，高中36）
- 地图筛选、搜索、热力图、编辑/删除
- 每周自动数据验证

**适合场景**: 招生推广工具、家长咨询辅助

---

## 6. C/D 类资产 (历史封盘)

### 6.1 aoxue-edu docs/ 文档库（14分 - C类）

- 40+ 文档文件（审计报告、PRD、UI规范、排课方案等）
- `docs/progress.md` —— 完整开发日志
- `docs/PRD-v1.0.md` —— 产品需求文档
- `docs/database-schema-v1.0.md` —— 数据库schema
- `docs/local-use-foundation-plan.md` —— 本地使用方案
- 价值在于知识沉淀，可直接用于恢复开发

### 6.2 taiyuan-schools-map schools.db（12分 - C类）

- 学校位置数据库
- 数据与 `data/schools.json` 可能不一致
- 历史口径曾漂移（49 -> 149 -> 169 -> 67）

### 6.3 shanxi-edu-hot local-reports/ alerts（8分 - D类）

- 50+ 个 alert JSON 文件
- 采集运行日志，属临时运行态数据
- 无长期保留价值

### 6.4 taiyuan-schools-map reports/（9分 - D类）

- 2 份学校数据验证报告
- 2 份候选学校 JSON
- 属阶段性产物

### 6.5 aoxue-edu 测试数据库（8分 - D类）

- 7 个 test_*.db 文件
- 集成测试/调试用
- 无业务价值，可清理

---

## 7. X 类禁止入仓 (生产数据库、备份)

**以下路径绝对不可进入任何代码仓库**：

| 路径 | 说明 | 风险 |
|------|------|------|
| `aoxue-edu/aoxue_edu_production.db` | 生产数据库，含真实学员/订单/工资数据 | 极高 - 隐私泄露 |
| `aoxue-edu/aoxue_edu_production.db.bak.*` | 生产库备份 | 极高 - 隐私泄露 |
| `aoxue-edu/aoxue_edu_prod.db` | 可能为旧生产库 | 高 |
| `aoxue-edu/aoxue_edu.db` | 开发库（带真实数据） | 高 |
| `aoxue-edu/aoxue.db` | 旧数据库 | 中 |
| `aoxue-edu/app.db` | 旧数据库 | 中 |
| `aoxue-edu/backups/db/*` | 数据库备份目录 | 极高 - 历史全量数据 |
| `aoxue-edu/backups/*` | 15个业务修复备份 | 高 |
| `taiyuan-schools-map/schools.db` | 学校数据库 | 中 |
| `aoxue-edu/logs/*` | 日志文件 | 中 - 可能含敏感信息 |
| `aoxue-edu/test_*.db` | 测试数据库 | 低 - 但仍不应入仓 |

**建议**: 所有 `.db`, `.sqlite`, `.db-journal`, `logs/` 应加入 `.gitignore`（如果尚未加入）。

---

## 8. 分流建议

### 入 shanxi-edu-hot 仓库

| 资产 | 理由 |
|------|------|
| shanxi-edu-hot 代码 + docs/ | 本就是该仓库的一部分，继续在此维护 |
| shanxi-edu-hot 蓝图文档 | 核心业务定位文档，应保留 |

### 入 aoxue-edu 仓库

| 资产 | 理由 |
|------|------|
| aoxue-edu 代码（app/ frontend/ scripts/ tests/） | 完整产品，应保留在此仓库 |
| aoxue-edu docs/ 核心文档 | PRD、schema、审计报告等知识资产 |
| aoxue-edu pack-aoxue.sh / start-all.sh | 运维部署资产 |

### 仅本地保留 (不进任何仓库)

| 资产 | 理由 |
|------|------|
| 所有 .db / .sqlite 文件 | X类，生产数据泄露风险 |
| 所有 backups/ 目录 | X类，含历史全量数据 |
| 所有 logs/ 文件 | 运行态日志，无长期价值 |
| taiyuan-schools-map 代码+数据 | B类但独立产品，可本地维护，暂不入仓 |
| shanxi-edu-hot local-reports/ | D类，运行日志 |

### 需要考虑的新仓库

| 建议 | 理由 |
|------|------|
| shanxi-edu-hot 与 aoxue-edu 的"整合方案"文档 | 两者互补（内部ERP + 外部情报），可以 shanxi-edu-hot 的子模块或独立 repo 承载 |

---

## 9. 需要总控裁决的问题

### Q1: aoxue-edu 是否解封重启？
- 当前状态：已封盘 (2026-04-29)，100% 完成度
- 核心价值：培训机构 ERP 完整产品
- 裁决点：是否作为 "培训机构老板自用系统" 的核心产品继续开发？

### Q2: 生产数据库如何处理？
- `aoxue_edu_production.db` 可能包含真实学员/订单/工资数据
- 裁决点：是否需要脱敏后保留一份"干净"示例库用于演示/开发？

### Q3: taiyuan-schools-map 是否整合进 shanxi-edu-hot？
- 学校地图可作为升学情报的地理可视化补充
- 裁决点：是作为独立产品维护还是整合为 shanxi-edu-hot 的地图模块？

### Q4: 预期的 4 个教育技能为何不存在？
- `aoxue-edu-development`, `aoxue-feishu-query`, `aoxue-data-query`, `school-data-quality-fix` 均未在 `~/.claude/skills/` 中找到
- 裁决点：是否需要创建？还是这些能力已内嵌在项目文档中？

### Q5: aoxue-edu 的 40+ 篇文档如何精简？
- 大量审计报告、排期计划、修复方案分散在 docs/ 和根目录
- 裁决点：是否需要归档/精简到 docs/archive/，保留核心文档即可？

---

## 10. 下一步建议

### 立即行动 (本周)

1. **确认 .gitignore 覆盖**：确保所有 `.db`, `.sqlite`, `.db-journal`, `logs/`, `backups/`, `venv/`, `node_modules/` 已在两个仓库的 `.gitignore` 中
2. **生产数据备份**：将 `aoxue_edu_production.db` 额外备份到安全位置（非项目目录），然后从仓库工作区移除或加入 .gitignore
3. **aoxue-edu 解封评估**：如果确定要重启，需先解封服务 + 确认数据完整性 + 跑一次回归测试

### 短期行动 (2周内)

4. **文档精简**：将 aoxue-edu docs/ 归档为：
   - `docs/core/` —— PRD、schema、启动指南（保留）
   - `docs/archive/` —— 历史审计报告、排期计划（归档）
5. **shanxi-edu-hot 认证恢复**：当前 BLOCKED 在微信公众号采集认证，需优先解决
6. **技能创建评估**：确认是否需要创建预期的 4 个教育技能，或已有能力是否足够

### 中期行动 (1个月内)

7. **aoxue-edu + shanxi-edu-hot 整合方案**：设计两套系统的集成方案（ERP + 情报台 = 培训机构老板完整工作台）
8. **taiyuan-schools-map 维护策略调整**：改为 diff/report-first 模式，避免数据口径漂移
9. **清理测试数据库**：删除 7 个 test_*.db 文件，释放空间

---

*审计完成。所有判断基于只读分析，未修改任何文件。*
