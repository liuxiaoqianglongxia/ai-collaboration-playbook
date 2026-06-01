# Codex Task Package｜PLAYBOOK-DRIVE-NATIVE-V2-1-ABSORPTION-PATCH-CANDIDATE

task_id: PLAYBOOK-DRIVE-NATIVE-V2-1-ABSORPTION-PATCH-CANDIDATE
owner: Codex
controller: ChatGPT Pro
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
repo: liuxiaoqianglongxia/ai-collaboration-playbook

## Goal

Add a minimal V2.1 absorption patch that strengthens Drive-native V2 without renaming the stable baseline or disrupting old projects already using V2.

## Branch

Create a new branch:

```text
docs/drive-native-v2-1-absorption-patch
```

## Required Additive Files

Add the files from this package:

```text
standards/CHATGPT_DRIVE_TOOL_CAPABILITY_BOUNDARY_V2_1.md
standards/DRIVE_NATIVE_V2_ABSORPTION_AND_COMPATIBILITY_POLICY.md
standards/CLAUDE_CODE_FIRST_PASS_ROUTING_V2_1.md
guides/OLD_PROJECT_V2_ABSORPTION_GUIDE.md
guides/SMALL_PROJECT_DRIVE_NATIVE_V2_MINIMAL_GUIDE.md
templates/drive-native-v2/DRIVE_WRITE_FALLBACK_TO_CODEX_TEMPLATE.md
templates/drive-native-v2/CODEX_CLAUDE_INTERACTIVE_FIRST_PASS_TEMPLATE.md
templates/drive-native-v2/OLD_PROJECT_ABSORPTION_REPORT_TEMPLATE.md
checklists/drive-native-v2/DRIVE_PARENT_FOLDER_VERIFICATION_CHECKLIST.md
checklists/drive-native-v2/V2_1_ABSORPTION_ACCEPTANCE_CHECKLIST.md
protocols/drive-native-v2/V2_1_ABSORPTION_PATCH_FLOW.md
reports/chatgpt/pro-review/PRO_REVIEW_START_HERE_V2_1.md
reports/chatgpt/playbook-v2-1-controller-report.md
```

## Required Entrypoint Updates

Update these files with short patch notes only:

```text
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
reports/latest.md
guides/DRIVE_NATIVE_V2_USER_GUIDE.md
templates/drive-native-v2/README.md
```

Rules:

```text
- Keep stable baseline as PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS.
- Add patch-level candidate reference only.
- Do not replace V2 with V2.1 as the stable baseline.
- Do not restore tasks/codex/latest.md as default daily dispatch.
- Do not require old projects to rewrite all files immediately.
```

## Claude Code First-pass Requirement

Before finalizing, run Claude Code in interactive first-pass mode if available.

Give Claude the task in:

```text
tasks/claude/PLAYBOOK-DRIVE-NATIVE-V2-1-FIRST-PASS-REVIEW.md
```

Claude must review for:

```text
- baseline confusion
- old-project rollout risk
- registry default-dispatch residue
- Drive write/fallback ambiguity
- Claude/Codex responsibility conflict
- private local path leakage
```

Codex must verify or reject Claude findings before final integration.

If Claude Code is unavailable, record:

```text
Claude Code first-pass: skipped
reason: <reason>
Codex compensating checks: <checks>
```

## Checks

Run:

```text
git status -sb
git diff --check
rg -n "<DO_NOT_CREATE_A_NEW_V2_1_STABLE_BASELINE>|stable: <do-not-create-new-stable-baseline>|DRIVE_NATIVE_V2_CANDIDATE" README.md CHATGPT_START_HERE.md AI_AGENT_ONBOARDING.md reports/latest.md guides/ standards/ templates/ checklists/ protocols/ || true
rg -n "tasks/codex/latest.md.*default|GitHub-backed registry.*default daily|GitHub-first" README.md CHATGPT_START_HERE.md AI_AGENT_ONBOARDING.md guides/ standards/ templates/ protocols/ checklists/ || true
rg -n "<PRIVATE_LOCAL_PATH_OR_ACCOUNT_SPECIFIC_DRIVE_PATTERN>" README.md CHATGPT_START_HERE.md AI_AGENT_ONBOARDING.md guides/ standards/ templates/ protocols/ checklists/ reports/chatgpt || true
```

Interpretation:

```text
- V2_1 as stable baseline: FAIL
- DRIVE_NATIVE_V2_CANDIDATE in current stable entrypoint: FAIL unless historical section clearly labeled
- GitHub registry as default daily dispatch: FAIL
- private path in public docs: FAIL
```

## Report

Write:

```text
reports/codex/playbook-drive-native-v2-1-absorption-patch-candidate.md
reports/codex/latest.md
```

Report must include:

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
branch:
commit:
files changed:
Claude Code first-pass: PASS / PARTIAL PASS / skipped
checks:
old-project absorption impact:
forbidden scope confirmation:
next action:
```

## Forbidden Scope

```text
No business project changes.
No deployment.
No database changes.
No secrets changes.
No force push.
No tag deletion.
No main rewrite.
No PR merge without ChatGPT acceptance.
```
