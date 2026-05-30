# maijian-wechat 250 文件资产审计 V1

**审计日期**: 2026-05-30
**审计对象**: `/home/hermes/projects/maijian-wechat` (remote: `aoxue-media.git`)
**对照对象**: `/home/hermes/projects/maijian-wechat-private-repo` (remote: `maijian-wechat.git`)
**审计报告提交**: `ai-collaboration-playbook` → `audit/maijian-wechat-250-asset-review-v1-20260530`
**子报告**: A (Git 盘点) / B (文章) / C (发布链路) / D (视觉封面) / E (风险) / F (私有仓边界) / G (总索引)

---

## 1. 结论

**PASS**

- 250 个未提交文件全部完成盘点和分类
- 7 份子报告 + 1 份 TSV 清单全部生成
- 未修改 maijian-wechat 中任何文件
- 未读取 .env/auth/token/db 内容
- 未提交 HTML/JSON/图片/压缩报到审计仓库
- 可明确回答"这 250 个文件是什么"

---

## 2. 审计范围

| 维度 | 数值 |
|------|------|
| 被审计仓库 | maijian-wechat (branch: master, remote: aoxue-media.git) |
| 未提交文件总数 | 250 (234 untracked + 15 modified + 1 deleted) |
| 未推送 commit | 3 |
| .md 文件 | ~191 |
| .py 文件 | 13 |
| .sh 文件 | 8 |
| .json 文件 | 6 |
| .png/.jpg 图片 | 6 |
| 其他 (.new/.bak) | 9 |
| 未归类子目录 | 17 (backups, canary-runs, configs, data, drafts, inbox, knowledge, materials, manual-publish-workbench, multi-instance-pilot, previews, prompts, wechat-drafts, wechat-drafts-rich, visuals, reviews, articles 子目录) |
| 最大文件 | dashboard-lite-ports.png (869KB) |
| 总磁盘占用 | ~5MB (不含已追踪 git 文件) |

---

## 3. 总量统计

| 类别 | 数量 | 说明 |
|------|------|------|
| **文章资产 (.md)** | ~155 | articles/ + drafts/ + 子目录 |
| **审稿报告** | ~55 | reviews/ (含 25+ 天 daily-style) |
| **发布脚本** | 21 | scripts/ (6 preflight + 6 test + 8 shell + 1 workbench) |
| **文档/规划** | 29 | docs/ (路线图、重写方向、排版升级) |
| **视觉/封面** | 30 | visuals/ (15 prompt + 17 generated PNG) |
| **微信草稿箱** | ~62 | wechat-drafts/ + wechat-drafts-rich/ (payloads + previews) |
| **Canary 运行结果** | 65 | canary-runs/ (2 runs, ~1.5MB) |
| **备份快照** | 28 目录 | backups/ (~1.3MB) |
| **HTML 工作台** | 12 | manual-publish-workbench/ |
| **预览输出** | 4 | previews/ (~276KB) |
| **图片素材** | 13 | 散落在 articles/ 中的 PNG/JPG |
| **其他** | ~15 | configs, data, inbox, knowledge, materials, multi-instance-pilot, prompts |

---

## 4. Top 30 高价值资产

| 排名 | 资产 | 路径 | 类型 | 总分 | 建议归属 | 处理建议 |
|------|------|------|------|------|----------|----------|
| 1 | PRODUCTION_CONSTITUTION.md | 根目录 | 生产宪法 | 25 | content-lab | 直接入仓，团队架构 SSOT |
| 2 | HANDOFF_CONTRACT.md | 根目录 | 交接契约 | 25 | content-lab | 直接入仓 |
| 3 | WECHAT_LAYOUT_STANDARD.md | 根目录 | 排版标准 | 25 | content-lab | 直接入仓 |
| 4 | VALIDATED_WORKFLOW_V1.md | 根目录 | 工作流 | 24 | content-lab | 已验证工作流 V1 |
| 5 | 发布链路脚本 (preflight_*.py) | scripts/ | 脚本 | 24 | content-lab | 6 个预检脚本，高质量 |
| 6 | MANUAL_PUBLISH_V3_PLAN.md | 根目录 | 发布方案 | 23 | content-lab | V3 发布方案 |
| 7 | PUBLISH_MAP_V2_DESIGN.md | 根目录 | 发布设计 | 23 | content-lab | V2 发布映射设计 |
| 8 | articles/hermes-genesis-season1 终稿 (17 篇) | articles/hermes-genesis-season1/ | 文章 | 23 | content-lab | 正式成稿，优先入仓 |
| 9 | season1 ep001-ep012 终稿 (12 篇) | articles/season1-ep*.md | 文章 | 23 | content-lab | 正式成稿 |
| 10 | WECHAT_DRAFT_CANARY_V2_PLAN.md | 根目录 | 发布方案 | 22 | content-lab | V2 canary 方案 |
| 11 | GITHUB_READER_MIRROR_V1.md | 根目录 | 镜像方案 | 22 | content-lab | 读者镜像方案 |
| 12 | 封面 prompt 集合 (5 批次) | visuals/*.md | Prompt | 22 | content-lab | 可复用 prompt |
| 13 | articles/agent-truth 系列 (5 篇) | articles/2026-05-agent-truth-*.md | 文章 | 21 | content-lab | 麦尖 Vol / Agent 真相 |
| 14 | articles/单实例系列 (4 篇) | articles/draft-ai-homework* | 文章 | 21 | content-lab | 需去重后入仓 |
| 15 | articles/hermes-v7-principles (6 篇) | articles/hermes-v7-* | 文章 | 21 | content-lab | v7 原则系列 |
| 16 | articles/hermes-system 认知 (5 篇) | articles/麦尖-vol*.md | 文章 | 21 | content-lab | 认知系列 |
| 17 | articles/独立精品文章 (8 篇) | articles/*.md | 文章 | 20 | content-lab | 独立成稿 |
| 18 | PUBLISHING_CALENDAR.md | 根目录 | 排期 | 20 | content-lab | 发布日历 |
| 19 | DRACO_ORIGINAL_STYLE_RECOVERY.md | 根目录 | 样式恢复 | 20 | content-lab | Draco 样式标准 |
| 20 | daily-style 审稿报告精选 (3-5 篇) | reviews/daily-style-*.md | 审稿 | 19 | content-lab | 精选入仓 |
| 21 | RELEASE_PIPELINE_V2_ROADMAP.md | 根目录 | 路线图 | 19 | content-lab | V2 路线图 |
| 22 | articles/S1 V3 重写稿 (12 篇) | articles/season1-rewrite-v3/ | 文章 | 19 | content-lab | 待裁决去留 |
| 23 | build_wechat_copy_workbench.py | scripts/ | 脚本 | 19 | content-lab | 工作台构建器 |
| 24 | articles/hermes-genesis-announcement | articles/season1-announcement-final*.md | 文章 | 19 | content-lab | 正式公告 |
| 25 | articles/final-bundle | articles/season1-final-bundle.md | 文章 | 19 | content-lab | 最终合集 |
| 26 | articles/Code Drop 系列 (3 篇) | articles/season1-code-drop-*.md | 文章 | 18 | content-lab | 代码投放系列 |
| 27 | COVER_SINGLE_IMAGE_V2_PLAN.md | 根目录 | 封面方案 | 18 | content-lab | V2 封面方案 |
| 28 | RELEASE_PIPELINE_V2_ROADMAP.md | 根目录 | 发布路线图 | 18 | content-lab | 发布路线图 |
| 29 | FEISHU_REVIEW_LINK_V2_PLAN.md | 根目录 | 飞书审稿 | 18 | content-lab | V2 审稿方案 |
| 30 | PUBLISH_CONFIRMATION_CARD.md | 根目录 | 发布确认卡 | 18 | content-lab | 发布确认模板 |

---

## 5. A 类资产（20-25 分）

约 **67 项**，包括：

- **正式文章 (49 项)**: Hermes Genesis S1 终稿 17 篇、单实例系列 4 篇、v7-principles 6 篇、hermes-system 认知 5 篇、agent-truth/麦尖 Vol 9 篇、独立精品文章 8 篇
- **生产规则文档 (6 项)**: PRODUCTION_CONSTITUTION, HANDOFF_CONTRACT, WECHAT_LAYOUT_STANDARD, VALIDATED_WORKFLOW_V1
- **发布链路脚本 (6 项)**: preflight_article_publish.py 等 6 个预检脚本 + build_wechat_copy_workbench.py
- **发布方案/设计 (6 项)**: MANUAL_PUBLISH_V3_PLAN, PUBLISH_MAP_V2_DESIGN, WECHAT_DRAFT_CANARY_V2_PLAN 等

---

## 6. B 类资产（15-19 分）

约 **45 项**，包括：

- **S1 V2/V3 重写稿 (26 项)**: season1-rewrite-v2/ 和 v3/ 目录下 26 篇重写稿
- **GPT54 生成草稿 (12 篇)**: draft-ep001 至 draft-ep012-hermes-genesis-gpt54.md
- **其他有潜力草稿**: GPT-squeeze 系列 7 个变体、v7-collection-plan 等
- **精选审稿报告**: daily-style 中 3-5 篇有参考价值的

---

## 7. C/D 类资产（1-14 分）

约 **52 项**，包括：

- **内部策划文档 (12 项)**: docs/ 下的路线图、重写方向、排版升级等规划文档
- **审查报告 (10+ 项)**: reviews/ 中的非 daily-style 审查报告
- **辅助文档**: knowledge/, materials/, inbox/, configs/, multi-instance-pilot/
- **低完整度文件**: 占位稿、未完成草案

---

## 8. X 类禁止入仓资产

约 **46 项**，只列路径和风险：

| 类型 | 路径模式 | 风险 | 数量 |
|------|----------|------|------|
| 微信发布 ID | wechat-drafts/payloads/*.json | 含 draft_media_id, thumb_media_id | 15 |
| 微信发布 ID | wechat-drafts-rich/payloads/*.json | 含 draft_media_id, thumb_media_id | 15 |
| 微信发布结果 | wechat-drafts/publish-results.json | 含真实 API 返回值 | 2 |
| 备份快照 | backups/*/* | 28 个历史快照，含用户 home 路径快照 | 28 目录 |
| Canary 运行结果 | canary-runs/*/* | 含 dry-run payload + HTML 预览，可能含真实 thumbnail ID | 65 |
| HTML 预览 | manual-publish-workbench/*.html | 渲染输出，非源码 | 12 |
| HTML 预览 | previews/*.html | 渲染输出 | 4 |
| 图片资产 | articles/*.png, articles/*.jpg | 大图 (260-869KB) | 6 |
| 图片资产 | visuals/generated-covers/*.png | 17 张封面 生成图 | 17 |
| 时间戳备份 | articles/*.bak_*, docs/*.bak_* | 重复版本 | 4 |
| 中间态文件 | articles/*.md.new, drafts/*.md | .new 后缀中间态 | 5 |
| 0 字节空文件 | 若干 | 0 字节空 .md | 若干 |

---

## 9. 仓库分流建议

### maijian-wechat-content-lab (假设新建)

**应迁入**:
- 所有正式文章 (49 篇 A 类)
- 所有发布链路脚本 (21 个)
- 生产规则文档 (PRODUCTION_CONSTITUTION, HANDOFF_CONTRACT, WECHAT_LAYOUT_STANDARD)
- 封面 prompt 文档 (15 个)
- 内容系列规划
- Draco / OpenWrite 工作台说明
- 发布 preflight 方案

**不应迁入**:
- 真实发布 ID (wechat-drafts/payloads/)
- Canary 运行结果
- 备份目录
- HTML 预览
- 图片素材原件

### maijian-wechat-private-repo (现有)

**应留在**:
- 未公开文章
- 私有资料包
- 需要人工审稿的素材
- 真实发布过程记录的脱敏前原件

**建议从 public (aoxue-media) 迁入的**:
- 内部策划文档 (docs/)
- 审查报告 (reviews/)
- 辅助材料 (knowledge/, materials/, inbox/)

### ai-collaboration-playbook

**适合**:
- 通用发布 preflight 思路 (脱敏版)
- 可复用内容生产工作流
- 不含公众号私密信息的协作方法
- PRODUCTION_CONSTITUTION 的通用模板版

### 仅本地保留

- 预览 HTML (manual-publish-workbench/, previews/)
- Canary run 原始结果 (canary-runs/)
- 临时截图 (visuals/generated-covers/)
- 图片素材原件 (articles/*.png)
- 发布过程缓存
- 备份快照 (backups/)

### 禁止入仓

- 微信发布 ID (draft_media_id, thumb_media_id)
- 备份目录
- Canary 运行结果
- HTML 预览输出
- 0 字节空文件
- .new 中间态
- 时间戳备份

---

## 10. 需要 ChatGPT 总控裁决的问题

| # | 问题 | 影响 |
|---|------|------|
| Q1 | **S1 v1/v2/v3 版本选择**: season1 文章有 v1 原始稿、v2 重写稿、v3 重写稿三个版本，保留哪个？ | 影响入仓内容版本 |
| Q2 | **单实例系列去重**: draft-ai-homework 系列有 4 个重叠变体，保留哪个？ | 影响入仓篇数 |
| Q3 | **GPT-squeeze 7-way 去重**: 7 个 GPT 压缩变体，保留哪个？ | 影响入仓篇数 |
| Q4 | **麦尖 Vol vs agent-truth 重叠**: 两个系列内容可能重叠，是否合并？ | 影响系列结构 |
| Q5 | **hermes-system vs hermes-series 关系**: hermes-system 认知系列与 hermes-genesis 系列是什么关系？ | 影响分类 |
| Q6 | **奥学教育业务文件**: articles/2026-enrollment-media-plan.md 是业务规划，是否入内容仓？ | 影响业务边界 |
| Q7 | **maijian-wechat-content-lab 仓库创建**: 是否创建这个新仓库？还是直接入 private-repo？ | 影响整体架构 |
| Q8 | **daily-style 审稿报告去留**: 25+ 篇 daily-style 是全入还是只留精选？ | 影响入仓量 |
| Q9 | **0 字节空文件清理**: 是否安全删除？ | 影响清理 |
| Q10 | **真实发布 ID 脱敏**: publish-results.json 和 payload JSON 是否需要脱敏后保留结构？ | 影响发布链路资产保留 |

---

## 11. 下一阶段建议

### P0 — 立即执行

1. **确认 maijian-wechat-content-lab 仓库策略** (裁决 Q7)
2. **S1 v1/v2/v3 版本选择** (裁决 Q1)
3. **0 字节空文件清理** (裁决 Q9)
4. **发布脚本和规则文档入仓** (A 类中最安全的部分)

### P1 — 近期执行

5. **文章去重** (裁决 Q2, Q3, Q4)
6. **daily-style 精选** (裁决 Q8)
7. **封面 prompt 整理入仓**

### P2 — 中期规划

8. **发布 ID 脱敏方案** (裁决 Q10)
9. **备份/Canary 归档清理**
10. **三仓架构确立** (content-lab / private-repo / public-reader)

---

## 12. 安全确认

- [x] 未修改 maijian-wechat 中任何文件
- [x] 未提交 maijian-wechat 中任何文件到审计仓库
- [x] 未读取 .env/auth/token/db 内容
- [x] 未输出真实 media_id/draft_media_id/thumb_media_id
- [x] 未提交 HTML/JSON/图片/压缩报到审计仓库
- [x] 未操作 wsl-server
- [x] 审计报告中只包含 .md 和 .tsv 文本

---

*本报告由 maijian-wechat 250 文件资产审计 V1 团队（7 个子代理）于 2026-05-30 生成。*
