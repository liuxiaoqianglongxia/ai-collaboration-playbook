# Codex Task Draft

## Task

```text
task_id: PLAYBOOK-V1.2-SELF-DOGFOOD-STABLE-FREEZE-V1
goal: self-test V1.2 and freeze it as stable if checks pass
repository: liuxiaoqianglongxia/ai-collaboration-playbook
branch: main
```

## Scope

Allowed:

- active entry docs
- personalization final
- Pro review entry
- Codex report and latest pointer
- repository-local self-test workbench

Forbidden:

- `AI_COLLABORATION_MODE_V4.md`
- production deployment
- database changes
- credential or secret changes
- force push
- cross-project writes

## Claude Code Support

```text
mode: read-only first-pass attempted by Codex
final_integrator: Codex
```

## Acceptance

- V1.2 self-test workbench exists.
- V1.2 is current stable in active entry docs.
- V1.1 history remains visible.
- No normal-flow doc tells the user to directly assign Claude Code.
- Codex latest pointer is cleared after completion.

## Handoff

The authoritative task is `tasks/codex/PLAYBOOK-V1.2-SELF-DOGFOOD-STABLE-FREEZE-V1.md`.
