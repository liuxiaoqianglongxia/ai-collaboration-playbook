# Old Project Absorption Minimal

Old projects should not redo all V2 documents to adopt Task Hall.

## Minimal copy

Copy only the small `task-hall/` skeleton into the existing project Drive
workbench:

- `task-hall/README.md`
- `task-hall/00_BOARD.md`
- `task-hall/01_NOW.md`
- `task-hall/02_ACCEPTANCE_QUEUE.md`
- `task-hall/docs/active/fixed-docs.json`
- `task-hall/db/`
- `task-hall/tasks/YYYYMMDD/`
- `task-hall/reports/YYYYMMDD/`
- `task-hall/acceptance/YYYYMMDD/`
- `task-hall/agents/*/inbox/`
- `task-hall/agents/*/outbox/`
- `task-hall/indexes/`
- `task-hall/web/index.html`

## Add only these lines to the project control note

```text
Task Hall status: enabled
Task Hall mode: DOC_FIRST_FILE_NATIVE_MVP
Task Hall entry: task-hall/00_BOARD.md
```

## Do not do this

- Do not make old projects redo all Drive-native V2 docs.
- Do not restore GitHub daily task registry as the default dispatch surface.
- Do not pause business work longer than needed to add the skeleton.
- Do not modify production, database, secrets, release, rollback, or deployment flows during absorption.

## Later canary scope

- `shanxi-edu-hot`: placement cleanup only.
- `sub2api-maijian`: duplicate inventory plus placement cleanup only.

Those projects are not modified by this canary.
