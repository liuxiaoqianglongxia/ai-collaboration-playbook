# Claude Task Package Template

task_id: <TASK-ID>
mode: DRIVE_NATIVE_V2
owner: Claude Code
coordinator: Codex

## Role

Claude Code provides first-pass support. Codex remains final integrator.

## Allowed

- read scoped files
- analyze failures
- draft localized patch suggestions
- identify risks

## Forbidden

- final integration
- deployment
- database or secret changes
- release, tag, or branch cleanup decisions

## Output

Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED

- findings:
- risks:
- suggested follow-up:
