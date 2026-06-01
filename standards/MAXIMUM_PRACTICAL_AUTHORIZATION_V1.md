# Maximum Practical Authorization Standard V1

> Standard ID: `MAXIMUM_PRACTICAL_AUTHORIZATION_V1`
> Status: Candidate in `PLAYBOOK_OPERATIONAL_BASELINE_V1.2_CANDIDATE`

## Purpose

Reduce unnecessary approval friction while keeping high-risk actions protected.

Ordinary work should be allowed by default inside the active task and project routing profile.

Do not ask for approval for every small action when the current task already authorizes it.

## Default Allowed Zone

When the active task and project routing profile allow the work, agents may normally:

- read project fact-source files;
- update documentation inside allowed paths;
- create or update task packages, reports, and latest pointers;
- edit local code in allowed files;
- run local tests, linters, type checks, and build checks;
- coordinate Claude Code as bounded first-pass support;
- commit and push low-risk collaboration or milestone work when the task explicitly asks for it;
- create tags when the task explicitly asks for a version anchor.

## Protected Zone

Explicit confirmation is required for:

- production deployment;
- database writes, migrations, or data deletion;
- credential, token, cookie, secret, or `.env` changes;
- service restarts or process killing outside the task scope;
- destructive filesystem cleanup;
- force push or history rewrite;
- production automation or publish chain changes;
- changing billing, permissions, access control, or ownership;
- cross-repository writes;
- actions that expose private data outside the approved workspace.

## Project Overrides

The project routing profile may tighten defaults.

Examples:

```text
deployment_allowed: no
database_changes_allowed: no
claude_file_edits_allowed: patch-only
direct_main_allowed: docs-only
tag_creation_allowed: explicit-task-only
```

Project facts override generic convenience rules.

## Approval Pattern

Ask for confirmation when:

- the action is in the protected zone;
- the task scope is unclear;
- a tool needs broader permission than the task allowed;
- the working tree contains unrelated changes that affect the task;
- the change could be irreversible or user-visible in production.

Do not ask again for the same low-risk action when the task already authorized the category and the project profile does not forbid it.

## Forbidden Drift

Maximum practical authorization is not blanket authorization.

It does not allow:

- bypassing task scope;
- weakening GitHub fact-source discipline;
- making Drive the durable source;
- giving Claude Code final integration authority;
- changing production, databases, secrets, or deploy chains by default.
