# Decisions

## Active Decisions

| Date | Decision | Reason | Durable Link |
|---|---|---|---|
| 2026-06-01 | Promote V1.2 from candidate to stable if validation passes | The playbook itself is a valid self-dogfood project and V1.2 docs passed internal consistency checks | `reports/latest.md` |
| 2026-06-01 | Keep Drive as daily workbench, not code workspace | Prevents Drive/GitHub split-brain and keeps code in local Git | `standards/DRIVE_FIRST_WORKFLOW_V1.md` |
| 2026-06-01 | Keep Claude Code as Codex-coordinated first-pass worker | Uses Claude Code without replacing Codex final integration | `standards/CLAUDE_FIRST_CODEX_FINAL_V1.md` |

## Pending Decisions

- Whether future projects need project-specific tag naming beyond `dev-ok`, `pre-prod`, `prod`, and `rollback-before`.

## Rule

Daily notes may start in a workbench. Milestone decisions must be copied to the project repository.
