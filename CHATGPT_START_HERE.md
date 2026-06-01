# CHATGPT_START_HERE

## Current Baseline

```text
stable: PLAYBOOK_OPERATIONAL_BASELINE_V1.2
candidate: DRIVE_NATIVE_V2_CANDIDATE
reports/latest.md: PARTIAL PASS on the V2 candidate branch
```

This repository is the general AI collaboration playbook. It is not a business project repository and does not contain production application code.

V1.2 keeps V4 intact and adds a faster operating layer:

```text
Drive daily workbench
WSL/local Git for real development
GitHub main for milestone code and facts
GitHub tags for release and rollback anchors
Claude Code first-pass support coordinated by Codex
Codex final integration
```

Drive-native V2 candidate keeps V1.2 as the historical stable baseline while changing the daily operating surface:

```text
Drive: daily task, report, material, screenshot, handoff, temporary acceptance, decision record, daily log
GitHub: stable result, version management, release, rollback, final reusable docs
GitHub daily task pointers: not the default V2 dispatch surface
```

## Read Order For A New ChatGPT Session

Read these first:

```text
reports/latest.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
standards/DRIVE_FIRST_WORKFLOW_V1.md
standards/MAIN_ONLY_TAG_VERSIONING_V1.md
standards/CLAUDE_FIRST_CODEX_FINAL_V1.md
standards/DRIVE_NATIVE_WORKFLOW_V2.md
standards/GITHUB_RELEASE_AND_VERSION_POLICY_V2.md
guides/DRIVE_NATIVE_V2_USER_GUIDE.md
standards/MAXIMUM_PRACTICAL_AUTHORIZATION_V1.md
standards/TASK_PACKAGE_REGISTRY_V1_1.md
standards/EXECUTION_LANE_MANAGEMENT_V1.md
standards/CLAUDE_CODE_COORDINATION_V1.md
standards/ROUTING_AND_EXTENSIBILITY_V1.md
protocols/GITHUB_AI_COLLABORATION.md
templates/USER_FACING_TASK_ANNOUNCEMENT.md
templates/PROJECT_ROUTING_PROFILE.md
tasks/codex/latest.md
tasks/claude/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

If files conflict, treat `reports/latest.md` as the current status source and historical reports as evidence, not current state.

## Operating Mode

The stable operating mode is `PLAYBOOK_OPERATIONAL_BASELINE_V1.2`.

The current candidate upgrade is `DRIVE_NATIVE_V2_CANDIDATE`. Do not mark it as `PLAYBOOK_OPERATIONAL_BASELINE_V2` until ChatGPT acceptance promotes it.

The target is:

```text
使用层极简
执行层清楚
留痕层完整
风险层兜底
```

Do not simplify by weakening capability. Simplify the user layer. Keep the execution and traceability layers strong behind the scenes.

V2 daily surface:

```text
Drive holds daily tasks, reports, screenshots, materials, handoffs, temporary acceptance notes, decisions, and daily logs.
Drive is the daily fact source.
Drive is not the production deploy source.
```

GitHub surface:

```text
GitHub main: stable code/docs.
GitHub tags: release and rollback anchors.
GitHub PRs: review and candidate stabilization when needed.
GitHub reports: release summary, milestone summary, public reusable docs, rollback notes.
```

Daily user guide:

```text
guides/USER_OPERATING_GUIDE_V1.md
```

Execution lane rule:

```text
One stage has one active execution lane.
Default: one active Codex task at a time.
If Claude Code is needed, Codex coordinates it inside the active Codex task.
```

## Role Model

```text
ChatGPT: controller, architecture judgment, task package, acceptance, safe lightweight GitHub writes when available
GitHub: single source of truth, state machine, trace log
Codex: delivery lead, local execution, final integration, reports
Claude Code: local engineering enhancement, first-pass draft fixes, deep analysis, review
```

Hermes, Qwen, MCP, heartbeat, automation, and subagents are not default members. Use them only when a project fact source or explicit user authorization requires them.

## ChatGPT Direct-Work Rule

If ChatGPT has GitHub write access and the task is safe documentation / task-package / pointer / report / acceptance work, ChatGPT should do it directly.

Do not hand off safe controller work to Codex just to show process.

Use Codex for local execution, code changes, tests, integration, PR delivery, and heavy validation.

If ChatGPT does not have GitHub write access, say so clearly and do not claim that anything was written to GitHub.

## Current Task Pointers

```text
tasks/codex/latest.md: none / NO_ACTIVE_CODEX_TASK
tasks/claude/latest.md: none / NO_ACTIVE_CLAUDE_TASK
```

GitHub daily task pointers are not the default Drive-native V2 dispatch surface. Use them only when a stable repository-backed task package is explicitly needed.

## Safety Boundary

Do not modify:

```text
AI_COLLABORATION_MODE_V4.md unless explicitly authorized
business repositories
production servers
databases
credentials or secrets
automation publish chains
```

Do not promote experimental lab material into stable standards without a separate promotion gate.

Pro review and final personalization:

```text
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE.md
reports/chatgpt/personalization/PERSONALIZATION_FINAL_V1_2.md
```

## Next Recommended Action

Use this playbook as the stable V1.2 baseline for concrete projects. For each project, read the project's own fact source first and do not mix project state across repositories.
