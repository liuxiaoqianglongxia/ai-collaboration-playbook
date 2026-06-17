# Old Project V2 Absorption Guide

baseline: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
status: candidate

## Purpose

Upgrade projects already using Drive-native V2 without creating a second collaboration mode or interrupting active work.

## Rule

Do not tell old projects to migrate from V2 to a new baseline.

Tell them:

```text
Keep V2. Absorb the V2.1 patch-level rules.
```

## Minimal Flow

### Step 1: Read current project facts

Read:

```text
Drive workbench:
00_HOME.md
01_CURRENT.md
02_INDEX.md
03_ROUTING.md
04_DECISIONS_LATEST.md
05_RELEASE_POLICY.md
reports/latest or latest Codex report

GitHub stable facts:
README.md
CHATGPT_START_HERE.md
AGENTS.md
CLAUDE.md
CURRENT.md
TASKS.md
DECISIONS.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

If some files are absent, do not fail immediately. Record the missing files and choose Level 1 absorption unless the missing file blocks task routing.

### Step 2: Add Level 1 patch lines

In project Drive `00_HOME.md` or `01_CURRENT.md`, add:

```text
baseline: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
chatgpt_drive_write_rule: verify_parent_folder_or_fallback_to_codex
codex_drive_fallback: local_google_drive_sync_directory
claude_code_route: interactive_first_pass_under_codex_when_useful
registry_role: compatibility_only
```

Do not rewrite all project docs unless explicitly in scope.

### Step 3: Use the new fallback rule on the next task

When ChatGPT cannot reliably write the intended Drive file:

```text
- create a short Codex task
- instruct Codex to write through the local Google Drive sync directory
- require Codex to verify parent folder and report path
```

### Step 4: Use Claude Code only when it saves Codex work

Use Claude Code first-pass for high-token analysis and local reasoning.

Do not use Claude Code for:

```text
- final integration
- PR ownership
- release decisions
- tag operations
- production, database, or secret work
```

### Step 5: Report absorption result

Use:

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
baseline: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
files changed:
files intentionally not changed:
risks:
next action:
```

## PASS Criteria

```text
- Project still has one stable baseline: V2.
- Patch-level is visible in Drive current state.
- ChatGPT Drive write boundary is recorded.
- Codex fallback is available.
- Claude Code route is defined but not forced.
- GitHub registry is not restored as default daily dispatch.
- No business code, deployment, database, secrets, tags, or force push touched.
```

## PARTIAL PASS Criteria

Use `PARTIAL PASS` when:

```text
- patch lines are added but some old files still say candidate
- Drive workbench exists but parent-folder verification still needs real-task testing
- Claude route is documented but not yet tested
- project has old GitHub registry pointers that are inactive but not fully annotated
```

## BLOCKED Criteria

Use `BLOCKED` when:

```text
- no Drive workbench can be found
- no GitHub stable facts can be found
- current project state depends on chat history only
- applying the patch requires touching production, DB, secrets, or unrelated repo files
```
