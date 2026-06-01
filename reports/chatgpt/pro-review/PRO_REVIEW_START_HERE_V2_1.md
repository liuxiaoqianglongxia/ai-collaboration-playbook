# PRO_REVIEW_START_HERE_V2_1

purpose: ChatGPT Pro review entry for `DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE`
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
status: candidate review entry

## Review Question

Does the V2.1 absorption patch improve Drive-native V2 without creating a second baseline or confusing old projects already using V2?

## Required Inputs

Review:

```text
PATCH_MANIFEST.md
standards/CHATGPT_DRIVE_TOOL_CAPABILITY_BOUNDARY_V2_1.md
standards/DRIVE_NATIVE_V2_ABSORPTION_AND_COMPATIBILITY_POLICY.md
standards/CLAUDE_CODE_FIRST_PASS_ROUTING_V2_1.md
guides/OLD_PROJECT_V2_ABSORPTION_GUIDE.md
guides/SMALL_PROJECT_DRIVE_NATIVE_V2_MINIMAL_GUIDE.md
protocols/drive-native-v2/V2_1_ABSORPTION_PATCH_FLOW.md
reports/codex/playbook-drive-native-v2-1-absorption-patch-candidate.md
```

## Required Checks

```text
1. V2 remains current stable baseline.
2. V2.1 is additive patch-level, not competing stable baseline.
3. ChatGPT Drive write boundary is clear.
4. Codex local Drive sync fallback is actionable.
5. Drive parent-folder verification is required after writes.
6. User does not need to copy long task packages in normal flow.
7. GitHub-backed registry remains compatibility only.
8. Claude Code interactive first-pass routing is practical and bounded.
9. Old projects can absorb Level 1 patch quickly.
10. No production, database, secret, force-push, tag-delete, or unrelated-project risk.
```

## Expected Output

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED

1. Executive verdict
2. Evidence reviewed
3. What changed
4. What remains weak
5. Old-project absorption verdict
6. ChatGPT / Drive write boundary verdict
7. Claude Code / Codex routing verdict
8. GitHub registry compatibility verdict
9. Required changes before promotion
10. Final recommendation
```

## Decision Rule

```text
PASS:
Patch is coherent, additive, and safe for old-project absorption.

PARTIAL PASS:
Patch is directionally correct but needs small edits before promotion.

FAIL:
Patch creates a competing baseline, restores GitHub-first default dispatch, or makes old-project adoption confusing.

BLOCKED:
Required Codex/Claude reports or patch files are missing.
```
