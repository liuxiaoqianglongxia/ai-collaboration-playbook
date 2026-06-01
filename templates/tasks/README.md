# tasks

Copy this directory into a project repository only when adopting the GitHub-backed task-package registry compatibility layer.

After copying, this file becomes:

```text
tasks/README.md
```

## Purpose

`tasks/` is the project-local compatibility registry for executable AI task packages.

Drive-native V2 uses Drive task packages by default. ChatGPT writes these GitHub pointers only when a project explicitly enables repository-backed task dispatch.

## Entry Points

```text
tasks/codex/latest.md
tasks/claude/latest.md
```

When this compatibility layer is enabled, Codex reads `tasks/codex/latest.md`.

When this compatibility layer is enabled, Claude Code reads `tasks/claude/latest.md`.

## Rules

- Do not infer tasks from chat history when a registry exists.
- Save historical task packages as named files.
- Keep latest pointer files short.
- Keep one active execution lane per project stage.
- If `tasks/codex/latest.md` is `ACTIVE_CODEX_TASK`, do not create another active Codex task for the same stage.
- If Claude Code is needed, Codex coordinates it inside the active Codex task.
- Do not treat this template directory as the project fact source until it has been copied, adapted, and committed inside the project repository.
- If a latest pointer conflicts with `CURRENT.md`, `TASKS.md`, or `reports/latest.md`, stop and report `BLOCKED`.
