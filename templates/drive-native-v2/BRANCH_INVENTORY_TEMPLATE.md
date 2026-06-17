# Branch Inventory Template

inventory_id: <INVENTORY-ID>
repo: <owner/repo>
default_branch: <branch>
origin/main HEAD: <sha>

## Counts

- open PR count:
- closed merged PR count:
- remote branches total:
- remote branches merged into origin/main:
- remote branches not merged into origin/main:
- protected branches:

## Candidate Delete Branches

| branch | tip | proof | PR |
| --- | --- | --- | --- |

## Must Keep Branches

- main
- dev if present
- release/* if present
- prod/* if present
- hotfix/* if present
- protected branches

## Uncertain Branches

| branch | reason |
| --- | --- |
