# Cleanup Candidates -- maijian-wechat

**Audit Date**: 2026-05-30
**Auditor**: Sub-agent F (Cleanup Candidates)
**Project**: `/home/hermes/projects/maijian-wechat`

---

## 1. 审计范围

| Category | Path(s) | File Count | Total Size |
|----------|---------|------------|------------|
| Root project | `maijian-wechat/` | ~130 files | ~12MB |
| 0-byte files | `articles/*.md` (3 files) | 3 | 0B |
| .md.new intermediates | `articles/*.md.new` (5 files) | 5 | ~60KB |
| .bak_* snapshots | `articles/*.bak_*`, `docs/*.bak_*` | 3 | ~200KB |
| HTML previews | `previews/` | 4 | ~200KB |
| Canary runs | `canary-runs/` (2 dirs) | 64 | ~1.4MB |
| Backup snapshots | `backups/` (28 subdirs) | ~150+ | ~1.3MB |
| Generated covers | `visuals/generated-covers/` | 18 | ~244KB |
| Cover PNGs in articles | `articles/*.png` + `articles/season1-rewrite-v3/*.png` | 8 | ~80KB |
| WeChat draft previews | `wechat-drafts/previews/`, `wechat-drafts-rich/previews/` | 40 | ~2MB |
| Manual publish workbench HTML | `manual-publish-workbench/*.html` | 9 | ~500KB |
| GPT-squeeze variants | `drafts/` | 10 | ~160KB |
| Season1 rewrite v3 intermediates | `articles/season1-rewrite-v3/` | ~25 | ~300KB |
| Season1 final pack article | `articles/hermes-genesis-season1/` | ~5 | ~50KB |

---

## 2. 清理候选表

### 2.1 0 字节文件 (Empty .md files)

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `articles/EP011.md` | 0 bytes, placeholder only, superseded by `season1-rewrite-v3/season1-ep011-v3.md` | Delete | Yes | Low -- content exists in rewrite-v3 |
| `articles/FinalBundle.md` | 0 bytes, placeholder only, superseded by `season1-rewrite-v3/season1-final-bundle-v3.md` | Delete | Yes | Low -- content exists in rewrite-v3 |
| `articles/CodeDrop02.md` | 0 bytes, placeholder only, superseded by `season1-rewrite-v3/season1-code-drop-02-v3.md` | Delete | Yes | Low -- content exists in rewrite-v3 |

### 2.2 .md.new 中间文件

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `articles/2026-05-agent-truth-1.md.new` | Unfinished intermediate, no corresponding final file exists | Archive then delete | Yes | Medium -- may contain draft content worth reviewing first |
| `articles/2026-05-agent-truth-2.md.new` | Unfinished intermediate, no corresponding final file exists | Archive then delete | Yes | Medium -- may contain draft content worth reviewing first |
| `articles/2026-05-agent-truth-3.md.new` | Unfinished intermediate, no corresponding final file exists | Archive then delete | Yes | Medium -- may contain draft content worth reviewing first |
| `articles/2026-05-agent-truth-4.md.new` | Unfinished intermediate, no corresponding final file exists | Archive then delete | Yes | Medium -- may contain draft content worth reviewing first |
| `articles/2026-05-agent-truth-5.md.new` | Unfinished intermediate, no corresponding final file exists | Archive then delete | Yes | Medium -- may contain draft content worth reviewing first |

### 2.3 .bak_* 备份快照

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `articles/season1-ep012.md.bak_20260515_153618` | Dated backup, current version exists in `season1-rewrite-v3/` | Delete | Yes | Low -- current version preserved |
| `articles/season1-final-bundle.md.bak_20260515_153618` | Dated backup, current version exists in `season1-rewrite-v3/` | Delete | Yes | Low -- current version preserved |
| `docs/progress.md.bak_20260511_maijian_wechat_progress_apply` | Dated backup of progress doc, outdated | Delete | Yes | Low -- historical record only |

### 2.4 HTML 预览 (Previews)

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `previews/hermes-feishu-print-assistant-preview.html` | Old v1 preview, superseded by v3 | Delete | No | Low -- v3 version exists |
| `previews/hermes-feishu-print-assistant-preview-v2.html` | Old v2 preview, superseded by v3 | Delete | No | Low -- v3 version exists |
| `previews/hermes-feishu-print-assistant-dryrun.json` | Dry-run data, debugging artifact | Delete | No | None |
| `previews/hermes-feishu-print-assistant-preview-v3.html` | Latest preview, still useful for reference | Keep (or archive) | Yes | Low -- rendered preview, source exists |
| `wechat-drafts/previews/*.html` (18 files) | Rendered HTML previews of published articles; WeChat articles already published | Delete | Yes | Low -- published content preserved in source .md |
| `wechat-drafts-rich/previews/*.html` (20 files) | Rendered HTML previews of rich articles; includes v2 variants and local previews | Delete | Yes | Low -- published content preserved in source .md |
| `wechat-drafts-rich/previews/season1-announcement-final-v2-local-preview.md` | Local preview markdown, superseded by final | Delete | No | None |
| `manual-publish-workbench/*.html` (9 files) | Workbench HTML variants for style testing and draft comparison | Delete | Yes | Low -- style decisions documented in theme V1/V2 docs |

### 2.5 Canary Runs

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `canary-runs/mjw-20260518-ai-homework-canary-v1/` (324KB, 30 files) | Completed canary run, all gates passed, no further use | Delete | No | None -- historical test data |
| `canary-runs/mjw-20260521-final-public-pack-v3-1/` (1.1MB, 34 files) | Completed canary run for v3.1 final pack, already merged | Delete | No | None -- historical test data |

### 2.6 备份快照 (backups/ -- 28 subdirectories)

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `backups/article-type-router-20260517-143053/` (156KB) | Backup of superseded version | Delete | Yes | Low -- current version in articles/ |
| `backups/canary-fast-v2-20260518-213415/` (68KB) | Old canary backup, superseded | Delete | No | None |
| `backups/direct-draft-main-path-20260521-143351/` (24KB) | Old canary backup | Delete | No | None |
| `backups/draco-style-recovery-20260520-232341/` (32KB) | Old style backup | Delete | No | Low |
| `backups/final-public-pack-codeblock-layout-fix-20260521-164302/` (24KB) | Old layout fix backup | Delete | No | None |
| `backups/final-public-pack-layout-fix-20260521-161654/` (24KB) | Old layout fix backup | Delete | No | None |
| `backups/manual-publish-v3-20260519-111520/` (20KB) | Old manual publish backup | Delete | Yes | Low |
| `backups/production-consolidation-20260517-130326/` (4KB) | Old production snapshot | Delete | No | Low |
| `backups/production-integration-20260517-132800/` (260KB) | Old integration snapshot | Delete | Yes | Medium -- largest backup dir |
| `backups/publish-format-fix-v1-20260518-102429/` (32KB) | Old format fix backup | Delete | No | None |
| `backups/publish-map-v2-a2 through a6/` (5 dirs, ~80KB) | Iteration snapshots, superseded | Delete | No | None |
| `backups/reader-mirror-copy-workbench-20260519-115836/` (24KB) | Old reader mirror backup | Delete | No | None |
| `backups/release-canary-v1-20260518-180154/` (32KB) | Old canary release backup | Delete | No | None |
| `backups/release-v2-stage-package-20260518-171839/` (20KB) | Old release backup | Delete | No | None |
| `backups/short-command-v1-20260517-211850/` (24KB) | Old command backup | Delete | No | None |
| `backups/v3-draco-style-default-20260521-141329/` (56KB) | Old style backup | Delete | No | Low |
| `backups/workbench-theme-v1-1 through v1-4/` (4 dirs, ~288KB) | Theme iteration workbench backups | Delete | Yes | Low -- final theme in MAIJIAN_WECHAT_THEME_V1/V2 docs |
| `backups/workbench-theme-v2-20260520-144356/` (76KB) | Theme v2 backup | Delete | Yes | Low -- final theme in MAIJIAN_WECHAT_THEME_V2_PROPOSAL.md |
| `backups/workflow-v1-freeze-20260517-193731/` (12KB) | Old workflow freeze backup | Delete | No | Low -- current workflow in VALIDATED_WORKFLOW_V1.md |

### 2.7 图片中间产物

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `visuals/generated-covers/season1-ep001.png` through `season1-ep012.png` (12 files) | Generated cover images, superseded by `season1-rewrite-v3/*.png` and `articles/*.png` | Delete | Yes | Low -- cover images exist in articles/ |
| `visuals/generated-covers/season1-announcement-final-v2.png` | Announcement cover, published already | Delete | No | Low |
| `visuals/generated-covers/season1-announcement-test.png` | Test cover image | Delete | No | None |
| `visuals/generated-covers/season1-code-drop-01/02/03.png` | Code drop covers, superseded by articles/ versions | Delete | Yes | Low |
| `visuals/generated-covers/season1-final-bundle.png` | Final bundle cover, superseded | Delete | Yes | Low |
| `articles/season1-ep012-cover.png` | Cover image, current version also in rewrite-v3/ | Keep or archive | Yes | Low -- duplicate in rewrite-v3 |
| `articles/season1-final-bundle.png` | Cover image, current version also in rewrite-v3/ | Keep or archive | Yes | Low -- duplicate in rewrite-v3 |
| `articles/season1-code-drop-02-workbench.png` | Workbench screenshot | Keep | No | Low -- may be referenced in docs |
| `articles/draft-ai-homework-cover-temp.png` | Temp cover, likely superseded | Delete | No | None |
| `articles/season1-ep011.png` | Cover image, current version in rewrite-v3/ | Keep or archive | Yes | Low -- duplicate in rewrite-v3 |
| `articles/hermes-genesis-season1/final-public-pack-article/assets/*.png` (4 files) | Dashboard lite screenshots, may be referenced in published article | Keep | Yes | Medium -- may be embedded in article |
| `articles/season1-rewrite-v3/ep001-cover.png`, `season1-ep011-cover.png`, `season1-ep012-cover.png` | Current cover images in rewrite-v3 | Keep | No | High -- actively used |

### 2.8 重复 Drafts (drafts/ -- GPT-squeeze 变体)

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `drafts/20260527-gpt-squeeze-v4-full.md` (76KB) | Large intermediate, superseded by `drafts/gpt-squeeze-final.md` | Delete | Yes | Low -- final version exists |
| `drafts/20260527-squeeze-gpt-sop.md` (7KB) | SOP draft, superseded | Delete | Yes | Low |
| `drafts/20260527-v3.1-collaboration-final.md` (17KB) | Collaboration draft, superseded | Delete | Yes | Low |
| `drafts/20260527-v3.1-combined-final.md` (13KB) | Combined draft, superseded | Delete | Yes | Low |
| `drafts/20260527-final-sop.md` (6KB) | SOP draft, superseded | Delete | Yes | Low |
| `drafts/20260527-github-fact-source.md` (7KB) | Fact source draft | Delete | Yes | Medium -- may be source of truth for facts |
| `drafts/20260527-gpt-image-2-codex-oauth.md` (6KB) | Image/OAuth draft | Delete | Yes | Medium -- may contain useful config notes |
| `drafts/gpt-squeeze-final.md` (23KB) | Final squeeze variant -- review before deleting | Archive, then delete | Yes | Medium -- likely the definitive version |
| `drafts/ip-whitelist-draft.md` (6KB) | IP whitelist draft -- operational doc | Keep | Yes | Medium -- may be referenced for deployment |

### 2.9 低价值占位稿 / Editor Plans

| Path | Reason | Recommended Action | Needs Human Confirmation | Risk If Deleted |
|------|--------|--------------------|--------------------------|-----------------|
| `articles/season1-rewrite-v3/season1-v3-direction-matrix.md` | Direction matrix, planning artifact | Archive | Yes | Low |
| `articles/season1-rewrite-v3/season1-v3-doc-map.json` | Doc mapping, planning artifact | Archive | Yes | Low |
| `articles/season1-rewrite-v3/season1-v3-review-index.md` | Review index, planning artifact | Archive | Yes | Low |
| `articles/season1-rewrite-v3/updates-20260427-role-memory-dashboard/` | Subdirectory with role-memory dashboard updates | Review then archive | Yes | Medium |
| `inbox/hermes-feishu-print-assistant-wechat.md` | Inbox artifact, feishu print assistant | Delete | No | Low |

---

## 3. 分批清理建议

### Batch 1: Safe Delete (no confirmation needed)
- `previews/hermes-feishu-print-assistant-preview.html`
- `previews/hermes-feishu-print-assistant-preview-v2.html`
- `previews/hermes-feishu-print-assistant-dryrun.json`
- `canary-runs/` (both subdirectories, 64 files)
- `backups/canary-fast-v2-20260518-213415/`
- `backups/direct-draft-main-path-20260521-143351/`
- `backups/final-public-pack-codeblock-layout-fix-20260521-164302/`
- `backups/final-public-pack-layout-fix-20260521-161654/`
- `backups/publish-format-fix-v1-20260518-102429/`
- `backups/publish-map-v2-a2 through a6/` (5 dirs)
- `backups/reader-mirror-copy-workbench-20260519-115836/`
- `backups/release-canary-v1-20260518-180154/`
- `backups/release-v2-stage-package-20260518-171839/`
- `backups/short-command-v1-20260517-211850/`
- `backups/workflow-v1-freeze-20260517-193731/`
- `visuals/generated-covers/season1-announcement-test.png`
- `articles/draft-ai-homework-cover-temp.png`
- `inbox/hermes-feishu-print-assistant-wechat.md`

**Expected reclaim**: ~2.2MB, ~90 files

### Batch 2: Low-Risk Delete (quick human confirmation)
- `articles/EP011.md`, `articles/FinalBundle.md`, `articles/CodeDrop02.md` (0-byte placeholders)
- `articles/season1-ep012.md.bak_20260515_153618`, `articles/season1-final-bundle.md.bak_20260515_153618`, `docs/progress.md.bak_*`
- `backups/draco-style-recovery-20260520-232341/`
- `backups/v3-draco-style-default-20260521-141329/`
- `backups/production-consolidation-20260517-130326/`
- `visuals/generated-covers/` (all 18 PNGs)
- `wechat-drafts/previews/` (18 HTML files)
- `wechat-drafts-rich/previews/` (20 HTML files + 1 .md)
- `manual-publish-workbench/*.html` (9 files)
- `drafts/` intermediates (except `gpt-squeeze-final.md` and `ip-whitelist-draft.md`)

**Expected reclaim**: ~3MB, ~80 files

### Batch 3: Review Required (medium risk)
- `articles/2026-05-agent-truth-{1..5}.md.new` (5 files -- review for salvageable content)
- `backups/production-integration-20260517-132800/` (260KB, largest backup)
- `backups/workbench-theme-v1-{1..4}/` and `workbench-theme-v2/` (5 dirs)
- `backups/article-type-router-20260517-143053/`
- `backups/manual-publish-v3-20260519-111520/`
- `drafts/20260527-github-fact-source.md`, `drafts/20260527-gpt-image-2-codex-oauth.md`
- `drafts/gpt-squeeze-final.md`
- `drafts/ip-whitelist-draft.md`
- `articles/hermes-genesis-season1/final-public-pack-article/assets/*.png` (4 screenshots)
- `articles/season1-rewrite-v3/` planning artifacts (direction-matrix, doc-map, review-index)

**Expected reclaim**: ~800KB, ~40 files

### Batch 4: Archive Candidates (preserve before delete)
- `previews/hermes-feishu-print-assistant-preview-v3.html` (latest preview)
- `articles/season1-ep012-cover.png`, `articles/season1-final-bundle.png`, `articles/season1-ep011.png` (duplicates of rewrite-v3 versions)
- `articles/season1-code-drop-02-workbench.png` (may be referenced)
- `articles/season1-rewrite-v3/updates-20260427-role-memory-dashboard/`

---

## 4. 需要总控裁决的问题

1. **agent-truth-{1..5}.md.new 内容价值**: 这些 .new 文件包含未完成的 Agent Truth 系列稿件。是否应先审阅内容再决定去留？如果内容无价值，可直接删除。

2. **backups/ 目录的保留策略**: 当前 backups/ 包含 28 个子目录共 1.3MB。建议全部清理后，改为 git tag 或外部快照机制。是否需要保留最新的一个完整快照（如 production-integration-20260517-132800）？

3. **wechat-drafts/previews/ 和 wechat-drafts-rich/previews/**: 这些 HTML 预览文件是已发布文章的渲染产物。如果文章已上线，这些文件可以安全删除。但需要确认是否有任何未发布的版本。

4. **drafts/gpt-squeeze-final.md**: 这是 7-way GPT-squeeze 变体中的最终版本（23KB），但文件名中仍有 "final" 标识。需要确认是否已合并到正式 articles/ 目录。

5. **visuals/generated-covers/ vs articles/*.png**: 两套封面图片存在重复。建议保留 articles/ 和 rewrite-v3/ 中的版本，删除 visuals/generated-covers/ 全套。

6. **articles/hermes-genesis-season1/assets/*.png**: 这 4 张 dashboard-lite 截图可能被嵌入在已发布的文章中。删除后可能影响文章可读性。

7. **inbox/hermes-feishu-print-assistant-wechat.md**: 这是 inbox 中的飞书打印助手文章草稿，看似已完成迁移。确认无用后可直接删除。

---

## 5. 下一步建议

1. **立即执行 Batch 1**: 无需确认的 90 个文件可立即删除，预计释放 ~2.2MB。

2. **发送 Batch 2 + Batch 3 确认清单给项目所有者**: 将需要人工确认的项目标出，批量审批。

3. **建立 .gitignore 规则**: 添加以下规则防止未来积累同类中间产物：
   ```
   *.md.new
   *.bak_*
   previews/*.html
   canary-runs/
   backups/
   visuals/generated-covers/
   drafts/*-squeeze-*.md
   ```

4. **建立归档机制**: 对 Batch 4 的档案候选，建议打包为 `.tar.gz` 存入 `archives/` 目录，而非散落在项目根目录。

5. **定期清理任务**: 建议将清理检查纳入 release pipeline，每次发布后自动清理 canary-runs 和 backups。

6. **评估 articles/ 目录结构**: 当前 articles/ 包含 ~100+ 文件，建议按 season/episode 重新组织，减少扁平化目录的文件数。
