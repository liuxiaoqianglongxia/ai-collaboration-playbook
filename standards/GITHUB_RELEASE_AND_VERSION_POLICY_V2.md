# GitHub Release And Version Policy V2

> Standard ID: `GITHUB_RELEASE_AND_VERSION_POLICY_V2`
> Status: Stable in `PLAYBOOK_OPERATIONAL_BASELINE_V2`

## Purpose

Keep GitHub clean as the stable result, release, rollback, and reusable documentation carrier for Drive-native V2.

## GitHub Responsibilities

GitHub stores:

- stable main code/docs
- optional dev branch
- release tags
- rollback tags
- release notes
- milestone summaries
- public reusable documentation
- PR records and review history

GitHub does not store by default:

- daily task chatter
- raw screenshots
- temporary handoffs
- raw materials
- transient acceptance notes

## Branch Policy

Keep:

- `main`
- `dev` when intentionally active
- `release/*`
- `prod/*`
- `hotfix/*`
- protected branches
- unmerged or uncertain branches

Delete only after inventory:

- non-protected work branches
- not main/dev/release/prod/hotfix
- with a merged PR or a tip reachable from `origin/main`
- with no unmerged commits
- already listed in a branch inventory report

## Tag Policy

Tags are version anchors. Do not delete tags during branch cleanup.

Recommended classes:

- `dev-ok-YYYYMMDD`
- `pre-prod-YYYYMMDD`
- `prod-YYYYMMDD`
- `rollback-before-YYYYMMDD`

## Release Sync Policy

Sync to GitHub only when the result is:

- stable reusable documentation
- release summary
- milestone summary
- production deployment reference
- rollback note

V2 stable documentation may move from draft to ready after role-conflict, private-path, cross-project pollution, and registry-residue checks pass.
