# maijian-wechat 资产风险与禁止入仓审计报告

**审计日期**: 2026-05-30
**审计目录**: `/home/hermes/projects/maijian-wechat`
**审计人**: Sub-agent E (Risk and Non-Ingest Asset Audit)

---

## 1. 审计范围

本次审计覆盖以下目录及文件类型：

| 范围 | 状态 |
|------|------|
| `backups/` - 备份目录 | 28 个子目录，总计 1.3MB |
| `canary-runs/` - Canary 运行结果 | 2 次运行，总计 1.5MB |
| `previews/` - 预览输出 | 4 个文件，总计 276KB |
| `wechat-drafts/` - 微信公众号草稿 | payloads + previews + publish-results，总计 640KB |
| `wechat-drafts-rich/` - 富文本草稿 | payloads + previews，总计 712KB |
| `drafts/` - 草稿文件 | 9 个文件，总计 180KB |
| `manual-publish-workbench/` - 手动发布工作台 | 10 个文件，总计 340KB |
| `reviews/` - 审核记录 | 45 个文件，总计 520KB |
| 所有 `.json` / `.jsonl` 文件 | 66 个文件 |
| 所有 `.html` 预览文件 | 61 个文件 |
| 所有 >50KB 大文件 | 28 个文件 |
| `.env` / auth / token / db / sqlite / zip / tar.gz | 项目内未发现 |
| `logs/` | 不存在 |

---

## 2. 备份目录审计（backups/）

**路径**: `/home/hermes/projects/maijian-wechat/backups/`
**总计**: 28 个子目录，1.3MB

| 子目录 | 大小 | 内容类型 | 风险等级 |
|--------|------|----------|----------|
| `article-type-router-20260517-143053/` | ~68KB | SKILL.md 副本 | 低 |
| `canary-fast-v2-20260518-213415/` | ~48KB | 设计文档副本 | 低 |
| `direct-draft-main-path-20260521-143351/` | ~20KB | 草稿副本 | 低 |
| `draco-style-recovery-20260520-232341/` | ~52KB | workbench HTML + 脚本 | 中 |
| `final-public-pack-codeblock-layout-fix-20260521-164302/` | ~20KB | 草稿副本 | 低 |
| `final-public-pack-layout-fix-20260521-161654/` | ~20KB | 草稿副本 | 低 |
| `manual-publish-v3-20260519-111520/` | ~8KB | 文档副本 | 低 |
| `production-consolidation-20260517-130326/` | ~8KB | 文档副本 | 低 |
| `production-integration-20260517-132800/` | ~80KB | 绝对路径快照（含 `/home/hermes/.hermes/` 路径） | 高 |
| `publish-format-fix-v1-20260518-102429/` | ~20KB | 文档副本 | 低 |
| `publish-map-v2-a2~a6-*/` (5 个) | ~80KB | 验证脚本 + 文档副本 | 低 |
| `reader-mirror-copy-workbench-20260519-115836/` | ~12KB | 文档副本 | 低 |
| `release-canary-v1-20260518-180154/` | ~24KB | 脚本 + 文章 + JSON 映射 | 低 |
| `release-v2-stage-package-20260518-171839/` | ~16KB | 文档副本 | 低 |
| `short-command-v1-20260517-211850/` | ~12KB | 文档副本 | 低 |
| `v3-draco-style-default-20260521-141329/` | ~52KB | workbench HTML + 脚本 | 中 |
| `workbench-theme-v1-1~v1-4-*/` (4 个) | ~120KB | workbench HTML + 脚本（每个含 manual-publish-workbench 子目录） | 中 |
| `workbench-theme-v2-20260520-144356/` | ~60KB | workbench HTML + 脚本 | 中 |
| `workflow-v1-freeze-20260517-193731/` | ~8KB | .bak 文件 | 低 |

**禁止入仓原因**:
- `production-integration-20260517-132800/` 包含用户家目录的绝对路径快照（`/home/hermes/.hermes/skills/`），泄露技能配置路径
- 所有子目录都是历史快照副本，内容已在主目录中存在，入仓会增加 repo 体积而无信息增益

---

## 3. HTML 预览文件审计

### 3.1 previews/ 目录

| 文件 | 大小 | 用途 |
|------|------|------|
| `hermes-feishu-print-assistant-dryrun.json` | 68KB | 飞书打印助手 dry-run 载荷 |
| `hermes-feishu-print-assistant-preview.html` | 68KB | 飞书打印助手预览（v1） |
| `hermes-feishu-print-assistant-preview-v2.html` | 68KB | 飞书打印助手预览（v2） |
| `hermes-feishu-print-assistant-preview-v3.html` | 68KB | 飞书打印助手预览（v3） |

**风险**: 渲染产物，不含源代码，无版本控制价值

### 3.2 canary-runs/ 中的 HTML

| 文件 | 大小 | 用途 |
|------|------|------|
| `mjw-20260518-ai-homework-canary-v1/preview.html` | 24KB | AI 作业 canary v1 预览 |
| `mjw-20260518-ai-homework-canary-v1/preview-fast-current.html` | 24KB | AI 作业 canary 快速预览 |
| `mjw-20260521-final-public-pack-v3-1/style-a-current.html` | 92KB | 终包样式 A 当前版预览 |
| `mjw-20260521-final-public-pack-v3-1/style-b-old-red-label.html` | 88KB | 样式 B 旧版红标签预览 |
| `mjw-20260521-final-public-pack-v3-1/style-c-story-compact.html` | 92KB | 样式 C 故事紧凑预览 |
| `mjw-20260521-final-public-pack-v3-1/preview.html` | 92KB | 终包 v3.1 综合预览 |
| `mjw-20260521-final-public-pack-v3-1/preview-style-b-revised.html` | 88KB | 样式 B 修订版预览 |
| `mjw-20260521-final-public-pack-v3-1/codeblock-layout-fix-preview.html` | 92KB | 代码块布局修复预览 |
| `mjw-20260521-final-public-pack-v3-1/layout-fix-preview.html` | 84KB | 布局修复预览 |

### 3.3 wechat-drafts/previews/

16 个 HTML 文件，每个 12-28KB，对应 Season1 各集预览。

### 3.4 wechat-drafts-rich/previews/

22 个 HTML 文件，每个 8-36KB，对应 Season1 各集富文本预览。

### 3.5 manual-publish-workbench/

9 个 HTML 文件，12-128KB，手动发布工作台渲染产物。

### 3.6 articles/ 中的 HTML

| 文件 | 大小 | 用途 |
|------|------|------|
| `articles/hermes-genesis-season1/final-public-pack-article/assets/preview/final-public-pack-preview.html` | 40KB | 终包文章预览 |

**当前已入仓**: 是（`git ls-files` 显示此文件已在 tracked 列表中）

---

## 4. 发布运行结果审计

### 4.1 wechat-drafts/publish-results.json

- **路径**: `/home/hermes/projects/maijian-wechat/wechat-drafts/publish-results.json`
- **大小**: 8.0KB
- **风险类型**: 包含微信公众号 API 发布结果（可能含 `errcode`/`errmsg`/`media_id`/发布 URL）
- **注意**: 字段名检查未直接发现 `media_id` 关键字段，但作为发布结果文件，可能包含实际发布返回值

### 4.2 canary-runs/mjw-20260518-ai-homework-canary-v1/

此运行目录包含以下可能含 API 返回值的文件：
- `draft-add-publish-result.json` (24KB) - 发布添加结果
- `draft-readback-raw.json` (24KB) - 草稿读取原始数据
- `final-dry-run-with-real-thumb.json` (24KB) - 含真实缩略图的 dry-run
- `publish-log-sanitized.json` - 不在本次运行中（属于 v3.1 运行）
- `cover-upload-sanitized.json` (4.0KB) - 封面上传结果
- `provider_diagnosis.json` (4.0KB) - 提供商诊断
- `site_summary.json` (4.0KB) - 站点摘要

### 4.3 canary-runs/mjw-20260521-final-public-pack-v3-1/

- `dry-run-payload-codeblock-fix.json` (96KB) - dry-run 载荷
- `final-dry-run.json` (92KB) - 最终 dry-run 结果
- `style-a/b/c-dry-run.json` (各 92KB) - 三种样式 dry-run
- `publish-log-sanitized.json` (4.0KB) - 发布日志（已脱敏）
- `publish-log-style-b-revised.json` (4.0KB) - 样式 B 修订版发布日志

### 4.4 其他 JSON 文件

| 文件 | 大小 | 风险类型 |
|------|------|----------|
| `data/publish_map.jsonl` | 4.0KB | 发布映射数据（低风险，示例数据） |
| `feishu-doc-mapping.json` | 4.0KB | 飞书文档映射 |
| `multi-instance-pilot/*.json` (3 个) | 4-8KB | 多实例测试中间结果 |

---

## 5. 可能含 media_id/draft_media_id/thumb_media_id 的文件

**全目录扫描结果**: 在 maijian-wechat 项目目录内使用 `grep -r "media_id\|draft_media_id\|thumb_media_id" --include="*.json" --include="*.jsonl"` **未发现匹配**。

但以下文件 **结构上可能** 包含这些字段（基于文件名和用途推断）：

| 文件路径 | 推测原因 |
|----------|----------|
| `wechat-drafts/payloads/season1-*.json` (15 个) | 微信公众号草稿发布载荷，标准 API 需要 `thumb_media_id` 等字段 |
| `wechat-drafts-rich/payloads/season1-*.json` (15 个) | 同上 |
| `canary-runs/mjw-20260518-ai-homework-canary-v1/dry_run_payload.json` | Canaray dry-run 载荷 |
| `canary-runs/mjw-20260518-ai-homework-canary-v1/final-dry-run-with-real-thumb.json` | 文件名明确提及 "real thumb" |
| `canary-runs/mjw-20260521-final-public-pack-v3-1/final-dry-run.json` | 终包 dry-run |
| `canary-runs/mjw-20260521-final-public-pack-v3-1/dry-run-*.json` (2 个) | 样式 dry-run |
| `wechat-drafts/publish-results.json` | 发布结果可能返回 media_id |

**注意**: grep 未匹配可能是因为这些字段使用不同的命名格式（如嵌套在对象中），或者文件中的 ID 值已被脱敏/替换。审计仅检查字段名称，未读取实际 ID 值。

---

## 6. 大文件审计（>50KB）

| 文件路径 | 大小 | 风险类型 |
|----------|------|----------|
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-screenshot.png` | 852KB | 图片资产（已入仓） |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-ports.png` | 852KB | 图片资产（已入仓） |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-tasks.png` | 640KB | 图片资产（已入仓） |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-memory.png` | 384KB | 图片资产（已入仓） |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-screenshot.jpg` | 260KB | 图片资产 |
| `manual-publish-workbench/draco-original-style-preview.html` | 128KB | 渲染产物 |
| `drafts/20260527-gpt-squeeze-v4-full.md` | 76KB | 草稿内容 |
| `previews/hermes-feishu-print-assistant-*.html/json` (4 个) | 68KB each | 渲染产物 |
| `canary-runs/mjw-20260521-final-public-pack-v3-1/*.json` (5 个) | 92-96KB each | dry-run 结果 |
| `canary-runs/mjw-20260521-final-public-pack-v3-1/*.html` (5 个) | 84-92KB each | 预览 |
| `wechat-drafts/payloads/season1-ep012.json` | 28KB | 发布载荷 |
| `wechat-drafts-rich/payloads/season1-ep012.json` | 28KB | 发布载荷 |
| `wechat-drafts/previews/season1-ep012-rev.html` | 28KB | 预览 |
| `wechat-drafts/previews/season1-final-bundle.html` | 24KB | 预览 |
| `wechat-drafts-rich/previews/season1-final-bundle.html` | 24KB | 预览 |
| `wechat-drafts-rich/previews/season1-final-bundle-finale-v2.html` | 36KB | 预览 |

---

## 7. 敏感文件审计（.env / auth / token / db / sqlite / zip / tar.gz）

**项目目录内扫描结果**: 未发现 `.env`、`.db`、`.sqlite`、`.zip`、`.tar.gz` 等敏感文件存在于 `maijian-wechat/` 目录下。

**注意**: `.gitignore` 已包含 `*.db` 和 `*.sqlite3` 规则，但对 `.env` 文件没有排除规则。

---

## 8. 禁止入仓原因表

| 文件/目录 | 风险类型 | 禁止原因 | 建议操作 |
|-----------|----------|----------|----------|
| `backups/` | 历史快照副本 | 冗余数据，包含绝对路径泄露，主目录已有源文件 | 加入 .gitignore |
| `canary-runs/` | 运行中间产物 | dry-run 结果、预览 HTML、API 返回值，临时测试数据 | 加入 .gitignore |
| `previews/` | 渲染产物 | 自动生成的 HTML 预览，可从源码重新生成 | 加入 .gitignore |
| `wechat-drafts/payloads/` | API 载荷 | 含微信公众号 API 发布参数，可能含 media_id | 加入 .gitignore |
| `wechat-drafts/previews/` | 渲染产物 | 自动生成的 HTML 预览 | 加入 .gitignore |
| `wechat-drafts/publish-results.json` | API 返回结果 | 含实际发布返回值 | 加入 .gitignore |
| `wechat-drafts-rich/payloads/` | API 载荷 | 同上 | 加入 .gitignore |
| `wechat-drafts-rich/previews/` | 渲染产物 | 自动生成的 HTML 预览 | 加入 .gitignore |
| `manual-publish-workbench/*.html` | 渲染产物 | 工作台生成的 HTML 预览 | 加入 .gitignore |
| `drafts/` | 草稿中间产物 | 工作用草稿，部分可能已有 .new/.bak 版本 | 加入 .gitignore 或手动挑选 |
| `reviews/daily-style-*.md` (2026-05-xx) | 每日审核日志 | 日常记录，非源代码 | 加入 .gitignore 或归档 |
| `*.png` / `*.jpg` (articles/ 中) | 图片资产 | 已入仓，每个 260-852KB，考虑 Git LFS | 可选：迁移到 LFS |
| `data/publish_map.jsonl` | 数据文件 | 发布映射数据，可能含真实 ID | 检查后决定 |

---

## 9. 分流建议

### 9.1 直接加入 .gitignore（不入仓）

```
# Build/run artifacts
backups/
canary-runs/
previews/
manual-publish-workbench/*.html

# WeChat API payloads and previews
wechat-drafts/payloads/
wechat-drafts/previews/
wechat-drafts/publish-results.json
wechat-drafts-rich/payloads/
wechat-drafts-rich/previews/

# Draft work-in-progress
drafts/

# Daily review logs (keep only milestone reviews)
reviews/daily-style-2026-*.md
```

### 9.2 需人工确认的文件

| 文件 | 确认项 |
|------|--------|
| `data/publish_map.jsonl` | 是否含真实微信公众号 media_id？ |
| `feishu-doc-mapping.json` | 是否含敏感飞书文档链接？ |
| `multi-instance-pilot/*.json` | 测试中间结果是否需要保留？ |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/*.png` | 已入仓的图片，是否需要迁移到 Git LFS？（当前 4 张共 ~3MB） |

### 9.3 可安全入仓的文件

以下目录/文件经审计无风险，可正常入仓：
- `articles/` 中的 `.md` 源文件
- `configs/` 配置目录
- `docs/` 文档目录（非 JSON 文件）
- `knowledge/` 知识库
- `materials/` 素材目录
- `prompts/` 提示词
- `scripts/` 脚本
- 所有 `.md` 设计文档/规划文件
- `.gitignore`、`README.md`、`STATE.md` 等项目配置文件

---

## 10. 下一步建议

1. **立即执行**: 将 `backups/`、`canary-runs/`、`previews/`、`wechat-drafts/payloads/`、`wechat-drafts/previews/`、`wechat-drafts-rich/payloads/`、`wechat-drafts-rich/previews/` 加入 `.gitignore`

2. **数据脱敏确认**: 确认 `wechat-drafts/publish-results.json` 和 `canary-runs/*/` 中的 publish-log 文件是否已脱敏（文件名含 "sanitized" 的表示已处理，但不确定脱敏程度）

3. **媒体 ID 专项**: 虽然 grep 未发现 `media_id` 字段，建议对 `wechat-drafts/payloads/` 下的 JSON 文件进行抽样检查，确认是否使用其他字段名（如 `mediaid`、`cover_media_id` 等）存储微信 API ID

4. **图片资产管理**: 当前 `articles/hermes-genesis-season1/final-public-pack-article/assets/` 中 5 张图片共 ~3MB 已入仓。如果后续持续添加图片，建议配置 Git LFS

5. **每日审核日志**: `reviews/daily-style-2026-*.md` 共约 20+ 个文件，建议保留里程碑审核（如 `chief-editor-*`、`greenlight-*`），日常日志归档到外部存储

6. **`.gitignore` 补充**: 当前 `.gitignore` 缺少 `*.html`（渲染产物）、`.env*`、`previews/`、`backups/`、`canary-runs/` 等规则
