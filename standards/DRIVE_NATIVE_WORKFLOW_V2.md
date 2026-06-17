# Drive-native Workflow V2

> Standard ID: `DRIVE_NATIVE_WORKFLOW_V2`
> Status: Stable in `PLAYBOOK_OPERATIONAL_BASELINE_V2`

## Purpose

Define the Drive-native daily workflow while keeping GitHub as the durable carrier for stable results, versions, releases, rollback anchors, and reusable documentation.

## Core Model

```text
Drive-native V2 = daily development collaboration
GitHub = stable result / version management / release / rollback / reusable documentation
```

Drive owns the daily working surface:

- task packages
- reports
- daily logs
- decision records
- handoffs
- temporary acceptance
- screenshots and materials

GitHub owns the stable and reusable surface:

- main stable code/docs
- optional dev branch
- release tags
- rollback tags
- release notes
- milestone summaries
- final reusable documentation

## Daily Flow

1. ChatGPT reads Drive current state, decisions, reports, and acceptance notes.
2. ChatGPT creates or updates the Drive task package.
3. Codex executes when local work, validation, branch cleanup, PR creation, or GitHub sync is needed.
4. Claude Code may provide first-pass engineering support only when coordinated by Codex.
5. Codex writes a named Drive report.
6. ChatGPT accepts from Drive and GitHub evidence.
7. Stable reusable results are synced to GitHub through a branch, PR, main commit, tag, release note, or milestone summary.

## GitHub Pointer Rule

`tasks/codex/latest.md` and `tasks/claude/latest.md` remain valid historical repository-backed mechanisms, but they are compatibility entries. Normal Drive-native V2 work uses Drive task packages.

Use GitHub task pointers only when an executable task must be anchored in the repository.

## Stable Rule

Current stable status:

```text
PLAYBOOK_OPERATIONAL_BASELINE_V2
PASS
```

V1.1 and V1.2 remain historical baselines.

## Safety

Do not:

- store secrets, production credentials, databases, or build caches in Drive
- deploy from Drive
- treat raw Drive materials as stable GitHub documentation
- force push
- delete main, tags, protected branches, or unmerged branches
- modify unrelated business projects
