# C-D: sub2api worktree 价值审计

## 1. 审计范围

- 项目: sub2api 主仓库的 8 个 git worktree
- 共享 .git: `/home/codex/projects/sub2api/.git`
- 读取文件: 各 worktree 目录结构、DECISIONS.md、AGENTS.md、REPORTS/ 等顶层文档
- 未读取: 代码 diff、.env、db、node_modules

## 2. worktree 清单

| Worktree 名 | 路径 | 分支 | 大小 | 未提交 | 最后活跃 | 初步判断 |
|-------------|------|------|------|--------|----------|----------|
| sub2api-delivery-clean | /home/codex/projects/sub2api-delivery-clean | (worktree branch) | 42M | 0 | 2026-05-28 | **可能活跃** — 完整协作文档集 |
| sub2api-pr1-docs-ops | /home/codex/projects/sub2api-pr1-docs-ops | (worktree branch) | 34M | 0 | 2026-05-29 | **可能活跃** — 最近的 worktree，完整 docs+reports |
| sub2api-pr1-docs-ops-v2 | /home/codex/projects/sub2api-pr1-docs-ops-v2 | (worktree branch) | 256K | 0 | 2026-05-29 | **可能活跃** — v2 迭代，刚创建 |
| sub2api-pr2-upstream-integration | /home/codex/projects/sub2api-pr2-upstream-integration | (worktree branch) | 151M | 0 | 2026-05-22 | **需确认** — 上游集成 PR2 |
| sub2api-local-dev | /home/codex/projects/sub2api-local-dev | (worktree branch) | 无 | 0 | 2026-05-23 | **需确认** — 本地开发环境 |
| sub2api-upstream-v129-sync | /home/codex/projects/sub2api-upstream-v129-sync | (worktree branch) | 149M | 0 | 2026-05-22 | **可能过期** — upstream v1.29 同步 |
| sub2api-qwen-fix | /home/codex/projects/sub2api-qwen-fix | (worktree branch) | 196K | 0 | 2026-05-14 | **可能过期** — Qwen 修复，早期实验 |
| sub2api-qwen-thinking | /home/codex/projects/sub2api-qwen-thinking | (worktree branch) | 196K | 0 | 2026-05-15 | **可能过期** — Qwen thinking 实验 |

## 3. 资产评分表

| 资产 | 路径 | 建议归属 | 复用价值 | 完整度 | 整合难度 | 风险分 | 业务相关度 | 总分 | 分类 | 处理建议 |
|------|------|---------|---------|--------|----------|--------|-----------|------|------|----------|
| sub2api-pr1-docs-ops | sub2api-pr1-docs-ops/ | sub2api-maijian | 4 | 5 | 5 | 5 | 5 | 24 | **A** | 最新 docs-ops worktree，完整协作集 |
| sub2api-delivery-clean | sub2api-delivery-clean/ | sub2api-maijian | 4 | 5 | 5 | 5 | 5 | 24 | **A** | 交付清理版，完整 AGENTS/CLAUDE/RUNBOOK |
| sub2api-pr1-docs-ops-v2 | sub2api-pr1-docs-ops-v2/ | sub2api-maijian | 3 | 3 | 5 | 5 | 5 | 21 | **A** | v2 迭代，刚创建，等待开发 |
| sub2api-pr2-upstream-integration | sub2api-pr2-upstream-integration/ | sub2api-maijian | 3 | 3 | 4 | 5 | 4 | 19 | **B** | 上游集成，可能有价值但需确认 |
| sub2api-local-dev | sub2api-local-dev/ | sub2api-maijian | 2 | 2 | 4 | 5 | 4 | 17 | **B** | 本地开发 worktree，通用价值低 |
| sub2api-upstream-v129-sync | sub2api-upstream-v129-sync/ | sub2api-maijian | 2 | 2 | 3 | 4 | 3 | 14 | **C** | v1.29 同步，可能已被上游替代 |
| sub2api-qwen-fix | sub2api-qwen-fix/ | — | 1 | 1 | 3 | 4 | 2 | 11 | **D** | Qwen 早期修复，5月中旬，可能已合并 |
| sub2api-qwen-thinking | sub2api-qwen-thinking/ | — | 1 | 1 | 3 | 4 | 2 | 11 | **D** | Qwen thinking 实验，5月中旬，可能已过期 |

## 4. A 类资产

1. **sub2api-pr1-docs-ops** — 最新 docs-ops worktree (24分)
2. **sub2api-delivery-clean** — 交付清理版 (24分)
3. **sub2api-pr1-docs-ops-v2** — v2 迭代 (21分)

## 5. B 类资产

1. **sub2api-pr2-upstream-integration** — 上游集成 (19分)
2. **sub2api-local-dev** — 本地开发 (17分)

## 6. C/D 类资产

1. **sub2api-upstream-v129-sync** — v1.29 同步 (14分)
2. **sub2api-qwen-fix** — Qwen 早期修复 (11分)
3. **sub2api-qwen-thinking** — Qwen thinking 实验 (11分)

## 7. X 类禁止入仓资产

Worktree 本身不产生敏感文件，但需注意：
- 各 worktree 可能共享主仓库的 .git/objects，不应单独处理
- 各 worktree 目录下的 .env / db 文件同样适用主仓库的敏感规则

## 8. 分流建议

| 目标 | 资产 |
|------|------|
| **sub2api-maijian** | 所有 worktree 分支应合并或关闭后回归主仓库 |
| **playbook** | delivery-clean 和 pr1-docs-ops 中的协作文档模式可提炼 |
| **待裁决** | qwen-fix, qwen-thinking, upstream-v129-sync — 需确认是否已合并到 upstream |

## 9. 需要总控裁决的问题

1. **qwen-fix 和 qwen-thinking 是否已合并到 upstream** — 如果是，可以安全 prune
2. **upstream-v129-sync 是否已被后续版本替代** — 检查 upstream 当前版本
3. **local-dev worktree 是否有活跃开发** — 如有，保留；如无，可 prune
4. **pr1-docs-ops 和 pr1-docs-ops-v2 的关系** — v2 是否是 v1 的迭代？如果是，v1 是否可以关闭
5. **pr2-upstream-integration 的 PR 状态** — 是否已 merge 到 upstream

## 10. 下一步建议

1. P0: `git worktree list` 确认各 worktree 分支对应的 PR/issue 状态
2. P0: 检查 upstream (Wei-Shaw/sub2api) 当前版本，判断 v129-sync 是否过期
3. P1: 对于已合并的 worktree，执行 `git worktree prune` 清理
4. P1: 保留 pr1-docs-ops, pr1-docs-ops-v2, delivery-clean 三个活跃 worktree
5. P2: 考虑是否需要这么多 worktree — 是否可以用分支切换代替
