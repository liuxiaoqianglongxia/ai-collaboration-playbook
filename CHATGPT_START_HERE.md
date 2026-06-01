# CHATGPT_START_HERE

## Current Baseline

```text
stable: PLAYBOOK_OPERATIONAL_BASELINE_V2
reports/latest.md: PASS
```

This repository is the general AI collaboration playbook. It is not a business project repository and does not contain production application code.

Drive-native V2 is the current stable operating baseline:

```text
Drive daily fact source
WSL/local Git for real development
GitHub main for stable code/docs
GitHub tags for release and rollback anchors
Claude Code first-pass support coordinated by Codex
Codex final integration
```

V1.1 and V1.2 remain historical stable baselines. V2 changes the daily operating surface:

```text
Drive: daily task, report, material, screenshot, handoff, temporary acceptance, decision record, daily log
GitHub: stable result, version management, release, rollback, final reusable docs
repository-backed task registry: compatibility surface only
```

## Read Order For A New ChatGPT Session

Read these first:

```text
QUICK_START.md
reports/latest.md
guides/USER_OPERATING_GUIDE_V1.md
README.md
AI_AGENT_ONBOARDING.md
AI_COLLABORATION_MODE_V4.md
standards/DRIVE_NATIVE_WORKFLOW_V2.md
standards/GITHUB_RELEASE_AND_VERSION_POLICY_V2.md
guides/DRIVE_NATIVE_V2_USER_GUIDE.md
reports/codex/latest.md
reports/claude/latest.md
```

Read `tasks/codex/latest.md` and `tasks/claude/latest.md` only when the current project explicitly uses the GitHub-backed compatibility registry.

If files conflict, treat `reports/latest.md` as the current status source and historical reports as evidence, not current state.

## Operating Mode

The stable operating mode is `PLAYBOOK_OPERATIONAL_BASELINE_V2`.

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
Drive: daily fact source, daily task/report/material/acceptance/decision workspace
GitHub: stable result, version management, release, rollback, reusable docs
Codex: delivery lead, local execution, final integration, reports
Claude Code: local engineering enhancement, first-pass draft fixes, deep analysis, review
```

Hermes, Qwen, MCP, heartbeat, automation, and subagents are not default members. Use them only when a project fact source or explicit user authorization requires them.

## ChatGPT Direct-Work Rule

If ChatGPT has GitHub write access and the task is safe stable documentation / release summary / milestone summary / rollback note work, ChatGPT may do it directly.

Do not hand off safe controller work to Codex just to show process.

Use Codex for local execution, code changes, tests, integration, PR delivery, and heavy validation.

If ChatGPT does not have GitHub write access, say so clearly and do not claim that anything was written to GitHub.

## Compatibility Task Pointers

```text
tasks/codex/latest.md: none / NO_ACTIVE_CODEX_TASK
tasks/claude/latest.md: none / NO_ACTIVE_CLAUDE_TASK
```

These pointers are compatibility entries. They are not the default Drive-native V2 dispatch surface. Use them only when a stable repository-backed task package is explicitly needed.

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
reports/chatgpt/personalization/PERSONALIZATION_FINAL_V2.md
```

## Next Recommended Action

Use this playbook as the stable V2 baseline for concrete projects. For each project, read its Drive workbench and GitHub stable facts first, and do not mix project state across repositories.
