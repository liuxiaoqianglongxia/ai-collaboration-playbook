# MANIFEST｜sub2api-maijian misroute recovery｜2026-05-30

## 1. Recovery metadata

```text
source_repository: liuxiaoqianglongxia/sub2api-maijian
source_commit: f542c0101f2a44396ee07b9f466a99607789eda5
target_repository: liuxiaoqianglongxia/ai-collaboration-playbook
target_branch: recovery/sub2api-misroute-20260530
recovery_date: 2026-05-30
archive_root: archive/recovered-from-sub2api-misroute/2026-05-30/
```

## 2. Why this archive exists

A previous GitHub connector session intended to initialize `liuxiaoqianglongxia/ai-collaboration-playbook`, but the write path was routed to the business repository `liuxiaoqianglongxia/sub2api-maijian`.

The files below belong to the AI collaboration playbook, not to the business repository. This manifest records recovery only. It does not clean, delete, restore, or otherwise modify `sub2api-maijian`.

## 3. Status vocabulary

```text
recovered: source path exists at source_commit and has been archived under archive_root.
missing_at_source_commit: source path does not exist at source_commit and cannot be archived.
skipped_with_reason: intentionally not archived, with a reason recorded.
```

## 4. Recovery result

```text
conclusion: PASS
recovered_count: 15
missing_at_source_commit_count: 0
skipped_with_reason_count: 0
```

## 5. File manifest

| source_path | archive_path | status | notes |
|---|---|---|---|
| `README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/README.md` | recovered | Archived from the source commit. |
| `AI_AGENT_ONBOARDING.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/AI_AGENT_ONBOARDING.md` | recovered | Archived from the source commit. |
| `AI_COLLABORATION_MODE_V4.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/AI_COLLABORATION_MODE_V4.md` | recovered | Archived from the source commit; this recovered artifact does not replace the current V4 main spec. |
| `NEW_PROJECT_BOOTSTRAP.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/NEW_PROJECT_BOOTSTRAP.md` | recovered | Archived from the source commit. |
| `modules/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/modules/README.md` | recovered | Archived from the source commit. |
| `templates/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/templates/README.md` | recovered | Archived from the source commit. |
| `checklists/README.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/checklists/README.md` | recovered | Archived from the source commit. |
| `lab/CODEX_AGENTIC_WORKBENCH_V0_1.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/CODEX_AGENTIC_WORKBENCH_V0_1.md` | recovered | Archived from the source commit. |
| `lab/CODEX_HERMES_TRANSLATION_NOTES.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/CODEX_HERMES_TRANSLATION_NOTES.md` | recovered | Archived from the source commit. |
| `lab/experiments/001-heartbeat-readonly.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/001-heartbeat-readonly.md` | recovered | Archived from the source commit. |
| `lab/experiments/002-skill-start-here-audit.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/002-skill-start-here-audit.md` | recovered | Archived from the source commit. |
| `lab/experiments/003-subagent-readonly-scout.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/003-subagent-readonly-scout.md` | recovered | Archived from the source commit. |
| `lab/experiments/004-memory-distillation.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/004-memory-distillation.md` | recovered | Archived from the source commit. |
| `lab/experiments/005-mcp-docs-context.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/lab/experiments/005-mcp-docs-context.md` | recovered | Archived from the source commit. |
| `reports/latest.md` | `archive/recovered-from-sub2api-misroute/2026-05-30/reports/latest.md` | recovered | Archived from the source commit, completing the earlier archive gap. |

## 6. Boundaries

```text
This recovery does not enter V0.3.
This recovery does not create examples/.
This recovery does not test Claude Code.
This recovery does not modify the V4 mainline spec.
This recovery does not write to sub2api-maijian.
This recovery does not clean sub2api-maijian.
This recovery does not touch business code, sensitive local configuration, databases, deployment, or automation.
```

## 7. Follow-up

The archive is complete enough to allow Full Whitepaper Recovery. Cleanup of `sub2api-maijian` must remain a separate task owned by that project controller.
