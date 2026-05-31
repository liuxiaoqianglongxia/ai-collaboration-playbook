# content-lab-safe-ingest-v1

## 0. Role

You are the main execution agent for safely ingesting low-risk maijian-wechat assets into `maijian-wechat-content-lab`.

This is the only package in this set that may write to `maijian-wechat-content-lab`.

## 1. Goal

Copy only low-risk A-class Markdown/script assets from `/home/hermes/projects/maijian-wechat` into `/home/hermes/projects/maijian-wechat-content-lab`, preserving source traceability and generating manifests and reports.

This package must not clean, delete, publish, call APIs, or modify the source repository.

## 2. Required environment

Run only in `wsl-hermes` as user `hermes`.

First command:

```bash
whoami
pwd
hostname
```

Stop with `BLOCKED` if `whoami` is not `hermes`.

## 3. Repositories

Source repo, read-only:

```text
/home/hermes/projects/maijian-wechat
```

Target repo, writable:

```text
/home/hermes/projects/maijian-wechat-content-lab
```

Fact source repo, read-only:

```text
/home/hermes/projects/ai-collaboration-playbook
```

Required fact-source branch/files:

```text
audit/maijian-wechat-250-asset-review-v1-20260530
  field-audits/maijian-wechat/2026-05-30/index.md
  field-audits/maijian-wechat/2026-05-30/raw-file-inventory.tsv

audit/maijian-wechat-content-routing-plan-v1-20260530
  field-audits/maijian-wechat/2026-05-30/content-routing-v1/index.md
  field-audits/maijian-wechat/2026-05-30/content-routing-v1/content-lab-routing-plan.md
  field-audits/maijian-wechat/2026-05-30/content-routing-v1/article-dedup-matrix.md
  field-audits/maijian-wechat/2026-05-30/content-routing-v1/publishing-assets-routing-plan.md
  field-audits/maijian-wechat/2026-05-30/content-routing-v1/visual-prompt-routing-plan.md
  field-audits/maijian-wechat/2026-05-30/content-routing-v1/redaction-policy.md
  field-audits/maijian-wechat/2026-05-30/content-routing-v1/routing-manifest.tsv
```

## 4. Strict prohibitions

Do not:

- modify `/home/hermes/projects/maijian-wechat`
- modify `/home/hermes/projects/maijian-wechat-private-repo`
- read `.env`, `auth.json`, token, secret, database, log, browser profile, or backup contents
- copy JSON/JSONL/HTML/images/backups/canary outputs
- copy files containing real `media_id`, `draft_media_id`, `thumb_media_id`, app secrets, access tokens, or API keys
- publish to WeChat
- call WeChat/Feishu/image APIs
- delete or clean source files
- operate `wsl-server`
- force push

## 5. Allowed asset classes

Only copy low-risk A-class assets:

### A. Production and workflow docs

Allowed examples from audit reports:

```text
PRODUCTION_CONSTITUTION.md
HANDOFF_CONTRACT.md
WECHAT_LAYOUT_STANDARD.md
VALIDATED_WORKFLOW_V1.md
MANUAL_PUBLISH_V3_PLAN.md
PUBLISHING_CALENDAR.md
DRACO_ORIGINAL_STYLE_RECOVERY.md
PUBLISH_CONFIRMATION_CARD.md
```

Suggested target directories:

```text
production/
publishing/sop/
style-guides/
```

### B. Preflight and publishing scripts

Allowed patterns only after scan:

```text
scripts/preflight_*.py
scripts/validate_*.py
scripts/run_*_tests.sh
scripts/build_wechat_copy_workbench.py
```

Before copying each script, scan it for sensitive markers:

```bash
grep -nE "APPID|APP_SECRET|SECRET|TOKEN|ACCESS_TOKEN|media_id|draft_media_id|thumb_media_id|password|api_key" <file> || true
```

If a real value appears, skip. If only placeholder/prohibition text appears, copy and record as safe textual reference.

Suggested target directories:

```text
publishing/preflight/
publishing/scripts/
```

### C. Final articles only

Only copy Markdown articles explicitly identified as final, official, published, or final public pack in the audit outputs.

Do not copy:

```text
rewrite candidates
v1/v2/v3 drafts
GPT54 drafts
GPT-squeeze variants
.md.new
.bak
0-byte files
placeholder articles
unfinished drafts
```

Suggested target directories:

```text
articles/hermes-genesis-season1/final/
articles/season1/
articles/agent-truth/
articles/hermes-v7-principles/
```

### D. Cover prompt and style documentation

Only copy Markdown/TXT prompt/style docs.

Do not copy images, screenshots, generated covers, or HTML previews.

Suggested target directories:

```text
visuals/prompts/
style-guides/
```

## 6. Target branch

In target repo:

```bash
cd /home/hermes/projects/maijian-wechat-content-lab
git fetch origin
git checkout main
git pull --ff-only origin main
git checkout -b feature/content-lab-safe-ingest-v1-20260530
```

If branch exists, inspect state. If not clean, stop with `BLOCKED`.

## 7. Required outputs in target repo

Reports/manifests:

```text
reports/ingest/content-lab-safe-ingest-v1.md
reports/ingest/content-lab-safe-ingest-v1-repo-check.md
reports/ingest/article-ingest-report.md
reports/ingest/publishing-ingest-report.md
reports/ingest/visual-prompt-ingest-report.md
reports/ingest/safety-scan-report.md
manifests/content-lab-safe-ingest-v1-candidates.tsv
manifests/content-lab-safe-ingest-v1-copied.tsv
manifests/content-lab-safe-ingest-v1-skipped.tsv
manifests/content-lab-safe-ingest-v1-conflicts.tsv
```

Manifests must include source path, target path, copied/skipped status, reason, safety scan result, and human review requirement.

## 8. No overwrite rule

If target exists:

1. do not overwrite;
2. compare name and size;
3. if different, add to conflicts manifest;
4. skip copy unless target path is clearly empty and safe.

## 9. Final safety scan

Before commit:

```bash
git status --short
find . -type f \( -name "*.json" -o -name "*.jsonl" -o -name "*.html" -o -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.webp" -o -name "*.zip" -o -name "*.tar.gz" -o -name "*.db" -o -name "*.sqlite" -o -name ".env" -o -name "auth.json" \)
grep -RInE "draft_media_id|thumb_media_id|media_id|access_token|appsecret|APP_SECRET|SECRET=|TOKEN=|api_key" . || true
```

If forbidden files are newly added or real secrets/IDs are detected, stop with `BLOCKED` and do not commit.

## 10. Commit and push

Only commit to `maijian-wechat-content-lab`.

Commit message:

```text
feat: ingest safe maijian wechat content assets v1
```

Push branch:

```text
origin/feature/content-lab-safe-ingest-v1-20260530
```

Create PR if possible:

```text
feat: ingest safe maijian wechat content assets v1
```

PR body must state:

- only low-risk A-class assets copied
- no JSON/HTML/images/backups/canary copied
- no real publish IDs copied
- source repo untouched
- safety scan passed

## 11. PASS criteria

PASS requires:

1. target branch created;
2. source repo untouched;
3. no forbidden file types copied;
4. scripts scanned;
5. manifests and reports generated;
6. safety scan passes;
7. commit and push succeed;
8. PR link or manual PR link provided.

## 12. Final report format

```markdown
# content-lab-safe-ingest-v1 Execution Report

1. Status: PASS / PARTIAL PASS / BLOCKED
2. Source repo:
3. Target repo:
4. Branch:
5. Commit hash:
6. Push status:
7. PR link:
8. Copied file count:
9. Skipped file count:
10. Conflict count:
11. Needs-review count:
12. Generated report/manifest files:
13. Safety scan result:
14. git status -sb:
15. git diff --cached --name-only:
16. Safety confirmation:
17. Next recommendation:
```
