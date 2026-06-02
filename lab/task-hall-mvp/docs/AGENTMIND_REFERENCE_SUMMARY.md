# AgentMind Reference Summary

## Source

- Repository: https://github.com/wangdingding2026/agentmind2026
- Default branch observed: `v0.1-stabilization`
- Observation mode: read-only reference through GitHub metadata and README.

## Useful ideas for Task Hall MVP

AgentMind is positioned as a heterogeneous agent command center with unified
entry, routing, shared memory, audit, task panel, health checks, and DAG
orchestration. The Task Hall canary borrows only the small parts that fit
Drive-native V2:

- a local task panel concept, implemented here as `00_BOARD.md` and `web/index.html`
- an event timeline, implemented as `db/events.jsonl` and SQLite `events`
- an agent registry shape, implemented as per-agent inbox/outbox directories and Hermes heartbeat stub
- an audit trail, implemented as append-only events
- a context pack, implemented as lightweight manifest and report/decision indexes
- optional SQLite, implemented as `db/taskhall.sqlite`

## Rejected for this canary

- no AgentMind dependency
- no replacement of Drive-native V2
- no automatic unknown CLI scanning
- no multi-user server
- no memory system replacing Drive/GitHub fact sources
- no production deploy, release, rollback, secret, or database workflow

## Resulting design decision

Keep Task Hall as a file-native Drive workbench module. Use AgentMind only as
reference for observability and routing vocabulary, not as a required runtime.
