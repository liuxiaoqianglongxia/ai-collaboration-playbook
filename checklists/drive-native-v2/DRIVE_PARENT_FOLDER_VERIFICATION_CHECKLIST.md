# Drive Parent-folder Verification Checklist

checklist_id: DRIVE_PARENT_FOLDER_VERIFICATION_CHECKLIST
base_stable: PLAYBOOK_OPERATIONAL_BASELINE_V2 / PASS
patch: DRIVE_NATIVE_V2_1_ABSORPTION_PATCH_CANDIDATE
status: candidate

Use this checklist after any ChatGPT, Codex, or manual Drive file creation/update that is intended to become a project fact.

## Required Checks

- [ ] File name matches intended task/report/material name.
- [ ] Parent folder is the intended project Drive workbench folder or subfolder.
- [ ] File is not only in Drive root.
- [ ] File is not only in an unknown or personal scratch folder.
- [ ] File has a stable relative project path.
- [ ] If local sync was used, the local path corresponds to the intended Drive folder.
- [ ] Root-level duplicate search performed when a prior failed write is suspected.
- [ ] Duplicate cleanup recommendation recorded if needed.
- [ ] Public GitHub docs do not depend on private local Drive paths as the only access route.

## PASS

All required checks pass.

## PARTIAL PASS

The file exists and is usable, but duplicate cleanup or path normalization remains.

## FAIL

The file is in the wrong folder or cannot be found.

## BLOCKED

The tool cannot inspect the parent folder and no Codex/local sync fallback is available.
