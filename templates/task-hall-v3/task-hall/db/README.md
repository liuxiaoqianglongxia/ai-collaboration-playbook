# Database

Task Hall state files:

- `tasks_current.json` — current task registry
- `reports_current.json` — current report registry
- `events.jsonl` — event log (JSONL append-only)
- `taskhall.sqlite` — SQLite mirror of tasks, reports, and events

These files are managed by `python3 -m taskhall`. Do not edit manually.
