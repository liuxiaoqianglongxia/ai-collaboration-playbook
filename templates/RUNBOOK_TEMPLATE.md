# RUNBOOK Template — Operations Manual

> **Purpose**: Document how to start, stop, monitor, and troubleshoot services in this project.
> **Applies to**: Any deployed or locally running service.
> **Place at**: Project root as `RUNBOOK.md` or in `runbooks/` directory.

> **Template Authority**: This file is an upstream template from `ai-collaboration-playbook`. When copied into a project repository, remove the `_TEMPLATE` suffix and fill in service-specific details (ports, commands, health checks). The project-local copy becomes the execution authority for that project, while this template remains the upstream baseline.

## How to use

- Every service gets its own section.
- Include health check URLs, start/stop commands, and rollback procedures.
- Update this file whenever deployment changes.

---

## Environment

| Field | Value |
|-------|-------|
| **Environment** | [Local / WSL / Production / Staging] |
| **OS** | [Linux / WSL2 / macOS] |
| **Runtime** | [Python 3.x / Node 20.x / Docker / etc.] |
| **Deployment Directory** | [Path or Docker volume] |

## Services

### [Service Name]

| Field | Value |
|-------|-------|
| **Port** | [Port number] |
| **Protocol** | [HTTP / HTTPS / WebSocket] |
| **Health Check** | `curl http://localhost:[port]/health` |
| **Expected Response** | `{"status": "ok"}` or HTTP 200 |

#### Start

```bash
# Start command
[command]

# Or via systemd (if applicable)
systemctl --user start [service-name]
```

#### Stop

```bash
# Stop command
[command]

# Or via systemd
systemctl --user stop [service-name]
```

#### Restart

```bash
[command]
```

#### Logs

```bash
# Log location or command
[command to view logs]
```

## Backup

| What | Where | Frequency | How |
|------|-------|-----------|-----|
| [Database / Config / Data] | [Path or volume] | [Daily / Weekly / Before changes] | [Backup command] |

## Rollback

| Scenario | Steps |
|----------|-------|
| [Service fails after restart] | 1. [Step 1] 2. [Step 2] 3. [Step 3] |
| [Database migration fails] | 1. [Step 1] 2. [Step 2] 3. [Step 3] |
| [Health check fails] | 1. [Step 1] 2. [Step 2] 3. [Step 3] |

## Prohibited Actions

- [ ] Do NOT restart production services without backup
- [ ] Do NOT modify `.env` or token files directly
- [ ] Do NOT delete database files without export
- [ ] Do NOT force restart services while health checks are failing
- [ ] Do NOT skip rollback plan when making changes

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| [Service won't start] | [Port conflict / Missing config / Permission] | [Fix steps] |
| [Health check fails] | [Dependency down / Config error / Resource exhaustion] | [Fix steps] |
| [Slow response] | [Database lock / Memory pressure / Network] | [Fix steps] |
| [Disk full] | [Log growth / Database growth / Cache] | [Fix steps] |

## Change Log

| Date | Change | Changed By | Reason |
|------|--------|-----------|--------|
| YYYY-MM-DD | [What changed] | [Who] | [Why] |
