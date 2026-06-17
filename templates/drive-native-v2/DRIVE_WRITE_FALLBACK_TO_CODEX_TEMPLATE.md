# Drive Write Fallback To Codex Template

task_id: <TASK-ID>
mode: DRIVE_NATIVE_V2
patch_level: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
owner: Codex
created_by: ChatGPT controller

## Why This Task Exists

ChatGPT could not reliably write to the intended project Drive workbench, or could not verify the parent folder after creating/updating a Drive file.

Codex must use the local Google Drive sync directory to create or update the intended Markdown file and then report evidence.

## Target Project

```text
project: <PROJECT-NAME>
repo: <OWNER/REPO>
drive_workbench_relative_path: <Google Drive/project-folder>
target_file_relative_path: <path inside project Drive workbench>
```

## Required Action

1. Locate the local Google Drive sync directory for the project.
2. Verify the project workbench root.
3. Create or update the target file.
4. Verify the file exists in the intended parent folder.
5. Check whether a root-level or unknown-location duplicate exists.
6. Write a named Codex report in the project Drive workbench.

## Allowed Scope

```text
Drive project workbench files only:
<allowed paths>

GitHub files only if stable sync is explicitly required:
<allowed GitHub paths or none>
```

## Forbidden Scope

```text
production
Databases
Secrets
Unrelated repositories
Force push
Tag deletion
Main rewrite
Business-code edits unless explicitly listed
```

## Required Report Fields

```text
Conclusion: PASS / PARTIAL PASS / FAIL / BLOCKED
project:
task_id:
drive_workbench_relative_path:
local_sync_path_used: <private report only; do not copy into public GitHub docs>
target_file_created_or_updated:
parent_folder_verified: yes/no
root_level_duplicate_found: yes/no
duplicate_cleanup_needed: yes/no
files_changed:
checks_run:
forbidden_scope_touched: yes/no
next_action:
```

## Acceptance

ChatGPT accepts only when:

```text
- parent_folder_verified: yes
- target file path is inside project Drive workbench
- root duplicate status is known
- forbidden scope was not touched
- report is written and findable
```
