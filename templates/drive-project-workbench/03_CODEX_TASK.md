# Codex Task Draft

## Task

```text
task_id:
goal:
repository:
branch:
```

## Scope

Allowed:

- `<file-or-directory>`

Forbidden:

- production deployment
- database changes
- credential or secret changes
- force push
- cross-project writes

## Claude Code Support

```text
mode: none / read-only / patch-only / bounded-edit
final_integrator: Codex
```

## Acceptance

- `<criterion>`

## Handoff

> **V3 Task Hall compatibility note**: Under V3 Task Hall, the authoritative task file is `<project>/task-hall/tasks/YYYYMMDD/<TASK_ID>.md`. Write execution reports to `<project>/task-hall/reports/YYYYMMDD/<TASK_ID>_REPORT.md`. GitHub `tasks/codex/latest.md` is compatibility-only and not the default daily dispatch surface.
