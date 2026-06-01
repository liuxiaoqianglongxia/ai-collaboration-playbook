# Drive First Workflow Standard V1

> Standard ID: `DRIVE_FIRST_WORKFLOW_V1`
> Status: Stable in `PLAYBOOK_OPERATIONAL_BASELINE_V1.2`

## Purpose

Define the fast daily workbench layer for project coordination.

This standard does not change the V4 four-piece model:

```text
ChatGPT remains controller and acceptance owner.
GitHub remains the durable fact source and milestone ledger.
Codex remains the final integrator.
Claude Code remains an engineering support worker coordinated by Codex.
```

## Core Rule

Drive is the daily workbench for:

- tasks;
- reports;
- screenshots;
- materials;
- handoffs;
- temporary acceptance notes.

Drive is not the live code workspace.

Code stays in WSL/local Git. In Codex work, WSL/local Git means the local execution workspace where Codex reads, edits, tests, commits, and tags.

GitHub stays the milestone version source, production reference, and rollback point.

## Workbench Layout

```text
Google Drive/AI工作台/<project>/
  00_CURRENT.md
  01_TASKS.md
  02_DECISIONS.md
  03_CODEX_TASK.md
  04_CODEX_REPORT.md
  05_CHATGPT_ACCEPTANCE.md
  screenshots/
  materials/
  exports/
  archive/
```

## File Purposes

`00_CURRENT.md`:

```text
Current project state, active goal, current blocker, and next action.
Short enough for daily scanning.
```

`01_TASKS.md`:

```text
Daily task queue, current active task, candidate next steps, and closed items.
Detailed executable task packages still belong in the project fact source when execution starts.
```

`02_DECISIONS.md`:

```text
Short decision log for daily coordination.
Milestone or architecture decisions must be copied back to the project repository.
```

`03_CODEX_TASK.md`:

```text
Daily handoff draft for Codex.
When execution begins, the authoritative task is the GitHub task package or the project repository task file.
```

`04_CODEX_REPORT.md`:

```text
Daily report draft or summary.
Final Codex execution reports must be written to the project repository.
```

`05_CHATGPT_ACCEPTANCE.md`:

```text
Temporary acceptance notes for fast review.
Final acceptance must reference GitHub facts, code diffs, tests, tags, runtime evidence, or project repository reports.
```

`screenshots/`:

```text
Screenshots and visual evidence for daily triage.
Important evidence should be linked from the final report.
```

`materials/`:

```text
Inputs, drafts, specs, exports from tools, customer notes, and raw references.
```

`exports/`:

```text
Shareable outputs copied from the workbench.
```

`archive/`:

```text
Closed daily notes and obsolete drafts.
Archive content is historical evidence, not current status.
```

## Drive To GitHub Sync

Drive accelerates daily work, but GitHub remains the durable source for milestones.

Sync Drive content back to GitHub when any of these happens:

- a Codex task starts and needs an executable task package;
- a task closes with PASS, PARTIAL PASS, FAIL, or BLOCKED;
- a decision affects code, architecture, deployment, risk, or project ownership;
- a main commit, release tag, production anchor, or rollback point is created;
- ChatGPT needs an acceptance snapshot that future sessions must trust.

Do not keep two competing current states. If Drive and GitHub disagree during project work, read GitHub facts before making a final judgment.

## Forbidden Drift

Do not:

- use Drive as the live code workspace;
- store secrets or production credentials in Drive workbench files;
- treat Drive notes as final acceptance when GitHub evidence is required;
- remove GitHub as milestone source, production reference, or rollback point;
- ask the user to manage long task packages manually when an agent can write the durable task file.
