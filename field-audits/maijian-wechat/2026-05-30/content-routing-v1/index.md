# maijian-wechat 内容资产分流计划 V1

**审计日期**: 2026-05-31
**前置审计**: maijian-wechat 250 文件资产审计 V1
**审计报告分支**: `audit/maijian-wechat-250-asset-review-v1-20260530`
**本计划分支**: `audit/maijian-wechat-content-routing-plan-v1-20260530`
**子报告**: A (内容仓路由) / B (文章去重) / C (发布链路路由) / D (视觉封面路由) / E (脱敏策略) / F (清理候选) / G (任务包) / H (总索引)

---

## 1. 结论

**PASS**

- 250 个未提交文件全部完成分流规划
- 8 份子报告 + 1 份 TSV manifest 全部生成
- 未修改 maijian-wechat / private-repo / content-lab 中任何文件
- 未提交任何内容资产、HTML、JSON、图片、压缩包
- 未读取真实发布 ID、token、密钥
- Q1-Q10 总控裁决全部写入计划

---

## 2. 输入事实源

| 文件 | 来源分支 |
|------|----------|
| `index.md` | audit/maijian-wechat-250-asset-review-v1-20260530 |
| `git-inventory.md` | audit/maijian-wechat-250-asset-review-v1-20260530 |
| `article-assets-audit.md` | audit/maijian-wechat-250-asset-review-v1-20260530 |
| `publishing-pipeline-audit.md` | audit/maijian-wechat-250-asset-review-v1-20260530 |
| `visual-cover-assets-audit.md` | audit/maijian-wechat-250-asset-review-v1-20260530 |
| `risk-and-non-ingest-assets.md` | audit/maijian-wechat-250-asset-review-v1-20260530 |
| `private-repo-boundary-audit.md` | audit/maijian-wechat-250-asset-review-v1-20260530 |
| `raw-file-inventory.tsv` | audit/maijian-wechat-250-asset-review-v1-20260530 |

---

## 3. 总控裁决摘要

| 裁决 | 内容 |
|------|------|
| **Q1 S1 版本选择** | 正式入仓只选最终稿/已发布稿。v1/v2/v3 重写稿暂列 `drafts/archive/rewrite-candidates/` |
| **Q2 单实例系列去重** | 不删除文件。建立去重矩阵，推荐 series-01~04 + cover-article-final 为主版本 |
| **Q3 GPT-squeeze 7-way 去重** | 不删除文件。推荐 20260528-squeeze-gpt-sop.md (23KB, YAML FM) 为主版本，其余为实验样稿 |
| **Q4 麦尖 Vol vs agent-truth** | agent-truth = 主题系列，麦尖 Vol = 公众号栏目包装。保留麦尖 Vol 为公众号发布主版本 |
| **Q5 hermes-system vs hermes-genesis** | 两个独立系列，内容不重叠。hermes-system = 框架概念，hermes-genesis = S1 叙事系列。两者都保留 |
| **Q6 奥学教育业务文件** | 2026-enrollment-media-plan.md 和 2026-04-summer-ai-day-launch.md 含业务敏感信息，禁止入 content-lab |
| **Q7 仓库策略** | 使用现有 maijian-wechat-content-lab 作为内容仓。content-lab = 正式文章 + SOP + prompt；private-repo = 终稿 + 资料包；maijian-wechat = 历史工作区只读 |
| **Q8 daily-style** | 精选 3-5 篇代表性复盘进入 content-lab，其余留在 private repo 或本地归档 |
| **Q9 0 字节空文件** | 列为"可清理候选"，本轮不删除 |
| **Q10 真实发布 ID 脱敏** | 真实发布 ID 原件不入仓。只允许生成脱敏结构样例（REDACTED_* 占位符） |

---

## 4. 推荐分流总表

| 路由 | 数量 | 说明 |
|------|------|------|
| **content-lab 首批安全入仓** | ~65 项 | 正式文章 35 + 生产规则 4 + 发布脚本 7 + 封面 prompt 10 + 发布方案 8 + Draco 样式 1 |
| **private repo 保留** | ~45 项 | v2/v3 重写稿 26 + GPT54 草稿 12 + 内部策划 7 |
| **ai-collaboration-playbook 方法论** | ~15 项 | preflight 思路 + 发布 SOP + 工作流方法 |
| **仅本地保留** | ~85 项 | HTML 预览 60 + canary 结果 65 + 图片 23 + 备份 28 目录 |
| **禁止入仓** | ~46 项 | 发布 ID 30 + 备份 28 目录 + canary 65 + 中间态 9 |

---

## 5. content-lab 首批安全入仓候选

### 5.1 生产规则 (4 项)
- PRODUCTION_CONSTITUTION.md → `rules/production-constitution.md`
- HANDOFF_CONTRACT.md → `rules/handoff-contract.md`
- WECHAT_LAYOUT_STANDARD.md → `rules/wechat-layout-standard.md`
- VALIDATED_WORKFLOW_V1.md → `rules/validated-workflow-v1.md`

### 5.2 发布链路脚本 (7 项)
- preflight_article_publish.py → `scripts/preflight/article-publish.py`
- preflight_canary_fast.py → `scripts/preflight/canary-fast.py`
- preflight_cover_single.py → `scripts/preflight/cover-single.py`
- preflight_publish_bundle.py → `scripts/preflight/publish-bundle.py`
- preflight_release_v2_offline.py → `scripts/preflight/release-v2-offline.py`
- validate_publish_map.py → `scripts/validate/publish-map.py`
- build_wechat_copy_workbench.py → `scripts/tools/build-workbench.py`

### 5.3 发布方案/设计 (8 项)
- MANUAL_PUBLISH_V3_PLAN.md → `sop/manual-publish-v3.md`
- PUBLISH_MAP_V2_DESIGN.md → `sop/publish-map-v2-design.md`
- WECHAT_DRAFT_CANARY_V2_PLAN.md → `sop/canary-v2-plan.md`
- PUBLISHING_CALENDAR.md → `sop/publishing-calendar.md`
- COVER_SINGLE_IMAGE_V2_PLAN.md → `sop/cover-single-v2.md`
- RELEASE_PIPELINE_V2_ROADMAP.md → `sop/release-pipeline-v2.md`
- PUBLISH_CONFIRMATION_CARD.md → `sop/publish-confirmation-card.md`
- FEISHU_REVIEW_LINK_V2_PLAN.md → `sop/feishu-review-v2.md`

### 5.4 封面 prompt (10 项)
- prompts/2026-04-22-season1-cover-brief.md → `visuals/cover-brief.md`
- prompts/2026-04-22-season1-cover-prompts.md → `visuals/season1-cover-prompts.md`
- visuals/2026-04-22-season1-cover-prompts-batch-{a,b,c}.md → `visuals/batch-{a,b,c}.md`
- visuals/2026-04-22-season1-cover-prompts-index.md → `visuals/index.md`
- visuals/2026-04-17-series-prompts.md → `visuals/4-rules-prompts.md`
- visuals/2026-05-agent-series-prompts.md → `visuals/agent-series-prompts.md`

### 5.5 系列文章终稿 (35+ 项，需人工确认版本后迁入)
- Hermes Genesis S1: season1-ep001~ep012.md (12 篇)
- 单实例系列: series-01~04.md (4 篇)
- v7-principles: v7-principles-01~06.md (6 篇)
- hermes-system: vol1~4.md (4 篇)
- agent-truth/麦尖 Vol: agent-truth-1~5.md (5 篇)
- 独立精品文章: 20260528-squeeze-gpt-sop.md 等 (8 篇)

---

## 6. 暂缓入仓候选

| 类别 | 数量 | 说明 |
|------|------|------|
| S1 v2/v3 重写稿 | ~26 | season1-rewrite-v2/ 和 v3/ 目录，需裁决去留 |
| GPT-squeeze 变体 | ~7 | 7 个变体，需选择主版本 |
| daily-style 非精选 | ~20 | 25+ 篇 daily-style 中除精选 3-5 篇外的部分 |
| 未公开文章 | 若干 | 需人工确认是否公开 |
| 私有资料包 | 若干 | private-repo 中的 packages/ 和 release-candidates/ |
| 内部策划文档 | ~12 | docs/ 下的路线图、方向矩阵、排版升级等 |
| 审查报告非精选 | ~10 | reviews/ 中的非 daily-style 审查报告 |

---

## 7. 禁止入仓资产

| 类型 | 数量 | 风险 |
|------|------|------|
| 微信发布 ID (payload JSON) | 30 | 含 draft_media_id, thumb_media_id |
| 备份快照 (backups/) | 28 目录 | 历史副本，含用户路径快照 |
| Canary 运行结果 (canary-runs/) | 65 文件 | 含 dry-run payload + HTML 预览 |
| HTML 预览 | ~60 | 渲染输出，非源码 |
| 图片原件 | ~23 | 生成封面 + 文章配图 |
| 0 字节空文件 | 3 | EP011.md, FinalBundle.md, CodeDrop02.md |
| .new 中间态 | 5 | agent-truth-1~5.md.new |
| 时间戳备份 | 3 | .bak_* 文件 |
| 奥学教育业务文件 | 2 | 含品牌/运营敏感信息 |

---

## 8. 需要人工确认

| # | 问题 | 影响范围 |
|---|------|----------|
| C1 | S1 v1 是否确认为正式主版本？ | ep001~ep012, code-drop-01~03, final-bundle |
| C2 | GPT-squeeze 主版本选 v4-full (76KB) 还是 gpt-squeeze-final (23KB)？ | GPT-squeeze 系列 |
| C3 | agent-truth-5-viral-benchmark 是否独立于麦尖 Vol？ | agent-truth 系列 |
| C4 | S1 final vs final-public-pack 哪个仓库的版本更权威？ | final-bundle 版本选择 |
| C5 | daily-style 精选哪 3-5 篇？ | reviews/daily-style-*.md |
| C6 | 0 字节文件是否可以安全删除？ | EP011.md, FinalBundle.md, CodeDrop02.md |
| C7 | canary-runs/ 是否需要保留结构化摘要？ | canary 运行结果 |
| C8 | backups/ 中 production-integration 快照含用户路径，是否需要紧急清理？ | 隐私风险 |

---

## 9. 下一阶段建议

**推荐首选**: **content-lab-safe-ingest-v1**（Task Package 1）

理由：这是最直接的价值兑现路径。65+ 项低风险 A 类资产可以直接迁入 content-lab，不需要等待全部裁决完成——只需确认 S1 主版本后即可执行。

其他任务包按优先级排列：
1. content-lab-safe-ingest-v1 — 安全入仓
2. maijian-article-dedup-v1 — 去重清单
3. maijian-publish-record-redaction-v1 — 发布 ID 脱敏
4. maijian-cleanup-v1 — 清理候选（可选，需人工确认）

---

*本计划由 maijian-wechat 内容资产分流计划 V1 团队于 2026-05-31 生成。*
