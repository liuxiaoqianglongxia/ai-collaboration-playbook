# maijian-wechat 资产价值审计 v1

> 日期: 2026-05-30
> 审计人: hermes (Claude Code)
> 级别: H-C 只读高层分类，不读正文内容
> 范围: `maijian-wechat` + `maijian-wechat-private-repo`

---

## 1. 审计范围

| 项目 | 路径 |
|---|---|
| 主仓库 | `/home/hermes/projects/maijian-wechat/` |
| 私有仓库 | `/home/hermes/projects/maijian-wechat-private-repo/` |

- `maijian-wechat`: 139 个文件 (articles/), 28 个子目录, 21 根目录文档
- `maijian-wechat-private-repo`: 14 个子目录, 4 根目录文档

## 2. 读取的安全文件

| 文件 | 用途 |
|---|---|
| `README.md` (两项目) | 项目定位说明 |
| `PRODUCTION_CONSTITUTION.md` | 生产宪法，流水线规则 |
| `HANDOFF_CONTRACT.md` | 交接契约格式 |
| `WECHAT_LAYOUT_STANDARD.md` | 排版规范 |
| `data/publish_map.jsonl` (前 3 行) | 发布映射结构 |
| 各目录 `ls` 清单 | 仅文件名列举，无内容读取 |

**未读取（禁止项）**: `.env`, `auth.json`, `*.db`, `logs`, `backups`, 任何文章正文内容, `feishu-doc-mapping.json` 中的敏感映射。

## 3. 资产评分表

评分维度 (1-5): 复用价值 | 当前完整度 | 整合难度 | 风险程度 | 业务相关度 (反向: 5=高风险)

### 3.1 主仓库 maijian-wechat

| # | 资产 | 复用 | 完整 | 整合 | 风险 | 业务 | 总分 | 等级 |
|---|---|---|---|---|---|---|---|---|
| A1 | PRODUCTION_CONSTITUTION.md | 5 | 5 | 2 | 2 | 5 | 19 | B |
| A2 | HANDOFF_CONTRACT.md | 5 | 5 | 2 | 1 | 5 | 18 | B |
| A3 | WECHAT_LAYOUT_STANDARD.md | 5 | 5 | 2 | 1 | 5 | 18 | B |
| A4 | articles/ (已发布/正式稿) | 4 | 4 | 3 | 2 | 5 | 18 | B |
| A5 | articles/ (连载系列 vol1-6, ep001-012) | 4 | 5 | 3 | 2 | 5 | 19 | B |
| A6 | articles/hermes-genesis-season1/ | 4 | 4 | 3 | 2 | 5 | 18 | B |
| A7 | scripts/ 发布流水线 (21 脚本) | 4 | 4 | 3 | 3 | 5 | 19 | B |
| A8 | data/publish_map.jsonl | 3 | 4 | 4 | 4 | 5 | 20 | A |
| A9 | canary-runs/ (2 次完整跑) | 3 | 3 | 4 | 4 | 4 | 18 | B |
| A10 | visuals/ 封面 Prompt (13 文件) | 4 | 4 | 3 | 1 | 4 | 16 | B |
| B1 | docs/ 工作流文档 (~28 文件) | 4 | 3 | 3 | 1 | 4 | 15 | B |
| B2 | reviews/ 审稿报告 (~54 文件, 含 daily-style) | 3 | 3 | 3 | 1 | 3 | 13 | C |
| B3 | manual-publish-workbench/ (11 HTML) | 3 | 3 | 4 | 1 | 4 | 15 | B |
| B4 | configs/wechat-style-story.yaml | 3 | 3 | 3 | 1 | 4 | 14 | C |
| B5 | knowledge/ domain + viral | 3 | 2 | 3 | 1 | 3 | 12 | C |
| B6 | prompts/ 封面 brief | 3 | 3 | 3 | 1 | 3 | 13 | C |
| B7 | materials/ archive+daily+episodes+style+weekly | 2 | 2 | 4 | 1 | 3 | 12 | C |
| C1 | drafts/ (9 份草稿) | 2 | 2 | 4 | 2 | 3 | 13 | C |
| C2 | previews/ (4 预览 HTML+JSON) | 1 | 2 | 4 | 2 | 3 | 12 | C |
| C3 | inbox/ (1 文件) | 1 | 1 | 5 | 1 | 2 | 10 | C |
| C4 | wechat-drafts/ + wechat-drafts-rich/ | 2 | 2 | 4 | 4 | 3 | 15 | B |
| D1 | backups/ (28 个备份快照) | 1 | 1 | 5 | 3 | 1 | 11 | C |
| D2 | .new / .bak / .bak_ 临时文件 (多篇) | 1 | 1 | 5 | 1 | 1 | 9 | D |
| D3 | hermes-genesis-season1 (articles 子目录, 含 rewrite) | 3 | 3 | 4 | 2 | 4 | 16 | B |
| X1 | feishu-doc-mapping.json (含真实飞书链接/ID) | - | - | - | - | - | X | X |

### 3.2 私有仓库 maijian-wechat-private-repo

| # | 资产 | 复用 | 完整 | 整合 | 风险 | 业务 | 总分 | 等级 |
|---|---|---|---|---|---|---|---|---|
| P1 | README.md + CURRENT.md + MANIFEST.md | 3 | 4 | 2 | 1 | 4 | 14 | C |
| P2 | articles/hermes-genesis-season1/ | 4 | 4 | 3 | 2 | 5 | 18 | B |
| P3 | publish/ (checklist, format-audit, reward-delivery) | 3 | 3 | 3 | 1 | 4 | 14 | C |
| P4 | release-candidates/ (v1.1 pack + zip) | 3 | 4 | 3 | 2 | 4 | 16 | B |
| P5 | packages/ (minimal + practical pack) | 4 | 3 | 3 | 2 | 4 | 16 | B |
| P6 | task-packs/ (4 模板骨架) | 3 | 2 | 3 | 1 | 3 | 12 | C |
| P7 | cover/ prompts (空) | 1 | 1 | 5 | 1 | 2 | 10 | C |
| P8 | scripts/build_wechat_copy_workbench.py | 3 | 3 | 3 | 2 | 4 | 15 | B |
| P9 | public-export-dryruns/ | 2 | 2 | 4 | 2 | 3 | 13 | C |
| P10 | local-dryrun-artifacts/ (1 zip) | 2 | 2 | 4 | 2 | 3 | 13 | C |

## 4. A 类资产 (20-25 分)

### publish_map.jsonl (A8, 20 分)
- **内容**: 2 条完整发布记录，含 article_id, title, local_md_path, SHA256, feishu 链接, cover, thumb_media_id, draft_media_id, status, confirmed_by
- **价值**: 发布链路唯一结构化真值源，审计追溯必须
- **整合**: 需脱敏 (feishu_doc_url, thumb_media_id, draft_media_id, wechat_api_proxy) 后方可入仓
- **建议**: 脱敏后进入 `maijian-wechat-content-lab` 的 `data/publish_map/` 目录

## 5. B 类资产 (15-19 分)

### 文章资产 (已发布/正式稿)
- `articles/` 中约 40+ 份正式/连载文章 (season1-ep001~012, vol1-6, agent-truth 系列, hermes-system-series)
- `articles/hermes-genesis-season1/` 子目录含最终打包产物
- **复用价值**: 核心内容资产，可直接用于内容仓
- **建议**: 整体入仓 `maijian-wechat-content-lab/articles/`

### 发布链路 (scripts/)
- 21 个脚本: preflight, canary, publish_bundle, validate_publish_map, cover_single, release_v2, manual_publish
- **价值**: 自动化发布工具链，可复用
- **建议**: 入仓 `maijian-wechat-content-lab/scripts/publish/`

### 封面 Prompt (visuals/)
- 13 个封面 prompt 文件 (按文章/批次组织)
- **价值**: 封面设计可复用 Prompt 模板
- **建议**: 入仓 `maijian-wechat-content-lab/visuals/covers/`

### 生产规则文档
- PRODUCTION_CONSTITUTION.md, HANDOFF_CONTRACT.md, WECHAT_LAYOUT_STANDARD.md
- 以及: ARTICLE_TYPE_ROUTER.md, MAIJIAN_WECHAT_THEME_V1/V2, PUBLISH_MAP_V2_DESIGN, VALIDATED_WORKFLOW_V1, PUBLISH_CONFIRMATION_CARD, RELEASE_PIPELINE_V2_ROADMAP, MANUAL_PUBLISH_V3_PLAN, DRACO_STYLE_DEFAULT_V3
- **建议**: 入仓 `maijian-wechat-content-lab/docs/governance/`

### 工作流文档 (docs/)
- ~28 个设计文档/进度报告/索引
- **建议**: 精选入仓，去重后的核心流程文档入 `maijian-wechat-content-lab/docs/workflow/`

### 审稿报告 (reviews/)
- 约 54 个文件，含 daily-style 日常风格追踪 (~25 天), chief-editor 审稿报告, tech-materials
- **价值**: 风格一致性审计线索
- **建议**: daily-style 系列保留近期 30 天精华，历史版入 `maijian-wechat-content-lab/qa/reviews/`

### manual-publish-workbench/
- 11 个 HTML 工作台预览文件
- **建议**: 入仓 `maijian-wechat-content-lab/previews/workbench/`

### 私有仓库关键资产
- articles/hermes-genesis-season1/ -> 入 content-lab
- release-candidates/ -> 入 content-lab/releases/
- packages/ -> 入 content-lab/packages/
- publish/ checklists -> 入 content-lab/docs/publish-checklists/

## 6. C/D 类资产 (1-14 分)

### C 类 (临时/缓存/低优先级但可保留)
- `drafts/` (9 份草稿) -> 已废弃的中间稿，保留但标记为草稿
- `previews/` (4 预览) -> 历史预览，已过时
- `inbox/` (1 文件) -> 收件箱，需确认是否已处理
- `configs/` (1 yaml) -> 样式配置，可复用
- `knowledge/` (domain + viral) -> 知识库骨架，尚不完整
- `prompts/` -> 封面 brief，少量
- `materials/` -> 素材归档，需整理
- `backups/` (28 个) -> 自动备份，不入仓但建议本地保留
- 私有仓库: task-packs (空骨架), cover/ (空), public-export-dryruns, local-dryrun-artifacts

### D 类 (应清理)
- 所有 `.new`, `.bak`, `.bak_*` 临时文件 (~10+ 个) -> 建议清理或合并到 git history
- `hermes-genesis-season1` articles 目录下的 `season1-rewrite-v2/`, `season1-rewrite-v3/` -> 旧版重写中间态

## 7. X 类禁止入仓

| 资产 | 原因 |
|---|---|
| `feishu-doc-mapping.json` | 含真实飞书文档 URL 和 ID，敏感映射 |
| `data/publish_map.jsonl` 原始文件 | 含 `wechat_api_proxy` 内网 IP、`thumb_media_id`、`draft_media_id`、飞书链接 -> 需脱敏后方可入仓 |
| `canary-runs/*/` 中的 dry-run JSON | 含真实微信 media_id、草稿 ID -> 需脱敏 |
| 任何 `.env` 文件 | 凭据 |
| `wechat-drafts/publish-results.json` | 可能含真实发布结果和 media_id |
| `backups/` 完整目录 | 批量备份，含重复和中间态 |

## 8. 分类判断

| 类别 | 判断标准 | 示例 |
|---|---|---|
| **文章资产** | 正式稿/连载终稿/已发布稿 | articles/ 中非 draft 前缀的 .md |
| **发布链路** | 脚本 + 映射 + canary | scripts/, data/publish_map.jsonl, canary-runs/ |
| **封面 Prompt** | 封面设计 prompt | visuals/, prompts/ |
| **预览/缓存/临时** | 中间产物，非终稿 | drafts/, previews/, *.bak, *.new, backups/ |
| **应保留但暂不入仓** | 有价值但需整理 | knowledge/, materials/, reviews/daily-style 历史 |
| **应清理但需人工确认** | 旧版中间态 | season1-rewrite-v2/, rewrite-v3/, .bak 文件 |

## 9. 建议进入 maijian-wechat-content-lab 的资产

```
maijian-wechat-content-lab/
  articles/                    # 所有正式文章 (约 40+ .md)
    hermes-genesis-season1/   # 连载系列子目录
  docs/
    governance/               # PRODUCTION_CONSTITUTION, HANDOFF_CONTRACT, LAYOUT_STANDARD, THEME 等
    workflow/                 # 精选 docs/ 工作流文档
    publish-checklists/       # 私有仓库 publish/ 内容
  scripts/publish/            # 21 个发布脚本
  visuals/covers/             # 封面 Prompt
  qa/reviews/                 # 精选审稿报告
  data/publish_map/           # 脱敏后的 publish_map.jsonl
  releases/                   # release-candidates/
  packages/                   # packages/ 内容包
  previews/workbench/         # manual-publish-workbench HTML
```

## 10. 需要总控裁决的问题

1. **publish_map.jsonl 脱敏策略**: 需要决定哪些字段必须脱敏 (wechat_api_proxy IP, media_id, draft_media_id, feishu_doc_url) 后才能入公开仓
2. **backups/ 去留**: 28 个备份快照是全部保留、只保留最近 N 个、还是完全不入仓？
3. **reviews/daily-style 系列**: 25+ 天每日风格报告是全部入仓还是只保留精华摘要？
4. **wechat-drafts/ + wechat-drafts-rich/**: 含 payloads 和 previews，是否入仓？可能含微信 API 敏感字段
5. **私有仓库与主仓库的文章重复**: articles/hermes-genesis-season1 在两个仓库都存在，入仓时如何合并？
6. **.bak/.new 临时文件清理**: 是否可以安全删除还是需要归档？
7. **knowledge/ 和 materials/**: 当前结构较零散，是原样入仓还是先整理？

## 11. 下一步建议

1. **P0**: 确认 publish_map.jsonl 脱敏规则，生成脱敏副本
2. **P0**: 将 PRODUCTION_CONSTITUTION.md + HANDOFF_CONTRACT.md + WECHAT_LAYOUT_STANDARD.md 入仓 (无敏感信息)
3. **P1**: 批量迁移 articles/ 正式稿到 content-lab (排除 draft/ .bak/ .new 文件)
4. **P1**: 迁移 scripts/ 发布工具链到 content-lab
5. **P1**: 迁移 visuals/ 封面 Prompt 到 content-lab
6. **P2**: 整理 reviews/ 审稿报告，保留核心审计文档
7. **P2**: 清理 .bak/.new 临时文件 (确认后)
8. **P2**: 裁决上述 7 个总控问题后执行剩余迁移
