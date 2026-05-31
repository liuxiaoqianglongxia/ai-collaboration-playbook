# Content-Lab 分流方案 v1

> 生成日期：2026-05-30
> 审计来源：`maijian-wechat` (工作区)、`maijian-wechat-private-repo` (内容资产仓预扫描)、`maijian-wechat-previews` (预览制品)
> 适用范围：约 170 articles/ 文件 + docs/ + materials/ + knowledge/ + configs/ + canary-runs/ + backups/

---

## 一、审计范围

| 来源 | 路径 | 文件量级 | 说明 |
|------|------|----------|------|
| 工作区 | `maijian-wechat/articles/` | ~170 文件 | 正式稿、重写稿(v2/v3)、草稿、封面、系列文章 |
| 工作区 | `maijian-wechat/docs/` | ~30 文件 | 生产流程、发布计划、排版方案、运营计划 |
| 工作区 | `maijian-wechat/materials/` | ~30 文件 | 每日复盘、原始素材、历史归档 |
| 工作区 | `maijian-wechat/knowledge/` | 4 文件 | 病毒式传播分析、领域知识种子 |
| 工作区 | `maijian-wechat/configs/` | 1 文件 | `wechat-style-story.yaml` |
| 工作区 | `maijian-wechat/canary-runs/` | ~10 运行 | 发布预演、样式 A/B/C 测试 |
| 工作区 | `maijian-wechat/manual-publish-workbench/` | ~10 文件 | 排版工作台 HTML |
| 工作区 | `maijian-wechat/backups/` | ~20 运行 | 历史打包备份 |
| 预制品 | `maijian-wechat-previews/` | ~7 文件 | 最终预览截图 |
| 资产仓 | `maijian-wechat-private-repo/articles/` | ~35 文件 | final-bundle 风险检查、final-public-pack 多版本草稿、预览图 |
| 资产仓 | `maijian-wechat-private-repo/` 其余 | ~40 文件 | 发布检查单、任务包、public-export-dryruns |

**总审计文件量：约 300+**

---

## 二、推荐进入 content-lab 的资产组

### 2.1 已发布/最终稿系列文章（主版本）

**设计目标路径：** 已发布公众号文章作为内容仓核心资产，以「麦尖 Vol」栏目包装为主版本。

| 内容组 | 主版本（推荐入仓） | 原始路径 |
|--------|-------------------|----------|
| 麦尖 Vol 系列 Vol.1-4 | `麦尖-vol1-群聊瞎忙到系统协作.md` | `maijian-wechat/articles/` |
| | `麦尖-vol2-自动写作到SOP组合.md` | |
| | `麦尖-vol3-35角色在线只有一人换帽.md` | |
| | `麦尖-vol4-给AI装上海马体.md` | |
| Hermes System Series Vol.1-4 | `hermes-system-series-vol1.md` | `maijian-wechat/articles/` |
| | `hermes-system-series-vol2.md` | |
| | `hermes-system-series-vol3.md` | |
| | `hermes-system-series-vol4.md` | |
| Hermes 工作台 Series Vol.1-4,6 | `hermes-series-vol1-cognition.md` | `maijian-wechat/articles/` |
| | `hermes-series-vol2-memory.md` | |
| | `hermes-series-vol3-architecture.md` | |
| | `hermes-series-vol4-teams.md` | |
| | `hermes-series-vol6-practice.md` | |
| Season 1 正式 EP 系列 | `season1-ep001.md` 至 `season1-ep012.md` | `maijian-wechat/articles/` |
| Season 1 Code Drop 01-03 | `season1-code-drop-01-foundation.md` | `maijian-wechat/articles/` |
| | `season1-code-drop-02-workbench.md` | |
| | `season1-code-drop-03-role-memory.md` | |
| Season 1 Final Bundle | `season1-final-bundle.md` | `maijian-wechat/articles/` |
| Season 1 官宣 | `season1-announcement-final-v2.md` | `maijian-wechat/articles/` |
| 2026-05 Agent Truth 系列 | `2026-05-agent-truth-1.md` | `maijian-wechat/articles/` |
| | `2026-05-agent-truth-2.md` | |
| | `2026-05-agent-truth-3.md` | |
| | `2026-05-agent-truth-4.md` | |
| | `2026-05-agent-truth-5.md` | |
| 榨干 GPT 订阅 | `20260528-squeeze-gpt-sop.md` | `maijian-wechat/articles/` |
| 单实例系列定稿 | `2026-04-17-single-instance-final.md` | `maijian-wechat/articles/` |
| | `2026-04-17-single-instance-cover-article-final.md` | |
| 飞书打印助手 | `hermes-feishu-print-assistant.md` | `maijian-wechat/articles/` |

**入仓建议路径结构：**
```
content-lab/
  articles/
    maijian-vol/
      vol1-群聊瞎忙到系统协作.md
      vol2-自动写作到SOP组合.md
      vol3-35角色在线只有一人换帽.md
      vol4-给AI装上海马体.md
    hermes-system-series/
      vol1-cognition.md
      vol2-memory.md
      vol3-architecture.md
      vol4-teams.md
      vol6-practice.md
    hermes-workbench/
      vol1.md ~ vol4.md
    season1/
      ep001.md ~ ep012.md
      code-drop-01.md
      code-drop-02.md
      code-drop-03.md
      final-bundle.md
      announcement.md
    agent-truth/
      agent-truth-1.md ~ agent-truth-5.md
    standalone/
      squeeze-gpt-sop.md
      single-instance-final.md
      single-instance-cover-article-final.md
      feishu-print-assistant.md
```

### 2.2 生产流程与 SOP

**设计目标路径：** 公众号发布 SOP、排版规范、发布流程文档作为可复用生产资产入仓。

| 文件 | 原始路径 | 入仓目标路径 |
|------|----------|-------------|
| PRODUCTION_CONSTITUTION.md | `maijian-wechat/` | `content-lab/sops/production-constitution.md` |
| MANUAL_PUBLISH_V3_PLAN.md | `maijian-wechat/` | `content-lab/sops/manual-publish-v3-plan.md` |
| RELEASE_PIPELINE_V2_ROADMAP.md | `maijian-wechat/` | `content-lab/sops/release-pipeline-v2-roadmap.md` |
| VALIDATED_WORKFLOW_V1.md | `maijian-wechat/` | `content-lab/sops/validated-workflow-v1.md` |
| WECHAT_LAYOUT_STANDARD.md | `maijian-wechat/` | `content-lab/sops/wechat-layout-standard.md` |
| HANDOFF_CONTRACT.md | `maijian-wechat/` | `content-lab/sops/handoff-contract.md` |
| PUBLISHING_CALENDAR.md | `maijian-wechat/` | `content-lab/sops/publishing-calendar.md` |
| ARTICLE_REQUEST_TEMPLATE.md | `maijian-wechat/` | `content-lab/sops/article-request-template.md` |
| ARTICLE_TYPE_ROUTER.md | `maijian-wechat/` | `content-lab/sops/article-type-router.md` |
| PUBLISH_CONFIRMATION_CARD.md | `maijian-wechat/` | `content-lab/sops/publish-confirmation-card.md` |
| SHORT_COMMAND_USAGE_V1.md | `maijian-wechat/` | `content-lab/sops/short-command-usage-v1.md` |

### 2.3 封面 Prompt 与设计规范

**设计目标路径：** 封面生成 Prompt、排版主题规范作为设计资产入仓。

| 文件 | 原始路径 | 入仓目标路径 |
|------|----------|-------------|
| COVER_SINGLE_IMAGE_V2_PLAN.md | `maijian-wechat/` | `content-lab/design/cover-single-image-v2-plan.md` |
| MAIJIAN_WECHAT_THEME_V1.md | `maijian-wechat/` | `content-lab/design/theme-v1.md` |
| MAIJIAN_WECHAT_THEME_V2_PROPOSAL.md | `maijian-wechat/` | `content-lab/design/theme-v2-proposal.md` |
| DRACO_ORIGINAL_STYLE_RECOVERY.md | `maijian-wechat/` | `content-lab/design/draco-original-style-recovery.md` |
| DRACO_STYLE_DEFAULT_V3.md | `maijian-wechat/` | `content-lab/design/draco-style-default-v3.md` |
| hermes-series-cover-prompts.md | `maijian-wechat/articles/` | `content-lab/design/hermes-series-cover-prompts.md` |
| feishu_media_team_cover_prompts_card.md | `maijian-wechat/articles/` | `content-lab/design/feishu-media-team-cover-prompts.md` |
| feishu_media_team_release_card.md | `maijian-wechat/articles/` | `content-lab/design/feishu-media-team-release-card.md` |
| wechat-style-story.yaml | `maijian-wechat/configs/` | `content-lab/design/wechat-style-story.yaml` |
| season1-final-bundle.png | `maijian-wechat/articles/` | `content-lab/design/assets/season1-final-bundle.png` |
| season1-ep011.png | `maijian-wechat/articles/` | `content-lab/design/assets/season1-ep011.png` |
| season1-ep012-cover.png | `maijian-wechat/articles/` | `content-lab/design/assets/season1-ep012-cover.png` |

### 2.4 病毒式传播与选题分析

| 文件 | 原始路径 | 入仓目标路径 |
|------|----------|-------------|
| one-person-one-team-viral-analysis.md | `maijian-wechat/knowledge/viral/` | `content-lab/research/viral/one-person-one-team-analysis.md` |
| wechat-hook-playbook-test.md | `maijian-wechat/knowledge/viral/` | `content-lab/research/viral/wechat-hook-playbook.md` |
| ARTICLE_05161810-hook-title-structure.md | `maijian-wechat/knowledge/viral/` | `content-lab/research/viral/hook-title-structure.md` |

### 2.5 排版工作台代表性制品

**设计目标路径：** 仅精选 3-5 个代表性排版预览入仓作为参考样例，其余留在本地。

| 文件 | 原始路径 | 入仓目标路径 |
|------|----------|-------------|
| squeeze-gpt-sop-workbench.html | `maijian-wechat/manual-publish-workbench/` | `content-lab/workbench/squeeze-gpt-sop-workbench.html` |
| style-compare-report.md | `maijian-wechat/manual-publish-workbench/` | `content-lab/workbench/style-compare-report.md` |
| draco-style-story.html | `maijian-wechat/manual-publish-workbench/` | `content-lab/workbench/draco-style-story.html` |
| style-compare-report.md | `maijian-wechat/canary-runs/mjw-20260521-final-public-pack-v3-1/style-restore-report.md` | `content-lab/workbench/style-restore-report.md` |

---

## 三、推荐留在 private repo 的资产组

**设计目标路径：** 未定稿、含内部审查信息、多版本迭代的草稿保留在 `maijian-wechat-private-repo`。

| 内容组 | 文件/目录 | 原始路径 | 保留理由 |
|--------|----------|----------|----------|
| Final Bundle 风险检查 | `final-bundle-risk-check.md` | `maijian-wechat-private-repo/articles/hermes-genesis-season1/final-bundle/` | 内部审查过程 |
| | `final-bundle-change-notes.md` | | |
| | `final-bundle-polished.md` | | 含审稿痕迹 |
| Final Public Pack 多版本草稿 | `final-public-pack-draft-v1.md` 至 `v3-1.md` | `maijian-wechat-private-repo/articles/hermes-genesis-season1/final-public-pack-article/` | 多版本迭代稿，未最终定稿 |
| Final Public Pack 变更日志 | `final-public-pack-change-notes-v2/v3.md` | | |
| Final Public Pack 风险检查 | `final-public-pack-risk-check-v1.md` | | |
| Final Public Pack 工作台 | `final-public-pack-workbench.html` | | 内部排版工具 |
| Final Public Pack 预览图 | `assets/` 下全部图片 | | 内部预览素材 |
| 发布检查单 | `final-bundle-publish-checklist.md` | `maijian-wechat-private-repo/publish/checklists/` | 内部发布流程 |
| 发布奖励文案 | `reward-delivery-copy.md` | `maijian-wechat-private-repo/publish/reward-delivery/` | 内部运营流程 |
| 任务包骨架 | `task-packs/` 全部 `.gitkeep` | `maijian-wechat-private-repo/task-packs/` | 模板骨架，未完成 |
| 发布脚本 | `build_wechat_copy_workbench.py` | `maijian-wechat-private-repo/scripts/` | 内部工具 |
| Release Candidates | `hermes-genesis-season1-practical-pack-v1.1/` | `maijian-wechat-private-repo/release-candidates/` | 候选发布包 |
| Packages | `hermes-genesis-minimal-pack-v0.1/` | `maijian-wechat-private-repo/packages/` | 资料包草案 |
| Local Dryrun Artifacts | `local-dryrun-artifacts/` | `maijian-wechat-private-repo/` | 本地试验产物 |
| Public Export Dryruns | `public-export-dryruns/` | `maijian-wechat-private-repo/` | 脱敏导出预演 |
| MANIFEST.md / CURRENT.md | 根目录 | `maijian-wechat-private-repo/` | 仓管理文件 |

---

## 四、仅本地保留资产组

**设计目标路径：** 本地归档或工作区内归档，不入任何远程仓库。

| 内容组 | 文件/目录 | 原始路径 | 保留理由 |
|--------|----------|----------|----------|
| Session 批次原始记录 | `materials/archive/session-batch-a/b/c-*.md` | `maijian-wechat/materials/archive/` | 个人工作日志，无公开价值 |
| 历史编排证据包 | `materials/archive/*-evidence-pack.md` | `maijian-wechat/materials/archive/` | 考证中间过程 |
| 每日复盘 | `materials/daily/2026-04-21.md` 等 | `maijian-wechat/materials/daily/` | 日常过程记录（Q8：精选 1-2 篇代表性复盘可入 content-lab） |
| Episode 原始素材 | `materials/episodes/episode-001.md` 等 | `maijian-wechat/materials/episodes/` | 未加工的原始素材 |
| 历史序列草稿 | `materials/archive/season1-final-sequence*.md` | `maijian-wechat/materials/archive/` | 过程草稿 |
| 历史时间线 | `materials/archive/timeline.md` | | 过程记录 |
| Docs 进度文件 | `docs/progress.md` | `maijian-wechat/docs/` | 过程追踪 |
| Canary 运行日志 | `backups/` 全部目录 | `maijian-wechat/backups/` | 历史预演快照 |
| Canary 运行详细 | `canary-runs/` 除精选外的全部 | `maijian-wechat/canary-runs/` | 技术预演记录 |
| Data 示例 | `data/examples/` | `maijian-wechat/data/` | 本地数据示例 |
| Preview 制品 | `maijian-wechat-previews/` | `~/projects/maijian-wechat-previews/` | 独立预览项目 |
| .bak / .bak_* 文件 | 全部 `.bak` 后缀 | 散落在 `articles/` | 自动备份副本 |
| `.new` 文件 | `2026-05-agent-truth-{1,2,3,4,5}.md.new` | `maijian-wechat/articles/` | 未保存的工作区副本 |

**Q8 daily-style 精选建议：** 从 `materials/daily/` 中最多选 2 篇（如 `2026-04-22.md` 可能是关键节点日）进入 content-lab 的 `content-lab/retrospectives/`，其余保留本地。

---

## 五、禁止入仓资产组

**设计目标路径：** 这些资产禁止进入任何远程仓库。

| 内容组 | 标识特征 | 原始路径 | 禁止理由 |
|--------|----------|----------|----------|
| 0 字节空文件 | `FinalBundle.md` (0 bytes) | `maijian-wechat/articles/` | Q9: 可清理候选 |
| | `CodeDrop02.md` (0 bytes) | | |
| | `EP011.md` (0 bytes) | | |
| 真实发布 ID | 含真实 `media_id` / `draft_media_id` / `thumb_media_id` 的文件 | `data/publish_map.jsonl`, `canary-runs/*/publish-log*.json`, `canary-runs/*/dry-run*.json` | Q10: 真实发布 ID 需脱敏，原件不入仓 |
| 敏感配置 | 含 token/API key 的文件 | `~/.maijian-token`, 任何 `.env` | 认证凭据 |
| 飞书文档链接（含内部 token） | 含 `feishu.cn/docx/` 的内部文档索引 | `docs/*.md` 中的链接 | 内部协作文档，不公开 |

---

## 六、去重矩阵

### 6.1 Q2 单实例系列去重矩阵

| 候选 | 文件 | 行数 | 状态 | 推荐 |
|------|------|------|------|------|
| 主版本 | `2026-04-17-single-instance-final.md` | ~完整 | **最终稿** | **入仓主版本** |
| 草稿1 | `2026-04-17-single-instance-draft.md` | ~完整 | 草稿 | drafts/ (private) |
| 封面文章 | `2026-04-17-single-instance-cover-article-final.md` | ~完整 | 封面配套文章 | 入仓（互补资产） |
| 计划文档 | `2026-04-17-series-plan-single-instance.md` | ~完整 | 规划文档 | private repo |

### 6.2 Q3 GPT-squeeze 7-way 去重矩阵

| 候选 | 文件 | 行数 | 状态 | 推荐 |
|------|------|------|------|------|
| 主版本 | `20260528-squeeze-gpt-sop.md` | ~完整 | **最终发布稿** | **入仓主版本** |
| 候选2 | `drafts/gpt-squeeze-final.md` | ~完整 | 最终草稿 | drafts/archive (private) |
| 候选3 | `drafts/20260527-squeeze-gpt-sop.md` | ~完整 | v1 草稿 | drafts/archive (private) |
| 候选4 | `drafts/20260527-gpt-squeeze-v4-full.md` | ~完整 | v4 完整版 | drafts/archive (private) |
| 候选5 | `articles/20260527-squeeze-gpt-sop.md` | ~完整 | 旧版 | drafts/archive (private) |
| 候选6 | `manual-publish-workbench/draft-gpt-subscription-company-workbench.html` | HTML | 排版工作台 | 仅本地 |
| 候选7 | `articles/draft-gpt-subscription-company.md` | ~完整 | 姊妹篇草稿 | drafts/archive (private) |

### 6.3 Q4 麦尖 Vol vs Agent Truth 重叠分析

| 主题 | 麦尖 Vol 版本 | Agent Truth 版本 | 内容关系 | 主版本推荐 |
|------|--------------|-----------------|----------|------------|
| 群聊/团队协作 | `麦尖-vol1-群聊瞎忙到系统协作.md` (540行) | `2026-05-agent-truth-1.md` (533行) | 同一主题不同包装 | 麦尖 Vol 版（公众号栏目包装） |
| AI 订阅/额度管理 | `麦尖-vol2-自动写作到SOP组合.md` (624行) | `2026-05-agent-truth-2.md` (270行) | 不同子主题 | 两篇可共存（不重复） |
| AI 团队/角色分工 | `麦尖-vol3-35角色在线只有一人换帽.md` (627行) | `2026-05-agent-truth-3.md` (323行) | 同一主题不同详略 | 麦尖 Vol 版（更详实） |
| AI 记忆/持久化 | `麦尖-vol4-给AI装上海马体.md` (702行) | `2026-05-agent-truth-4.md` (409行) | 同一主题不同详略 | 麦尖 Vol 版（更详实） |
| 传播基准测试 | 无对应 Vol | `2026-05-agent-truth-5.md` (431行) | 独有内容 | Agent Truth 版 |

**结论：** 麦尖 Vol = 公众号正式栏目包装（详实版），Agent Truth = 主题系列精简版。content-lab 优先保留麦尖 Vol 版本作为主版本，Agent Truth 版本如内容差异显著可保留为补充版。

### 6.4 Season 1 多版本去重矩阵

| EP | 原始版 | v2 重写 | v3 重写 | 推荐主版本 |
|----|--------|---------|---------|-----------|
| EP001 | `season1-ep001.md` | `season1-ep001-v2.md` | `season1-ep001-v3.md` | 待总控确认 |
| EP002 | `season1-ep002.md` | `season1-ep002-v2.md` | `season1-ep002-v3.md` | 待总控确认 |
| EP003 | `season1-ep003.md` | `season1-ep003-v2.md` | `season1-ep003-v3.md` | 待总控确认 |
| EP004 | `season1-ep004.md` | `season1-ep004-v2.md` | `season1-ep004-v3.md` | 待总控确认 |
| EP005 | `season1-ep005.md` | `season1-ep005-v2.md` | `season1-ep005-v3.md` | 待总控确认 |
| EP006 | `season1-ep006.md` | `season1-ep006-v2.md` | `season1-ep006-v3.md` | 待总控确认 |
| EP007 | `season1-ep007.md` | `season1-ep007-v2.md` | `season1-ep007-v3.md` | 待总控确认 |
| EP008 | `season1-ep008.md` | `season1-ep008-v2.md` | `season1-ep008-v3.md` | 待总控确认 |
| EP009 | `season1-ep009.md` | `season1-ep009-v2.md` | `season1-ep009-v3.md` | 待总控确认 |
| EP010 | `season1-ep010.md` | `season1-ep010-v2.md` | `season1-ep010-v3.md` | 待总控确认 |
| EP011 | `season1-ep011.md` | `season1-ep011-v2.md` | `season1-ep011-v3.md` | 待总控确认 |
| EP012 | `season1-ep012.md` | `season1-ep012-v2.md` | `season1-ep012-v3.md` | 待总控确认 |
| Code Drop 01 | `season1-code-drop-01-foundation.md` | - | `season1-code-drop-01-v3.md` | 待总控确认 |
| Code Drop 02 | `season1-code-drop-02-workbench.md` | - | `season1-code-drop-02-v3.md` | 待总控确认 |
| Final Bundle | `season1-final-bundle.md` | - | `season1-final-bundle-v3.md` | 待总控确认 |

**策略：** 按 Q2 规则，不删除任何版本。建立 `articles/season1/` 目录下的主版本 + `drafts/archive/season1-v2-rewrites/` + `drafts/archive/season1-v3-rewrites/` 三层结构。

---

## 七、分流建议

### 7.1 三分流模型

```
maijian-wechat (工作区)
  |
  +-- [流入] content-lab (正式内容资产仓)
  |     条件：已发布稿 / 最终定稿 / 正式 SOP / 设计规范 / 可公开资产
  |     比例：约 15-20% 文件
  |
  +-- [流入] maijian-wechat-private-repo (私有内容资产仓)
  |     条件：未公开文章 / 多版本草稿 / 内部审查 / 发布过程记录
  |     比例：约 25-30% 文件
  |
  +-- [本地保留] maijian-wechat (工作区) 或本地归档
        条件：原始素材 / 日志 / 自动备份 / Canary 制品 / 过程草稿
        比例：约 50-60% 文件
```

### 7.2 入仓前检查清单

进入 content-lab 的每个文件需满足：
- [ ] 是最终稿/已发布稿/官方最终版本（Q1: S1 版本选择）
- [ ] 不含真实 `media_id` / `draft_media_id` / `thumb_media_id`（Q10）
- [ ] 不含 token / API key / 认证信息
- [ ] 不为 0 字节（Q9）
- [ ] 在去重矩阵中已被推荐为主版本（Q2/Q3/Q4）
- [ ] 如为 Vol vs Agent Truth 重叠，已确认麦尖 Vol 优先（Q4）

---

## 八、需要总控裁决的问题

### C1: Season 1 主版本选择
12 篇 EP + 3 篇 Code Drop + Final Bundle 各有 3 个版本（原始/v2/v3）。
**建议：** 按 Q1 规则，如已有已发布版本则选已发布版；如均未发布则选 v3 为候选主版本。
**需总控确认：** 是否全部 Season 1 内容已发布？如未发布，哪一版本为最终候选？

### C2: Agent Truth vs 麦尖 Vol 的最终策略
两系列覆盖相同主题但包装不同。
**建议：** content-lab 保留麦尖 Vol 作为主版本（公众号栏目），Agent Truth 作为补充版保留在 private repo。
**需总控确认：** 是否需要将 Agent Truth 精简版也入仓作为"快速阅读版"？

### C3: drafts/ 目录的整理策略
工作区 `drafts/` 包含 9 个文件，全部为各种草稿。
**建议：** 全部保留本地，不入任何远程仓。
**需总控确认：** 是否有需要提炼入仓的草稿？

### C4: Hermes System Series vs Hermes Workbench Series 的关系
两套 Vol 系列（hermes-system-series-vol1-4 vs hermes-series-vol1-4,6）主题有重叠。
**建议：** 两套均为正式文章，均入仓，但需总控确认是否存在内容重复。
**需总控确认：** 两套是否为同一系列的不同包装？是否需要合并？

### C5: content-lab 目录结构的最终方案
本文档给出了建议的入仓路径结构。
**需总控确认：** 目录结构是否按「系列」分组，还是按「栏目」（麦尖 Vol / Hermes / 独立文章）分组？

### C6: canary-runs 与 backups 的保留策略
约 30 个预演快照分布在两个目录。
**建议：** 仅精选 1-2 个代表性预演入 content-lab/workbench/，其余本地保留。
**需总控确认：** 是否有技术价值需要保留全部 canary 历史？

### C7: knowledge/domain/ 的入仓判断
`knowledge/domain/2026-04-23-ai-topic-seed-test.md` 为选题种子。
**建议：** 入仓至 `content-lab/research/`。
**需总控确认：** 选题种子是否属于可公开内容资产？

### C8: 每日复盘精选
Q8 要求精选 3-5 篇代表性复盘。`materials/daily/` 仅有 3 篇（04-21, 04-22, 04-23）。
**建议：** 3 篇全部精选入仓，因为数量刚好在范围内。
**需总控确认：** 这 3 天的复盘是否具有代表性？

---

## 九、下一步建议

### 短期（本轮）
1. **总控确认 C1-C8 裁决项** -- 特别是 Season 1 主版本选择和 Vol/Agent Truth 策略
2. **创建 content-lab 目录骨架** -- 按本文档第 2 节建议的结构创建空目录
3. **标记 0 字节文件** -- `FinalBundle.md`、`CodeDrop02.md`、`EP011.md` 列为可清理候选（Q9），等待确认后决定是否删除
4. **脱敏 publish_map.jsonl** -- 如有需要，生成脱敏结构样例入仓（Q10）

### 中期
5. **执行文件迁移（模拟）** -- 不实际移动文件，先建立 content-lab 内的索引文件（如 `CONTENT_ROUTING_INDEX.md`），用相对引用指向工作区文件
6. **完成去重矩阵标注** -- 为每个去重组标注「主版本」和「替代版本」字段
7. **建立 content-lab 入仓 SOP** -- 基于本文档第五节的禁止规则，编写入仓验收检查单

### 长期
8. **定期归档流程** -- 建立「已发布文章自动入仓」的 Cron/脚本流程
9. **版本清理计划** -- 当 v2/v3 重写稿被正式采用后，清理旧版本
10. **aoxue-media 只读索引** -- 对 `~/projects/aoxue-media/` 建立只读引用索引（Q8: 本轮只读不提交不清理）

---

## 附录：文件统计

| 分类 | 文件数 | 占比 |
|------|--------|------|
| articles/ 总文件 | ~170 | 100% |
| 其中正式稿/最终稿 | ~35 | ~20% |
| 其中 v2 重写稿 | ~14 | ~8% |
| 其中 v3 重写稿 | ~17 | ~10% |
| 其中草稿/草案 | ~30 | ~18% |
| 其中封面/图片资产 | ~10 | ~6% |
| 其中 .bak/.new | ~10 | ~6% |
| 其中 0 字节空文件 | 3 | ~2% |
| 其中编辑计划/SOP | ~5 | ~3% |
| docs/ 总文件 | ~30 | -- |
| materials/ 总文件 | ~30 | -- |
| knowledge/ 总文件 | 4 | -- |
| canary-runs/ 运行数 | ~10 | -- |
| backups/ 运行数 | ~20 | -- |

---

*本方案为 v1 草案，待总控裁决后更新。所有路径均为相对路径示意，实际迁移需以绝对路径执行。*
