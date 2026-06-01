# Drive-native V2 Absorption And Compatibility Policy

standard_id: DRIVE_NATIVE_V2_ABSORPTION_AND_COMPATIBILITY_POLICY
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
status: candidate

## Purpose

Allow projects already using Drive-native V2 to absorb V2.1 improvements without a disruptive migration or a new collaboration vocabulary.

## Stability Rule

Do not rename the current stable baseline during patch rollout.

Keep:

```text
stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
```

Add only:

```text
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
```

After acceptance:

```text
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH / PASS
```

## Absorption Levels

### Level 0: Existing V2 project

The project already has:

```text
Drive workbench
GitHub stable facts
Codex report path
Drive task package flow
GitHub-backed registry compatibility only
```

No urgent rewrite required.

### Level 1: Minimal patch absorption

Add these lines to the project Drive `00_HOME.md` or `01_CURRENT.md`:

```text
baseline: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
chatgpt_drive_write_rule: verify_parent_folder_or_fallback_to_codex
codex_drive_fallback: local_google_drive_sync_directory
claude_code_route: interactive_first_pass_under_codex_when_useful
registry_role: compatibility_only
```

This is the default upgrade for active old projects.

### Level 2: Active execution project

Add the following templates or references when a new Codex task is created:

```text
DRIVE_WRITE_FALLBACK_TO_CODEX_TEMPLATE.md
CODEX_CLAUDE_INTERACTIVE_FIRST_PASS_TEMPLATE.md
DRIVE_PARENT_FOLDER_VERIFICATION_CHECKLIST.md
```

### Level 3: Full project hygiene pass

Do only during a maintenance window or explicit collaboration-upgrade task.

Actions:

```text
- update all project Drive entry files
- clean candidate/stable residue
- normalize report paths
- deprecate active GitHub task pointers unless explicitly needed
- add old-project absorption report
```

## No-confusion Rule

A project must not show two active baselines.

Wrong:

```text
stable: PLAYBOOK_OPERATIONAL_BASELINE_V2
stable: DRIVE_NATIVE_V2_1_AS_STABLE_BASELINE
```

Correct:

```text
stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
```

## GitHub-backed Registry Rule

Repository-backed task pointers remain compatibility entries.

Use them only when:

```text
- the project has no usable Drive task surface, or
- a task must be anchored in GitHub for audit, PR, release, rollback, or external reviewer access, or
- the project explicitly declares GitHub-backed registry as active for that task.
```

They are not the default daily dispatch surface.

## Candidate/stable Residue Rule

A Drive or GitHub entry file may mention historical candidate work only under a clearly labeled section:

```text
Historical / archived candidate records
```

Current state fields must not say candidate after stable acceptance.

## Old-project Safe Upgrade Rule

For old projects already doing real work, do not interrupt business execution with a full documentation rewrite.

Default sequence:

```text
1. Add Level 1 patch lines.
2. Apply fallback rule on the next ChatGPT/Codex task.
3. Apply Claude routing rule only when engineering analysis is useful.
4. Defer full entry-file normalization to the next maintenance task.
```
