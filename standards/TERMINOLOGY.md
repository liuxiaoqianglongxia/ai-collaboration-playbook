# AI Collaboration Terminology

> **Purpose**: Standardize terms used across the AI collaboration playbook.
> **Version**: 1.0
> **Maintained in**: `ai-collaboration-playbook/standards/TERMINOLOGY.md`

---

## Core Terms

| Term | Definition | Context |
|------|-----------|---------|
| **总控 (Total Control)** | The orchestrator role — typically ChatGPT. Responsible for task decomposition, architecture judgment, acceptance criteria, and directing other agents. | Four-piece collaboration pattern |
| **执行线 (Execution Line)** | A focused work stream with a specific goal, scope, and deliverable. Each execution line has its own branch, tasks, and acceptance criteria. | Task management |
| **事实源 (Fact Source)** | The authoritative location for project truth. Under V2 and V3 Task Hall, Drive (or the local filesystem) is the daily fact source/workbench for tasks, reports, and materials; GitHub is the stable result/version surface for finalized docs, releases, and reusable artifacts. They serve different layers — do not treat one as replacing the other. | Project governance |
| **资产底账 (Asset Inventory)** | A comprehensive read-only inventory of all files, repositories, skills, standards, and reusable assets in a given environment. | Audit phase |
| **资产价值审计 (Asset Value Audit)** | An assessment that scores inventoried assets on reuse value, completeness, integration difficulty, risk, and business relevance. Assigns A/B/C/D/X classification. | Post-inventory phase |
| **入仓 (Enter Repository)** | The process of moving an asset from local/private/experimental state into a managed GitHub repository. Must pass safety checks (no secrets, no DBs, no logs). | Asset integration |
| **出仓 (Exit Repository)** | The process of removing or archiving assets from a repository. May involve migration to local-only, archival, or deletion. | Asset lifecycle |
| **脱敏 (Desensitization)** | Removing or replacing sensitive information (keys, tokens, internal URLs, personal data) before an asset enters a repository. Uses placeholder values. | Security |
| **冻结 (Freeze)** | A state where no changes are allowed to a project, file, or asset until a decision is made. Freeze is not archive — the asset still exists, just locked. | Risk management |
| **清理 (Cleanup)** | Removal of files, directories, or artifacts that are confirmed to have no reuse value, are duplicates, or are security risks. Requires human confirmation. | Maintenance |
| **归档 (Archive)** | Moving an asset to an archive location (not deleted, not active). Archives are preserved for reference but not maintained. | Asset lifecycle |
| **生产环境 (Production Environment)** | The live deployment environment serving real users. Subject to strict safety rules: no direct modification, rollback plan required, health checks mandatory. | Operations |
| **worktree** | A Git feature allowing multiple working trees from a single repository, each on a different branch. Useful for parallel development but requires lifecycle management. | Git operations |
| **子代理 (Sub-Agent)** | An agent launched by a parent agent to handle a specific sub-task. Must follow the same safety rules as the parent. Findings must be synthesized, not dumped raw. | Agent collaboration |
| **任务包 (Task Package)** | A self-contained unit of work assigned to an agent. Includes: goal, input, expected output, acceptance criteria, constraints, and stop conditions. | Task delegation |

## Status Values

| Status | Meaning | When to Use |
|--------|---------|-------------|
| ACTIVE | Project is under active development | Regular commits, open tasks |
| FROZEN | Project is temporarily locked | Waiting for decision, risk identified |
| ARCHIVED | Project is preserved for reference but not maintained | Completed, superseded, or paused indefinitely |
| EXPERIMENTAL | Project is a proof-of-concept or early experiment | Not production-ready, high uncertainty |
| PRODUCTION | Project serves real users with SLA expectations | Health checks, monitoring, rollback plans required |
| DEPRECATED | Project is being phased out | Migration in progress, sunset date planned |
| BLOCKED | Project cannot proceed due to external constraints | Missing access, unresolved dependency |
| UNKNOWN | Project status cannot be determined | No recent activity, no documentation |

## Result Values

| Result | Meaning |
|--------|---------|
| PASS | All acceptance criteria met, no risks introduced |
| PARTIAL PASS | Core work done but some items need follow-up |
| FAIL | Acceptance criteria not met or regressions introduced |
| BLOCKED | Cannot proceed due to missing context or risks |

## Task Hall Task Lifecycle States

These states apply to individual Task Hall task packages, NOT to projects. They are enforced by the Task Hall CLI (`lab/task-hall-mvp/taskhall/cli.py`). They coexist with but do not replace the project-level status values above.

| State | Meaning | Allowed Transitions |
|-------|---------|---------------------|
| DRAFT | Task package is being written; not yet ready for assignment | → READY, → ARCHIVED |
| READY | Task package is complete and available for claiming | → CLAIMED, → BLOCKED, → ARCHIVED |
| CLAIMED | An agent has claimed the task but not started work | → IN_PROGRESS, → BLOCKED, → ARCHIVED |
| IN_PROGRESS | Agent is actively working on the task | → NEEDS_ACCEPTANCE, → BLOCKED, → ARCHIVED |
| NEEDS_ACCEPTANCE | Work is done and submitted for review | → ACCEPTED, → NEEDS_REVISION, → BLOCKED, → ARCHIVED |
| NEEDS_REVISION | Review found issues; task goes back for rework | → READY, → BLOCKED, → ARCHIVED |
| ACCEPTED | Task passed acceptance review (final state) | → (terminal) |
| BLOCKED | Task cannot proceed due to external constraints | → READY, → ARCHIVED |
| ARCHIVED | Task is closed without completion (final state) | → (terminal) |

Final states (terminal): ACCEPTED, ARCHIVED.

Note: BLOCKED appears both here (task-level) and in project-level status. They share the same semantic meaning (cannot proceed due to external constraints) but apply to different scopes. A project being BLOCKED does not mean all its tasks are BLOCKED, and vice versa.
