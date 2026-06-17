# Codex Claude Orchestration

## Purpose

Use this checklist when Codex coordinates Claude Code inside an active task.

## Before Claude

```text
active_codex_task:
repo_verified: yes/no
branch:
allowed_scope:
claude_mode: read-only / patch-only / bounded-edit
```

## Prompt Boundary

- State the parent Codex task.
- List allowed files or directories.
- List forbidden actions.
- Require Claude Code to stop before commit, push, tag, PR, deploy, database, or secret work.
- Require a concise evidence summary.

## After Claude

```text
claude_scope:
accepted:
rejected:
codex_validation:
final_integrator: Codex
```

## Report

Codex report should include whether Claude Code was used, what evidence it produced, what Codex accepted or rejected, and what validation Codex ran afterward.
