# Latest Report｜PLAYBOOK_OPERATIONAL_BASELINE_V2

## 状态

```text
PLAYBOOK_OPERATIONAL_BASELINE_V2
```

## 结论

PASS

## 当前主线成果

`ai-collaboration-playbook` 已完成 `PLAYBOOK_OPERATIONAL_BASELINE_V2` 稳定提升测试。

V2 将日常协作事实源迁移到 Drive 工作台，并把 GitHub 收口为稳定成果、版本管理、release、rollback 和最终可复用文档承载。V1.1/V1.2 保留为历史稳定基线。

## Patch-level candidate

```text
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
stable remains: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
```

Purpose:

```text
Drive write boundary
Codex local Drive sync fallback
old-project absorption levels
Claude Code interactive first-pass routing
```

```text
daily_fact_source: Google Drive
github_role: stable version / release / rollback / final reusable docs
github_active_task_pointer: none
```

V4 四件套角色模型保持不变：

```text
ChatGPT: controller, task package, acceptance
Drive: daily fact source, daily task/report/material/acceptance/decision workspace
GitHub: stable result, version management, release, rollback, reusable docs
Codex: local executor and final integrator
Claude Code: first-pass engineering support coordinated by Codex
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
V1.2 Candidate Implementation: PASS
V1.2 Self-Dogfood Stable Freeze: PASS
```

## V2 稳定层

```text
Drive-native daily workflow: PASS
GitHub release and version policy: PASS
Drive-native templates: PASS
Drive-native checklists: PASS
Drive-native protocols: PASS
Branch cleanup policy: PASS
GitHub stable sync: PASS
Private path leak scan: PASS
Cross-project pollution scan: PASS
Role conflict scan: PASS
Registry default-dispatch residue scan: PASS
Public docs final audit: PASS
```

## 当前稳定入口

```text
QUICK_START.md
CHATGPT_START_HERE.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
standards/DRIVE_NATIVE_WORKFLOW_V2.md
standards/GITHUB_RELEASE_AND_VERSION_POLICY_V2.md
guides/DRIVE_NATIVE_V2_USER_GUIDE.md
templates/drive-native-v2/
checklists/drive-native-v2/
protocols/drive-native-v2/
standards/CHATGPT_DRIVE_TOOL_CAPABILITY_BOUNDARY_V2_1.md
standards/DRIVE_NATIVE_V2_ABSORPTION_AND_COMPATIBILITY_POLICY.md
standards/CLAUDE_CODE_FIRST_PASS_ROUTING_V2_1.md
guides/OLD_PROJECT_V2_ABSORPTION_GUIDE.md
guides/SMALL_PROJECT_DRIVE_NATIVE_V2_MINIMAL_GUIDE.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_FINAL_V2.md
```

## 兼容任务指针

```text
tasks/codex/latest.md: none / NO_ACTIVE_CODEX_TASK
tasks/claude/latest.md: none / NO_ACTIVE_CLAUDE_TASK
```

这些指针是兼容入口，不是 Drive-native V2 默认日常派工入口。

## 当前操作原则

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

Drive-native V2 model:

```text
Drive 管日常任务、报告、截图、材料、交接、临时验收、决策记录和 daily log。
GitHub 管稳定成果、版本、release、rollback、final reusable docs。
Codex 做执行、集成、验证、GitHub 同步和报告。
Claude Code 做 Codex 编排下的 first-pass 工程支持。
ChatGPT 做总控、任务设计、验收和 release decision。
```

## 保留边界

```text
V4 四件套不变。
GitHub 是稳定成果、版本锚点、release、rollback 和 final reusable docs 承载。
Drive 是日常事实源，不是生产部署源。
WSL/local Git 仍是真实开发空间。
Codex 仍是交付负责人和最终集成者。
Claude Code 仍是工程增强工具和 first-pass worker，不替代 Codex。
ChatGPT 仍是总控、任务包设计者和验收方。
Google Drive 不是第五个 Agent。
Hermes 不是默认四件套成员。
未接入自动化。
未处理业务项目。
未执行生产类操作。
```

## 下一步建议

```text
1. 将 PLAYBOOK_OPERATIONAL_BASELINE_V2 作为当前稳定协作基线使用。
2. 具体项目接入时先建 Drive workbench，再定义 GitHub stable sync 点。
3. V1.1/V1.2 历史记录继续保留。
4. 不恢复 GitHub registry 指针作为默认日常派工方式。
```
