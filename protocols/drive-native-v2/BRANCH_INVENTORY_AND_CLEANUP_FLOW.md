# Branch Inventory And Cleanup Flow

protocol_id: BRANCH_INVENTORY_AND_CLEANUP_FLOW
status: candidate

## Inventory Commands

```text
git fetch --all --prune
git branch -r --sort=-committerdate
git branch -r --merged origin/main
git branch -r --no-merged origin/main
gh pr list --state all
gh pr list --state open
```

## Delete Rule

Delete only branches listed in the inventory and proven merged or reachable from `origin/main`.

Never delete main, tags, protected branches, release/prod/hotfix branches, or unmerged branches.

## Post-check

```text
git fetch --all --prune
git branch -r --sort=-committerdate
gh pr list --state open
git status -sb
```
