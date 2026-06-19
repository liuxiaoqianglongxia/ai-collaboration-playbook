# 贡献指南

本仓库是 AI 协作总规范库，用于沉淀可复用的项目协作流程、任务模板、验收清单、Drive-native 日常工作台规则，以及 GitHub 稳定成果、版本、release、rollback 的承载方式。

当前稳定基线：`PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS`。

## 一、仓库定位

本仓库适合提交：

- 通用 AI 协作规范
- 项目接入模板
- 任务包模板
- 报告模板
- 验收清单
- Drive-native V2 工作流改进
- GitHub release / rollback / version policy 改进
- 新项目接入经验沉淀

本仓库不接受：

- 具体业务项目源码
- 生产密钥、账号、数据库连接信息
- 私有本机路径作为唯一入口
- 未脱敏客户资料
- 未经整理的聊天记录大段粘贴
- 与当前 playbook 无关的实验材料

## 二、协作原则

Drive-native V2 的核心分工：

```text
Drive：日常任务、报告、材料、截图、交接、临时验收、决策记录、daily log。
GitHub：稳定成果、版本管理、release、rollback、final reusable docs。
WSL/local Git：真实代码或文档编辑、测试、集成。
ChatGPT：总控、任务设计、验收和 release decision。
Codex：执行、集成、验证、GitHub 同步和报告。
Claude Code：由 Codex 编排的 WSL/local 工程执行支持。
```

贡献内容必须遵守：

- 不恢复 GitHub-backed registry 为默认日常派工方式。
- 不把 Drive 当作生产部署源。
- 不把 GitHub 当作日常材料堆放区。
- 不让用户复制大段任务包来维持流程。
- 稳定成果必须能回到 GitHub main、tag、release note、rollback note 或正式报告。

## 三、提交方式

推荐流程：

1. 从 `main` 创建语义清晰的分支。
2. 修改前先读取 `reports/latest.md`、`CHATGPT_START_HERE.md`、`README.md`。
3. 文档改动必须说明影响范围。
4. PR 需要写清楚：目标、改动文件、验证方式、风险边界。
5. 合并前确认没有私有路径、密钥、业务项目污染和候选状态残留。

分支命名建议：

```text
docs/<topic>-v1
standards/<topic>-v1
templates/<topic>-v1
checklists/<topic>-v1
protocols/<topic>-v1
```

## 四、PR 验收清单

提交 PR 前至少检查：

```text
- 是否只改 playbook 范围内的通用规范或模板？
- 是否没有业务项目源码混入？
- 是否没有密钥、账号、数据库信息？
- 是否没有私有本机路径作为唯一入口？
- 是否没有把 candidate 写成 stable？
- 是否没有把 GitHub-backed registry 恢复为默认日常派工入口？
- 是否能让其他项目复用？
- 是否更新了相关 README、guide、standard、template 或 report 指针？
```

## 五、版本与发布

`main` 只承载稳定成果。

推荐版本出口：

```text
main：当前稳定文档和规范
tag：稳定版本锚点、release、rollback
PR：候选稳定化和审阅记录
reports/latest.md：当前稳定状态入口
reports/codex/latest.md：最新 Codex 执行报告入口
```

`PLAYBOOK_OPERATIONAL_BASELINE_V2` 是当前稳定基线。后续若进入 V3，必须先经过候选、测试、验收，再提升为稳定基线。

## 六、旧材料分类

本仓库中以下材料明确归类为 **history / reference / lab**，不作为默认执行入口：

- **V1 / V1.1 / V1.2 文档**（`standards/*_V1.md`, `standards/*_V2.md`）— 历史稳定基线，保留用于回滚证据和历史参考。
- **GitHub task registry**（`tasks/codex/latest.md`, `tasks/claude/latest.md`）— 兼容层，非默认日常派工入口。
- **whitepapers/** — 研究成果和白皮书草稿，不是执行指南。
- **lab/** — 实验验证，未推广前不作为默认入口。
- **archive/** — 迁移和抢救记录，仅作为证据和素材。
- **旧模板**（`templates/` 根目录文件）— 保留为历史模板，V3 默认模板为 `templates/task-hall-v3/`。

当前默认入口始终是 `QUICK_START.md` 和 `standards/TASK_HALL_V3.md`。
