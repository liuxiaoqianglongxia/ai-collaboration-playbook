# 视觉与封面素材审计报告 — maijian-wechat

**日期**: 2026-05-30
**审计范围**: visuals/, prompts/ (视觉相关), previews/, 以及全 repo 图片文件
**审计人**: Sub-agent D (只读)

---

## 1. 审计范围

| 路径 | 类型 | 数量 |
|------|------|------|
| `visuals/*.md` | 封面 prompt 文件 | 13 |
| `visuals/generated-covers/*.png` | 已生成封面 PNG | 17 |
| `prompts/*.md` | 封面 prompt/brief | 2 |
| `previews/*.{html,json}` | HTML 预览 + JSON | 4 |
| 全 repo 图片 (*.png/*.jpg/*.webp) | 散落在 articles/ 的封面和截图 | 13 |

总计 49 个资产文件。

---

## 2. 读取的安全文件

以下 `.md` 文件被读取用于分类，不含敏感信息：

**visuals/ 目录 (13 个):**
- `visuals/2026-04-14-10min-file-gov-visual.md` — 早期文章配图方案（文件治理主题，含 Nano Banana 封面 prompt + 4 张内配图描述）
- `visuals/2026-04-14-system-upgrade-visual.md` — 系统规范升级复盘视觉方案（封面 + 2 内配图，机器人角色隐喻）
- `visuals/2026-04-17-cover-prompts.md` — 单/多实例对比文章封面（2 方案：全息沙盘 + 战术地图）
- `visuals/2026-04-17-norms-cover-prompts.md` — 规范注入文章封面（2 方案：对比图 + 数据注入流）
- `visuals/2026-04-17-norms-4-docs-prompts.md` — 4 个核心规范文档的配图 prompt（端口/状态/上下文/角色注入）
- `visuals/2026-04-17-series-prompts.md` — 4 条铁律系列封面 prompt（端口/STATE/上下文/角色注入脚本）
- `visuals/2026-04-22-season1-cover-prompts-batch-a.md` — Season 1 Batch A 封面（官宣 + EP001-004 + Code Drop 01，共 6 项）
- `visuals/2026-04-22-season1-cover-prompts-batch-b.md` — Season 1 Batch B 封面（EP005-009 + Code Drop 02，共 6 项）
- `visuals/2026-04-22-season1-cover-prompts-batch-c.md` — Season 1 Batch C 封面（EP010-012 + Code Drop 03 + Final Bundle，共 5 项）
- `visuals/2026-04-22-season1-cover-prompts-index.md` — Season 1 封面 prompt 总索引
- `visuals/2026-04-launch-images.md` — 4月招生启动视觉（公众号封面 + 抖音竖屏海报，非 Hermes 系列）
- `visuals/2026-05-agent-series-prompts.md` — Agent 实战系列封面 prompt（5 篇）

**prompts/ 目录 (2 个):**
- `prompts/2026-04-22-season1-cover-brief.md` — Season 1 封面视觉总纲/设计 brief（色系、材质、镜头感、禁止项、出图顺序）
- `prompts/2026-04-22-season1-cover-prompts.md` — Season 1 Cover Prompt Pack（17 篇，每篇 Google AI + Nano Banana 双版本）

**previews/ 目录 (4 个):**
- `previews/hermes-feishu-print-assistant-preview.html` — 飞书打印助手文章 HTML 预览
- `previews/hermes-feishu-print-assistant-preview-v2.html` — v2 版（内容相同）
- `previews/hermes-feishu-print-assistant-preview-v3.html` — v3 版（内容相同）
- `previews/hermes-feishu-print-assistant-dryrun.json` — 飞书打印助手 JSON 数据

---

## 3. 封面 Prompt 审计表

### 3.1 Season 1 系列（核心资产）

| 文件 | 条目数 | 风格 | 规格 | 质量评估 | 评分 |
|------|--------|------|------|----------|------|
| `prompts/2026-04-22-season1-cover-brief.md` | 设计 brief（非具体 prompt） | 暗色科技 + 编辑级 | 900x383 | 高。定义了全季视觉 DNA、色系、禁止项、出图顺序，是复用性最强的文件 | **A (22/25)** |
| `prompts/2026-04-22-season1-cover-prompts.md` | 17 篇（双版本） | 摄影/桌面写实 | 900x383 | 高。每篇 Google AI + Nano Banana 两套，含交付清单和阶段情绪映射 | **A (23/25)** |
| `visuals/2026-04-22-season1-cover-prompts-batch-a.md` | 6 项 | 暗色科技 + 编辑插画 | 900x383 | 高。含视觉 DNA 表、禁止项、整季连贯性检查 | **A (22/25)** |
| `visuals/2026-04-22-season1-cover-prompts-batch-b.md` | 6 项 | 科幻电影插画 | 900x383 | 高。核心意象、情绪描述完整，连续性检查表 | **A (22/25)** |
| `visuals/2026-04-22-season1-cover-prompts-batch-c.md` | 5 项 | 科幻电影插画 | 900x383 | 高。含 Final Bundle 收官设计 | **A (22/25)** |
| `visuals/2026-04-22-season1-cover-prompts-index.md` | 索引 | — | — | 中。仅链接文件，无独立内容 | **B (16/25)** |

### 3.2 早期/独立文章封面

| 文件 | 条目数 | 风格 | 质量评估 | 评分 |
|------|--------|------|----------|------|
| `visuals/2026-04-17-cover-prompts.md` | 2 方案 | 赛博朋克全息 | 中。有具体 prompt，但仅针对单篇文章 | **B (17/25)** |
| `visuals/2026-04-17-norms-cover-prompts.md` | 2 方案 | 赛博朋克 | 中。对比图+数据注入流 | **B (17/25)** |
| `visuals/2026-04-17-norms-4-docs-prompts.md` | 4 项 | 赛博朋克全息蓝图 | 中偏高。四张规范文档配图，统一风格 | **B (18/25)** |
| `visuals/2026-04-17-series-prompts.md` | 4 项 | 赛博朋克全息 | 高。4 条铁律系列，有使用说明和色彩表 | **B (19/25)** |

### 3.3 历史/低复用 Prompt

| 文件 | 条目数 | 分类 | 质量评估 | 评分 |
|------|--------|------|----------|------|
| `visuals/2026-04-14-10min-file-gov-visual.md` | 1 封面 + 4 内配图 | 历史专用 | 中。针对早期单篇文章，复用性低 | **C (14/25)** |
| `visuals/2026-04-14-system-upgrade-visual.md` | 1 封面 + 2 内配图 | 历史专用 | 中。复盘文档，内配图描述较详细但已过时 | **C (13/25)** |
| `visuals/2026-04-launch-images.md` | 2 项 | 文章专用 | 低。招生启动视觉，非 Hermes 主线，风格与其他不一致 | **C (12/25)** |
| `visuals/2026-05-agent-series-prompts.md` | 5 项 | 可复用系列 | 中偏高。Agent 实战系列，统一规范但条目较少 | **B (18/25)** |

---

## 4. 图片素材审计表

### 4.1 visuals/generated-covers/（已生成封面）

| 路径 | 大小 (bytes) | 格式 | 用途 |
|------|-------------|------|------|
| `visuals/generated-covers/season1-announcement-final-v2.png` | 12,539 | PNG | Season 1 官宣封面 |
| `visuals/generated-covers/season1-announcement-test.png` | 13,846 | PNG | 官宣封面测试版 |
| `visuals/generated-covers/season1-code-drop-01-foundation.png` | 15,859 | PNG | Code Drop 01 封面 |
| `visuals/generated-covers/season1-code-drop-02-workbench.png` | 16,326 | PNG | Code Drop 02 封面 |
| `visuals/generated-covers/season1-code-drop-03-role-memory.png` | 17,450 | PNG | Code Drop 03 封面 |
| `visuals/generated-covers/season1-ep001.png` | 8,708 | PNG | EP-001 封面 |
| `visuals/generated-covers/season1-ep002.png` | 9,154 | PNG | EP-002 封面 |
| `visuals/generated-covers/season1-ep003.png` | 12,092 | PNG | EP-003 封面 |
| `visuals/generated-covers/season1-ep004.png` | 11,593 | PNG | EP-004 封面 |
| `visuals/generated-covers/season1-ep005.png` | 8,600 | PNG | EP-005 封面 |
| `visuals/generated-covers/season1-ep006.png` | 9,708 | PNG | EP-006 封面 |
| `visuals/generated-covers/2026-04-22-season1-cover-prompts-batch-c.md` | — | — | (见上文) |
| `visuals/generated-covers/season1-ep007.png` | 9,872 | PNG | EP-007 封面 |
| `visuals/generated-covers/season1-ep008.png` | 8,918 | PNG | EP-008 封面 |
| `visuals/generated-covers/season1-ep009.png` | 10,173 | PNG | EP-009 封面 |
| `visuals/generated-covers/season1-ep010.png` | 9,298 | PNG | EP-010 封面 |
| `visuals/generated-covers/season1-ep011.png` | 10,861 | PNG | EP-011 封面 |
| `visuals/generated-covers/season1-ep012.png` | 8,379 | PNG | EP-012 封面 |
| `visuals/generated-covers/season1-final-bundle.png` | 9,917 | PNG | Final Bundle 收官封面 |

**统计**: 17 张 PNG，总大小约 203 KB。均为小尺寸草稿级封面（8-17 KB），分辨率可能较低或高度压缩。

### 4.2 articles/ 散落的图片

| 路径 | 大小 (bytes) | 格式 | 用途 |
|------|-------------|------|------|
| `articles/draft-ai-homework-cover-temp.png` | 4,532 | PNG | 草稿临时封面（非正式发布） |
| `articles/season1-code-drop-02-workbench.png` | 16,326 | PNG | 与 visuals/ 重复，同步副本 |
| `articles/season1-ep011.png` | 10,861 | PNG | 与 visuals/ 重复 |
| `articles/season1-ep012-cover.png` | 10,064 | PNG | 与 visuals/ 重复（命名略有不同） |
| `articles/season1-final-bundle.png` | 9,917 | PNG | 与 visuals/ 重复 |
| `articles/season1-rewrite-v3/ep001-cover.png` | 7,722 | PNG | rewrite-v3 分支封面 |
| `articles/season1-rewrite-v3/season1-ep011-cover.png` | 11,722 | PNG | rewrite-v3 分支封面 |
| `articles/season1-rewrite-v3/season1-ep012-cover.png` | 10,064 | PNG | rewrite-v3 分支封面 |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-memory.png` | 391,547 | PNG | Dashboard 截图（内存） |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-ports.png` | 868,733 | PNG | Dashboard 截图（端口） |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-screenshot.jpg` | 265,679 | JPG | Dashboard 截图（主界面） |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-screenshot.png` | 868,643 | PNG | Dashboard 截图（主界面 PNG） |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/dashboard-lite-tasks.png` | 652,496 | PNG | Dashboard 截图（任务） |

**统计**: 13 张图片。其中 4 张是 visuals/ 的副本（重复），3 张是 rewrite-v3 分支的版本（可能过时），4 张是 draft-ai-homework 临时封面，4 张 Dashboard 截图是真正的大图资产（256KB-868KB）。

---

## 5. HTML 预览文件审计

| 文件 | 大小 (bytes) | 格式 | 用途 | 评分 |
|------|-------------|------|------|------|
| `previews/hermes-feishu-print-assistant-preview.html` | 66,784 | HTML | 飞书打印助手文章微信排版预览 | **B (16/25)** |
| `previews/hermes-feishu-print-assistant-preview-v2.html` | 66,784 | HTML | v2 版（与 v1 大小相同，内容可能相同） | **B (15/25)** |
| `previews/hermes-feishu-print-assistant-preview-v3.html` | 66,943 | HTML | v3 版（略大，可能微调） | **B (15/25)** |
| `previews/hermes-feishu-print-assistant-dryrun.json` | 67,561 | JSON | 飞书打印助手 JSON 数据/配置 | **B (15/25)** |

**观察**: 3 个 HTML 文件大小几乎相同，说明版本间差异极小。建议合并为单一文件，用 git tag/branch 管理版本。

---

## 6. 可复用 vs 历史 vs 专用 Prompt 分类

### 6.1 可复用 Prompt（应保留并迁移到中央仓库）

| 文件 | 原因 |
|------|------|
| `prompts/2026-04-22-season1-cover-brief.md` | 全季视觉 DNA 定义，可迁移为后续季的设计系统 |
| `prompts/2026-04-22-season1-cover-prompts.md` | 17 篇双版本 prompt，格式统一，可直接用于生图管线 |
| `visuals/2026-04-22-season1-cover-prompts-batch-{a,b,c}.md` | Season 1 分批 prompt，含完整禁止项和连贯性检查 |
| `visuals/2026-05-agent-series-prompts.md` | Agent 系列统一规范，有复用价值 |

### 6.2 历史 Prompt（已过时或不再活跃使用）

| 文件 | 原因 |
|------|------|
| `visuals/2026-04-14-10min-file-gov-visual.md` | 早期文章，已被 Season 1 系列取代 |
| `visuals/2026-04-14-system-upgrade-visual.md` | 复盘文档，含机器人隐喻与后续风格不兼容 |
| `visuals/2026-04-launch-images.md` | 招生启动视觉，与 Hermes 主线风格割裂 |
| `visuals/2026-04-22-season1-cover-prompts-index.md` | 纯索引，可合并到 README |

### 6.3 专用 Prompt（文章级，复用性有限但有参考价值）

| 文件 | 原因 |
|------|------|
| `visuals/2026-04-17-cover-prompts.md` | 单篇文章封面，赛博风格与 Season 1 不一致 |
| `visuals/2026-04-17-norms-cover-prompts.md` | 单篇文章，风格过渡期 |
| `visuals/2026-04-17-norms-4-docs-prompts.md` | 4 个规范文档配图，统一风格但用途窄 |
| `visuals/2026-04-17-series-prompts.md` | 4 条铁律系列，比单篇好但不如 Season 1 完整 |

---

## 7. 分流建议

### 7.1 保留并归档（高价值）

- `prompts/2026-04-22-season1-cover-brief.md` → 迁移为 `visuals/design-system/` 设计系统文件
- `prompts/2026-04-22-season1-cover-prompts.md` → 保留为 prompt 包主文件
- `visuals/2026-04-22-season1-cover-prompts-batch-{a,b,c}.md` → 保留为批次文件
- `visuals/generated-covers/` 全部 17 张 → 保留（虽然小但已是可用封面）

### 7.2 合并或清理（低价值/重复）

- `articles/` 下与 `visuals/generated-covers/` 重复的 4 张 PNG → **删除**，使用 visuals/ 的单一副本
- `previews/` 中 3 个几乎相同的 HTML → **保留最新 v3，删除 v1/v2**（或用 git 管理版本）
- `articles/draft-ai-homework-cover-temp.png` → 4.5 KB 草稿，确认是否还需要，可**删除**
- `visuals/2026-04-22-season1-cover-prompts-index.md` → 纯索引，**合并到 README 或删除**
- `visuals/2026-04-launch-images.md` → 非主线业务，**归档到 backups/** 或删除

### 7.3 重命名/重组

- `visuals/2026-04-17-*.md`（4 个文件）风格介于赛博朋克和 Season 1 之间，建议：
  - 如不再使用 → 移入 `backups/`
  - 如仍有参考值 → 合并为一个 `visuals/2026-04-early-covers.md`

---

## 8. 需要总控裁决的问题

1. **风格分裂**: 项目存在三套视觉风格体系——
   - 早期（2026-04-14）：机器人隐喻，Nano Banana 英文 prompt
   - 过渡期（2026-04-17）：赛博朋克全息风格
   - 成熟期（2026-04-22+）：暗色科技+编辑级摄影，Draco/Nano Banana 双版本
   建议统一采用成熟期风格，废弃早期/过渡期文件。

2. **图片重复**: articles/ 下有 4-7 张与 visuals/ 重复的封面 PNG。是否确认删除副本？

3. **预览版本膨胀**: previews/ 中 3 个 HTML 文件大小几乎相同（66,784 / 66,784 / 66,943 bytes），内容疑似相同。是否确认只保留 v3？

4. **非主线资产**: `visuals/2026-04-launch-images.md` 是招生启动视觉（抖音/公众号），与 Hermes AI 产品线无关。是否归档到独立项目目录？

5. **Dashboard 截图**: `articles/hermes-genesis-season1/final-public-pack-article/assets/` 下 5 张大图（总约 3 MB）是 Dashboard Lite 产品截图。是否需要保留？是否考虑压缩为 webp？

6. **rewrite-v3 封面**: `articles/season1-rewrite-v3/` 下 3 张封面是否与 visuals/ 最终版一致？如一致可删除分支副本。

---

## 9. 下一步建议

1. **去重**: 删除 articles/ 下与 visuals/generated-covers/ 重复的封面 PNG
2. **合并**: previews/ 保留 v3 HTML，其余用 git tag 管理
3. **归档**: 将早期/过渡期 prompt 移入 backups/ 或合并
4. **压缩**: Dashboard 截图转为 webp（预计节省 50-70% 空间）
5. **规范化**: 建立 `visuals/design-system/` 目录，存放可复用的视觉 DNA 和规范
6. **清理索引**: 将 season1-cover-prompts-index.md 内容合并到 visuals/README.md

---

*审计完成。未复制任何图片，未执行 OCR，未读取敏感文件。*
