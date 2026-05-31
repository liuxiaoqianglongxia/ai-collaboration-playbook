# 发布资产路由计划 (Publishing Assets Routing Plan v1)

**项目**: maijian-wechat
**审计日期**: 2026-05-30
**控制器裁决 Q10**: 真实发布 ID 原件不入仓；只允许生成脱敏结构样例
**适用范围**: 所有 maijian-wechat 仓库中与发布流程相关的文件、脚本、数据、配置

---

## 1. 审计范围

| # | 资产类别 | 文件/目录 | 记录数(估) |
|---|---------|-----------|-----------|
| 1 | 发布 SOP | MANUAL_PUBLISH_V3_PLAN, WECHAT_LAYOUT_STANDARD, PUBLISHING_CALENDAR, PUBLISH_CONFIRMATION_CARD | 4 个 Markdown 文件 |
| 2 | preflight 脚本 | preflight_article_publish.py, preflight_canary_fast.py, preflight_cover_single.py, preflight_publish_bundle.py, preflight_release_v2_offline.py + 配套测试/运行脚本 | ~15 个 .py/.sh |
| 3 | render/preview 工具 | build_wechat_copy_workbench.py, run_wechat_copy_workbench.sh | 2 个脚本 |
| 4 | OpenWrite/Draco 工作台 | manual-publish-workbench/*.html, configs/wechat-style-story.yaml | ~10 个 HTML + 1 YAML |
| 5 | publish_map 设计 | PUBLISH_MAP_V2_DESIGN.md, PUBLISH_MAP_V2_VALIDATION_PLAN.md | 2 个 Markdown |
| 6 | publish_map 真实数据 | data/publish_map.jsonl | 2 条记录 |
| 7 | canary 运行结果 | canary-runs/mjw-20260518-ai-homework-canary-v1/, canary-runs/mjw-20260521-final-public-pack-v3-1/ | ~60 个文件(合计) |
| 8 | wechat-drafts payload | wechat-drafts/payloads/*.json, wechat-drafts-rich/payloads/*.json | ~32 个 JSON (16+16) |
| 9 | 飞书审稿链路 | FEISHU_REVIEW_LINK_V2_PLAN.md | 1 个 Markdown |
| 10 | 微信草稿箱 canary 策略 | WECHAT_DRAFT_CANARY_V2_PLAN.md | 1 个 Markdown |

**排除范围 (禁止读取)**: `.env`, `auth/`, `token*`, `db/`, 任何包含凭证/密钥/数据库连接的文件

---

## 2. 读取的安全文件

以下文件在本次审计中已安全读取或可安全读取（不含敏感凭证）：

| 文件路径 | 读取方式 | 敏感字段检查 |
|----------|---------|-------------|
| MANUAL_PUBLISH_V3_PLAN.md | 纯文本 | 无凭证 |
| WECHAT_LAYOUT_STANDARD.md | 纯文本 | 无凭证 |
| PUBLISHING_CALENDAR.md | 纯文本 | 无凭证 |
| PUBLISH_CONFIRMATION_CARD.md | 纯文本 | 无凭证 |
| scripts/preflight_*.py | Python 源码 | 无硬编码凭证 |
| scripts/test_preflight_*.py | Python 源码 | 无硬编码凭证 |
| scripts/run_*.sh | Shell 脚本 | 无硬编码凭证 |
| scripts/build_wechat_copy_workbench.py | Python 源码 | 无硬编码凭证 |
| scripts/run_wechat_copy_workbench.sh | Shell 脚本 | 无硬编码凭证 |
| configs/wechat-style-story.yaml | YAML 样式配置 | 无凭证 |
| PUBLISH_MAP_V2_DESIGN.md | 纯文本 | 无凭证 |
| PUBLISH_MAP_V2_VALIDATION_PLAN.md | 纯文本 | 无凭证 |
| FEISHU_REVIEW_LINK_V2_PLAN.md | 纯文本 | 无凭证 |
| WECHAT_DRAFT_CANARY_V2_PLAN.md | 纯文本 | 无凭证 |
| manual-publish-workbench/*.html | HTML 预览 | 无凭证 |
| data/publish_map.jsonl | **含真实 ID** | thumb_media_id, draft_media_id 等 -- 需脱敏 |
| wechat-drafts/payloads/*.json | **含真实 ID** | thumb_media_id=DRY_RUN_MEDIA_ID (已脱敏), 但含完整文章内容 |
| wechat-drafts-rich/payloads/*.json | **含真实 ID** | 同上 |
| canary-runs/*/* | **混合** | 部分文件含 thumb_media_id, draft_media_id, 部分已 sanitized |

---

## 3. 资产评分表

评分维度:
- **可复用性 (R)**: 1-5 分，是否可作为通用方法论复用到其他项目
- **安全敏感度 (S)**: 1-5 分，5 = 含真实 ID/凭证，1 = 完全公开安全
- **方法价值 (M)**: 1-5 分，是否包含值得沉淀的方法论/设计思想
- **工程价值 (E)**: 1-5 分，是否包含可复用的工程代码

| # | 资产 | R | S | M | E | 综合评级 |
|---|------|---|---|---|---|---------|
| 1 | MANUAL_PUBLISH_V3_PLAN | 4 | 1 | 5 | 2 | **A** -- 核心方法论 |
| 2 | WECHAT_LAYOUT_STANDARD | 4 | 1 | 4 | 2 | **A** -- 可通用化 |
| 3 | PUBLISHING_CALENDAR | 2 | 1 | 2 | 1 | **C** -- 项目专属 |
| 4 | PUBLISH_CONFIRMATION_CARD | 3 | 1 | 4 | 2 | **B** -- 模板有价值 |
| 5 | preflight_article_publish.py | 3 | 1 | 3 | 4 | **A** -- 可复用脚本 |
| 6 | preflight_canary_fast.py | 4 | 1 | 4 | 4 | **A** -- 核心脚本 |
| 7 | preflight_cover_single.py | 3 | 1 | 3 | 4 | **A** -- 可复用脚本 |
| 8 | preflight_publish_bundle.py | 3 | 1 | 3 | 4 | **A** -- 可复用脚本 |
| 9 | preflight_release_v2_offline.py | 3 | 1 | 3 | 4 | **A** -- 可复用脚本 |
| 10 | 配套测试/运行脚本 | 3 | 1 | 2 | 3 | **B** -- 辅助工具 |
| 11 | build_wechat_copy_workbench.py | 3 | 1 | 3 | 4 | **A** -- 可复用工具 |
| 12 | run_wechat_copy_workbench.sh | 3 | 1 | 2 | 3 | **B** -- 辅助工具 |
| 13 | OpenWrite/Draco HTML | 2 | 1 | 2 | 3 | **B** -- 模板参考 |
| 14 | wechat-style-story.yaml | 3 | 1 | 3 | 3 | **B** -- 样式配置可复用 |
| 15 | PUBLISH_MAP_V2_DESIGN | 4 | 1 | 5 | 1 | **A** -- 核心设计文档 |
| 16 | PUBLISH_MAP_V2_VALIDATION_PLAN | 4 | 1 | 4 | 1 | **A** -- 验证方法论 |
| 17 | data/publish_map.jsonl | 1 | **5** | 2 | 1 | **D** -- 含真实 ID |
| 18 | canary-runs 结果 | 1 | **4** | 3 | 2 | **D** -- 混合含真实数据 |
| 19 | wechat-drafts payloads | 2 | **4** | 3 | 1 | **D** -- 含完整文章内容+结构 |
| 20 | wechat-drafts-rich payloads | 2 | **4** | 3 | 1 | **D** -- 同上 |
| 21 | FEISHU_REVIEW_LINK_V2_PLAN | 4 | 1 | 5 | 1 | **A** -- 核心方法论 |
| 22 | WECHAT_DRAFT_CANARY_V2_PLAN | 4 | 1 | 5 | 1 | **A** -- 核心方法论 |

**评级说明**:
- **A 级**: 高可复用性 + 低敏感度 -- 优先进入 content-lab
- **B 级**: 中等价值 -- 脱敏后进入 content-lab 或进入 ai-collaboration-playbook
- **C 级**: 低复用性 -- 仅方法论摘要进入 ai-collaboration-playbook
- **D 级**: 高敏感度 -- 禁止入仓或必须脱敏

---

## 4. 各类别路由表

### 4.1 发布 SOP (类别 1)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| MANUAL_PUBLISH_V3_PLAN.md | **content-lab** (直接) | 全文入仓，无敏感内容 |
| WECHAT_LAYOUT_STANDARD.md | **content-lab** (直接) | 全文入仓，通用排版规范 |
| PUBLISHING_CALENDAR.md | **ai-collaboration-playbook** (方法版) | 提取日历治理方法论，项目专属细节不入库 |
| PUBLISH_CONFIRMATION_CARD.md | **content-lab** (直接) | 确认卡片模板，可复用 |

### 4.2 preflight 脚本 (类别 2)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| preflight_article_publish.py | **content-lab** (直接) | 通用发布前检查脚本 |
| preflight_canary_fast.py | **content-lab** (直接) | 核心 canary 脚本，方法论价值高 |
| preflight_cover_single.py | **content-lab** (直接) | 封面处理脚本 |
| preflight_publish_bundle.py | **content-lab** (直接) | 批量发布脚本 |
| preflight_release_v2_offline.py | **content-lab** (直接) | 离线发布脚本 |
| test_preflight_*.py | **content-lab** (直接) | 测试脚本随主脚本一起 |
| run_*.sh | **content-lab** (直接) | 运行脚本 |

### 4.3 render/preview 工具 (类别 3)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| build_wechat_copy_workbench.py | **content-lab** (直接) | 通用渲染工具 |
| run_wechat_copy_workbench.sh | **content-lab** (直接) | 随主工具一起 |

### 4.4 OpenWrite/Draco 工作台 (类别 4)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| manual-publish-workbench/*.html | **ai-collaboration-playbook** (方法版) | 仅保留 HTML 模板结构作为参考样例，去除具体文章内容 |
| configs/wechat-style-story.yaml | **content-lab** (直接) | 通用微信样式配置 |

### 4.5 publish_map 设计 (类别 5)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| PUBLISH_MAP_V2_DESIGN.md | **content-lab** (直接) | 核心设计文档，方法论价值极高 |
| PUBLISH_MAP_V2_VALIDATION_PLAN.md | **content-lab** (直接) | 验证方法论，可复用 |

### 4.6 publish_map 真实数据 (类别 6)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| data/publish_map.jsonl | **禁止入仓** -- 仅生脱敏结构样例 | 根据 Q10 裁决，真实发布 ID 原件不入仓。生成脱敏结构样例（将 media_id/draft_media_id/thumb_media_id 替换为占位符），样例进入 content-lab |

### 4.7 canary 运行结果 (类别 7)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| canary-runs/**/preview.html | **ai-collaboration-playbook** (方法版) | 保留结构作为预览效果参考 |
| canary-runs/**/*-sanitized.* | **content-lab** (直接) | 已脱敏文件可入仓 |
| canary-runs/**/*-summary.* | **content-lab** (直接) | 摘要/统计文件，无敏感 ID |
| canary-runs/**/v2-canary-fast-confirmation.* | **ai-collaboration-playbook** (方法版) | 确认流程模板 |
| canary-runs/**/final-dry-run*.json | **禁止入仓** -- 仅生成脱敏样例 | 含真实 draft_media_id/thumb_media_id |
| canary-runs/**/draft-add-publish-result.json | **禁止入仓** -- 仅生成脱敏样例 | 含真实 ID |
| canary-runs/**/draft-readback*.json | **禁止入仓** -- 仅生成脱敏样例 | 含真实 ID |
| canary-runs/**/validate_publish_map_*.txt | **本地保留** | 运行时验证日志，无长期方法价值 |
| canary-runs/**/cover_prompt*.md | **content-lab** (直接) | 封面 prompt 模板可复用 |

### 4.8 wechat-drafts payload (类别 8)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| wechat-drafts/payloads/*.json | **禁止入仓** -- 仅生成脱敏结构样例 | 含完整微信文章内容 + 文章结构，根据 Q10 不直接入仓 |
| wechat-drafts-rich/payloads/*.json | **禁止入仓** -- 仅生成脱敏结构样例 | 同上 |
| 脱敏结构样例 (待生成) | **content-lab** | 替换所有 media_id/thumb_media_id/draft_media_id 为占位符，保留 payload JSON schema 和字段注释 |

### 4.9 飞书审稿链路 (类别 9)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| FEISHU_REVIEW_LINK_V2_PLAN.md | **content-lab** (直接) | 审稿流程方法论，高复用价值 |

### 4.10 微信草稿箱 canary 策略 (类别 10)

| 文件 | 路由目标 | 处理方式 |
|------|---------|---------|
| WECHAT_DRAFT_CANARY_V2_PLAN.md | **content-lab** (直接) | canary 策略方法论，高复用价值 |

---

## 5. 分流建议

```
maijian-wechat 发布资产
├── content-lab (直接入仓)
│   ├── SOP: MANUAL_PUBLISH_V3_PLAN, WECHAT_LAYOUT_STANDARD, PUBLISH_CONFIRMATION_CARD
│   ├── preflight 脚本: 全部 .py + .sh (15 个文件)
│   ├── render 工具: build_wechat_copy_workbench.py + run_wechat_copy_workbench.sh
│   ├── 样式配置: configs/wechat-style-story.yaml
│   ├── publish_map 设计: PUBLISH_MAP_V2_DESIGN, PUBLISH_MAP_V2_VALIDATION_PLAN
│   ├── 飞书审稿: FEISHU_REVIEW_LINK_V2_PLAN
│   ├── canary 策略: WECHAT_DRAFT_CANARY_V2_PLAN
│   ├── canary 脱敏文件: *-sanitized.*, *summary.*
│   ├── 封面 prompt: canary-runs/**/cover_prompt*.md
│   └── 脱敏结构样例: publish_map 样例, draft payload 样例 (待生成)
│
├── ai-collaboration-playbook (方法论版)
│   ├── 发布日历方法论: 从 PUBLISHING_CALENDAR 提取治理模式
│   ├── HTML 模板参考: manual-publish-workbench/*.html 结构
│   ├── 预览参考: canary-runs/**/preview.html 结构
│   └── 确认流程模板: v2-canary-fast-confirmation.*
│
├── 本地保留 (不入库)
│   └── canary 运行验证日志: validate_publish_map_*.txt
│
└── 禁止入仓 (仅脱敏样例)
    ├── publish_map 真实数据: data/publish_map.jsonl
    ├── canary 含真实 ID 文件: final-dry-run*, draft-add*, draft-readback*, cover-upload-sanitized.json(含真实thumb)
    ├── wechat-drafts payloads: wechat-drafts/payloads/*.json
    └── wechat-drafts-rich payloads: wechat-drafts-rich/payloads/*.json
```

---

## 6. 需要总控裁决的问题

| # | 问题 | 影响范围 | 建议 |
|---|------|---------|------|
| Q1 | wechat-drafts payload 中的完整文章内容是否允许以脱敏形式 (保留文章结构但替换标题/内容为占位文本) 进入 content-lab 作为 JSON schema 参考？ | 类别 8 | 建议允许 -- 结构有价值，内容替换为 lorem ipsum |
| Q2 | canary-runs 中的封面图片路径 (cover_image_path 指向本地文件系统) 在脱敏样例中应如何处理？ | 类别 6, 7 | 建议替换为 `/path/to/cover.png` 占位符 |
| Q3 | publish_map.jsonl 中的 feishu_doc_url / feishu_doc_id 是否视为敏感信息？ | 类别 6 | 建议保留 URL 结构但替换 doc_id 为占位符 |
| Q4 | wechat_api_proxy 地址 (如 `http://172.23.128.1:7078`) 是否视为敏感基础设施信息？ | 类别 6, 7 | 建议替换为 `http://PROXY_HOST:PROXY_PORT` |
| Q5 | 脱敏样例文件的命名规范？ | 全局 | 建议 `*-sanitized-schema.json` / `*-structure-example.jsonl` |
| Q6 | PUBLISHING_CALENDAR.md 是否包含项目专属的排期信息 (日期/文章对应关系)？如果是，这些是否需要脱敏？ | 类别 1 | 建议提取方法论后，项目排期部分不入库 |
| Q7 | canary-runs 中已标记为 sanitized 的文件 (如 openai_provider_check_sanitized.json) 是否可以直接入仓而无需二次审查？ | 类别 7 | 建议总控确认后直接入仓 |
| Q8 | 路由计划 v1 本身是否需要版本管理，后续审计迭代如何追踪变更？ | 全局 | 建议在 content-lab 中建立 `routing/` 目录，按 v1/v2/... 版本管理 |

---

## 7. 下一步建议

### 7.1 立即执行 (P0)

1. **生成 publish_map 脱敏结构样例**
   - 基于 data/publish_map.jsonl 的 2 条记录
   - 替换: media_id, draft_media_id, thumb_media_id, feishu_doc_id, sha256, 本地路径, API 代理地址
   - 输出: `content-lab/publishing/publish-map-structure-example.jsonl`

2. **生成 draft payload 脱敏结构样例**
   - 从 wechat-drafts/payloads/ 任选 1 个文件
   - 替换: 所有 media_id 为占位符，文章内容替换为结构化占位文本
   - 保留: 完整 JSON schema, style 配置对象, articles 数组结构
   - 输出: `content-lab/publishing/draft-payload-structure-example.json`

3. **生成 canary 脱敏运行样例**
   - 从 canary-runs/ 中提取关键文件 (dry-run, confirmation, cover-upload)
   - 全面脱敏后输出为样例集
   - 输出: `content-lab/publishing/canary-run-example/`

### 7.2 短期执行 (P1)

4. **content-lab 入库**: 迁移所有 A 级和 B 级安全文件
5. **ai-collaboration-playbook 方法版**: 编写 PUBLISHING_CALENDAR 方法论摘要、HTML 模板参考文档
6. **路由计划 v2**: 根据总控对 Q1-Q8 的裁决更新本计划

### 7.3 中期执行 (P2)

7. **自动化脱敏流水线**: 编写脚本，自动从 maijian-wechat 提取 publish_map/draft payload 并生成脱敏样例
8. **定期同步机制**: 建立 maijian-wechat -> content-lab 的定期同步流程 (仅同步安全文件)
9. **审计日志**: 记录每次资产迁移的审计 trail

---

## 附录: 安全红线

以下信息在任何情况下 **不得** 以任何形式进入 content-lab 或 ai-collaboration-playbook:

- 真实 `media_id` / `draft_media_id` / `thumb_media_id` (微信 API ID)
- 真实飞书 `doc_id` / `doc_url` (完整链接)
- 任何 `.env` 文件内容
- 任何 token / API key / 凭证
- 数据库连接字符串
- 内部代理地址 (如 `172.23.128.1:7078`)
- 未脱敏的 sha256 值 (可保留哈希算法说明，但具体哈希值替换)
- 用户真实姓名 / 确认人信息

脱敏统一占位符规范:
- media_id: `"MEDIA_ID_PLACEHOLDER"`
- draft_media_id: `"DRAFT_MEDIA_ID_PLACEHOLDER"`
- thumb_media_id: `"THUMB_MEDIA_ID_PLACEHOLDER"`
- feishu_doc_id: `"FEISHU_DOC_ID_PLACEHOLDER"`
- 本地路径: `"/path/to/local/file"`
- API 代理: `"http://PROXY_HOST:PROXY_PORT"`
- sha256: `"SHA256_PLACEHOLDER"`
