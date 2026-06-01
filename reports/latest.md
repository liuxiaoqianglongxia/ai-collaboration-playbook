# Latest Report｜PLAYBOOK_OPERATIONAL_BASELINE_V1.2_CANDIDATE

## 状态

```text
PLAYBOOK_OPERATIONAL_BASELINE_V1.2_CANDIDATE
```

## 结论

PASS

## 当前主线成果

`ai-collaboration-playbook` 已完成 `PLAYBOOK_OPERATIONAL_BASELINE_V1.1` 收口，并新增 `PLAYBOOK_OPERATIONAL_BASELINE_V1.2_CANDIDATE` 操作层。

V1.2 candidate 是候选升级，不是推翻 V1.1：

```text
stable baseline: PLAYBOOK_OPERATIONAL_BASELINE_V1.1
candidate layer: PLAYBOOK_OPERATIONAL_BASELINE_V1.2_CANDIDATE
Drive-first / main+tag / Claude-first-pass / Codex-final: PASS
V4 four-piece role model: unchanged
```

## V1.1 历史保留

```text
V0.1 Bootstrap: PASS
V0.2 Templates & Checklists: PASS
V0.2.5 Misroute Recovery: PASS
V0.2.6 Full Whitepaper Recovery: PASS
Collaboration Template Pack V1: PASS
Execution Environment Ownership: PASS
TASK-PACKAGE-REGISTRY-V1.1: PASS
Playbook Dogfood tasks/ Registry: PASS
Claude Code Read-only Review: PARTIAL PASS accepted as candidate-gate evidence
ChatGPT Independent Acceptance: PASS
PR #6 Merge Closeout: PASS
V1.1 Operational Cleanup: PASS
Execution Lane Management: PASS
Claude Code Coordination: PASS
User-Facing Task Announcement: PASS
Final User Guide / Routing / Pro Review Prep: PASS
```

## V1.2 Candidate 新增层

```text
Drive-first daily workflow: PASS
Main-only + tag versioning: PASS
Claude-first-pass / Codex-final: PASS
Maximum practical authorization: PASS
Drive workbench templates: PASS
Claude worker templates: PASS
User-facing docs and personalization candidate: PASS
```

## 当前稳定入口

```text
CHATGPT_START_HERE.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
standards/DRIVE_FIRST_WORKFLOW_V1.md
standards/MAIN_ONLY_TAG_VERSIONING_V1.md
standards/CLAUDE_FIRST_CODEX_FINAL_V1.md
standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
templates/drive-project-workbench/
templates/CLAUDE_BOUNDED_IMPLEMENTATION_TASK.md
templates/CLAUDE_PATCH_WORKER_TASK.md
templates/CODEX_CLAUDE_ORCHESTRATION.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md
```

## 当前任务指针

```text
tasks/codex/latest.md: none / NO_ACTIVE_CODEX_TASK
tasks/claude/latest.md: none / NO_ACTIVE_CLAUDE_TASK
```

当前没有活跃 Codex 或 Claude Code 任务。

## 当前操作原则

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

V1.2 candidate 日常模型：

```text
Drive 管日常任务、报告、截图、材料、交接和临时验收笔记。
WSL/local Git 管真实代码编辑、测试和集成。
GitHub main 管里程碑代码和协作事实。
GitHub tags 管 dev-ok、pre-prod、prod、rollback 等版本锚点。
Claude Code 做 Codex 编排下的 first-pass 工程支持。
Codex 做最终集成、验证、push main、tag、必要时 PR、报告。
ChatGPT 做总控、任务包、验收和轻量 GitHub 写入。
```

## 保留边界

```text
V4 四件套不变。
GitHub 仍是里程碑事实源、版本锚点、生产依据和回滚点。
Drive 是日常工作台，不是 live code workspace，也不是最终里程碑事实源。
WSL/local Git 仍是真实开发空间。
Codex 仍是交付负责人和最终集成者。
Claude Code 仍是工程增强工具和 first-pass worker，不替代 Codex。
ChatGPT 仍是总控、任务包设计者和验收方。
Hermes 不是默认四件套成员。
未接入自动化。
未处理业务项目。
未处理 sub2api-maijian。
未执行生产类操作。
```

## 下一步建议

```text
1. 将 V1.1 继续作为稳定基线，将 V1.2 candidate 作为更快的日常操作层试用。
2. 业务项目采用 Drive-first 时，必须定义 Drive 到 GitHub 的同步点，避免两套 current state。
3. main+tag 适合低风险里程碑锚点；需要 review/integration 保护时仍使用 branch/PR。
4. Claude Code first-pass 应由 Codex 编排，Codex 必须复核 diff、验证并写报告。
5. ChatGPT Pro 深度复核可从 reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md 开始。
6. Personal Details / Custom Instructions 仍以 reports/chatgpt/personalization/PERSONALIZATION_CANDIDATE_V1.md 为候选，需 ChatGPT 验收后再冻结。
```
