# V3 Task Hall Project Intake Checklist

**Purpose**: Validate a new or existing project for Task Hall V3 readiness. Run before writing the first task package.

## A. New Project - Collaboration Base (Bootstrap Only)

- [ ] Project Drive workbench skeleton does NOT yet exist (if it does, skip to Section B).
- [ ] Codex has been instructed to create the workbench via local Drive sync (not Google Drive API).
- [ ] Minimum workbench structure verified after Codex creates it:

```text
<project-name>/
  00_HOME.md
  01_CURRENT.md
  02_INDEX.md
  task-hall/
    00_BOARD.md
    01_NOW.md
    02_ACCEPTANCE_QUEUE.md
    docs/active/
    tasks/
    reports/
    indexes/
    db/
```

- [ ] `taskhall check --path <project>/task-hall --mode workbench` returns PASS.
- [ ] No business code was modified during bootstrap.
- [ ] Project routing profile created or confirmed (who is ChatGPT, Codex, Claude Code for this project).
- [ ] Fixed Google Docs sockets registered in `docs/active/fixed-docs.json` (if project uses Google Docs).
- [ ] Drive local sync path confirmed (e.g., `G:/My Drive/<project>/`).

## B. Existing / Old Project - Migration Assessment

- [ ] Current collaboration surface identified: Drive workbench / GitHub registry / other.
- [ ] If using V1.1 GitHub task registry (`tasks/codex/latest.md`), note it as compatibility-only, not primary.
- [ ] If using old Drive templates, assess whether to migrate to `templates/task-hall-v3/`.
- [ ] Existing task state captured: active tasks, pending reports, acceptance items.
- [ ] Old materials classified:
  - [ ] V1/V1.1/V1.2 docs -> history/reference
  - [ ] Whitepapers -> research artifacts
  - [ ] Lab experiments -> not default until promoted
  - [ ] Archive -> evidence only, not active guidance
- [ ] If migrating, run `taskhall check` on current workbench (if any) and note failures.
- [ ] Decision made: adopt V3 task-hall structure, stay on current surface, or hybrid.

## C. Pre-Task Gate (Both New and Existing)

- [ ] `standards/TASK_HALL_V3.md` read and understood.
- [ ] `QUICK_START.md` read as daily entry point.
- [ ] Bootstrap gate checked (workbench exists or Codex instruction issued).
- [ ] Hard boundaries confirmed: no main edits, no business code, no production, no secrets, no force push, no branch/tag deletion, no GitHub registry restoration.
- [ ] ChatGPT acceptance criterion defined (PASS / PARTIAL_PASS / FAIL / BLOCKED).
- [ ] Codex execution environment ready (WSL/local, code access, test commands known).

## D. Post-Intake

- [ ] First task package written to `task-hall/tasks/YYYYMMDD/<TASK_ID>.md`.
- [ ] Task ingested via `taskhall ingest`.
- [ ] Board built via `taskhall build-board`.
- [ ] Codex notified to claim and execute.
