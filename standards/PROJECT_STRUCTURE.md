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
├── TASKS.md               # Task tracking list
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
| `reports/claude/` | Claude Code audit findings | Read-only analysis results |
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
