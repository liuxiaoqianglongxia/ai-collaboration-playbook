# DECISIONS Template — Architecture Decision Records

> **Purpose**: Record why decisions were made, what alternatives were considered, and what the consequences are.
> **Applies to**: Any project where multiple agents or humans make architectural choices.
> **Place at**: Project root as `DECISIONS.md` or in `decisions/` directory.

## How to use

- Every significant decision gets one ADR entry.
- Write the decision at the time it's made — do not backfill from memory.
- Mark deprecated decisions when superseded by new ones.

---

## Decision Log

### ADR-[NNN]: [Short title]

| Field | Value |
|-------|-------|
| **Date** | YYYY-MM-DD |
| **Status** | Proposed / Accepted / Deprecated / Superseded |
| **Decided by** | [ChatGPT / Claude Code / Codex / Human] |
| **Superseded by** | ADR-[NNN] (if applicable) |

**Background**

> What problem or situation led to this decision?

**Options Considered**

| Option | Pros | Cons |
|--------|------|------|
| [Option A] | [Why] | [Why not] |
| [Option B] | [Why] | [Why not] |

**Decision**

> Which option was chosen and why?

**Consequences**

> What are the positive and negative outcomes of this decision?
> - (+) [Positive consequence]
> - (-) [Negative consequence or risk]

**Scope of Impact**

> Which files, modules, or systems are affected?

**Rollback**

> How can this decision be reversed if needed?

---

## Example

### ADR-001: Use SQLite for Project State Storage

| Field | Value |
|-------|-------|
| **Date** | 2026-04-15 |
| **Status** | Accepted |
| **Decided by** | ChatGPT |

**Background**: Project needs a lightweight local database for state tracking. PostgreSQL is overkill for single-instance deployment.

**Options Considered**:

| Option | Pros | Cons |
|--------|------|------|
| SQLite | Zero config, file-based, portable | No concurrent writes, limited scale |
| PostgreSQL | Production-grade, concurrent access | Heavy deployment, overkill |
| JSON files | Simple, no dependency | No queries, race conditions |

**Decision**: Use SQLite for local state. It's zero-configuration and sufficient for single-instance use. If concurrency needs grow, we'll add a write-ahead lock layer.

**Consequences**:
- (+) Simple deployment, no external database needed
- (+) Easy to backup (single file)
- (-) Cannot handle concurrent writes without locking
- (-) Will need migration if we scale to multi-instance

**Scope of Impact**: `state.db`, all database access modules.

**Rollback**: Export data to JSON, migrate to PostgreSQL schema. Estimated 1-2 days of work.
