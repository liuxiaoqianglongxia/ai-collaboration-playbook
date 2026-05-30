# Private Repo Boundary Audit: maijian-wechat vs maijian-wechat-private-repo

审计日期: 2026-05-30
审计人: Sub-agent F (Private Repo Boundary Audit)
远程仓: github.com/liuxiaoqianglongxia/maijian-wechat.git

## 1. 审计范围

对比两个仓库:
- **maijian-wechat** (aoxue-media.git): 公开仓，GitHub 远程 `aoxue-media.git`，4 commits，包含文章、审核报告、飞书发布流程、微信排版、脚本等完整公众号生产资产。
- **maijian-wechat-private-repo** (maijian-wechat.git): 私有仓，GitHub 远程 `maijian-wechat.git`，10 commits，包含文章终稿、资料包、发布清单、奖励交付物等。

目标: 明确两仓的职责边界，识别重复内容，提出分流建议。

## 2. public repo 职责判断

**远程仓**: `https://github.com/liuxiaoqianglongxia/aoxue-media.git`

**定位**: 公众号生产全流程工作台 (尽管 README 描述为 "公开项目"，但实际包含大量生产中间态资产)。

**核心内容**:
| 类别 | 目录/文件 | 说明 |
|------|-----------|------|
| 文章草稿/终稿 | `articles/` (120+ files) | Hermes Genesis 全系列、Agent Truth 系列、Code Drop 等 |
| 审核报告 | `reviews/` (50+ files) | 每日 style review、技术材料审核、排版审核 |
| 发布流程脚本 | `scripts/` (17 files) | Canary、preflight、cover、publish 测试 |
| 微信草稿 payload | `wechat-drafts/`, `wechat-drafts-rich/` | 微信公众号 API payload JSON |
| 生产规范/流程文档 | 根目录 25 个 `.md` | HANDOFF_CONTRACT, PRODUCTION_CONSTITUTION, VALIDATED_WORKFLOW_V1 等 |
| 知识库 | `knowledge/` | 领域种子、爆款分析 |
| 素材管道 | `materials/` | 原始素材、分集素材 |
| 封面提示词 | `visuals/` | 各系列封面 prompt |
| Canary 运行记录 | `canary-runs/` | 发布链 Canary 运行 JSON/txt 日志 |
| 备份快照 | `backups/` (15 dirs) | 各阶段备份，含 SHA256SUMS |
| 多实例实验 | `multi-instance-pilot/` | 角色机器人注册、协作测试 |
| 飞书文档映射 | `feishu-doc-mapping.json` | 飞书文档 ID 映射 |
| 数据/配置 | `data/`, `configs/` | publish_map.jsonl, wechat-style-story.yaml |

**判断**: public repo 实际承载了**全部生产中间态资产**，包括大量草稿、审核报告、canary 日志、备份快照。它名义上是 "public"，但包含大量不应公开的中间产物。

## 3. private repo 职责判断

**远程仓**: `https://github.com/liuxiaoqianglongxia/maijian-wechat.git`

**定位**: 内部协作事实源 (per README: "Private production repository")。

**核心内容**:
| 类别 | 目录/文件 | 说明 |
|------|-----------|------|
| 文章终稿 | `articles/hermes-genesis-season1/final-bundle/` | final-bundle-polished.md + change-notes + risk-check |
| 文章终稿 | `articles/hermes-genesis-season1/final-public-pack-article/` | 5 个版本的 final-public-pack draft + change-notes + risk-check |
| 实战资料包 | `packages/hermes-genesis-season1-practical-pack/` (12 子目录) | 10 章节脱敏实战资料包 (README, 阅读路线, 基础规范, team-boss, 案例, 角色系统, Dashboard, 可复制提示词, 翻车点, FAQ, demo 项目) |
| 最小资料包 | `packages/hermes-genesis-minimal-pack-v0.1/` | 最小包定位 + 文件树 |
| 发布清单 | `publish/checklists/`, `publish/reward-delivery/` | 发布检查清单、奖励交付文案 |
| Release candidates | `release-candidates/hermes-genesis-season1-practical-pack-v1.1/` | v1.1 zip (61KB) + RELEASE_MANIFEST + delivery-message + final-checklist |
| 公共导出预览 | `public-export-dryruns/hermes-genesis-season1-pack-v0.1/` | v0.1 公共导出预览 (与 packages 内容同构，英文目录名) |
| 索引文件 | CURRENT.md, MANIFEST.md, README.md | 当前状态、持久索引、操作契约 |
| 脚本 | `scripts/build_wechat_copy_workbench.py` | 微信排版工作台构建脚本 |
| 空任务包 | `task-packs/` (4 dirs with .gitkeep) | 预留的任务包目录 |

**判断**: private repo 承载的是**终稿/可交付物/脱敏资料包/发布清单**。它的设计意图是 "内部协作事实源"，只保留经过审核的、可以提交给外部审核或发布的最终版本。

## 4. 重复内容识别

| 重复项 | public 位置 | private 位置 | 差异 |
|--------|-------------|-------------|------|
| build_wechat_copy_workbench.py | `scripts/build_wechat_copy_workbench.py` | `scripts/build_wechat_copy_workbench.py` | private 版本增加了 Draco style renderer 导入和 `--style` 参数，功能更完整 |
| final-bundle 文章 | `articles/final-bundle.md` | `articles/hermes-genesis-season1/final-bundle/final-bundle-polished.md` | 标题不同，内容有重叠但版本不同。public 版本标题为 "最终源码放送"，private 版本为 "最后一次源码放送"，属同一文章的不同迭代 |
| final-public-pack 文章 | public 无同名文件 | `articles/hermes-genesis-season1/final-public-pack-article/` 多个版本 | private 独有，是 final-bundle 的 "资料包公开版" 文章 |
| packages vs public-export-dryruns | -- | 两者同构 | `packages/hermes-genesis-season1-practical-pack/` 与 `public-export-dryruns/hermes-genesis-season1-pack-v0.1/` 内容同构，仅目录名中英文不同 (如 "00-先看我" vs "00-start-here")。v0.1 是早期导出，packages 是最新版本 |

**关键发现**: 没有精确重复的文件对，但有**同义不同版本**的文章 (final-bundle 有两个版本分别位于两仓)。

## 5. 哪些应迁入 maijian-wechat-content-lab

注: 当前系统中不存在 `maijian-wechat-content-lab` 仓库。以下假设将创建一个专门的 content-lab 仓库承接内容创作资产。

**应从 public repo (aoxue-media) 迁入 content-lab**:
- `articles/` 中的系列文章草稿和终稿 (Agent Truth, Hermes Genesis, Code Drop 等)
- `reviews/` 中的审核报告 (style review, tech review)
- `visuals/` 中的封面提示词
- `materials/` 中的原始素材和分集素材
- `knowledge/` 中的知识库
- `prompts/` 中的封面 prompt
- `editor-plan-*` 编辑计划文件
- `drafts/` 目录中的草稿

**理由**: 这些是**内容创作和审核**资产，属于 content-lab 的职责范围。

## 6. 哪些应留在 private repo

**应保留在 maijian-wechat-private-repo**:
- `articles/hermes-genesis-season1/final-bundle/` -- 已审核的终稿
- `articles/hermes-genesis-season1/final-public-pack-article/` -- 已审核的公开版文章终稿
- `packages/hermes-genesis-season1-practical-pack/` -- 脱敏后的实战资料包 (待发布)
- `packages/hermes-genesis-minimal-pack-v0.1/` -- 最小资料包
- `release-candidates/` -- 发布候选包 + zip
- `publish/checklists/` -- 发布检查清单
- `publish/reward-delivery/` -- 奖励交付文案
- `CURRENT.md`, `MANIFEST.md` -- 协作索引
- `scripts/build_wechat_copy_workbench.py` -- 排版工具脚本

**理由**: 这些是**可交付物/终稿/发布相关**资产，属于 production fact source 的职责。

## 7. 哪些不应进入任何远程仓

**应保留在本地 .gitignore 或清理**:

| 类别 | 位置 | 原因 |
|------|------|------|
| backups/ | public repo, 15 个备份目录 | 临时快照，应在发布后归档或删除，不需要推送到远程 |
| canary-runs/ | public repo | Canary 运行日志 (JSON/txt)，含可能的敏感信息 (sanitized 但不完全) |
| wechat-drafts/publish-results.json | public repo | 可能含发布结果中的敏感 ID |
| feishu-doc-mapping.json | public repo | 飞书文档 ID 映射，应保留在本地 |
| data/publish_map.jsonl | public repo | 发布映射，含可能的敏感信息 |
| previews/ | public repo | 本地 dryrun 产物，不需要推远程 |
| inbox/ | public repo | 收件箱，本地工作文件 |
| local-dryrun-artifacts/ | private repo | 本地 dryrun 产物 (.zip) |
| public-export-dryruns/ | private repo | 导出预览，与 packages 内容重复，可合并或删除 |

## 8. 分流建议

### 建议的三仓架构

| 仓库 | 职责 | 远程可见性 |
|------|------|-----------|
| **maijian-wechat-content-lab** (新建) | 内容创作: 草稿、审核报告、封面提示词、素材、编辑计划 | 公开 |
| **maijian-wechat-private-repo** (现有) | 生产事实源: 终稿、发布清单、脱敏资料包、Release candidates | 私有 |
| **hermes-genesis-season1-pack** (现有 public reader repo) | 面向读者的公开资料包 (接收 private repo 脱敏后的 packages) | 公开 |
| **aoxue-media** (现有 public repo) | 建议废弃或重定向到 content-lab | -- |

### 迁移路径

1. 创建 `maijian-wechat-content-lab`，将 `articles/`, `reviews/`, `visuals/`, `materials/`, `knowledge/`, `prompts/`, `drafts/` 移入
2. 清理 `backups/`, `canary-runs/`, `previews/`, `inbox/` -- 不移入新仓，本地保留或归档
3. `public-export-dryruns/` 合并到 `packages/` (保留最新版本，删除 v0.1 预览)
4. private repo 保留终稿和发布资产

## 9. 需要总控裁决的问题

1. **远程仓命名**: 当前 public repo 远程名为 `aoxue-media.git`，但本地目录为 `maijian-wechat`。是否需要统一命名？
2. **content-lab 是否新建**: 当前无 `maijian-wechat-content-lab` 目录。是否按三仓架构新建？还是复用现有 `maijian-wechat` 目录？
3. **a0xue-media.git 的命运**: 该远程仓是否继续作为主入口？还是废弃后将内容迁移到新仓？
4. **backups/ 和 canary-runs/**: 是否有保留价值？如无，可批量清理 (约 30+ 目录)。
5. **wechat-drafts/ vs wechat-drafts-rich/**: 两套微信草稿 payload 目录是否都在使用？rich 版本是否有增量价值？
6. **public-export-dryruns/ 冗余**: private repo 中 v0.1 导出预览与 packages 内容完全同构，是否删除 v0.1？
7. **build_wechat_copy_workbench.py**: 两仓各有一个版本 (private 版功能更全)。应保留在哪个仓？建议保留在 private repo (工具类)。

## 10. 下一步建议

1. **立即**: 将 `backups/` 和 `canary-runs/` 加入 `.gitignore`，防止更多临时文件被追踪
2. **低优先级**: 清理 public repo 根目录下散落的 25 个流程文档 (HANDOFF_CONTRACT, PRODUCTION_CONSTITUTION 等)，归类到统一目录
3. **需要决策后执行**: 按上述三仓架构分流，需要总控确认仓库命名和职责后批量迁移
4. **同步**: 确保 private repo 的 `final-bundle-polished.md` 与 public repo 的 `final-bundle.md` 合并为单一事实源
