# Playbook Task Package Registry

This directory is the live task-package registry for `liuxiaoqianglongxia/ai-collaboration-playbook`.

The playbook is the shared standards repository, and it must follow the V1.1 registry it defines for other projects.

## Roles

- ChatGPT writes task packages and performs acceptance.
- Codex receives implementation and closeout tasks through `tasks/codex/latest.md`.
- Claude Code receives read-only review or analysis tasks through `tasks/claude/latest.md`.
- Codex reports go in `reports/codex/`.
- Claude Code reports go in `reports/claude/`.
- ChatGPT task and acceptance snapshots go in `reports/chatgpt/task-packages/`.

## Stop Rule

If `tasks/codex/latest.md` or `tasks/claude/latest.md` conflicts with `reports/latest.md` or `TASKS.md`, stop and report `BLOCKED`.

## Current Entry Points

```text
tasks/codex/latest.md
tasks/claude/latest.md
```
