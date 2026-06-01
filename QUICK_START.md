# Quick Start｜Drive-native V2 使用说明

本页给第一次进入仓库的人使用。目标是：不用理解全部历史，也能在 10 分钟内把一个项目接入 AI 协作流程。

当前稳定基线：`PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS`。

## 1. 先理解一句话

```text
Drive 管日常协作，GitHub 管稳定成果。
```

- Drive：任务包、执行报告、材料、截图、交接、临时验收、决策记录、daily log。
- GitHub：稳定文档、版本、release、rollback、最终可复用规范。
- WSL/local Git：真实代码编辑、测试、集成。
- ChatGPT：总控、任务设计、验收、release decision。
- Codex：执行、集成、验证、GitHub 同步、报告。
- Claude Code：由 Codex 编排的 first-pass 工程支持。

## 2. 新项目接入的最小步骤

### Step 1：读取入口

先读这些文件：

```text
README.md
reports/latest.md
CHATGPT_START_HERE.md
NEW_PROJECT_BOOTSTRAP.md
AI_AGENT_ONBOARDING.md
guides/DRIVE_NATIVE_V2_USER_GUIDE.md
standards/DRIVE_NATIVE_WORKFLOW_V2.md
standards/GITHUB_RELEASE_AND_VERSION_POLICY_V2.md
```

### Step 2：给项目建 Drive 工作台

每个项目建立自己的 Drive 工作台，用来放日常材料和任务：

```text
<project-workbench>/
  00_HOME.md
  01_CURRENT.md
  02_INDEX.md
  03_ROUTING.md
  04_DECISIONS_LATEST.md
  05_RELEASE_POLICY.md
  tasks/
  reports/
  daily/
  decisions/
  acceptance/
  handoffs/
  materials/
  screenshots/
```

可参考：

```text
templates/drive-project-workbench/
templates/drive-native-v2/
checklists/drive-native-v2/
protocols/drive-native-v2/
```

### Step 3：项目 GitHub 仓库只放稳定成果

项目 GitHub 仓库建议保留：

```text
README.md
CHATGPT_START_HERE.md
AGENTS.md
CLAUDE.md
CURRENT.md
TASKS.md
DECISIONS.md
reports/latest.md
reports/codex/latest.md
```

GitHub 负责：

```text
main stable
release notes
rollback anchors
tags
milestone summaries
final reusable docs
```

不要把 GitHub 当成日常材料堆放区，也不要把 Drive 当成生产部署源。

## 3. 日常怎么派任务

用户只需要说目标，例如：

```text
按 V2 给这个项目生成一个登录修复任务包，并安排 Codex 执行。
```

ChatGPT 应该做背后判断：

```text
1. 读取项目 Drive 工作台和 GitHub 稳定事实。
2. 判断任务风险、范围、执行者和验收方式。
3. 将日常任务包写入 Drive。
4. 给用户只返回短指令。
5. Codex 读取 Drive 任务包执行。
6. Codex 把报告写回 Drive。
7. ChatGPT 验收，必要时把稳定成果同步到 GitHub。
```

用户侧短指令示例：

```text
任务已写入 Drive：tasks/codex/YYYYMMDD/<task-name>.md
请 Codex 读取该任务包执行，完成后写 Drive 报告。
```

## 4. 什么时候进入 GitHub

只有这些内容适合进入 GitHub：

```text
稳定规范
稳定代码
release summary
rollback note
milestone summary
可复用模板
最终验收报告
```

日常过程材料默认留在 Drive：

```text
临时任务
执行草稿
截图
原始材料
daily log
临时验收
中间交接
```

## 5. 高风险动作

以下动作必须单独确认：

```text
生产部署
数据库修改
密钥修改
删除文件/分支/tag
force push
服务重启
正式 release
rollback
```

## 6. 不要这样用

```text
不要让用户反复复制几千行任务包。
不要把 tasks/codex/latest.md 恢复为默认日常派工入口。
不要把 Drive 当生产部署源。
不要把 GitHub 当 daily log 或截图仓库。
不要把具体业务项目代码提交到本 playbook 仓库。
```

## 7. 最小验收标准

一个项目接入完成，至少满足：

```text
Drive 工作台可读写。
GitHub main 保持稳定成果。
日常任务能落 Drive。
Codex 能按 Drive 任务执行。
报告能回写 Drive。
ChatGPT 能基于报告做 PASS / PARTIAL PASS / FAIL / BLOCKED 验收。
稳定成果能同步回 GitHub。
```
