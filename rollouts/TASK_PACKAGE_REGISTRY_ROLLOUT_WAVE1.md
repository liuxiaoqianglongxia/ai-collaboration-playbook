# Task Package Registry Rollout Wave 1

## Goal

Extend `TASK-PACKAGE-REGISTRY-V1.1` from the playbook into real projects, but each project must read its own fact source, use its own PR, and complete its own acceptance.

## Rollout Principle

- Do not batch-write directly to business project `main` branches.
- Do not copy state across projects.
- Do not apply one project's `CURRENT.md`, `TASKS.md`, or `reports/latest.md` to another project.
- Each project first reads its own `CHATGPT_START_HERE.md`, `CURRENT.md`, `TASKS.md`, `AGENTS.md`, `CLAUDE.md`, `DECISIONS.md`, and `reports/latest.md`.
- Each project creates its own `tasks/` registry.
- Each project writes its own Codex report.
- Each project receives independent ChatGPT acceptance.

## Candidate Projects

- `maijian-wechat-content-lab`: completed canary; use as reference evidence, do not repeat automatically.
- `shanxi-edu-hot`: candidate for a later wave, but only after read-only project fact-source review.
- `sub2api-maijian`: excluded from wave 1 unless a separate project governance task is opened; do not mix it with playbook rollout.
- Other projects: require explicit user-specified repository before entry.

## Standard Project Task

Each project adoption task should use:

```text
PROJECT-TASK-PACKAGE-REGISTRY-ADOPTION-V1
```

## Required Output Per Project

```text
tasks/README.md
tasks/codex/_template.md
tasks/codex/latest.md
tasks/claude/_template.md
tasks/claude/latest.md
reports/chatgpt/task-packages/README.md
reports/codex/project-task-package-registry-adoption-v1.md
reports/latest.md update
TASKS.md update
DECISIONS.md update
```

## Stop Conditions

- Project fact source is missing.
- Project is in production incident, database, secret, or deployment risk.
- Repository routing is unclear.
- User asks for business development in the same task.
- Project already has a conflicting task registry.
