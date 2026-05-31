# maijian-wechat Task Packages

This directory contains task packages for the maijian-wechat asset recovery and content-lab consolidation line.

## Current phase

The WSL asset audit and content routing plan have already been completed. The next phases should proceed conservatively:

1. `content-lab-safe-ingest-v1.md` — main execution package for safely copying low-risk A-class assets into `maijian-wechat-content-lab`.
2. `content-lab-safe-ingest-review-v1.md` — independent read-only review of the ingest branch.
3. `content-lab-security-scan-v1.md` — independent security scan of the ingest branch.
4. `article-dedup-v1.md` — article deduplication planning only; no deletion and no migration.
5. `publish-record-redaction-v1.md` — publish ID redaction policy and examples only; no real IDs.
6. `content-lab-closeout-v1.md` — closeout after ingest + review + security scan.

## Parallel execution

Allowed parallel layout:

```text
Claude A -> content-lab-safe-ingest-v1.md
Claude B -> content-lab-safe-ingest-review-v1.md, after Claude A pushes branch
Claude C -> content-lab-security-scan-v1.md, after Claude A pushes branch
Claude D -> article-dedup-v1.md or publish-record-redaction-v1.md, read-only planning branch
```

Do not run two write agents against the same `maijian-wechat-content-lab` branch.

## Critical boundaries

- Do not modify `/home/hermes/projects/maijian-wechat`.
- Do not modify `/home/hermes/projects/maijian-wechat-private-repo`.
- Do not copy JSON/JSONL/HTML/images/backups/canary outputs.
- Do not read or output real `media_id`, `draft_media_id`, `thumb_media_id`, app secrets, tokens, or database contents.
- Do not operate `wsl-server`.
