# Claude Code First-pass Routing V2.1

standard_id: CLAUDE_CODE_FIRST_PASS_ROUTING_V2_1
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
status: candidate
scope: Codex-orchestrated Claude Code usage

## Purpose

Use Claude Code more aggressively for first-pass engineering work while keeping Codex responsible for final integration, validation, reports, PRs, tags, releases, and rollback decisions.

## Default Routing

```text
ChatGPT: controller, task design, acceptance, release decision
Codex: execution owner, final integrator, validation, report, GitHub sync
Claude Code: first-pass engineering worker under Codex orchestration
```

## When Claude Code Should Be First-pass

Codex should prefer Claude Code first-pass for:

```text
- deep code reading
- call-chain analysis
- failing-test localization
- lint/type/test error diagnosis
- small localized bugfix draft
- scoped mechanical edits
- low-risk refactor draft
- PR diff risk review
- alternative implementation comparison
```

## When Codex Must Own Execution Directly

Codex must remain first and final owner for:

```text
- repository state verification
- final diff review
- tests and validation
- commits
- pushes
- PR creation or merge preparation
- tags
- releases
- rollback notes
- production, database, secret, or deployment-adjacent work
```

## Preferred Mode Order

### 1. Interactive Claude Code first-pass

Use for long analysis, exploratory refactor planning, ambiguous codebase navigation, or multi-step engineering diagnosis.

Required guardrails:

```text
- start from an explicit task prompt
- define allowed paths
- define forbidden paths
- require stop-before-final-integration
- require report back to Codex
- no deployment
- no database changes
- no secret changes
- no force push
- no tag changes
```

### 2. Non-interactive read-only review

Use for quick second opinion, diff review, log summarization, or failure analysis when no edits are needed.

Required guardrails:

```text
- no write tools, if the local tool supports restriction
- output only findings, risks, suggested next steps
- Codex verifies before acting
```

### 3. Bounded implementation draft

Use only when scope is narrow and explicit.

Required guardrails:

```text
- allowed files listed
- forbidden files listed
- no final commit
- no PR
- no release
- no tag
- Codex reviews diff before accepting
```

## Evidence Capture

Codex report must include:

```text
Claude mode: interactive / non-interactive / bounded-edit / skipped
Claude task id:
Claude allowed scope:
Claude forbidden scope:
Claude files inspected:
Claude files changed or patch produced:
Claude recommendations accepted:
Claude recommendations rejected:
Codex final diff review: PASS / PARTIAL PASS / FAIL / BLOCKED
Codex checks run:
Forbidden scope touched: yes/no
```

## Quota Optimization Principle

Use Claude Code to spend Claude quota on high-token code reading and first-pass reasoning.

Preserve Codex quota for:

```text
- deterministic repo checks
- final integration
- validation
- report writing
- GitHub sync
```

## Auto-permission Safety Rule

Do not treat any automated permission mode as a replacement for Codex verification.

Even if Claude Code is allowed to edit files, Codex must still inspect the diff, run checks, and own the final report.
