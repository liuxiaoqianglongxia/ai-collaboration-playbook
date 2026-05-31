# Article Dedup Matrix -- maijian-wechat

**Date:** 2026-05-31
**Scope:** All articles in `maijian-wechat/` + `maijian-wechat-private-repo/`
**Rule:** No files deleted this round.

---

## Dedup Groups

---

### DG-01: S1 ep001-ep012 v1/v2/v3 + code-drops + bundle

Three rewrite passes of the same Season 1 corpus.

| Variant | Location | Files (12 eps + 3 code-drops + 1 bundle) | Total bytes |
|---|---|---|---|
| **v1 (final / published)** | `articles/season1-ep001.md` .. `season1-ep012.md` | 12 ep files | 77,946 |
| **v2 (rewrite)** | `articles/season1-rewrite-v2/season1-ep001-v2.md` .. `ep012-v2.md` | 12 ep files | 72,322 |
| **v3 (rewrite)** | `articles/season1-rewrite-v3/season1-ep001-v3.md` .. `ep012-v3.md` | 12 ep files + 2 code-drops + 1 bundle | 101,625 |

**Code-drop variants:**
- `articles/season1-code-drop-01-foundation.md` (4,506) -- v1
- `articles/season1-code-drop-02-workbench.md` (5,043) -- v1
- `articles/season1-code-drop-03-role-memory.md` (4,481) -- v1
- `articles/draft-code-drop-01-foundation.md` (4,115) -- draft
- `articles/draft-code-drop-02-workbench.md` (4,863) -- draft
- `articles/draft-code-drop-03-role-memory.md` (4,259) -- draft
- `articles/season1-rewrite-v3/season1-code-drop-01-v3.md` (11,553) -- v3
- `articles/season1-rewrite-v3/season1-code-drop-02-v3.md` (10,981) -- v3

**Bundle variants:**
- `articles/season1-final-bundle.md` (9,205) -- v1 (same content as `final-bundle.md`)
- `articles/season1-rewrite-v3/season1-final-bundle-v3.md` (6,339) -- v3
- `maijian-wechat-private-repo/articles/hermes-genesis-season1/final-bundle/final-bundle-polished.md` (18,098) -- private-repo final bundle

**Candidate files:**
```
articles/season1-ep001.md
articles/season1-ep002.md
...
articles/season1-ep012.md
articles/season1-rewrite-v2/season1-ep001-v2.md
...
articles/season1-rewrite-v2/season1-ep012-v2.md
articles/season1-rewrite-v3/season1-ep001-v3.md
...
articles/season1-rewrite-v3/season1-ep012-v3.md
articles/season1-code-drop-01-foundation.md
articles/season1-code-drop-02-workbench.md
articles/season1-code-drop-03-role-memory.md
articles/draft-code-drop-01-foundation.md
articles/draft-code-drop-02-workbench.md
articles/draft-code-drop-03-role-memory.md
articles/season1-rewrite-v3/season1-code-drop-01-v3.md
articles/season1-rewrite-v3/season1-code-drop-02-v3.md
articles/season1-final-bundle.md
articles/final-bundle.md   (identical to season1-final-bundle.md)
articles/season1-rewrite-v3/season1-final-bundle-v3.md
articles/season1-ep001-v3-rewrite.md
articles/season1-ep002-v3-rewrite.md
articles/season1-ep003-v3-rewrite.md
articles/season1-final-bundle.md.bak_20260515_153618
articles/season1-ep012.md.bak_20260515_153618
```

**Recommended primary:** `articles/season1-ep001.md` .. `articles/season1-ep012.md` (v1 final / published)

**Reason:** v1 is the version that was actually published to WeChat. Per controller decision Q1, the final published稿 is the canonical version for warehousing.

**Secondary keep policy:**
- v2 files -> `drafts/archive/rewrite-candidates/v2/`
- v3 files -> `drafts/archive/rewrite-candidates/v3/`
- v3 code-drops -> keep in `drafts/archive/rewrite-candidates/v3/` (significantly larger than v1, may contain useful material)
- draft-code-drops -> `drafts/archive/rewrite-candidates/drafts/`
- `.bak` files -> `drafts/archive/baks/`
- `final-bundle.md` (duplicate of `season1-final-bundle.md`) -> archive

**Risk:** LOW -- v1 is confirmed published. No content loss if v2/v3 are archived.

**Needs human review:** NO (for v1 selection). YES for whether v3 code-drops should be merged into production.

---

### DG-02: 单实例系列 (Single-Instance Series) -- 4 variants + final + cover + rewrite

Four serial articles about the single-instance pattern, plus a consolidated final, a cover article, and a rewrite.

**Candidate files:**
```
articles/2026-04-17-series-01-single-instance-vs-group-chat.md   (9,316 bytes)
articles/2026-04-17-series-02-how-one-ai-holds-49-roles.md      (7,880 bytes)
articles/2026-04-17-series-03-team-boss-mechanism.md            (11,709 bytes)
articles/2026-04-17-series-04-turn-ai-into-executor.md          (8,764 bytes)
articles/2026-04-17-single-instance-final.md                     (5,506 bytes)
articles/2026-04-17-single-instance-cover-article-final.md       (9,568 bytes)
articles/2026-04-17-stable-collaboration-rewrite.md              (5,952 bytes)
```

Supporting meta-files (not article content):
```
articles/2026-04-17-series-final-release-plan.md
articles/2026-04-17-series-plan-single-instance.md
articles/2026-04-17-series-publishing-pack.md
articles/2026-04-17-series-summary.md
articles/editor-plan-4-series.md
articles/editor-plan-single-instance.md
```

**Recommended primary:** The 4 serial articles (`series-01` through `series-04`) as the canonical series, plus `single-instance-cover-article-final.md` as the cover/landing piece.

**Reason:** The 4-part series represents the full narrative arc. `single-instance-final.md` (5,506 bytes) appears to be an earlier condensed version superseded by the 4-part series. `stable-collaboration-rewrite.md` is a rewrite of the theme but shorter than the original series articles.

**Secondary keep policy:**
- `single-instance-final.md` -> archive to `drafts/archive/single-instance/`
- `single-instance-cover-article-final.md` -> KEEP as cover article
- `stable-collaboration-rewrite.md` -> archive to `drafts/archive/rewrite-candidates/`
- Meta/planning files -> archive to `drafts/archive/planning/`

**Risk:** LOW -- the 4-part series is self-contained and published.

**Needs human review:** NO

---

### DG-03: GPT-squeeze 7-way

Seven different takes on the "GPT as subscription company" / squeeze SOP theme.

**Candidate files:**
```
articles/20260528-squeeze-gpt-sop.md              (7,309 bytes)   -- active SOP draft
drafts/20260527-squeeze-gpt-sop.md                (6,933 bytes)   -- SOP variant (drafts/)
articles/draft-gpt-subscription-company.md        (1,276 bytes)   -- short outline
drafts/20260527-gpt-squeeze-v4-full.md            (76,569 bytes)  -- full v4 (largest)
drafts/20260527-v3.1-combined-final.md            (13,290 bytes)  -- v3.1 combined
drafts/gpt-squeeze-final.md                       (22,871 bytes)  -- "final" squeeze
drafts/20260527-v3.1-collaboration-final.md       (17,448 bytes)  -- v3.1 collab
drafts/20260527-github-fact-source.md             (7,424 bytes)   -- fact source
```

**Recommended primary:** `drafts/20260527-gpt-squeeze-v4-full.md` (76,569 bytes) as the most comprehensive version, OR `drafts/gpt-squeeze-final.md` (22,871 bytes) as the named "final" if a shorter version is preferred.

**Reason:** The v4-full is 3x larger than the next largest candidate, suggesting it contains significantly more content. However, its name suggests it is a draft iteration. The `gpt-squeeze-final.md` has "final" in its name at a more moderate length. Both should be presented to human for selection.

**Secondary keep policy:**
- `20260528-squeeze-gpt-sop.md` + `20260527-squeeze-gpt-sop.md` -> keep as SOP reference docs
- `draft-gpt-subscription-company.md` -> archive (too short, likely an outline)
- `20260527-v3.1-combined-final.md` -> archive (superseded by v4/final)
- `20260527-v3.1-collaboration-final.md` -> archive (superseded)
- `20260527-github-fact-source.md` -> KEEP as source-of-truth reference, not an article

**Risk:** MEDIUM -- the 76KB v4-full may contain padding/duplication. Human should verify content quality before selecting.

**Needs human review:** YES -- choose between v4-full (comprehensive) and gpt-squeeze-final (named final).

---

### DG-04: 麦尖 Vol (4篇) vs agent-truth (5篇)

Same themes, different packaging. 麦尖 Vol is the WeChat column packaging; agent-truth is the theme series.

**麦尖 Vol (4 files):**
```
articles/麦尖-vol1-群聊瞎忙到系统协作.md          (9,328 bytes)
articles/麦尖-vol2-自动写作到SOP组合.md            (13,285 bytes)
articles/麦尖-vol3-35角色在线只有一人换帽.md       (11,357 bytes)
articles/麦尖-vol4-给AI装上海马体.md               (13,775 bytes)
```

**agent-truth (5 files + 1 injection):**
```
articles/2026-05-agent-truth-1.md                  (8,984 bytes)
articles/2026-05-agent-truth-2.md                  (6,227 bytes)
articles/2026-05-agent-truth-3.md                  (10,026 bytes)
articles/2026-05-agent-truth-4.md                  (12,175 bytes)
articles/2026-05-agent-truth-5-viral-benchmark.md  (10,739 bytes)
articles/writer-injection-agent-truth.md           (19,724 bytes)  -- meta/injection doc
```

**Supporting files (.new, .bak):**
```
articles/2026-05-agent-truth-1.md.new
articles/2026-05-agent-truth-2.md.new
articles/2026-05-agent-truth-3.md.new
articles/2026-05-agent-truth-4.md.new
articles/2026-05-agent-truth-5.md.new
articles/2026-05-agent-truth-5.md.bak
articles/editor-plan-agent-truth-series.md
articles/feishu_agent-truth-series-broadcast.md
```

**Theme mapping (by file size and naming inference):**

| 麦尖 Vol | agent-truth | Theme (inferred) |
|---|---|---|
| vol1 群聊瞎忙到系统协作 | agent-truth-1 | AI collaboration / group chat chaos |
| vol2 自动写作到SOP组合 | agent-truth-2 or agent-truth-4 | AI writing / SOP automation |
| vol3 35角色在线只有一人换帽 | agent-truth-3 | Multi-role / role switching |
| vol4 给AI装上海马体 | agent-truth-4 | Memory / hippocampus for AI |
| (no vol5) | agent-truth-5 viral-benchmark | Viral benchmark (extra theme) |

**Recommended primary:** 麦尖 Vol 1-4 as the primary versions for WeChat publication (they are purpose-built for the public account format). agent-truth 1-5 archived as theme reference / source material.

**Reason:** Per controller decision Q4, 麦尖 Vol = 公众号栏目包装, agent-truth = 主题系列. The 麦尖 Vol versions are more suitable for public account publishing. Note: 麦尖 has 4 vols, not 5; agent-truth has 5 articles. The 5th agent-truth (viral-benchmark) has no 麦尖 counterpart.

**Secondary keep policy:**
- agent-truth-1 through agent-truth-5 -> archive as theme source/reference
- `.new` files -> archive (likely in-progress edits)
- `.bak` files -> archive
- `writer-injection-agent-truth.md` -> KEEP as meta/editorial reference, not a publishable article
- Archived 麦尖 vols in `materials/archive/past-articles/` (vol1-vol4 copies exist there too)

**Risk:** LOW -- both versions serve different purposes. No deletion needed.

**Needs human review:** YES -- confirm theme mapping and decide whether agent-truth-5 (viral-benchmark) should get a 麦尖 Vol packaging.

---

### DG-05: hermes-system (Vol1-4) vs hermes-genesis (ep001-ep012)

Different series, minimal content overlap. hermes-system is a conceptual framework series; hermes-genesis is the S1 narrative series.

**hermes-system (4 files, no vol5/vol6 found):**
```
articles/hermes-system-series-vol1.md              (6,018 bytes)
articles/hermes-system-series-vol1-review.md       (4,257 bytes)
articles/hermes-system-series-vol2.md              (5,314 bytes)
articles/hermes-system-series-vol3.md              (7,188 bytes)
articles/hermes-system-series-vol4.md              (5,700 bytes)
```

**hermes-genesis (ep001-ep012 drafts + S1 final):**
```
articles/draft-2026-04-21-ep001-hermes-genesis.md          (9,262 bytes)
articles/draft-2026-04-21-ep001-hermes-genesis-polished.md (9,005 bytes)
articles/draft-2026-04-21-ep001-hermes-genesis-polished-short.md (6,069 bytes)
articles/draft-ep001-hermes-genesis-v2.md                   (8,463 bytes)
articles/draft-ep001-hermes-genesis-v3-gpt54.md             (5,415 bytes)
articles/draft-ep001-hermes-genesis-v4-gpt54.md             (6,327 bytes)
articles/draft-ep002-hermes-genesis-gpt54.md                (6,847 bytes)
articles/draft-ep003-hermes-genesis-gpt54.md                (similar)
...
articles/draft-ep012-hermes-genesis-gpt54.md                (similar)
articles/hermes-genesis-ep012.md                            (8,104 bytes)
articles/2026-04-21-hermes-genesis-execution-roadmap.md
articles/2026-04-21-hermes-genesis-long-series-master-plan.md
articles/2026-04-21-hermes-genesis-season1-announcement.md
```

**Recommended primary:** Both series are independent. KEEP ALL hermes-system vols and all hermes-genesis S1 finals. Archive intermediate genesis drafts (v2/v3/v4/gpt54 variants).

**Reason:** These are genuinely different series with different audiences. hermes-system = conceptual framework; hermes-genesis = narrative S1 launch series. Overlap is at the theme level only.

**Secondary keep policy:**
- hermes-genesis draft variants (v2/v3/v4/gpt54) -> `drafts/archive/genesis-drafts/`
- `polished` / `polished-short` variants -> `drafts/archive/genesis-drafts/`
- Planning docs (execution-roadmap, long-series-master-plan, announcement) -> archive as meta

**Risk:** LOW -- confirmed different series.

**Needs human review:** NO

---

### DG-06: Season1 ep001-ep012 final vs Hermes Genesis S1 final-public-pack

Same core content, different packaging. S1 final = individual episode files. final-public-pack = consolidated mega-article for public distribution.

**Candidate files:**
```
# S1 final (12 individual episodes, see DG-01 v1)
articles/season1-ep001.md .. articles/season1-ep012.md   (77,946 bytes total)

# Final public pack (maijian-wechat)
articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v2.md  (9,776 bytes)
articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v3-1.md (17,700 bytes)

# Final public pack (private repo, more complete)
private-repo/articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v1.md  (16,475 bytes)
private-repo/articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v2.md  (17,428 bytes)
private-repo/articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v3.md  (17,565 bytes)
private-repo/articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v3-1.md (17,559 bytes)

# Final public pack supporting docs (private repo)
private-repo/articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-change-notes-v2.md
private-repo/articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-change-notes-v3.md
private-repo/articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-risk-check-v1.md
```

**Recommended primary:** `private-repo/.../final-public-pack-draft-v3-1.md` (17,559 bytes) as the final public pack. It is the latest iteration in the private repo with the most complete assets. For maijian-wechat, use `articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v3-1.md` (17,700 bytes) as the working copy.

**Reason:** v3-1 is the latest named version in both repos. The private repo version has more complete supporting assets. The individual S1 episodes (DG-01) and the public pack serve different purposes: episodes for serial reading, pack for one-stop download.

**Secondary keep policy:**
- `final-public-pack-draft-v1.md`, `v2.md`, `v3.md` (private repo) -> archive to `drafts/archive/public-pack/`
- `final-public-pack-draft-v2.md` (maijian-wechat) -> archive
- Change notes, risk check files -> KEEP as editorial metadata
- Asset files (images, previews) -> KEEP with the primary

**Risk:** LOW -- v3-1 is clearly the latest iteration.

**Needs human review:** YES -- confirm which repo's v3-1 is the source of truth (they differ by ~140 bytes).

---

### DG-07: S1 重写稿 (v2/v3) vs final public pack

The v2 and v3 rewrites vs the consolidated final-public-pack mega-article. Different granularity: rewrites are per-episode; public pack is consolidated.

**Candidate files:**
```
# v2 rewrites (12 eps)
articles/season1-rewrite-v2/season1-ep001-v2.md .. ep012-v2.md  (72,322 bytes total)

# v3 rewrites (12 eps + code-drops + bundle)
articles/season1-rewrite-v3/season1-ep001-v3.md .. ep012-v3.md  (72,752 bytes eps)
articles/season1-rewrite-v3/season1-code-drop-01-v3.md           (11,553 bytes)
articles/season1-rewrite-v3/season1-code-drop-02-v3.md           (10,981 bytes)
articles/season1-rewrite-v3/season1-final-bundle-v3.md           (6,339 bytes)

# Final release total control v1 (in v3 dir)
articles/season1-rewrite-v3/final-release-total-control-v1/final-bundle-polished.md
articles/season1-rewrite-v3/final-release-total-control-v1/final-bundle-change-notes.md
articles/season1-rewrite-v3/final-release-total-control-v1/final-bundle-risk-check.md
articles/season1-rewrite-v3/final-release-total-control-v1/minimal-pack-file-tree.md
articles/season1-rewrite-v3/final-release-total-control-v1/minimal-pack-plan.md
articles/season1-rewrite-v3/final-release-total-control-v1/publish-checklist.md
articles/season1-rewrite-v3/final-release-total-control-v1/reward-delivery-copy.md

# v3 standalone root-level rewrites
articles/season1-ep001-v3-rewrite.md  (8,756 bytes)
articles/season1-ep002-v3-rewrite.md  (8,885 bytes)
articles/season1-ep003-v3-rewrite.md  (9,011 bytes)

# Final public pack (see DG-06)
articles/hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v3-1.md
```

**Recommended primary:**
- Per-episode canonical: `articles/season1-ep001.md` .. `ep012.md` (v1 final, see DG-01)
- Consolidated mega-article: `final-public-pack-draft-v3-1.md` (see DG-06)
- v2 and v3 rewrites -> archive

**Reason:** The rewrites are intermediate iterations. The v1 final is published. The public pack is a separate deliverable. Root-level v3-rewrite files (ep001-ep003 only) appear to be early drafts superseded by the full v3 directory.

**Secondary keep policy:**
- All v2 files -> `drafts/archive/rewrite-candidates/v2/`
- All v3 files in `season1-rewrite-v3/` -> `drafts/archive/rewrite-candidates/v3/`
- `final-release-total-control-v1/` supporting docs -> KEEP as editorial metadata
- Root-level v3-rewrite (ep001-003) -> `drafts/archive/rewrite-candidates/v3/`

**Risk:** LOW -- v1 is published, rewrites are clearly intermediate.

**Needs human review:** NO

---

## Zero-Byte Files (Q8: Cleanable Candidates)

Per controller decision Q9, these are listed but NOT deleted this round.

```
articles/FinalBundle.md                                          (0 bytes)
articles/CodeDrop02.md                                           (0 bytes)
articles/EP011.md                                                (0 bytes)
articles/season1-rewrite-v3/feishu/season1-ep001-v3.md.create.stderr  (0 bytes)
articles/season1-rewrite-v3/feishu/season1-ep002-v3.md.create.stderr  (0 bytes)
articles/season1-rewrite-v3/feishu/season1-ep003-v3.md.create.stderr  (0 bytes)
articles/season1-rewrite-v3/feishu/season1-v3-direction-matrix.md.create.stderr (0 bytes)
```

**Action:** Log as "cleanable candidates". Do not delete this round. The `.create.stderr` files are Feishu API error logs and can be safely removed in a future cleanup pass.

---

## Summary Table

| Group ID | Description | # Files | Recommended Primary | Risk | Human Review |
|---|---|---|---|---|---|
| **DG-01** | S1 ep001-ep012 v1/v2/v3 + code-drops + bundle | ~30 | v1 final (published) | LOW | NO (YES for v3 code-drop merge) |
| **DG-02** | 单实例系列 4 variants + final + cover + rewrite | 7 articles + 6 meta | 4-part series + cover article | LOW | NO |
| **DG-03** | GPT-squeeze 7-way | 8 | v4-full or gpt-squeeze-final (TBD) | MEDIUM | YES |
| **DG-04** | 麦尖 Vol (4) vs agent-truth (5) | 9 + 7 support | 麦尖 Vol 1-4 for WeChat | LOW | YES (agent-truth-5 coverage) |
| **DG-05** | hermes-system (Vol1-4) vs hermes-genesis (ep001-12) | 5 system + ~18 genesis | Keep both series; archive drafts | LOW | NO |
| **DG-06** | S1 final vs final-public-pack | 12 eps + 4 pack drafts | v3-1 public pack + v1 episodes | LOW | YES (repo source of truth) |
| **DG-07** | S1 v2/v3 rewrites vs final public pack | ~25 | v1 final + v3-1 pack; archive rewrites | LOW | NO |

**Total files in scope:** ~100
**Zero-byte files (cleanable):** 7
**Files requiring human review:** 4 groups (DG-01 code-drops, DG-03 squeeze selection, DG-04 agent-truth-5, DG-06 repo source)
