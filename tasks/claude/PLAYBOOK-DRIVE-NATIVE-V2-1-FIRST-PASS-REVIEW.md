# Claude Code Task｜PLAYBOOK-DRIVE-NATIVE-V2-1-FIRST-PASS-REVIEW

task_id: PLAYBOOK-DRIVE-NATIVE-V2-1-FIRST-PASS-REVIEW
owner: Claude Code
coordinator: Codex
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
mode: first-pass review

## Role

You are Claude Code working as a first-pass reviewer under Codex orchestration.

Codex remains final integrator. Do not commit, push, tag, release, deploy, or modify production-like resources.

## Goal

Review the V2.1 absorption patch candidate for clarity, scalability, and old-project safety.

## Review Scope

Read the proposed files:

```text
standards/CHATGPT_DRIVE_TOOL_CAPABILITY_BOUNDARY_V2_1.md
standards/DRIVE_NATIVE_V2_ABSORPTION_AND_COMPATIBILITY_POLICY.md
standards/CLAUDE_CODE_FIRST_PASS_ROUTING_V2_1.md
guides/OLD_PROJECT_V2_ABSORPTION_GUIDE.md
guides/SMALL_PROJECT_DRIVE_NATIVE_V2_MINIMAL_GUIDE.md
templates/drive-native-v2/DRIVE_WRITE_FALLBACK_TO_CODEX_TEMPLATE.md
templates/drive-native-v2/CODEX_CLAUDE_INTERACTIVE_FIRST_PASS_TEMPLATE.md
checklists/drive-native-v2/DRIVE_PARENT_FOLDER_VERIFICATION_CHECKLIST.md
protocols/drive-native-v2/V2_1_ABSORPTION_PATCH_FLOW.md
```

Also inspect current entrypoints:

```text
README.md
CHATGPT_START_HERE.md
AI_AGENT_ONBOARDING.md
reports/latest.md
guides/DRIVE_NATIVE_V2_USER_GUIDE.md
```

## Questions To Answer

1. Does the patch preserve V2 as the stable baseline?
2. Does it avoid forcing all old projects into a full rewrite?
3. Is the ChatGPT Drive write boundary operationally clear?
4. Is the Codex local Drive sync fallback actionable?
5. Does Claude Code remain first-pass only?
6. Does the routing encourage interactive Claude Code usage enough to reduce Codex analysis cost?
7. Does it accidentally restore GitHub-backed registry as default daily dispatch?
8. Are there private local path leaks in public docs?
9. Are there candidate/stable conflicts?
10. What is the smallest safe change before PR?

## Output Format

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED

1. Executive finding
2. Blocking issues
3. Non-blocking issues
4. Old-project absorption risk
5. Routing risk
6. Suggested edits
7. Codex final-validation requirements
```

## Forbidden

```text
No production.
No database.
No secrets.
No force push.
No tag changes.
No PR merge.
No final integration decision.
```
