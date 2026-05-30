# WSL Hermes Asset Audit — 2026-05-30

This audit was performed as a read-only inventory of all AI project assets
in the WSL environment at `/home/hermes/`.

## Files

- [`wsl-hermes-audit.md`](./wsl-hermes-audit.md) — Full audit report

## Scope

- `/home/hermes/projects/` — 35+ directories, 19 git repositories
- `/home/hermes/knowledge/` — standards, teams, team-memory, archive
- `/home/hermes/.hermes/` — 86 skills, 20+ plugins, 8 roles, agent core

## Key Findings

- 19 git repositories found, many with uncommitted changes
- 86 Hermes skills, 17 knowledge standards, extensive prompt/agent/workflow assets
- Multiple `.env` files and `auth.json` with API credentials detected
- Large state databases (~2.3GB) and production database backups require review
- maijian-wechat has 250 uncommitted files needing triage

## Next Steps

See Section 6 of the full report for prioritized recommendations.
