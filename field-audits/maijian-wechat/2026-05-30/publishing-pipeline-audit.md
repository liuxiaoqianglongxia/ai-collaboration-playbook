# 麦尖WeChat 发布流水线审计

**日期**: 2026-05-30
**审计人**: Sub-agent C (只读审计)
**范围**: `/home/hermes/projects/maijian-wechat` 发布管线资产

---

## 1. 审计范围

| 目录/文件 | 读取级别 | 说明 |
|-----------|----------|------|
| `scripts/` | 全读 | 所有 .py 和 .sh 文件内容 |
| `wechat-drafts/` | 结构 + 字段名 | payload JSON 字段名，不输出真实 ID |
| `wechat-drafts-rich/` | 结构 + 字段名 | 同上 |
| `canary-runs/` | 结构 | 文件名列表，不读内容 |
| `manual-publish-workbench/` | 列表 + 用途 | 文件名 + 用途描述 |
| `data/publish_map.jsonl` | 字段名 + 状态分布 | 2 行，不输出真实 ID |
| `docs/` | 发布相关文档 | preflight, validate, release plans |
| `configs/` | 列表 + 用途 | YAML 配置 |
| `inbox/` | 列表 | 收件箱文件 |
| `prompts/` | 列表 | 封面提示词 |

---

## 2. 读取的安全文件

以下文件已被安全读取（不含 .env、auth、token、db 等敏感文件）：

### scripts/ (21 文件)

**Python 脚本 (11)**:

| 文件 | 用途 |
|------|------|
| `preflight_article_publish.py` | 单篇 Markdown 发布前结构检查：frontmatter、H1 数量、固定结尾、敏感词检测、allow_publish 校验 |
| `preflight_canary_fast.py` | Canary 快速测试前置检查：文章 preflight + 代理地址 + thumb_media_id 或封面图 |
| `preflight_cover_single.py` | 封面 prompt + manifest 校验：required phrases、SHA256、敏感词、MOCK 占位符 |
| `preflight_publish_bundle.py` | 组合门：publish_map JSONL + 单篇文章 preflight 双校验 |
| `preflight_release_v2_offline.py` | Release V2 离线门：检查必需文件是否存在、文档关键词、脚本无网络导入、无发布链字符串 |
| `validate_publish_map.py` | publish_map JSONL 全字段校验：21 个必需字段、状态枚举、状态依赖、SHA256、路径合法性 |
| `build_wechat_copy_workbench.py` | 从 Markdown 构建微信复制工作台 HTML（Draco / V2 两种样式） |
| `test_preflight_article_publish.py` | article preflight 单元测试 |
| `test_preflight_canary_fast.py` | canary fast preflight 单元测试 |
| `test_preflight_cover_single.py` | cover single preflight 单元测试 |
| `test_preflight_publish_bundle.py` | publish bundle preflight 单元测试 |
| `test_preflight_release_v2_offline.py` | release v2 offline gate 单元测试 |
| `test_validate_publish_map.py` | publish_map validator 单元测试 |

**Shell 脚本 (8)**:

| 文件 | 用途 |
|------|------|
| `run_canary_fast_preflight_tests.sh` | Canary fast preflight 冒烟测试 |
| `run_cover_single_tests.sh` | 封面 preflight 测试 |
| `run_manual_publish_tool_eval.sh` | 手动发布工具评估 |
| `run_publish_bundle_tests.sh` | Bundle preflight 测试（组合 map + article） |
| `run_publish_map_validation_tests.sh` | publish_map validator 测试 |
| `run_publish_preflight_tests.sh` | 文章 preflight 测试（含 5 个示例用例） |
| `run_release_v2_offline_tests.sh` | Release V2 离线门完整测试（含 bundle + cover） |
| `run_wechat_copy_workbench.sh` | 微信复制工作台构建脚本 |

### 读取的文档 (顶层)

| 文件 | 用途 |
|------|------|
| `RELEASE_PIPELINE_V2_ROADMAP.md` | V2 发布路线图，定义默认主路径、已完成底座、剩余大块、红线 |
| `FEISHU_REVIEW_LINK_V2_PLAN.md` | 飞书审稿链路设计：mock/dry-run 能力、C7 前禁止项 |
| `COVER_SINGLE_IMAGE_V2_PLAN.md` | 单张封面图链路：规格 900x383 / 2.35:1、Prompt 规范、流程 |
| `WECHAT_DRAFT_CANARY_V2_PLAN.md` | 微信草稿箱 Canary 计划：13 项前置条件、执行边界 |
| `PUBLISH_MAP_V2_DESIGN.md` | publish_map V2 设计：字段定义、状态枚举、校验策略 |
| `PUBLISH_MAP_V2_VALIDATION_PLAN.md` | publish_map 校验计划 |
| `MANUAL_PUBLISH_V3_PLAN.md` | V3 手动复制发布主路径（WeMD/doocs/md） |
| `PUBLISH_CONFIRMATION_CARD.md` | 发布确认卡模板：10 项强制确认项 |
| `PUBLISHING_CALENDAR.md` | 发布日历 |
| `PRODUCTION_CONSTITUTION.md` | 生产宪法（规则基线） |
| `WECHAT_LAYOUT_STANDARD.md` | 微信排版标准 |

---

## 3. 资产评分表

评分维度：内容价值、完整度、复用性、风险安全、归仓清晰度（各 1-5 分，满分 25）

| 资产 | 内容价值 | 完整度 | 复用性 | 风险安全 | 归仓清晰度 | 总分 | 等级 |
|------|----------|--------|--------|----------|------------|------|------|
| `scripts/preflight_article_publish.py` | 5 | 5 | 5 | 5 | 5 | **25** | A |
| `scripts/validate_publish_map.py` | 5 | 5 | 5 | 5 | 5 | **25** | A |
| `scripts/preflight_canary_fast.py` | 5 | 4 | 4 | 5 | 4 | **22** | A |
| `scripts/preflight_cover_single.py` | 4 | 4 | 4 | 5 | 4 | **21** | A |
| `scripts/preflight_publish_bundle.py` | 4 | 4 | 4 | 5 | 4 | **21** | A |
| `scripts/preflight_release_v2_offline.py` | 5 | 4 | 4 | 5 | 4 | **22** | A |
| `scripts/build_wechat_copy_workbench.py` | 4 | 3 | 4 | 5 | 3 | **19** | B |
| `scripts/test_*.py` (6 个) | 4 | 4 | 4 | 5 | 4 | **21** | A |
| `scripts/run_*.sh` (8 个) | 3 | 3 | 3 | 5 | 3 | **17** | B |
| `data/publish_map.jsonl` | 5 | 2 | 4 | 3 | 2 | **16** | B |
| `data/examples/` | 5 | 5 | 5 | 5 | 5 | **25** | A |
| `configs/wechat-style-story.yaml` | 4 | 4 | 4 | 5 | 4 | **21** | A |
| `wechat-drafts/` | 3 | 3 | 2 | 2 | 2 | **12** | C |
| `wechat-drafts-rich/` | 3 | 3 | 2 | 2 | 2 | **12** | C |
| `canary-runs/` | 3 | 2 | 2 | 2 | 2 | **11** | C |
| `manual-publish-workbench/` | 4 | 3 | 3 | 5 | 3 | **18** | B |
| `docs/` (发布相关) | 4 | 4 | 4 | 5 | 3 | **20** | A |
| `prompts/` | 3 | 3 | 3 | 5 | 3 | **17** | B |
| `inbox/` | 2 | 2 | 1 | 3 | 2 | **10** | C |

**关键发现**：
- Preflight 脚本质量极高（6 个 A 级），具备完善的单元测试、敏感词检测、状态依赖校验
- `wechat-drafts/` 和 `wechat-drafts-rich/` 包含真实发布结果（draft_media_id、thumb_media_id），建议脱敏后入仓或归档
- `canary-runs/` 包含大量运行态日志和中间产物，不应入仓

---

## 4. 发布前检查脚本

### 4.1 文章级 preflight (`preflight_article_publish.py`)

**检查项**：
- frontmatter 字段：title, author, digest, allow_publish
- H1 必须恰好 1 个
- H2 推荐 2-5 个
- 固定公众号结尾必须恰好 1 次
- 敏感词扫描：token, secret, api_key, access_token, cookie 等 12 项
- 发布危险词：publish-default, draft/add, api.weixin.qq.com 等
- allow_publish 必须为 false（除非 --allow-publish-true）
- cover_image 不能包含 media_id 类值
- 路径合法性检查（legacy path 映射）

**输出**：JSON 或文本，status=PASS/FAIL + findings 列表

### 4.2 publish_map 校验 (`validate_publish_map.py`)

**21 个必需字段**：
article_id, title, local_md_path, source_md_sha256, feishu_doc_url, feishu_doc_id, preview_html_path, preview_url, cover_prompt_path, cover_image_path, cover_image_sha256, thumb_media_id, dry_run_log_path, draft_media_id, status, current_stage, created_at, updated_at, confirmed_by, confirmation_card_path, notes

**22 个状态枚举**：
从 draft_finalized -> metadata_checked -> ending_checked -> local_preview_created -> dry_run_passed -> feishu_doc_created -> mapped -> feishu_review_confirmed -> preview_confirmed -> cover_prompt_ready -> cover_candidates_created -> cover_confirmed -> cover_uploaded -> final_dry_run_passed -> confirmation_card_ready -> c7_authorized -> draft_published -> draft_verified -> stopped_at_draft / blocked

**校验规则**：
- SHA256 格式（64 位 hex）
- ISO 8601 时间戳
- confirmed_by 必须为 "强哥" 或 null
- 状态依赖（如 draft_published 要求 draft_media_id 非空）
- MOCK_ 占位符仅允许在 examples 中出现
- article_id 不能重复
- 敏感词全字段扫描

### 4.3 Canary 快速 preflight (`preflight_canary_fast.py`)

**检查项**：
- 文章 preflight 必须 PASS
- wechat_api_proxy 必须提供且格式正确（http://host:port）
- 必须提供 thumb_media_id 或 cover_image_path（二者选一）
- 封面图必须为 png/jpg/jpeg/webp，>10KB
- H2 数量 2-6

### 4.4 封面 preflight (`preflight_cover_single.py`)

**检查项**：
- Prompt 必须包含：900x383, 2.35:1, negative space, no watermark, no qr code, no fake chinese text
- Manifest 必须包含 article_id, prompt_path, cover_image_path, cover_image_sha256, status
- status 必须为 cover_prompt_ready / cover_confirmed / cover_uploaded 之一
- SHA256 校验
- confirmed_by 必须为 "强哥" 或 null

### 4.5 Release V2 离线门 (`preflight_release_v2_offline.py`)

**安全检查**：
- 必需文件是否存在（6 个 MD + 2 个 example + 2 个脚本）
- 文档关键词检查（5 个文档各有必需术语）
- 脚本禁止网络导入（requests, urllib, http.client, aiohttp, lark_oapi）
- 脚本禁止发布链字符串（publish-default, draft/add, api.weixin.qq.com 等 9 项）

### 4.6 Bundle preflight (`preflight_publish_bundle.py`)

组合 publish_map 校验 + 文章 preflight 双门。

---

## 5. 本地渲染/预览脚本

### `build_wechat_copy_workbench.py`

- **输入**：本地 Markdown
- **输出**：手动发布工作台 HTML
- **样式**：Draco（默认）或 V2 两种渲染器
- **Draco 配置**：profile=doocs, theme=grace, render_mode=story, primary_color=vitality-orange, font_size=15, line_height=1.8
- **依赖**：`/home/hermes/.hermes/skills/draco/feishu-doc-to-wechat-draft/scripts/wechat_draft_publisher/renderer.py`

### `run_wechat_copy_workbench.sh`

调用 build_wechat_copy_workbench.py 的 shell 入口。

---

## 6. 微信草稿箱 Canary 记录

### `canary-runs/` 结构

包含 2 次 canary 运行记录：

1. **mjw-20260518-ai-homework-canary-v1/**
   - 50 个文件，包括：preflight 输出、article/bundle/cover 各阶段产物、dry-run payload、sanitized JSON log、preview HTML、validate 各阶段记录
   - 记录了完整的 canary 生命周期：preflight -> cover 生成 -> upload -> draft/add -> draft/get 回查
   - 包含 provider 诊断、格式差异审计等中间文件

2. **mjw-20260521-final-public-pack-v3-1/**
   - 15 个文件，包括：dry-run payload、多样式预览（style-a/b/c）、publish log、layout fix 预览
   - 包含样式对比报告（style-restore-report.md）

**安全注意**：canary-runs 包含 sanitized 日志和 dry-run 结果，可能残留脱敏不彻底的 ID 值。

---

## 7. Draco 样式资产

### `configs/wechat-style-story.yaml`

Draco 渲染器样式配置：
- caption_mode: hidden
- code_line_numbers: false
- code_theme: github
- font_size: 15
- footnote_links: true
- heading_style: solid
- heading_styles: h1=border-bottom, h2=solid, h3-h6=default
- hr_style: dash
- indent_first_line: false
- justify: false
- line_height: 1.8
- mac_code_block: true
- primary-color: '#FA5151'
- profile: doocs
- render_mode: default
- theme: grace

### `manual-publish-workbench/` Draco 预览

4 个 Draco 样式预览 HTML：
- `draco-original-style-preview.html` — 原始样式
- `draco-style-default.html` — 默认样式
- `draco-style-story-leftbar.html` — 故事 + 左侧栏
- `draco-style-story.html` — 故事样式

---

## 8. OpenWrite 工作台

**注**：未发现 OpenWrite 相关文件。`manual-publish-workbench/` 目录下是 Draco 渲染的本地 HTML 工作台，用于手动复制粘贴到微信公众号后台：

| 文件 | 用途 |
|------|------|
| `draft-ai-homework-draco-workbench.html` | Draco 渲染的 AI 作业草稿工作台 |
| `draft-ai-homework-v2-fallback.html` | V2 备用渲染 |
| `draft-ai-homework-workbench.html` | 主工作台 |
| `draft-gpt-subscription-company-workbench.html` | GPT 订阅公司工作台 |
| `squeeze-gpt-sop-workbench.html` | Squeeze GPT SOP 工作台 |
| `style-compare-report.md` | 样式对比报告 |

---

## 9. 飞书审稿链路

### 设计 (`FEISHU_REVIEW_LINK_V2_PLAN.md`)

**核心原则**：
- 飞书文档是协作/审稿层，不是发布层事实源
- 本地 Markdown 永远是发布层事实源
- 不得从飞书反向覆盖本地 Markdown
- 飞书通过后仍以本地 Markdown 进入预览/dry-run

**publish_map 回写字段**：feishu_doc_url, feishu_doc_id

**C7 前禁止**：
- 不真实创建/更新飞书文档
- 不读飞书抓回稿作为发布源
- 不调用 lark-cli docs +fetch / +create / +update

**风险**：跨租户 not found、lark-cli 权限、飞书文档压扁换行、飞书被误当最终稿、doc_id 与 local_md_path 映射错、source_md_sha256 不一致

### 运行时 (`docs/team-runtime-guide.md`)

- 活跃编制 8 个角色，publisher 负责飞书文档、预览、微信草稿准备
- 飞书是协作层，本地 Markdown 是生产层

---

## 10. 不应入仓的运行态发布结果

以下资产不应入仓（运行态中间产物）：

| 路径 | 原因 |
|------|------|
| `canary-runs/` | 运行态日志、dry-run payload、sanitized 日志、中间产物 |
| `wechat-drafts/publish-results.json` | **包含真实发布结果**（16 篇已发布文章的 draft_media_id、thumb_media_id、feishu doc URL） |
| `wechat-drafts/previews/` (15 HTML) | 运行态渲染预览 |
| `wechat-drafts-rich/previews/` (21 HTML) | 同上，包含 v2/local-preview/story-v2 等变体 |
| `previews/` | 本地预览 HTML（未审计，推测为运行态） |
| `backups/` | 备份文件（未审计） |
| `dry-runs/` | dry-run 输出（未审计） |
| `data/publish_map.jsonl` | 当前 2 行均为 stopped_at_draft 状态，含真实 ID，建议脱敏或入 example 模式 |

### `wechat-drafts/payloads/` 结构

16 个 JSON payload，字段：ok, command, dry_run, draft_media_id, payload, style, doc
- **包含真实 draft_media_id**

### `wechat-drafts-rich/payloads/` 结构

字段同上，与 wechat-drafts/ 结构一致

---

## 11. 分流建议

### 入仓（长期保留）

| 资产 | 理由 |
|------|------|
| `scripts/` 全部 | 高质量 preflight + 测试脚本，是发布管线的核心资产 |
| `configs/wechat-style-story.yaml` | 唯一官方样式配置 |
| `data/examples/` | 完善的示例和校验用例 |
| `docs/` 发布相关文档 | 设计文档、路线图、计划 |
| `PUBLISH_MAP_V2_DESIGN.md` 等 8 个顶层设计文档 | 核心设计文档 |
| `prompts/` | 封面视觉总纲和提示词模板 |

### 归档（保留但标注为历史产物）

| 资产 | 理由 |
|------|------|
| `wechat-drafts/` payloads + publish-results | 历史发布记录，建议脱敏后归档 |
| `wechat-drafts-rich/` payloads | 同上 |
| `manual-publish-workbench/` | 工作台 HTML 是中间产物，但 Draco 样式对比有参考价值 |

### 不入仓（运行态，定期清理）

| 资产 | 理由 |
|------|------|
| `canary-runs/` | 运行态日志，应定期清理或归档到外部存储 |
| `previews/` | 渲染输出，可从源文件重新生成 |
| `backups/` | 临时备份 |
| `drafts/` | 草稿文件 |
| `materials/` | 素材 |

---

## 12. 需要总控裁决的问题

1. **wechat-drafts/publish-results.json 是否脱敏入仓**：包含 16 篇已发布文章的真实 draft_media_id 和 thumb_media_id。建议：脱敏后作为历史记录入档，原始文件保留在运行目录。

2. **data/publish_map.jsonl 是否替换为 MOCK 示例模式**：当前 2 行均为真实 stopped_at_draft 记录，含真实 ID。建议：保留原始文件但添加 `.real.` 后缀，改用 `data/examples/publish_map.example.jsonl` 作为入仓模板。

3. **canary-runs 清理策略**：当前 2 次 canary 运行产生 65 个文件。建议：保留 sanitized 摘要，清理中间产物。

4. **wechat-drafts vs wechat-drafts-rich 重复问题**：两个目录结构几乎完全一致（同 16 个 payload），仅有 rich 版本多了几个 v2/story-v2 变体预览。建议：合并或明确区分定位。

5. **Draco 渲染器外部依赖路径**：`build_wechat_copy_workbench.py` 硬编码引用 `/home/hermes/.hermes/skills/draco/feishu-doc-to-wechat-draft/scripts/`，该路径不在本项目内。建议：将依赖版本化或提供 fallback。

6. **V2 API 链路与 V3 手动复制的关系**：V3 已将手动复制设为默认主路径，但 scripts/ 中仍有大量 V2 API 相关 preflight。建议：明确 V2 脚本的保留策略（降级为 canary/diagnostic 用途）。

---

## 13. 下一步建议

1. **脱敏处理**：对 `wechat-drafts/publish-results.json`、`data/publish_map.jsonl`、`wechat-drafts/payloads/` 进行脱敏（替换真实 media_id 为 MOCK_ 占位符）
2. **canary-runs 归档**：将 canary-runs 目录移到归档位置或压缩保存
3. **文档索引化**：为 `docs/` 目录创建索引文件，标注哪些是设计文档、哪些是运行记录
4. **统一样式配置**：将 Draco 外部依赖的样式配置（`configs/wechat-style-story.yaml`）与 Draco 内置默认的关系文档化
5. **添加 .gitignore 或 .arcrepo 排除**：对运行态目录（canary-runs、previews、backups、dry-runs）添加排除规则
6. **preflight 覆盖率扩展**：当前 preflight 主要检查结构，可增加内容质量检查（如敏感数据泄露检测、链接可达性验证）
7. **publish_map 状态回写规范**：当前 publish_map.jsonl 仅 2 行，建议补充状态流转的文档说明，确保每次 canary 后状态正确回写
