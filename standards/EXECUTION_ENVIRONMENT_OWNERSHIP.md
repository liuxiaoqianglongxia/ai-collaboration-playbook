# Execution Environment Ownership Standard

> **Purpose**: Define the preferred execution owner for playbook, business, local WSL, production, database, deployment, audit, archive, and low-risk migration work.
> **Version**: 1.0
> **Maintained in**: `ai-collaboration-playbook/standards/EXECUTION_ENVIRONMENT_OWNERSHIP.md`
> **Status**: Accepted for `PLAYBOOK_OPERATIONAL_BASELINE_V1`

---

## 1. Principle

Execution ownership is chosen by repository role, runtime risk, and allowed write scope.

Before any agent writes files, it must verify the local target against the task packet:

| Required Check | Required Evidence |
|----------------|-------------------|
| `repository_full_name` | The GitHub repository full name matches the task target |
| `branch` | The current branch or temporary branch matches the allowed branch |
| README title | The root `README.md` title matches the expected project identity |
| Allowed write scope | The requested file paths are inside the explicit write allowlist |

If any check fails, the agent must stop and report `BLOCKED` instead of guessing.

## 2. Preferred Owner Matrix

| Work Type | Preferred Owner | Notes |
|-----------|-----------------|-------|
| `ai-collaboration-playbook` general standards, templates, protocols, checklists, and reports | Mac Codex | This repository is the shared playbook and should be maintained through controlled local branches and reviewable reports. |
| Business project implementation | Windows Codex | Business repositories usually need project-local runtime context, local services, and product-specific validation. |
| Local WSL tasks | Windows Codex | WSL-local paths, shells, services, caches, and working trees should stay with the Windows-side operator unless explicitly reassigned. |
| Production environment tasks | Windows Codex | Production-like runtime, deployment, rollback, health checks, and incident handling require the environment owner with direct operational context. |
| Database tasks | Windows Codex | Database reads, migrations, dumps, restores, and production data handling require the stricter environment owner and explicit backup/rollback rules. |
| Deployment tasks | Windows Codex | Deploy, publish, release, service restart, and remote environment changes should not be routed through the playbook-maintenance lane. |
| Large audits | Mac Codex or Windows Codex by source repository and risk | Assignment must be decided after repository identity, branch, README title, and write scope checks. |
| Historical resource archives | Mac Codex or Windows Codex by source repository and risk | Prefer read-only inventory first; write only to an explicit archive allowlist. |
| Low-risk asset migration | Mac Codex or Windows Codex by source repository and risk | Allowed only when source, destination, transformation rules, and prohibited paths are explicit. |

## 3. Playbook Repository Lane

Mac Codex is the preferred owner for the `liuxiaoqianglongxia/ai-collaboration-playbook` repository when the task is about:

- shared standards;
- reusable templates;
- checklists;
- protocols;
- playbook reports;
- controlled recovery preflight work;
- documentation-only integration reports.

Mac Codex must still use temporary branches for preflight and integration work unless the task explicitly authorizes direct writes to the target branch.

## 4. Business And Operations Lane

Windows Codex is the preferred owner when a task touches any of the following:

- business project source code;
- local WSL runtime state;
- production or staging environments;
- databases or database backups;
- deployment scripts or release flows;
- service health checks that require local runtime ownership;
- project-specific `.env`, credentials, cookies, or login data.

The playbook repository may document generic rules for these tasks, but it must not become the execution surface for business or production changes.

## 5. Shared Audit And Archive Lane

Large audits, historical resource archives, and low-risk material migrations may be assigned to either Mac Codex or Windows Codex only after a source-and-risk gate.

The source-and-risk gate must confirm:

1. The exact `repository_full_name`.
2. The exact branch or temporary branch.
3. The root `README.md` title.
4. The explicit allowed write scope.
5. The prohibited repositories, paths, tools, and runtime actions.
6. Whether the task is read-only, report-only, archive-only, or allowed to transform files.
7. Whether production, database, deployment, secrets, cookies, or login data are in scope.

If the task includes production, database, deployment, secrets, cookies, or login data, default ownership shifts to Windows Codex unless the controller provides a narrower exception.

## 6. Stop Rules

An agent must stop and report `BLOCKED` when:

- the repository full name cannot be verified;
- the local branch does not match the task branch plan;
- the README title does not match the expected project;
- the write scope is missing or ambiguous;
- the requested work would cross into a prohibited repository;
- the task asks for production, database, deployment, or secret handling without an explicit owner and safety packet;
- a merge preflight finds conflicts and the task forbids conflict resolution.

## 7. Report Requirements

Every ownership-sensitive task should report:

- repository full name;
- local path;
- local branch;
- upstream branch or target branch;
- verified README title;
- allowed write scope;
- prohibited scope confirmation;
- owner selected and reason;
- whether a PR is recommended;
- whether the task should stay frozen pending controller review.
