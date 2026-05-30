# Article Assets Audit — maijian-wechat

**审计日期**: 2026-05-30
**审计范围**: `articles/`, `drafts/` 及所有文章-like 路径下的 `.md` 文件
**审计方法**: 仅读取各文件前 20 行，提取标题、YAML frontmatter、结构线索。不复制正文内容。
**安全文件**: 所有读取均为 `.md` 源文件。已跳过 `.env`, `.png`, `.jpg`, `.json`, `.stderr`, `.stdout` 等。

---

## 1. 审计范围

| 路径 | 文件数(.md) | 说明 |
|------|------------|------|
| `articles/` 根目录 | ~100 | 文章、草稿、策划、封面 prompt |
| `articles/hermes-genesis-season1/final-public-pack-article/` | 2 | final-public-pack 的两个版本 |
| `articles/season1-rewrite-v2/` | 12 | S1 EP001-012 的 v2 重写稿 |
| `articles/season1-rewrite-v3/` | ~30 | S1 EP001-012 的 v3 重写稿 + Code Drop + 辅助文档 |
| `drafts/` | 9 | 独立草稿 |
| **合计** | **~155** | 含 .new, .bak 占位 |

---

## 2. 资产评分表

### 2.1 A 类资产（正式文章，质量高，可入仓）

| # | 路径前缀 (articles/) | 标题 | Series | Type | 内容 | 完整 | 复用 | 安全 | 归仓 | 总分 | 等级 | Bucket | Notes |
|---|---------------------|------|--------|------|------|------|------|------|------|------|------|--------|-------|
| 1 | `2026-04-17-series-01-single-instance-vs-group-chat.md` | 别再让AI们群聊了... | single-instance | formal | 4 | 5 | 5 | 4 | 5 | 23 | A | content-lab | 系列破圈篇，已定稿 |
| 2 | `2026-04-17-series-02-how-one-ai-holds-49-roles.md` | 1个AI怎么装下49个角色 | single-instance | formal | 4 | 5 | 5 | 4 | 5 | 23 | A | content-lab | 系列方法篇，已定稿 |
| 3 | `2026-04-17-series-03-team-boss-mechanism.md` | 单实例到底怎么跑起来的 | single-instance | formal | 4 | 5 | 5 | 4 | 5 | 23 | A | content-lab | 系列机制篇，已定稿 |
| 4 | `2026-04-17-series-04-turn-ai-into-executor.md` | AI为什么总在问"然后呢"(规则版) | single-instance | formal | 4 | 5 | 5 | 4 | 5 | 23 | A | content-lab | 系列终篇，已定稿 |
| 5 | `2026-04-17-context-injection.md` | 每次开AI新会话都要重新教一遍 | hermes-v7-principles | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | v7原理系列第2篇 |
| 6 | `2026-04-17-ports-norms.md` | AI帮我写代码，结果端口全被占了 | hermes-v4-rules | formal | 4 | 5 | 4 | 4 | 5 | 22 | A | content-lab | 铁律系列端口篇 |
| 7 | `2026-04-17-role-injection.md` | 一条命令，让AI带着SOP进场 | hermes-v4-rules | formal | 4 | 5 | 4 | 4 | 5 | 22 | A | content-lab | 铁律系列注入篇 |
| 8 | `2026-04-27-macos-word-print-without-office.md` | Mac上Word打印问题 | standalone | formal | 4 | 5 | 3 | 4 | 5 | 21 | A | content-lab | 独立技术文，有实用价值 |
| 9 | `cod-drop-02.md` | 源码放送02:单实例总控多团队骨架 | hermes-genesis-s1 | formal | 4 | 4 | 5 | 4 | 4 | 21 | A | content-lab | 有YAML FM，已定稿 |
| 10 | `ep-011.md` | Dashboard出来以后系统才真在跑 | hermes-genesis-s1 | formal | 4 | 4 | 5 | 4 | 4 | 21 | A | content-lab | 有YAML FM，已定稿 |
| 11 | `final-bundle.md` | 最终源码放送:这一季文章和代码 | hermes-genesis-s1 | formal | 4 | 4 | 5 | 4 | 4 | 21 | A | content-lab | 有YAML FM，S1收官 |
| 12 | `season1-code-drop-01-foundation.md` | 从翻车到模板:基础工具包v0.1.0 | hermes-genesis-s1 | formal | 4 | 4 | 5 | 4 | 4 | 21 | A | content-lab | Code Drop 01 |
| 13 | `season1-code-drop-02-workbench.md` | 源码放送:单实例工作台骨架 | hermes-genesis-s1 | formal | 4 | 4 | 5 | 4 | 4 | 21 | A | content-lab | Code Drop 02 |
| 14 | `season1-code-drop-03-role-memory.md` | Code Drop 03:角色档案和记忆桶 | hermes-genesis-s1 | formal | 4 | 4 | 5 | 4 | 4 | 21 | A | content-lab | Code Drop 03 |
| 15 | `season1-ep001.md` | 刚下载Hermes那天以为会自己变聪明 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP001 定稿 |
| 16 | `season1-ep002.md` | 规范越来越多AI反而更懵了 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP002 定稿 |
| 17 | `season1-ep003.md` | README越写越厚AI反而更迷路 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP003 定稿 |
| 18 | `season1-ep004.md` | STATE.md从补丁变身份证 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP004 定稿 |
| 19 | `season1-ep005.md` | 术语表和目录规范比换模型重要 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP005 定稿 |
| 20 | `season1-ep006.md` | AI不是同事它需要工作台 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP006 定稿 |
| 21 | `season1-ep007.md` | 怀疑多Bot群聊这条路 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP007 定稿 |
| 22 | `season1-ep008.md` | 十几个Bot不如1个大脑 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP008 定稿 |
| 23 | `season1-ep009.md` | 一个AI怎么装下35个角色 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP009 定稿 |
| 24 | `season1-ep010.md` | 给AI装上海马体 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP010 定稿 |
| 25 | `season1-ep011.md` | Dashboard出来系统像工地 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP011 定稿 |
| 26 | `season1-ep012.md` | 系统开始写自己 | hermes-genesis-s1 | formal | 5 | 4 | 5 | 4 | 4 | 22 | A | content-lab | S1 EP012 定稿，有FM |
| 27 | `season1-final-bundle.md` | 最终源码放送 | hermes-genesis-s1 | formal | 4 | 4 | 5 | 4 | 4 | 21 | A | content-lab | S1 Bundle，有FM |
| 28 | `20260528-squeeze-gpt-sop.md` | 榨干GPT订阅:AI在GitHub开公司 | gpt-squeeze | formal | 4 | 5 | 4 | 4 | 5 | 22 | A | content-lab | 有YAML FM，近期新作 |
| 29 | `2026-05-agent-truth-1.md` | Vol1:解散十几个AI机器人留一个大脑 | agent-truth | formal | 4 | 5 | 4 | 4 | 5 | 22 | A | content-lab | 麦尖Vol系列，有FM |
| 30 | `2026-05-agent-truth-2.md` | Vol2:别被Multi-Agent骗了 | agent-truth | formal | 4 | 5 | 4 | 4 | 5 | 22 | A | content-lab | 麦尖Vol系列，有FM |
| 31 | `2026-05-agent-truth-3.md` | Vol3:招5人不如给1个大脑换5套工作服 | agent-truth | formal | 4 | 5 | 4 | 4 | 5 | 22 | A | content-lab | 麦尖Vol系列，有FM |
| 32 | `2026-05-agent-truth-4.md` | Vol4:给AI装海马体喂真实素材包 | agent-truth | formal | 4 | 5 | 4 | 4 | 5 | 22 | A | content-lab | 麦尖Vol系列，有FM |
| 33 | `2026-05-agent-truth-5.md` | Vol5:透明协作达摩院每一步stdout | agent-truth | formal | 4 | 5 | 4 | 4 | 5 | 22 | A | content-lab | 麦尖Vol系列，有FM |
| 34 | `麦尖-vol1-群聊瞎忙到系统协作.md` | Vol1:解散7个内容群留一个总控 | 麦尖-自媒体 | formal | 4 | 5 | 4 | 4 | 4 | 21 | A | content-lab | 自媒体Vol系列 |
| 35 | `麦尖-vol2-自动写作到SOP组合.md` | Vol2:试过4种自动写稿前3种翻车 | 麦尖-自媒体 | formal | 4 | 5 | 4 | 4 | 4 | 21 | A | content-lab | 自媒体Vol系列 |
| 36 | `麦尖-vol3-35角色在线只有一人换帽.md` | Vol3:35角色在线一人换帽 | 麦尖-自媒体 | formal | 4 | 5 | 4 | 4 | 4 | 21 | A | content-lab | 自媒体Vol系列 |
| 37 | `麦尖-vol4-给AI装上海马体.md` | Vol4:给AI装上海马体喂真实素材包 | 麦尖-自媒体 | formal | 4 | 5 | 4 | 4 | 4 | 21 | A | content-lab | 自媒体Vol系列 |
| 38 | `hermes-series-vol1-cognition.md` | Vol1:AI是聊天机器人还是打工团队 | hermes-system | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | 有完整结构，高复用 |
| 39 | `hermes-series-vol2-memory.md` | Vol2:给AI建1170条事实记忆大脑 | hermes-system | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | 有完整结构 |
| 40 | `hermes-series-vol3-architecture.md` | Vol3:三层体系让AI不再失忆 | hermes-system | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | 有完整结构 |
| 41 | `hermes-series-vol4-teams.md` | Vol4:一个AI干所有事拆成5团队 | hermes-system | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | 有完整结构 |
| 42 | `hermes-series-vol6-practice.md` | Vol6:奥学教育系统从0到100% | hermes-system | formal | 4 | 5 | 4 | 3 | 4 | 20 | A | content-lab | 有完整结构 |
| 43 | `hermes-v7-principles-01-core-engine.md` | AI的工位长什么样:核心引擎 | hermes-v7-principles | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | v7原理系列第1篇 |
| 44 | `hermes-v7-principles-02-context-injection.md` | AI工作台怎么搭:上下文注入 | hermes-v7-principles | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | v7原理系列第2篇 |
| 45 | `hermes-v7-principles-03-memory-compression.md` | AI记忆存在哪:记忆系统压缩 | hermes-v7-principles | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | v7原理系列第3篇 |
| 46 | `hermes-v7-principles-04-tools-skills.md` | AI工具箱里有什么:工具注册技能 | hermes-v7-principles | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | v7原理系列第4篇 |
| 47 | `hermes-v7-principles-05-delegation-gateway.md` | AI团队怎么分工:子代理分派 | hermes-v7-principles | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | v7原理系列第5篇 |
| 48 | `hermes-v7-principles-06-safety-runtime.md` | AI会不会失控:安全机制运行时 | hermes-v7-principles | formal | 4 | 5 | 5 | 4 | 4 | 22 | A | content-lab | v7原理系列第6篇终篇 |
| 49 | `hermes-feishu-print-assistant.md` | 飞书变打印入口:Hermes+macOS+CUPS | standalone | formal | 4 | 4 | 3 | 4 | 4 | 20 | A | content-lab | 有YAML FM |

### 2.2 B 类资产（有价值，需少量处理或去重）

| # | 路径前缀 | 标题 | Series | Type | 总分 | 等级 | Bucket | Notes |
|---|---------|------|--------|------|------|------|--------|-------|
| 50 | `season1-rewrite-v3/season1-ep001-v3.md` | 刚下载Hermes先立规矩 | hermes-genesis-s1-v3 | draft | 19 | B | content-lab | v3重写稿，有FM但author不同(DracoVibeCoding) |
| 51 | `season1-rewrite-v3/season1-ep002-v3.md` ~ `season1-ep010-v3.md` | v3重写EP002-010 | hermes-genesis-s1-v3 | draft | 19 | B | content-lab | v3重写系列，有FM但风格与v1差异大 |
| 52 | `season1-rewrite-v3/season1-ep011-v3.md` | EP011 Dashboard看见真实运行 | hermes-genesis-s1-v3 | formal | 19 | B | content-lab | v3版，author=麦尖AI有FM |
| 53 | `season1-rewrite-v3/season1-ep012-v3.md` | EP012 系统开始写自己 | hermes-genesis-s1-v3 | formal | 19 | B | content-lab | v3版，author=麦尖AI有FM |
| 54 | `season1-rewrite-v3/season1-final-bundle-v3.md` | v3最终源码放送 | hermes-genesis-s1-v3 | draft | 17 | B | content-lab | v3版Bundle，author=DracoVibeCoding |
| 55 | `season1-rewrite-v3/season1-code-drop-01-v3.md` | v3不去GitHub先复制导航层 | hermes-genesis-s1-v3 | draft | 17 | B | content-lab | v3 Code Drop |
| 56 | `season1-rewrite-v3/season1-code-drop-02-v3.md` | v3工作台源码放送 | hermes-genesis-s1-v3 | draft | 17 | B | content-lab | v3 Code Drop |
| 57 | `season1-rewrite-v2/season1-ep001-v2.md` ~ `season1-ep012-v2.md` | v2重写EP001-012 | hermes-genesis-s1-v2 | version-history | 18 | B | private-repo | 中间版本，内容完整但已被v1/v3替代 |
| 58 | `2026-04-17-single-instance-final.md` | 一个AI分身成49个人 | single-instance | formal | 18 | B | content-lab | 有完整正文，与series-01内容高度重叠 |
| 59 | `2026-04-17-single-instance-cover-article-final.md` | 别再让AI们群聊了(cover版) | single-instance | duplicate | 17 | B | content-lab | 正文与series-01几乎相同 |
| 60 | `2026-04-17-stable-collaboration-rewrite.md` | 多Bot群聊是玩具单实例注入是工具 | single-instance | draft | 18 | B | content-lab | 结构与series-01相似度高 |
| 61 | `season1-ep001-v3-rewrite.md` | v3重写:刚下载Hermes | hermes-genesis-s1-v3 | draft | 18 | B | content-lab | v3早期重写稿 |
| 62 | `season1-ep002-v3-rewrite.md` | v3重写:规矩越来越多AI胡来 | hermes-genesis-s1-v3 | draft | 18 | B | content-lab | v3早期重写稿 |
| 63 | `season1-ep003-v3-rewrite.md` | v3重写:AI最缺的是导航图 | hermes-genesis-s1-v3 | draft | 18 | B | content-lab | v3早期重写稿 |
| 64 | `draft-ai-homework.md` | 很多人不是不会用AI是太急着交作业 | standalone | draft | 18 | B | content-lab | 有完整YAML FM，正文完整 |
| 65 | `draft-gpt-subscription-company.md` | 榨干GPT订阅AI在GitHub开公司 | gpt-squeeze | draft | 18 | B | content-lab | 与20260528-squeeze-gpt-sop.md内容高度重叠 |
| 66 | `draft-ai-collaboration-v4.md` | 我折腾出一套AI协作架构4个角色 | standalone | draft | 18 | B | content-lab | 有完整正文，独立选题 |
| 67 | `draft-code-drop-01-foundation.md` | 上一篇承认AI不会自己变聪明 | hermes-genesis-s1 | draft | 17 | B | content-lab | Code Drop 01 早期草稿 |
| 68 | `draft-code-drop-02-workbench.md` | Code Drop 02早期草稿 | hermes-genesis-s1 | draft | 17 | B | content-lab | 与season1-code-drop-02重叠 |
| 69 | `draft-code-drop-03-role-memory.md` | Code Drop 03早期草稿 | hermes-genesis-s1 | draft | 17 | B | content-lab | 与season1-code-drop-03重叠 |
| 70 | `hermes-system-series-vol1.md` | 老板花2000买AI账号 | hermes-system | formal | 17 | B | content-lab | 管理者视角版 |
| 71 | `hermes-system-series-vol2.md` | 给AI建工作台文件全乱套 | hermes-system | formal | 17 | B | content-lab | 管理者视角版 |
| 72 | `hermes-system-series-vol3.md` | 所有事丢给一个AI后理清烂摊子 | hermes-system | formal | 17 | B | content-lab | 管理者视角版 |
| 73 | `hermes-system-series-vol4.md` | 给AI建团队搭教育管理系统 | hermes-system | formal | 17 | B | content-lab | 管理者视角实战版 |
| 74 | `season1-announcement-final.md` | Hermes Genesis第一季官宣 | hermes-genesis-s1 | formal | 17 | B | content-lab | 已定稿官宣文案 |
| 75 | `season1-announcement-final-v2.md` | 第一季官宣v2 | hermes-genesis-s1 | draft | 17 | B | content-lab | v2版本与v1高度重叠 |
| 76 | `draft-final-bundle-season1.md` | 第一季收官十二集经历 | hermes-genesis-s1 | draft | 17 | B | content-lab | Bundle早期草稿 |
| 77 | `hermes-genesis-ep012.md` | 系统开始写自己不只是工具 | hermes-genesis-s1 | draft | 17 | B | content-lab | EP012另一版本 |

### 2.3 C/D 类资产（内部文档/策划/规划/低完整度）

| # | 路径前缀 | 标题 | Series | Type | 总分 | 等级 | Bucket | Notes |
|---|---------|------|--------|------|------|------|--------|-------|
| 78 | `2026-04-14-10min-file-gov-draft.md` | 桌面像案发现场10min文件治理 | standalone | draft | 14 | C | content-lab | 标题名有draft但正文完整 |
| 79 | `2026-04-14-system-upgrade-draft.md` | 系统规范重大升级 | standalone | draft | 14 | C | content-lab | 标题有draft但正文完整 |
| 80 | `2026-04-17-norms-injection-draft.md` | 多Agent群聊是玩具规范注入 | single-instance | draft | 14 | C | content-lab | 标题有draft，正文完整 |
| 81 | `2026-04-17-state-md-norms.md` | AI根本不知道项目进度 | standalone | draft | 14 | C | content-lab | 正文完整，可独立发布 |
| 82 | `2026-04-17-series-summary.md` | 让AI干活的4条铁律系列汇总 | hermes-v4-rules | plan | 13 | C | content-lab | 系列汇总，有FM |
| 83 | `2026-04-17-series-final-release-plan.md` | 单实例上下文治理系列最终发版 | single-instance | plan | 12 | C | local-only | 发布计划，非文章 |
| 84 | `2026-04-17-series-plan-single-instance.md` | 公众号系列发布方案v2 | single-instance | plan | 12 | C | local-only | 内部策划 |
| 85 | `2026-04-17-series-publishing-pack.md` | 系列发布包装方案 | single-instance | plan | 12 | C | local-only | 内部策划 |
| 86 | `2026-04-21-hermes-genesis-execution-roadmap.md` | Hermes长篇连载执行路线图 | hermes-genesis | plan | 12 | C | local-only | 内部路线图 |
| 87 | `2026-04-21-hermes-genesis-long-series-master-plan.md` | Hermes长篇连载总策划 | hermes-genesis | plan | 12 | C | local-only | 内部策划 |
| 88 | `2026-04-21-hermes-genesis-season1-announcement.md` | 官宣文案Cutoff-1版 | hermes-genesis-s1 | draft | 12 | C | local-only | 早期官宣草稿 |
| 89 | `2026-04-23-mini-draft-team-test.md` | AI接管内容生产线3个月翻4倍 | standalone | draft | 14 | C | content-lab | 正文完整，独立选题 |
| 90 | `2026-04-summer-ai-day-launch.md` | 暑假AI体验日免费预约 | aoxue-edu | formal | 12 | C | local-only | 教育招生文，非AI技术 |
| 91 | `2026-enrollment-media-plan.md` | 奥学教育2026自媒体执行方案 | aoxue-edu | plan | 10 | C | local-only | 内部运营方案 |
| 92 | `draft-2026-04-21-ep001-hermes-genesis-polished.md` | 刚下载Hermes以为会变聪明(润色) | hermes-genesis | draft | 13 | C | content-lab | EP001润色完整版 |
| 93 | `draft-2026-04-21-ep001-hermes-genesis-polished-short.md` | EP001润色短版 | hermes-genesis | draft | 13 | C | content-lab | 短版 |
| 94 | `draft-2026-04-21-ep001-hermes-genesis.md` | EP001原始草稿 | hermes-genesis | draft | 12 | C | local-only | 与polished高度重叠 |
| 95 | `draft-ep001-hermes-genesis-v2.md` | EP001 v2草稿 | hermes-genesis | draft | 13 | C | local-only | v2版本 |
| 96 | `draft-ep001-hermes-genesis-v3-gpt54.md` | EP001 v3-gpt54 | hermes-genesis | draft | 12 | C | local-only | GPT54生成版本 |
| 97 | `draft-ep001-hermes-genesis-v4-gpt54.md` | EP001 v4-gpt54 | hermes-genesis | draft | 12 | C | local-only | GPT54生成版本 |
| 98 | `draft-ep002~ep012-hermes-genesis-gpt54.md` (共11个) | EP002-012 gpt54生成稿 | hermes-genesis | draft | 12 | C | local-only | GPT54生成中间版本 |
| 99 | `editor-plan-4-series.md` | 4条铁律系列策划 | hermes-v4-rules | plan | 10 | C | local-only | 内部策划文档 |
| 100 | `editor-plan-agent-truth-series.md` | 拒绝Agent焦虑系列策划 | agent-truth | plan | 10 | C | local-only | 已归档，标为历史版 |
| 101 | `editor-plan-single-instance.md` | 单实例多Agent主编选题方案 | single-instance | plan | 10 | C | local-only | 内部策划 |
| 102 | `hermes-v7-collection-plan.md` | v7.0合集方案拆解 | hermes-v7-principles | plan | 10 | C | local-only | 合集策划 |
| 103 | `hermes-v7-principles-plan.md` | v7.0底层原理科普合集方案 | hermes-v7-principles | plan | 10 | C | local-only | 合集策划 |
| 104 | `series-coherence-review.md` | 四篇系列文章连贯性审查报告 | single-instance | plan | 10 | D | local-only | 审查报告 |
| 105 | `hermes-system-series-vol1-review.md` | vol1审查报告 | hermes-system | plan | 10 | D | local-only | 审查报告 |
| 106 | `writer-injection-agent-truth.md` | 历史版主笔注入包 | agent-truth | plan | 10 | D | local-only | 已归档 |
| 107 | `draft-ai-homework.before-chief-editor.md` | 太急着交作业(主编前版) | standalone | draft | 13 | C | local-only | 主编前版本 |
| 108 | `feishu_agent-truth-series-broadcast.md` | 单核多模态飞书播报 | agent-truth | plan | 8 | D | local-only | 播报卡片 |
| 109 | `feishu_media_team_cover_prompts_card.md` | 封面Prompt卡片 | single-instance | plan | 8 | D | local-only | 封面prompt |
| 110 | `feishu_media_team_release_card.md` | 发版状态播报卡片 | single-instance | plan | 8 | D | local-only | 播报卡片 |
| 111 | `hermes-series-cover-prompts.md` | 系列公众号封面图Prompt | hermes-system | plan | 8 | D | local-only | 封面prompt |
| 112 | `season1-rewrite-v3/season1-v3-direction-matrix.md` | V3方向矩阵 | hermes-genesis-s1-v3 | plan | 8 | D | local-only | 方向矩阵 |
| 113 | `season1-rewrite-v3/final-release-total-control-v1/` 下7个.md | 发布前精修辅助文档 | hermes-genesis-s1-v3 | plan | 8 | D | local-only | change-notes/risk-check/checklist等 |
| 114 | `season1-rewrite-v3/updates-20260427-role-memory-dashboard/` 下4个.md | 角色记忆闭环补丁文档 | hermes-genesis-s1-v3 | plan | 8 | D | local-only | 补丁报告/更新说明 |
| 115 | `2026-04-summer-ai-day-launch.md` | 暑期AI体验日招生 | aoxue-edu | formal | 11 | C | prohibit | 教育招生文，含业务信息 |

### 2.4 X 类资产（禁止入仓）

| # | 路径 | 风险 | Notes |
|---|------|------|-------|
| X1 | `drafts/ip-whitelist-draft.md` | 可能含微信公众号IP白名单配置 | 标题暗示运维配置 |
| X2 | `hermes-feishu-print-assistant.no-fm.md` | 无YAML FM版本，与正式版内容重复 | 去重后应删除 |
| X3 | `articles/hermes-series-vol2-memory.md.bak.20260416_180607` | 时间戳备份 | 与正式版重复 |
| X4 | `articles/season1-ep012.md.bak_20260515_153618` | 时间戳备份 | 与正式版重复 |
| X5 | `articles/season1-final-bundle.md.bak_20260515_153618` | 时间戳备份 | 与正式版重复 |
| X6 | `articles/2026-05-agent-truth-{1-5}.md.new` (5个) | .new占位/中间态 | 与对应正式版内容几乎一致 |
| X7 | `articles/2026-05-agent-truth-5.md.bak` | 备份 | 与正式版重复 |
| X8 | `articles/EP011.md`, `FinalBundle.md`, `CodeDrop02.md` | 0字节空文件 | 冗余，应删除 |
| X9 | `drafts/20260527-gpt-squeeze-v4-full.md` | 与`drafts/gpt-squeeze-final.md`和`articles/20260528-squeeze-gpt-sop.md`三重重叠 | 重复冗余 |
| X10 | `drafts/20260527-squeeze-gpt-sop.md` | 与`20260528-squeeze-gpt-sop.md`几乎相同 | 旧版重复 |
| X11 | `drafts/20260527-v3.1-collaboration-final.md` | 内部协作四件套配置prompt | 非文章，属工程配置 |
| X12 | `drafts/20260527-v3.1-combined-final.md` | 与gpt-squeeze文章重复 | 重复冗余 |
| X13 | `drafts/20260527-gpt-image-2-codex-oauth.md` | 技术教程但含API接入细节 | 可入仓但需脱敏审查 |
| X14 | `drafts/20260527-github-fact-source.md` | 与gpt-squeeze重叠 | 重复 |
| X15 | `drafts/20260527-final-sop.md` | 与squeeze-gpt-sop重叠 | 重复 |
| X16 | `draft-smoke-readme-not-database.md` | 与season1-ep003高度重叠 | 旧版重复 |
| X17 | `hermes-genesis-season1/final-public-pack-article/final-public-pack-draft-v{2,3-1}.md` | 打包草稿 | 中间产物 |
| X18 | `season1-rewrite-v3/feishu/*.stderr`, `*.stdout` | 命令执行输出 | 非文章 |
| X19 | `season1-rewrite-v3/season1-v3-doc-map.json` | JSON映射文件 | 工程文件 |
| X20 | `articles/draft-ai-homework-cover-temp.png` | 图片 | 非文本资产 |
| X21 | `articles/season1-code-drop-02-workbench.png` | 图片 | 非文本资产 |
| X22 | `articles/season1-ep011.png` | 图片 | 非文本资产 |
| X23 | `articles/season1-ep012-cover.png` | 图片 | 非文本资产 |
| X24 | `articles/season1-final-bundle.png` | 图片 | 非文本资产 |
| X25 | `articles/season1-rewrite-v3/*.png` | 图片 | 非文本资产 |
| X26 | `articles/hermes-genesis-season1/.../assets/` 下.png/.jpg | 截图资产 | 非文本资产 |
| X27 | `2026-enrollment-media-plan.md` | 含奥学教育内部运营计划 | 业务敏感，prohibit入公开仓 |
| X28 | `2026-04-summer-ai-day-launch.md` | 教育招生文案，含品牌信息 | 业务敏感，prohibit |

---

## 3. A 类资产清单（推荐优先入仓）

### 3.1 Hermes Genesis Season 1 正片 (14篇)
- `season1-ep001.md` ~ `season1-ep012.md`
- `season1-final-bundle.md`
- `season1-code-drop-01-foundation.md`, `season1-code-drop-02-workbench.md`, `season1-code-drop-03-role-memory.md`

### 3.2 单实例上下文治理系列 (4篇)
- `2026-04-17-series-01-single-instance-vs-group-chat.md`
- `2026-04-17-series-02-how-one-ai-holds-49-roles.md`
- `2026-04-17-series-03-team-boss-mechanism.md`
- `2026-04-17-series-04-turn-ai-into-executor.md`

### 3.3 hermes-v7-principles 底层原理 (6篇)
- `hermes-v7-principles-01-core-engine.md` ~ `hermes-v7-principles-06-safety-runtime.md`

### 3.4 hermes-system 认知系列 (5篇)
- `hermes-series-vol1-cognition.md` ~ `hermes-series-vol4-teams.md`, `hermes-series-vol6-practice.md`

### 3.5 agent-truth / 麦尖Vol (9篇)
- `2026-05-agent-truth-1.md` ~ `2026-05-agent-truth-5.md`
- `麦尖-vol1~vol4`

### 3.6 独立精品文章 (5篇)
- `2026-04-17-context-injection.md`
- `2026-04-17-ports-norms.md`
- `2026-04-17-role-injection.md`
- `2026-04-27-macos-word-print-without-office.md`
- `20260528-squeeze-gpt-sop.md`
- `hermes-feishu-print-assistant.md`
- `cod-drop-02.md`
- `ep-011.md`
- `final-bundle.md`

**A类合计: ~49篇**

---

## 4. B 类资产清单

### 4.1 S1 V2/V3 重写版本 (26篇)
- `season1-rewrite-v2/` 下12篇
- `season1-rewrite-v3/` 下EP001-010 v3 + code-drop v3等

### 4.2 GPT54 生成草稿 (12篇)
- `draft-ep001-hermes-genesis-v2.md` ~ `draft-ep012-hermes-genesis-gpt54.md`

### 4.3 其他有潜力的草稿 (10篇)
- `draft-ai-homework.md`, `draft-gpt-subscription-company.md`, `draft-ai-collaboration-v4.md` 等

**B类合计: ~28篇**

---

## 5. C/D 类资产

### C类 (约15篇): 内部策划、方向矩阵、审查报告、教育类文章
### D类 (约12篇): 播报卡片、封面prompt、执行日志、辅助文档

**C/D合计: ~27篇**

---

## 6. X 类禁止入仓 (28项)

| 风险类别 | 文件 | 风险说明 |
|---------|------|---------|
| 0字节空文件 | EP011.md, FinalBundle.md, CodeDrop02.md | 冗余 |
| 时间戳备份 | *.bak_20260515, *.bak.20260416 | 与正式版重复 |
| .new 中间态 | agent-truth-{1-5}.md.new | 与正式版重复 |
| 重复文章 | drafts/ 下多个gpt-squeeze变体 | 3-5重复制 |
| 内部策划 | editor-plan-*, feishu_*.md | 非文章 |
| 图片资产 | *.png, *.jpg | 非文本 |
| 业务敏感 | 2026-enrollment-media-plan.md | 内部运营数据 |
| 命令输出 | *.stderr, *.stdout | 非文章 |
| 工程配置 | v3.1-collaboration-final.md | 可能含API配置 |

---

## 7. 分流建议

| Bucket | 纳入范围 | 估算数量 | 操作 |
|--------|---------|---------|------|
| **content-lab** | A类49篇 + B类中可精修10篇 | ~59篇 | 直接迁移，建立series目录 |
| **private-repo** | B类V2/V3重写26篇 + GPT54草稿12篇 | ~38篇 | 存档，不公开，保留版本历史 |
| **local-only** | C/D类27篇策划/审查/辅助文档 | ~27篇 | 保留本地引用，不入公开仓 |
| **prohibit** | X类28项(业务敏感+内部配置+重复) | ~28篇 | 不迁移，可删除 |

---

## 8. 需要总控裁决的问题

1. **S1 版本选择**: season1-ep001~012 存在 v1(正式)、v2(rewrite-v2)、v3(rewrite-v3) 三个完整版本。v1已定稿但v3有YAML FM和不同author。应确认哪个作为入仓基准。
2. **单实例系列去重**: `series-01~04` 与 `single-instance-final.md`, `single-instance-cover-article-final.md`, `stable-collaboration-rewrite.md` 内容高度重叠。需决定保留哪个版本。
3. **GPT-squeeze 去重**: `articles/20260528-squeeze-gpt-sop.md`, `drafts/gpt-squeeze-final.md`, `drafts/20260527-squeeze-gpt-sop.md`, `drafts/20260527-v3.1-combined-final.md`, `drafts/20260527-gpt-squeeze-v4-full.md`, `drafts/20260527-github-fact-source.md`, `drafts/20260527-final-sop.md` 共7个变体。需确认最终版。
4. **麦尖Vol vs agent-truth**: `麦尖-vol1~4` 与 `2026-05-agent-truth-1~5` 内容主题高度重叠（同系列不同表述）。需决定保留哪套或是否合并。
5. **hermes-system vs hermes-series**: `hermes-series-vol1~6` 与 `hermes-system-series-vol1~4` 两套系统系列并存。需确认关系。
6. **业务敏感文件**: `2026-enrollment-media-plan.md` 和 `2026-04-summer-ai-day-launch.md` 含奥学教育品牌信息。需确认是否脱敏后入仓或完全隔离。
7. **0字节文件**: EP011.md, FinalBundle.md, CodeDrop02.md 为空文件但 `cod-drop-02.md`, `ep-011.md`, `final-bundle.md` 有内容。应删除空文件。

---

## 9. 下一步建议

1. **立即清理**: 删除0字节文件(.md)、.bak时间戳备份、.new中间态、*.stderr/*.stdout
2. **确认S1基准版本**: 与总控确认v1/v2/v3哪个作为入仓基准
3. **建立series目录**: 在content-lab中按series建立子目录（hermes-genesis-s1, single-instance, agent-truth, hermes-v7-principles, hermes-system, 麦尖-自媒体）
4. **去重**: 合并gpt-squeeze变体，合并麦尖Vol与agent-truth重叠
5. **YAML FM标准化**: A类中部分文件缺少YAML frontmatter，建议统一补充(title, author, series, date)
6. **业务文件隔离**: 奥学教育相关文件单独存放或脱敏
