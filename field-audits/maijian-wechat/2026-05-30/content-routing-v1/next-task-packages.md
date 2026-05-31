# 下一阶段任务包 — maijian-wechat 内容资产分流

**生成日期**: 2026-05-31
**前置**: maijian-wechat 250 文件资产审计 V1 + 内容资产分流计划 V1

---

## Task Package 1: content-lab-safe-ingest-v1

**目标**: 将 A 类低风险资产安全迁入 `maijian-wechat-content-lab`。

**入仓范围**:
- 生产规则文档: PRODUCTION_CONSTITUTION.md, HANDOFF_CONTRACT.md, WECHAT_LAYOUT_STANDARD.md, VALIDATED_WORKFLOW_V1.md
- 发布链路脚本: preflight_article_publish.py, preflight_canary_fast.py, preflight_cover_single.py, preflight_publish_bundle.py, preflight_release_v2_offline.py, validate_publish_map.py, build_wechat_copy_workbench.py
- 发布方案文档: MANUAL_PUBLISH_V3_PLAN.md, PUBLISH_MAP_V2_DESIGN.md, PUBLISHING_CALENDAR.md, COVER_SINGLE_IMAGE_V2_PLAN.md, RELEASE_PIPELINE_V2_ROADMAP.md, PUBLISH_CONFIRMATION_CARD.md, FEISHU_REVIEW_LINK_V2_PLAN.md, WECHAT_DRAFT_CANARY_V2_PLAN.md
- 封面 prompt: prompts/2026-04-22-season1-cover-brief.md, prompts/2026-04-22-season1-cover-prompts.md, visuals/2026-04-22-season1-cover-prompts-batch-{a,b,c}.md, visuals/2026-04-22-season1-cover-prompts-index.md
- 系列文章终稿 (需人工确认版本后迁入): season1-ep001~ep012.md, 2026-04-17-series-01~04.md, 2026-05-agent-truth-1~5.md, hermes-v7-principles-01~06.md, hermes-series-vol1~4.md, 麦尖-vol1~4.md, 20260528-squeeze-gpt-sop.md, cod-drop-02.md, ep-011.md, final-bundle.md

**禁止入仓**:
- 真实发布 ID (wechat-drafts/payloads/*.json, wechat-drafts-rich/payloads/*.json)
- HTML 文件
- 图片文件
- 备份目录
- Canary 运行结果
- 0 字节文件
- .new 中间态

**入仓前检查清单**:
- [ ] 确认 S1 v1/v2/v3 版本选择（Q1 裁决）
- [ ] 确认单实例系列主版本（Q2 裁决）
- [ ] 确认 GPT-squeeze 主版本（Q3 裁决）
- [ ] 确认麦尖 Vol vs agent-truth 策略（Q4 裁决）
- [ ] 确认 daily-style 精选（Q8 裁决）
- [ ] 确认 content-lab 仓库已存在或已创建
- [ ] 确认 .gitignore 已覆盖所有禁止类型

**预估工作量**: 2-3 小时

---

## Task Package 2: maijian-article-dedup-v1

**目标**: 对重叠文章版本建立主版本清单，不删除任何文件。

**去重组**:
1. DG-01: S1 v1/v2/v3 (~30 文件) — 主版本: v1 final (ep001~ep012.md)
2. DG-02: 单实例系列 4 变体 (7 文件) — 主版本: series-01~04 + cover-article-final
3. DG-03: GPT-squeeze 7-way (8 文件) — 需人工选择主版本
4. DG-04: 麦尖 Vol vs agent-truth (9 文件) — 主版本: 麦尖 Vol (适合公众号)
5. DG-05: hermes-system vs hermes-genesis (10 文件) — 两者保留，不同系列
6. DG-06: S1 final vs final-public-pack (2 文件) — 需人工确认权威版本
7. DG-07: S1 重写稿 vs public pack (~20 文件) — 主版本: v1 final + v3-1 pack

**输出**:
- 主版本清单 (canonical-versions-list.md)
- 归档建议清单 (archive-candidates.md)
- 需人工确认清单 (needs-human-review.md)

**禁止**: 不删除任何文件，不迁移任何文件。

**预估工作量**: 1-2 小时

---

## Task Package 3: maijian-publish-record-redaction-v1

**目标**: 对发布 ID 和 publish_map 做脱敏结构样例，不保留真实 ID。

**脱敏范围**:
- data/publish_map.jsonl (2 行真实记录)
- wechat-drafts/payloads/*.json (15 个)
- wechat-drafts-rich/payloads/*.json (15 个)
- canary-runs/*/*.json (含 dry-run payload)

**脱敏规则** (详见 redaction-policy.md):
- media_id → "REDACTED_MEDIA_ID"
- draft_media_id → "REDACTED_DRAFT_MEDIA_ID"
- thumb_media_id → "REDACTED_THUMB_MEDIA_ID"
- appid → "REDACTED_APPID"
- feishu_doc_url → "REDACTED_FEISHU_DOC_URL"
- feishu_doc_id → "REDACTED_FEISHU_DOC_ID"
- preview_url → "REDACTED_PREVIEW_URL"

**输出**:
- 脱敏后结构样例: `field-audits/maijian-wechat/2026-05-30/redacted-samples/`
- 脱敏脚本文档: `redaction-script.md`

**禁止**: 不读取真实 token，不输出真实 ID 值。

**预估工作量**: 1 小时

---

## Task Package 4: maijian-cleanup-v1 (可选)

**目标**: 清理明确无价值的文件（需人工确认后执行）。

**清理候选**:
- Batch 1 (安全): 0 字节文件 (3 个), .new 文件 (5 个), .bak 文件 (3 个) = 11 个
- Batch 2 (低风险): canary-runs/ (65 文件, 1.5MB), previews/ (4 文件, 276KB)
- Batch 3 (中风险): backups/ (28 目录, 1.3MB), HTML 工作台输出
- Batch 4 (需确认): 图片中间产物, 低价值占位稿

**总清理量**: ~90-200 文件, ~2-5MB

**禁止**: 未经人工确认不执行 Batch 3-4。

**预估工作量**: 30 分钟 - 2 小时
