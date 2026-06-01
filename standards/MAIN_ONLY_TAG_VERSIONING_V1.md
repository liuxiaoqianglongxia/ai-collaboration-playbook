# Main Only Tag Versioning Standard V1

> Standard ID: `MAIN_ONLY_TAG_VERSIONING_V1`
> Status: Stable in `PLAYBOOK_OPERATIONAL_BASELINE_V1.2`

## Purpose

Reduce branch ceremony while preserving version anchors and rollback points.

## Core Rule

Default:

```text
main only
```

Use tags for versions.

Use branches only when a real review or integration boundary is useful.

Do not use branches as version records.

Delete stale merged or closed branches when the repository workflow allows it.

Enable automatic branch cleanup when available.

## Tag Types

Suggested tag names:

```text
dev-ok-YYYYMMDD
pre-prod-YYYYMMDD
prod-YYYYMMDD
rollback-before-YYYYMMDD
```

Meaning:

`dev-ok-YYYYMMDD`:

```text
Main is locally validated enough to serve as a development anchor.
```

`pre-prod-YYYYMMDD`:

```text
Main is ready for pre-production validation or staging handoff.
```

`prod-YYYYMMDD`:

```text
Main is the production reference for a specific date or release window.
```

`rollback-before-YYYYMMDD`:

```text
Known rollback point captured before a risky release, migration, deploy, or cleanup.
```

## Branch Use

Branches remain useful for:

- risky code changes;
- review-heavy implementation;
- multi-commit integration;
- protected branch workflows;
- experiments that must not touch main;
- hotfixes that need isolated validation.

Branches are not the durable version record. After merge, the version anchor should be a tag on main.

## GitHub Relationship

GitHub remains the milestone source, production reference, and rollback point.

Main stores accepted milestone code and stable collaboration artifacts.

Tags store named anchors that can be used for release notes, deployment references, and rollback decisions.

## Forbidden Drift

Do not:

- keep stale branches as pseudo-releases;
- tag unreviewed or unvalidated commits as production anchors;
- create a branch only to record a version name;
- force push tags or main unless explicitly authorized;
- let tag creation imply deployment, database changes, or production rollout by itself.
