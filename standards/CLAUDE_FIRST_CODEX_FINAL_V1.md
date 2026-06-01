# Claude First Codex Final Standard V1

> Standard ID: `CLAUDE_FIRST_CODEX_FINAL_V1`
> Status: Stable in `PLAYBOOK_OPERATIONAL_BASELINE_V1.2`

## Purpose

Make Claude Code useful as a first-pass engineering worker while keeping Codex responsible for final integration.

This standard does not change the V4 four-piece model.

## Core Rule

```text
Claude Code may do bounded first-pass engineering work.
Codex reviews Claude output and remains final integrator.
```

Normal flow:

```text
ChatGPT defines the goal and acceptance boundary.
Codex reads the active task and verifies scope.
Codex coordinates Claude Code when it adds value.
Claude Code returns analysis, a patch, or bounded local work.
Codex accepts, edits, or rejects the output.
Codex runs validation, owns the final diff, commit, push, PR when needed, and report.
ChatGPT accepts from durable facts.
```

Claude Code is not the final integrator.

## Claude-First Task Types

Prefer Claude Code first-pass support for:

- deep code reading;
- call-chain analysis;
- test failure localization;
- localized bugfix draft;
- mechanical multi-file draft;
- low-risk refactor draft;
- alternative implementation notes;
- read-only diff risk review.

## Codex-First Task Types

Keep Codex first for:

- repository state verification;
- final diff review;
- test and validation ownership;
- commit, push, tag, PR, and report;
- tasks with unclear scope;
- integration across unrelated areas;
- production, deployment, database, credential, or irreversible work;
- any task where Claude Code would need unsafe broad write access.

## When Claude May Edit Files

Claude Code may edit files only when the active Codex task or a bounded Claude task says all of the following:

```text
allowed files or directories
forbidden files or directories
allowed commands or checks
stop conditions
expected output or report format
Codex final integration remains required
```

Even then, Codex must inspect the diff before keeping any change.

## When Claude Should Produce Patch Only

Use patch-only mode when:

- write permission is risky;
- the change touches shared or sensitive files;
- multiple implementation options should be compared;
- the task needs a clear review boundary;
- the repository is dirty before Claude starts;
- the user or project profile disallows tool writes.

Patch-only output can be a diff, implementation notes, or a file-by-file change plan. Codex decides what to apply.

## How Codex Coordinates Claude Code

Codex may coordinate Claude Code by:

- invoking a bounded non-interactive Claude Code prompt;
- writing or reading a `tasks/claude/<TASK-ID>.md` file;
- asking for read-only review with restricted tools;
- asking for a patch draft instead of file writes;
- capturing Claude evidence in the Codex report.

Codex must record:

```text
Claude scope
files inspected or changed by Claude
recommendations accepted
recommendations rejected
validation Codex ran after review
```

## Rejection Rules

Codex must reject Claude output that:

- changes files outside allowed scope;
- treats Drive as the durable fact source;
- removes GitHub as milestone source;
- weakens V4 role boundaries;
- makes Claude Code final integrator;
- pushes, tags, deploys, changes databases, or handles secrets;
- starts a second active Codex execution lane;
- relies on unstated chat context instead of repository facts.

## Evidence Rule

Claude Code output is evidence, not authority.

Final status remains:

```text
PASS / PARTIAL PASS / FAIL / BLOCKED
```

Codex assigns that status in its execution report based on repository facts, validation, and scope compliance.
