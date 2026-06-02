# Task Hall V3 Standard

**Status**: RC1 candidate (branch `release/playbook-v3-task-hall-rc1`)
**Precedence**: V3 supersedes prior task-dispatch surfaces when accepted; until then, V2 is the stable baseline.

## 1. Scope

Task Hall V3 is the **file-native task/workbench layer** for the Drive-native collaboration model. It formalizes:

- Workbench skeleton: `<project>/task-hall/` with board, now, acceptance queue, and sub-directories.
- Task packages: `<project>/task-hall/tasks/YYYYMMDD/<TASK_ID>.md` with a strict field format and state machine.
- Reports: `<project>/task-hall/reports/YYYYMMDD/<TASK_ID>_REPORT.md`.
- Local state: JSON + JSONL + SQLite in `<project>/task-hall/db/`.
- CLI: `python3 -m taskhall` (in `lab/task-hall-mvp/`) for init, ingest, claim, start, submit-report, accept, archive, revive, build-board, build-context-pack, serve, **check**.

Task Hall does **not** replace Drive or GitHub; it sits between them as the daily task execution surface.

## 2. Authority Order

Decision authority:

1. User.
2. ChatGPT acceptance verdict.
3. Codex delivery lead and final integrator.
4. Claude Code engineering execution tool coordinated by Codex.

Document conflict order:

1. `reports/latest.md` - current status of the playbook itself.
2. `standards/TASK_HALL_V3.md` (this file) - canonical V3 standard.
3. `QUICK_START.md` - one-page daily entry.
4. `lab/task-hall-mvp/README.md` - CLI and workbench entry.
5. `reports/codex/latest.md` - latest Codex report pointer.

Older documents (V1, V1.1, V1.2, old GitHub registry, whitepapers, lab experiments) are **history/reference/lab**, not default execution entry points. See Section 6.

## 3. Drive / GitHub Conflict Rule

```text
Drive is the daily fact source.
GitHub is the stable result surface.
When in doubt, write to Drive first, sync to GitHub later.
```

- Daily tasks, reports, screenshots, raw materials, daily logs -> Drive workbench.
- Stable docs, version anchors, release notes, rollback notes, reusable templates -> GitHub main.
- The `tasks/codex/latest.md` GitHub-backed registry is **compatibility-only**, not the default daily dispatch surface.

## 4. Hard Boundaries

Task Hall V3 (and this playbook repository) must **not**:

- Edit `main` branch directly - all changes go through the V3 RC1 branch and explicit acceptance.
- Touch business projects or their production code.
- Deploy to production or manage production systems.
- Store or manage production DB credentials, secrets, or keys.
- Delete branches, tags, or repositories.
- Force push to any branch.
- Restore the GitHub daily dispatch registry as a default entry point.
- Run as a production service - it is a local/dev tool only.

## 5. GitHub Compatibility Registry Rule

The V1.1 GitHub-backed task registry (`tasks/codex/latest.md`, `tasks/claude/latest.md`) remains as a **compatibility layer** only:

- It is not the default daily task queue.
- It is not connected to automation.
- It does not change the four-person model (ChatGPT / Drive / GitHub / Codex).
- It does not replace Drive as the daily fact source.
- Use it only when a project explicitly declares it as an entry point.

## 6. History / Archive Strategy

```text
V1 / V1.1 / V1.2 - stable history baselines, kept for reference and rollback evidence.
whitepapers/      - research artifacts, not execution guides.
lab/              - experiments; do not use as defaults until promoted.
archive/          - migration records, error recoveries, historical evidence.
templates/        - old templates remain; new default is templates/task-hall-v3/.
```

No historical material overrides the current V3 standard, V2 stable baseline, or the bootstrap gate.

## 7. Claude Code Default Engineering Contract

When Claude Code is invoked via Codex on a Task Hall task:

- **Engineering by default** - Claude Code may read, search, edit files, update docs/specs/tests/Task Hall code, run tests, and produce patches on the assigned V3 or task branch.
- **Read-only only when requested** - restrict Claude Code to read-only mode only when the task explicitly says "read-only audit" or equivalent.
- **High-budget execution** - do not create fake blockers by setting tiny local Claude Code budgets for V3 release work.
- **Scope-bounded** - stay inside the assigned branch, project, and task objective. Do not touch business projects unless the user assigned that business project.
- **No secrets / no production** - never read, log, or transmit credentials; never deploy or operate production systems.
- **Codex final integration** - Claude Code can edit and suggest, but Codex reviews, accepts or rejects changes, runs final tests, commits, pushes, reports, and owns the PR.

## 8. Codex / Claude / ChatGPT Minimal Chain

```text
ChatGPT -> writes task package to Drive workbench
Codex   -> reads task, executes locally, writes report to Drive workbench
Claude  -> engineering execution, patch drafting, tests, or review coordinated by Codex
ChatGPT -> reads report from Drive acceptance queue, renders PASS/PARTIAL_PASS/FAIL/BLOCKED
Codex   -> on PASS, syncs stable results to GitHub
```

No step is skipped. ChatGPT does not execute code. Codex does not accept its own work. Claude Code does not own final integration, push, or PR decisions.

## 9. Bootstrap Gate

Before writing any task package, verify the target project's Drive workbench exists:

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

If missing, **do not** use Google Drive API to create. Return a plain-text bootstrap instruction for Codex to create via local Drive sync.

Reference: `standards/DRIVE_TASK_HALL_BOOTSTRAP_GATE_V1.md`

## 10. Automation and Check Entry

The `taskhall check` command validates a workbench or project root:

```bash
python3 -m taskhall check --path <directory> [--mode workbench|project]
```

Returns JSON with `result: "PASS" | "FAIL"` and a `missing` list of required paths.

Used by:
- Codex pre-execution checklists
- ChatGPT bootstrap gate verification
- CI/CD gates (when a project adopts Task Hall)

## 11. Task State Machine

```
DRAFT -> READY -> CLAIMED -> IN_PROGRESS -> NEEDS_ACCEPTANCE -> ACCEPTED
  |        |         |           |              |              |
ARCHIVED ARCHIVED  ARCHIVED   ARCHIVED     NEEDS_REVISION   ARCHIVED
                                          |
                                        READY (cycle)
```

Final states: ACCEPTED, ARCHIVED - no further mutations allowed.

## 12. Related Files

- Entry: `QUICK_START.md`
- CLI: `lab/task-hall-mvp/`
- Bootstrap gate: `standards/DRIVE_TASK_HALL_BOOTSTRAP_GATE_V1.md`
- Template: `templates/task-hall-v3/`
- Intake checklist: `checklists/V3_TASK_HALL_PROJECT_INTAKE_CHECKLIST.md`
