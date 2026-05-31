# 视觉/Prompt 分流路由方案 v1

> 审计日期：2026-05-30
> 审计范围：`maijian-wechat` 仓库（`/home/hermes/projects/maijian-wechat`）
> 输出位置：`content-routing-v1/visual-prompt-routing-plan.md`
> 规则来源：总控（Hermes）视觉内容管理约定

---

## 0. 核心规则

| 规则 | 处理方式 |
|---|---|
| Prompt 文档（.md） | 可进入 content-lab |
| 图片原件（.png/.jpg） | 默认仅本地保留，不入仓 |
| 截图 | 默认仅本地保留，不入仓 |
| HTML 预览 | 不入仓 |
| 可复用样式说明 | 可进入 content-lab |

---

## 1. 审计范围

本次审计覆盖以下文件类型：

| 类别 | 覆盖路径 | 文件数 |
|---|---|---|
| 封面 prompt Markdown | `prompts/*.md`, `visuals/*.md` | 14 |
| 生成封面图片 | `visuals/generated-covers/*.png` | 18 |
| 文章附带图片 | `articles/*.png`, `articles/**/*.png`, `articles/**/*.jpg` | 10 |
| 截图 | `articles/hermes-genesis-season1/final-public-pack-article/assets/*.{png,jpg}` | 5 |
| HTML 预览 | `previews/*.html`, `canary-runs/*/*.html`, `wechat-drafts/previews/*.html`, `wechat-drafts-rich/previews/*.html`, `manual-publish-workbench/*.html` | 60 |
| Draco 样式说明 | `DRACO_ORIGINAL_STYLE_RECOVERY.md`, `configs/wechat-style-story.yaml` | 2 |
| 可复用视觉标准 | `prompts/2026-04-22-season1-cover-brief.md` | 1 |
| 文章专用视觉素材 | `visuals/2026-04-14-*.md` 等 | 2 |

---

## 2. 封面 Prompt 路由表

### 2.1 可复用 / 标准级 (进入 content-lab)

| 文件 | 路径 | 说明 |
|---|---|---|
| Season 1 封面视觉总纲 | `prompts/2026-04-22-season1-cover-brief.md` | 封面设计 brief，定义整体视觉标准和角色分工，**可复用** |

### 2.2 Season 1 批次 prompt (归档/参考)

| 文件 | 路径 | 状态 |
|---|---|---|
| Season 1 封面 prompt 索引 | `visuals/2026-04-22-season1-cover-prompts-index.md` | 历史批次索引 |
| Season 1 封面 prompt Batch A | `visuals/2026-04-22-season1-cover-prompts-batch-a.md` | 历史批次 |
| Season 1 封面 prompt Batch B | `visuals/2026-04-22-season1-cover-prompts-batch-b.md` | 历史批次 |
| Season 1 封面 prompt Batch C | `visuals/2026-04-22-season1-cover-prompts-batch-c.md` | 历史批次 |
| Season 1 封面 prompt 汇总 | `prompts/2026-04-22-season1-cover-prompts.md` | 历史汇总 |

### 2.3 规范类 prompt (部分可复用)

| 文件 | 路径 | 说明 |
|---|---|---|
| 封面设计规范 | `visuals/2026-04-17-cover-prompts.md` | 早期封面规范 |
| 规范注入-封面 | `visuals/2026-04-17-norms-injection-cover-prompts.md` | 规范注入类 |
| 规范-封面 | `visuals/2026-04-17-norms-cover-prompts.md` | 规范类 |
| 规范-4文档 | `visuals/2026-04-17-norms-4-docs-prompts.md` | 多文档规范 |
| 系列 prompt | `visuals/2026-04-17-series-prompts.md` | 系列文章 prompt |
| Agent 系列 prompt | `visuals/2026-05-agent-series-prompts.md` | Agent 真相系列 |

### 2.4 文章专用视觉 prompt (仅本地)

| 文件 | 路径 | 说明 |
|---|---|---|
| 10min 文件治理视觉 | `visuals/2026-04-14-10min-file-gov-visual.md` | 单篇文章专用 |
| 系统升级视觉 | `visuals/2026-04-14-system-upgrade-visual.md` | 单篇文章专用 |
| 4月启动图片 | `visuals/2026-04-launch-images.md` | 早期启动图记录 |

---

## 3. 图片素材路由表

### 3.1 生成封面图片 (`visuals/generated-covers/`)

> 规则：默认仅本地保留，不复制、不入仓

| 文件 | 大小 | 格式 | 用途 |
|---|---|---|---|
| `season1-ep001.png` | 8.6K | PNG | Season 1 EP001 封面 |
| `season1-ep002.png` | 9.0K | PNG | Season 1 EP002 封面 |
| `season1-ep003.png` | 12K | PNG | Season 1 EP003 封面 |
| `season1-ep004.png` | 12K | PNG | Season 1 EP004 封面 |
| `season1-ep005.png` | 8.4K | PNG | Season 1 EP005 封面 |
| `season1-ep006.png` | 9.5K | PNG | Season 1 EP006 封面 |
| `season1-ep007.png` | 9.7K | PNG | Season 1 EP007 封面 |
| `season1-ep008.png` | 8.8K | PNG | Season 1 EP008 封面 |
| `season1-ep009.png` | 10K | PNG | Season 1 EP009 封面 |
| `season1-ep010.png` | 9.1K | PNG | Season 1 EP010 封面 |
| `season1-ep011.png` | 11K | PNG | Season 1 EP011 封面 |
| `season1-ep012.png` | 8.2K | PNG | Season 1 EP012 封面 |
| `season1-announcement-final-v2.png` | 13K | PNG | 季终公告封面 |
| `season1-announcement-test.png` | 14K | PNG | 公告测试封面 |
| `season1-final-bundle.png` | 9.7K | PNG | 季终合集封面 |
| `season1-code-drop-01-foundation.png` | 16K | PNG | Code Drop #1 封面 |
| `season1-code-drop-02-workbench.png` | 16K | PNG | Code Drop #2 封面 |
| `season1-code-drop-03-role-memory.png` | 18K | PNG | Code Drop #3 封面 |

合计：18 张，总计约 201K

### 3.2 文章附带图片 (`articles/`)

| 文件 | 大小 | 格式 | 用途 |
|---|---|---|---|
| `articles/season1-ep012-cover.png` | 9.9K | PNG | EP012 封面（文章内嵌） |
| `articles/draft-ai-homework-cover-temp.png` | 4.5K | PNG | AI作业临时封面 |
| `articles/season1-final-bundle.png` | 9.7K | PNG | 季终合集封面（文章内嵌） |
| `articles/season1-code-drop-02-workbench.png` | 16K | PNG | Code Drop #2 封面（文章内嵌） |
| `articles/season1-ep011.png` | 11K | PNG | EP011 封面（文章内嵌） |
| `articles/season1-rewrite-v3/season1-ep012-cover.png` | 9.9K | PNG | EP012 封面 V3 重写版 |
| `articles/season1-rewrite-v3/ep001-cover.png` | 7.6K | PNG | EP001 封面 V3 重写版 |
| `articles/season1-rewrite-v3/season1-ep011-cover.png` | 12K | PNG | EP011 封面 V3 重写版 |

### 3.3 截图 (`articles/hermes-genesis-season1/final-public-pack-article/assets/`)

> 规则：仅本地保留，不入仓

| 文件 | 大小 | 格式 | 用途 |
|---|---|---|---|
| `dashboard-lite-ports.png` | 849K | PNG | Dashboard Lite 端口截图 |
| `dashboard-lite-screenshot.jpg` | 260K | JPG | Dashboard Lite 界面截图 |
| `dashboard-lite-memory.png` | 383K | PNG | Dashboard Lite 内存截图 |
| `dashboard-lite-screenshot.png` | 849K | PNG | Dashboard Lite 界面截图（PNG版） |
| `dashboard-lite-tasks.png` | 638K | PNG | Dashboard Lite 任务截图 |

合计：5 张，总计约 2.9M

---

## 4. HTML 预览路由表

> 规则：HTML 预览不入仓，仅本地保留

### 4.1 主预览目录 (`previews/`)

| 文件 | 大小 | 用途 |
|---|---|---|
| `hermes-feishu-print-assistant-preview.html` | 66K | 飞书打印助手预览 v1 |
| `hermes-feishu-print-assistant-preview-v2.html` | 66K | 飞书打印助手预览 v2 |
| `hermes-feishu-print-assistant-preview-v3.html` | 66K | 飞书打印助手预览 v3 |

### 4.2 Canary 预览 (`canary-runs/`)

#### mjw-20260518-ai-homework-canary-v1/

| 文件 | 用途 |
|---|---|
| `preview.html` | AI 作业 Canary 主预览 |
| `preview-fast-current.html` | AI 作业快速预览（当前版） |

#### mjw-20260521-final-public-pack-v3-1/

| 文件 | 用途 |
|---|---|
| `preview.html` | 最终公开包 v3.1 主预览 |
| `codeblock-layout-fix-preview.html` | 代码块布局修复预览 |
| `layout-fix-preview.html` | 布局修复预览 |
| `preview-style-b-revised.html` | Style B 修订预览 |
| `style-a-current.html` | Style A 当前版预览 |
| `style-b-old-red-label.html` | Style B 旧版红色标签预览 |
| `style-c-story-compact.html` | Style C Story Compact 预览 |

### 4.3 微信草稿预览 (`wechat-drafts/previews/`)

| 文件 | 大小 | 用途 |
|---|---|---|
| `season1-ep001.html` ~ `season1-ep012.html` | 9.5K-13K | Season 1 全 12 集微信预览 |
| `season1-ep012-rev.html` | 28K | EP012 修订版预览 |
| `season1-announcement-final-v2.html` | 9.7K | 季终公告 v2 预览 |
| `season1-code-drop-01/02/03.html` | 11K-12K | Code Drop 3 集预览 |
| `season1-final-bundle.html` | 22K | 季终合集预览 |

合计：18 个 HTML 文件

### 4.4 微信富文本预览 (`wechat-drafts-rich/previews/`)

| 文件 | 大小 | 用途 |
|---|---|---|
| `season1-ep001.html` ~ `season1-ep012.html` | 9.5K-13K | Season 1 全 12 集富文本预览 |
| `season1-announcement-final-v2.html` | 9.7K | 公告 v2 标准预览 |
| `season1-announcement-final-v2-local-preview.html` | 22K | 公告 v2 本地预览 |
| `season1-announcement-final-v2-story-v2.html` | 23K | 公告 v2 Story v2 预览 |
| `season1-code-drop-01-foundation.html` | 11K | Code Drop #1 预览 |
| `season1-code-drop-01-foundation-code-v2.html` | 18K | Code Drop #1 代码 v2 预览 |
| `season1-code-drop-02-workbench.html` | 12K | Code Drop #2 预览 |
| `season1-code-drop-03-role-memory.html` | 12K | Code Drop #3 预览 |
| `season1-final-bundle.html` | 21K | 季终合集预览 |
| `season1-final-bundle-finale-v2.html` | 33K | 季终合集 Finale v2 预览 |

合计：21 个 HTML 文件

### 4.5 工作台 HTML (`manual-publish-workbench/`)

| 文件 | 大小 | 用途 |
|---|---|---|
| `draco-original-style-preview.html` | 127K | Draco 原始样式预览 |
| `draco-style-default.html` | 24K | Draco 默认样式 |
| `draco-style-story.html` | 24K | Draco Story 样式 |
| `draco-style-story-leftbar.html` | 24K | Draco Story 左栏样式 |
| `draft-ai-homework-draco-workbench.html` | 32K | AI 作业 Draco 工作台 |
| `draft-ai-homework-v2-fallback.html` | 27K | AI 作业 V2 回退 |
| `draft-ai-homework-workbench.html` | 32K | AI 作业工作台 |
| `draft-gpt-subscription-company-workbench.html` | 12K | GPT 订阅公司工作台 |
| `squeeze-gpt-sop-workbench.html` | 28K | Squeeze GPT SOP 工作台 |

合计：9 个 HTML 文件

### 4.6 HTML 预览汇总

| 目录 | 文件数 | 处理建议 |
|---|---|---|
| `previews/` | 3 | 本地保留，可清理过期版本 |
| `canary-runs/` | 7 | 本地保留，canary 结束后可清理 |
| `wechat-drafts/previews/` | 18 | 本地保留 |
| `wechat-drafts-rich/previews/` | 21 | 本地保留 |
| `manual-publish-workbench/` | 9 | 本地保留 |

**总计：约 58 个 HTML 预览文件，全部不入仓。**

---

## 5. Draco 样式说明

| 文件 | 路径 | 分类 |
|---|---|---|
| Draco 原发布 Skill 样式恢复包 | `DRACO_ORIGINAL_STYLE_RECOVERY.md` | **可进入 content-lab**，可复用样式说明 |
| 微信 Story 样式配置 | `configs/wechat-style-story.yaml` | **可进入 content-lab**，渲染配置 |

---

## 6. OpenWrite 样式说明

经全面扫描，`MANUAL_PUBLISH_V3_PLAN.md` 中 **未发现 OpenWrite 相关章节**。该文件描述的是 WeMD / doocs/md 复制粘贴路径及 Draco 直推路径，不涉及 OpenWrite。

> **结论**：OpenWrite 样式说明当前为空分类。如需引入 OpenWrite 作为第三渲染渠道，需新建独立文档。

---

## 7. 可复用 vs 历史 vs 专用 Prompt 分类

### 7.1 可复用（进入 content-lab）

| 文件 | 理由 |
|---|---|
| `prompts/2026-04-22-season1-cover-brief.md` | 封面视觉总纲，定义角色分工和设计原则，适用于所有 Season 封面 |
| `visuals/2026-04-17-cover-prompts.md` | 基础封面规范，可能被后续季复用 |
| `visuals/2026-04-17-series-prompts.md` | 系列文章通用 prompt 框架 |
| `visuals/2026-05-agent-series-prompts.md` | Agent 真相系列 prompt，可能被其他系列参考 |
| `DRACO_ORIGINAL_STYLE_RECOVERY.md` | 样式恢复说明 |
| `configs/wechat-style-story.yaml` | 样式配置文件 |

### 7.2 历史批次（归档/参考）

| 文件集合 | 说明 |
|---|---|
| `visuals/2026-04-22-season1-cover-prompts-index.md` | Season 1 prompt 索引 |
| `visuals/2026-04-22-season1-cover-prompts-batch-{a,b,c}.md` | Season 1 分批次 prompt |
| `prompts/2026-04-22-season1-cover-prompts.md` | Season 1 prompt 汇总 |
| `visuals/2026-04-17-norms-*.md` (4 files) | 规范注入类文档 |

### 7.3 文章专用（仅本地，不进入 content-lab）

| 文件 | 说明 |
|---|---|
| `visuals/2026-04-14-10min-file-gov-visual.md` | 单篇文章专用 |
| `visuals/2026-04-14-system-upgrade-visual.md` | 单篇文章专用 |
| `visuals/2026-04-launch-images.md` | 早期启动图记录 |
| `visuals/generated-covers/*.png` (18 files) | 封面图片，仅本地 |
| `articles/**/*.png` (8 files) | 文章内嵌图片，仅本地 |
| `articles/hermes-genesis-season1/.../assets/*.{png,jpg}` (5 files) | 截图，仅本地 |

---

## 8. 分流建议

### 8.1 进入 content-lab（总控知识仓）

| 类别 | 文件数 | 说明 |
|---|---|---|
| 可复用 Prompt Markdown | 6 | 封面设计规范 + 系列 prompt 框架 |
| 可复用样式说明 | 2 | Draco 样式恢复说明 + YAML 配置 |
| **合计** | **8** | |

### 8.2 保留在 maijian-wechat 仓库（仅本地）

| 类别 | 文件数 | 说明 |
|---|---|---|
| 历史批次 prompt | 7 | Season 1 批次文件 + 规范注入 |
| 文章专用 prompt | 3 | 单篇文章专用 |
| 生成封面图片 | 18 | `visuals/generated-covers/` |
| 文章内嵌图片 | 8 | `articles/**/*.png` |
| 截图 | 5 | Dashboard Lite 截图 |
| **合计** | **41** | |

### 8.3 不入仓（HTML 预览，仅本地，可定期清理）

| 类别 | 文件数 | 说明 |
|---|---|---|
| 主预览 | 3 | `previews/*.html` |
| Canary 预览 | 7 | `canary-runs/*/*.html` |
| 微信草稿预览 | 18 | `wechat-drafts/previews/*.html` |
| 微信富文本预览 | 21 | `wechat-drafts-rich/previews/*.html` |
| 工作台 HTML | 9 | `manual-publish-workbench/*.html` |
| **合计** | **58** | 建议 canary 结束后清理 |

---

## 9. 需要总控裁决的问题

1. **Season 1 历史批次 prompt 的保留价值**
   - `visuals/2026-04-22-season1-cover-prompts-batch-{a,b,c}.md` 等 7 个文件是否保留到 content-lab 作为视觉风格演进记录？还是作为纯历史归档在 maijian-wechat 本地？

2. **重复封面处理**
   - `visuals/generated-covers/` 和 `articles/` 中存在同一封面的多份副本（如 `season1-ep012-cover.png` 出现在两处），是否清理一份？建议以 `visuals/generated-covers/` 为事实源，清理 `articles/` 下的重复副本。

3. **Dashboard Lite 截图去重**
   - `dashboard-lite-screenshot.png` (849K) 和 `dashboard-lite-screenshot.jpg` (260K) 内容重复但格式不同。是否仅保留 JPG 节省空间？

4. **HTML 预览清理策略**
   - 58 个 HTML 预览文件全部不入仓。是否建立自动清理规则（如 canary 运行结束后自动删除 `canary-runs/*/` 下的 HTML）？还是保留作为排版参考？

5. **可复用 prompt 的提取粒度**
   - `visuals/2026-04-17-norms-*.md` 系列包含规范注入方法论。其中哪些段落可以抽象为通用规范进入 content-lab？还是整体作为历史参考？

6. **OpenWrite 渠道引入决策**
   - 当前无任何 OpenWrite 相关文档。是否计划引入 OpenWrite 作为第三渲染渠道？如是，需要新建样式说明文档。

---

## 10. 下一步建议

| 步骤 | 动作 | 负责 | 优先级 |
|---|---|---|---|
| 1 | 总控裁决第 9 节的 6 个问题 | 总控 (Hermes) | P0 |
| 2 | 根据裁决结果，将可复用 prompt 和样式说明移入 content-lab | 总控 | P0 |
| 3 | 清理 `articles/` 下与 `visuals/generated-covers/` 重复的封面图片 | 本地维护 | P1 |
| 4 | 建立 `.gitignore` 规则：`*.html` in `previews/`, `canary-runs/`, `wechat-drafts/previews/`, `wechat-drafts-rich/previews/`, `manual-publish-workbench/` 不入仓 | 本地维护 | P1 |
| 5 | 建立 `.gitignore` 规则：`*.png`, `*.jpg` in `visuals/generated-covers/` 和 `articles/` 不入仓 | 本地维护 | P1 |
| 6 | 如总控决定引入 OpenWrite，新建 `content-lab/openwrite-style-guide.md` | 总控 | P2 |
| 7 | 对 `visuals/2026-04-17-norms-*.md` 系列提取通用规范段落进入 content-lab | 总控 | P2 |
| 8 | 建立 canary 结束后自动清理 HTML 预览的脚本或约定 | 本地维护 | P2 |

---

*本方案 v1 仅列路径、大小、格式、用途分类，不复制任何图片或 HTML 内容。*
