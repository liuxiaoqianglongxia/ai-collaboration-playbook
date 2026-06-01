# Task Package Registry Bootstrap Task Template

> V2 note: use this template only when a project explicitly needs the GitHub-backed task-package registry compatibility layer. The default V2 daily task surface is a Drive task package. The first registry task only creates compatibility routing files; it does not perform business development.

## 1. Task Name

```text
project-task-package-registry-bootstrap-v1
```

## 2. Background

This project already uses Drive-native V2 and explicitly needs GitHub-backed task-package pointers as a compatibility layer.

## 3. Goal

Create the project-level task-package registry:

```text
tasks/README.md
tasks/codex/_template.md
tasks/codex/latest.md
tasks/claude/_template.md
tasks/claude/latest.md
reports/chatgpt/task-packages/README.md
```

Do not start business implementation in this task.

## 4. Repository

```text
repository_full_name: <owner/name>
branch: <branch-name>
README title: <expected-title>
```

## 5. Allowed Scope

```text
tasks/
reports/chatgpt/task-packages/
reports/codex/
reports/latest.md
```

Adjust the allowed scope for the project before execution.

## 6. Forbidden Scope

- Do not modify business source code.
- Do not deploy.
- Do not modify databases.
- Do not modify credentials, tokens, cookies, or secrets.
- Do not change production configuration.
- Do not force push.
- Do not copy another project's private state into this repository.
- Do not treat template files as project facts before adapting them.

## 7. Execution Steps

1. Verify `repository_full_name`, current branch, root README title, and clean working tree.
2. Read existing project fact-source files, especially `CURRENT.md`, `TASKS.md`, and `reports/latest.md` when present.
3. Check whether `tasks/` or `reports/chatgpt/task-packages/` already exists.
4. Add the registry files only when they do not overwrite active project facts.
5. Set `tasks/codex/latest.md` to `NO_ACTIVE_CODEX_TASK`.
6. Set `tasks/claude/latest.md` to `NO_ACTIVE_CLAUDE_TASK`.
7. Write a Codex report describing what was created.
8. Leave business work for a separate task package.

## 8. Acceptance Criteria

- The project has a readable `tasks/README.md`.
- Codex has a latest pointer at `tasks/codex/latest.md`.
- Claude Code has a latest pointer at `tasks/claude/latest.md`.
- ChatGPT task package snapshots have a documented archive location.
- Existing project fact-source files are not contradicted.
- No business code, production config, databases, or secrets were touched.

## 9. Report Format

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Repository:
Branch:
Files created:
Files updated:
Validation:
Forbidden scope confirmation:
Next step:
```

## 10. Stop Conditions

Stop and report `BLOCKED` when:

- repository identity is unclear;
- existing registry files contain active project facts that would be overwritten;
- `CURRENT.md`, `TASKS.md`, or `reports/latest.md` conflicts with the requested registry state;
- the task requires business development, deployment, database, credential, or production work;
- the allowed write scope is missing or ambiguous.

## 11. Next Step

After registry bootstrap passes, ChatGPT may create a named Codex or Claude Code task package and update the relevant latest pointer.
