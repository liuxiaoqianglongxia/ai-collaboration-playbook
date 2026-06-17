# Small Project Drive-native V2 Minimal Guide

baseline: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
status: candidate

## Purpose

Give small projects a low-overhead version of Drive-native V2.

## Minimal Drive Workbench

Small projects may start with only:

```text
00_HOME.md
01_CURRENT.md
tasks/
reports/
decisions/
```

Optional until needed:

```text
daily/
acceptance/
handoffs/
materials/
screenshots/
```

## Minimal GitHub Stable Layer

Small projects may start with:

```text
README.md
CHATGPT_START_HERE.md
AGENTS.md
CLAUDE.md
reports/latest.md
```

Optional until needed:

```text
CURRENT.md
TASKS.md
DECISIONS.md
reports/codex/latest.md
reports/claude/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
```

## Mandatory Rules

Even small projects must keep:

```text
Drive = daily fact source
GitHub = stable result / release / rollback / reusable docs
ChatGPT Drive write = verify parent folder or fallback to Codex
Claude Code = first-pass under Codex, not final integrator
GitHub-backed registry = compatibility only unless explicitly active
```

## Minimal User Handoff

```text
任务：<TASK-ID>
入口：Drive task package
执行：Codex
Claude：需要深度代码分析时由 Codex 交互式调用
报告：Drive report
稳定同步：必要时 GitHub PR/tag/release note
```
