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

When execution starts, write the authoritative task to the project repository or GitHub task package.
