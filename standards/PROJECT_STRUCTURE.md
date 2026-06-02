# Project Structure Standard

> **Purpose**: Define the recommended directory structure for projects using the AI collaboration playbook.
> **Version**: 1.0
> **Maintained in**: `ai-collaboration-playbook/standards/PROJECT_STRUCTURE.md`

---

## Recommended Structure

For a project using the full four-piece collaboration pattern:

```
project-root/
├── AGENTS.md              # Multi-agent collaboration rules
├── CLAUDE.md              # Claude Code role definition (auto-read)
├── CHATGPT_START_HERE.md  # ChatGPT session entry point
├── CURRENT.md             # Current project state card
├── TASKS.md               # Task tracking list (compatibility/history; see V3 note below)
├── DECISIONS.md           # Architecture decision records (ADRs)
├── RUNBOOK.md             # Operations manual
├── README.md              # Project overview for humans
├── docs/                  # Additional documentation
├── reports/               # Execution and audit reports
│   ├── claude/            # Claude Code audit reports
│   ├── codex/             # Codex delivery reports
│   └── incident/          # Incident reports
├── orchestration/         # Task orchestration scripts
├── templates/             # Project-specific templates
├── checklists/            # Project-specific checklists
└── [source code dirs]     # Language-specific structure
```

## V3 Task Hall Workbench (Drive-native daily dispatch)

For projects using V3 Task Hall as their daily workbench, the task-hall skeleton lives in the Drive/local filesystem workbench, NOT as a subdirectory of this playbook repository. The old root-level `TASKS.md` style above is compatibility/history only — the default daily dispatch surface is the task-hall workbench.

Minimum Drive Task Hall workbench skeleton:

```
<project>/                        # e.g. G:/My Drive/<project>/ or local equivalent
├── 00_HOME.md                    # Project overview
├── 01_CURRENT.md                 # Current state card
├── 02_INDEX.md                   # Asset index
└── task-hall/                    # V3 Task Hall workbench root
    ├── 00_BOARD.md               # Kanban-style task board
    ├── 01_NOW.md                 # Current focus
    ├── 02_ACCEPTANCE_QUEUE.md    # Tasks awaiting review
    ├── docs/active/              # Fixed Google Docs registry
    ├── tasks/YYYYMMDD/           # Daily task packages
    ├── reports/YYYYMMDD/         # Daily execution reports
    ├── indexes/                  # Task and report indexes
    └── db/                       # SQLite canary state
```

Key rules:

- `task-hall/` lives in the project Drive workbench, not in the playbook repository.
- GitHub `tasks/codex/latest.md` and `tasks/claude/latest.md` are **compatibility/history only** — they are not the default daily dispatch surface when V3 Task Hall is enabled.
- The playbook repository (`ai-collaboration-playbook/`) ships the templates and CLI tool (`lab/task-hall-mvp/`); each project creates its own workbench instance via the bootstrap gate.

For a lightweight project (ChatGPT + Claude Code only):

```
project-root/
├── CLAUDE.md              # Claude Code role definition
├── CURRENT.md             # Current project state
├── TASKS.md               # Task list
├── README.md              # Project overview
└── [source code dirs]
```

## Directory Purposes

| Directory | Purpose | Examples |
|-----------|---------|----------|
| `docs/` | Extended documentation | Architecture diagrams, API docs, user guides |
| `reports/` | Audit and execution reports | Agent reports, acceptance checks |
| `reports/claude/` | Claude Code engineering/review findings | Engineering analysis, review, and implementation recommendation reports |
| `reports/codex/` | Codex delivery results | Integration reports, PR summaries |
| `reports/incident/` | Production incident reports | Root cause analysis, fix records |
| `orchestration/` | Task orchestration | Scripts that coordinate agent workflows |
| `templates/` | Project templates | Reusable structures for sub-projects |
| `checklists/` | Project checklists | Safety checks, acceptance criteria |

## Playbook vs Business Repository Boundary

| Asset Type | Playbook Repository | Business Repository |
|-----------|-------------------|-------------------|
| Generic collaboration templates | Yes (`templates/`) | Reference from playbook |
| Project-specific AGENTS.md | Template only | Customized version with real roles |
| Project-specific CLAUDE.md | Template only | Customized version with real paths |
| Execution reports | Template format only | Actual reports with real findings |
| Standards (TERMINOLOGY, PROJECT_STATE) | Yes (`standards/`) | Reference, do not copy |
| Business source code | No | Yes |
| Production configurations | No | Yes (in private repo) |
| Database files, .env, logs | No | No (gitignored) |

## Naming Conventions

- All files: lowercase with hyphens (`project-state.md`, not `ProjectState.md`)
- Directories: lowercase with hyphens (`reports/`, not `Reports/`)
- Dates in filenames: `YYYY-MM-DD-description.md`
- Templates: suffix with `_TEMPLATE.md` (e.g., `RUNBOOK_TEMPLATE.md`)
