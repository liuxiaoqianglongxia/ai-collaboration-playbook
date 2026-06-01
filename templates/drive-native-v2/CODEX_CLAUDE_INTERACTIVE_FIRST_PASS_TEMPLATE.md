# Codex-Claude Interactive First-pass Template

task_id: <TASK-ID>
mode: DRIVE_NATIVE_V2
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
owner: Codex
worker: Claude Code

## Purpose

Use Claude Code interactively for high-token first-pass analysis while preserving Codex as final integrator.

## Recommended Use

Use this template when the task benefits from:

```text
deep code reading
call-chain tracing
test-failure localization
localized bugfix draft
low-risk refactor draft
PR diff risk review
```

## Claude Interactive Prompt

```text
You are Claude Code working as a first-pass engineering worker under Codex orchestration.

Task: <TASK-ID>
Project: <PROJECT>
Goal: <GOAL>

Allowed paths:
<ALLOWLIST>

Forbidden paths:
<FORBIDDEN>

Rules:
- Do not deploy.
- Do not modify databases.
- Do not modify secrets.
- Do not force push.
- Do not create or delete tags.
- Do not commit or open PRs.
- Stop before final integration.
- Produce findings, risks, and a proposed patch or change plan.
- Codex will verify all outputs before acceptance.

Required output:
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
Files inspected:
Files changed or patch proposed:
Findings:
Risks:
Suggested checks:
Stop condition hit: yes/no
```

## Codex Validation After Claude

Codex must record:

```text
Claude mode: interactive
Claude output accepted: yes/no/partial
Accepted parts:
Rejected parts:
Reason for rejection:
Codex diff review:
Checks run:
Final files changed:
Forbidden scope touched: yes/no
```

## Quota Strategy

Let Claude spend tokens on broad reading and exploratory reasoning.

Let Codex spend tokens on final deterministic work:

```text
git status
git diff
tests
lint/type checks
report
GitHub sync
```
