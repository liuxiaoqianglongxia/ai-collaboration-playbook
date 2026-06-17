# Routing And Extensibility Standard V1

> **Standard ID**: `ROUTING_AND_EXTENSIBILITY_V1`
> **Status**: Historical stable baseline from `PLAYBOOK_OPERATIONAL_BASELINE_V1.2`
> **Current V2 note**: historical routing baseline. Current default routing starts from `QUICK_START.md` and `standards/DRIVE_NATIVE_WORKFLOW_V2.md`.
> **Maintained in**: `ai-collaboration-playbook/standards/ROUTING_AND_EXTENSIBILITY_V1.md`

---

## Purpose

Define how the playbook routes work across stable roles and optional tools without becoming rigid.

The playbook must remain reusable:

```text
General standards stay general.
Project-specific facts stay in the project repository.
Optional tools can be routed in, but they are not default members unless the project fact source explicitly says so.
```

V1.2 adds a Drive-first daily workbench and main+tag versioning layer. These layers do not replace the universal V4 roles.

## Layers

### Universal Layer

Applies to all projects using this playbook:

- GitHub is the durable milestone fact source.
- Drive may be the daily workbench for tasks, reports, screenshots, materials, handoffs, and temporary acceptance notes.
- WSL/local Git is the real code workspace.
- Main is the default milestone branch.
- Tags are the version, production, and rollback anchors.
- ChatGPT controls judgment, task packages, and acceptance.
- Codex owns local execution and final integration.
- Claude Code supports first-pass engineering work, deep analysis, and review when Codex coordinates it.
- One project stage has one active execution lane.

### Project Layer

Each project owns its own facts:

```text
CHATGPT_START_HERE.md
AGENTS.md
CLAUDE.md
CURRENT.md
TASKS.md
DECISIONS.md
reports/latest.md
tasks/codex/latest.md
tasks/claude/latest.md
```

Project files override generic examples. Generic playbook files do not prove the state of a business repository.

### Execution Lane

The default execution lane is one active Codex task.

Use this lane for:

- code changes;
- local commands;
- tests;
- multi-file integration;
- branch and PR delivery;
- main push and tag creation when authorized by the active task;
- execution reports.

### Tool Lane

Optional tools may support the active execution lane.

Examples:

- Claude Code for deep reading or review;
- Claude Code for bounded first-pass implementation or patch drafts;
- Qwen or another cheaper model for bounded batch summarization;
- MCP or browser/docs tools for official documentation lookup;
- local scripts for repeatable checks.

Tool-lane output is evidence. Codex and ChatGPT must review it before it changes final status.

### Research Lane

Use for read-only investigation before promotion.

Examples:

- lab experiments;
- historical resource review;
- official documentation research;
- Pro deep review;
- optional tool feasibility checks.

Research output should become candidate next steps, not immediate default process.

### High-Risk Lane

Use a separate safety task package and explicit user authorization for:

- production;
- deployment;
- database;
- credentials or secrets;
- data deletion;
- force push;
- automation publish chains;
- service restarts.

### Drive Workbench Lane

Use Drive for daily working material:

- current note;
- task queue;
- decision drafts;
- Codex handoff draft;
- Codex report draft;
- ChatGPT acceptance notes;
- screenshots and materials.

Drive lane output becomes durable only after it is synced into the project repository, GitHub report, commit, tag, PR, or acceptance snapshot.

## Routing Matrix

| Work Type | Default Route | Notes |
|---|---|---|
| Normal non-project chat | ChatGPT conversation | Does not trigger project controller mode |
| Project status or execution question | ChatGPT reads project facts | Then choose Drive, GitHub, Codex, or Claude route |
| Daily task/report/material note | Drive workbench | Sync durable facts back to GitHub when execution or acceptance starts |
| Safe documentation fix | ChatGPT direct work if GitHub write access exists | Codex only if local integration is needed |
| Task package creation | ChatGPT | Must write durable GitHub task file when execution is required |
| Local execution / tests / PR | Codex | Codex remains final integrator |
| Main push / tag anchor | Codex | Only when the active task authorizes it |
| Deep code reading / failure analysis | Codex coordinates Claude Code | Claude Code output is evidence, not authority |
| Bounded first-pass implementation | Codex coordinates Claude Code | Codex reviews diff and owns final integration |
| Read-only diff review | Claude Code through Codex or task pointer | Must preserve report evidence |
| Cheap batch summarization | Qwen or similar optional tool | Only inside a bounded task; no final authority |
| Historical method or automation idea | Hermes/lab/research lane | Not a default runtime member |
| Official docs lookup | MCP/browser/docs tool | Must not override project fact source |
| Pro deep review | Research lane | Produces recommendations for ChatGPT acceptance |
| Production/deploy/database/secret work | High-risk lane | Requires separate authorization and safety package |

## Flexibility Rules

- Do not turn the playbook into a one-size-fits-all process.
- Keep the universal layer small.
- Let each project define its own local commands, deployment rules, risk boundaries, and owner preferences.
- Let each project decide how much daily work belongs in Drive.
- Route optional tools by evidence and risk, not by hype.
- Promote lab ideas only after read-only evidence, report, acceptance, and clear rollback boundaries exist.

## Forbidden Drift

Do not:

- add Hermes, Qwen, MCP, heartbeat, automation, or subagents as default members;
- let Claude Code replace Codex as final integrator;
- let Drive replace GitHub as durable milestone source;
- use branches as version records when tags are the intended anchor;
- let optional tools write overlapping files without one responsible integrator;
- copy business project facts into generic standards;
- use generic templates as current project status.
