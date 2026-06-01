# Drive-native V2 User Guide

> Status: Candidate

## What Changed

Drive-native V2 moves daily collaboration into Drive and keeps GitHub for stable outcomes.

```text
Drive = daily fact source
GitHub = stable result / version / release / rollback / reusable docs
```

## How To Use It

For daily work, the controller reads and writes the Drive workbench:

- current state
- task package
- report
- daily log
- decision record
- handoff
- temporary acceptance
- materials and screenshots

For stable work, the controller or Codex syncs to GitHub:

- reusable docs
- PRs
- main commits
- tags
- release notes
- rollback notes

## User-facing Pattern

You can give a short instruction:

```text
Use the Drive task package and complete the current Codex task. Write the report back to Drive.
```

When a GitHub sync is needed:

```text
Sync the accepted reusable V2 docs to GitHub as a draft PR.
```

## What Not To Do

- Do not use GitHub daily task pointers as the default V2 dispatch surface.
- Do not keep branches as release records.
- Do not promote Drive raw materials directly to stable GitHub docs.
- Do not deploy, edit databases, change secrets, or force push without explicit authorization.

## Acceptance

V2 becomes stable only after ChatGPT acceptance confirms:

- Drive structure is complete
- entry files agree on V2 roles
- GitHub branch cleanup is safe
- reusable GitHub docs do not depend on a private Drive path as the only entrance
- forbidden scope was not touched
