# WSL Asset Audit — 2026-05-30

三个 WSL 环境的资产审计总账: `wsl-hermes`, `wsl-codex`, `wsl-server`。

## 审计报告

| 文件 | 说明 |
|------|------|
| [wsl-hermes-audit.md](./wsl-hermes-audit.md) | wsl-hermes 完整审计 (19 repos, 86 skills, 17 standards) |
| [wsl-codex-audit.md](./wsl-codex-audit.md) | wsl-codex 完整审计 (17 repos, 8 worktrees, 40+ collaboration assets) |
| [wsl-server-readonly-boundary.md](./wsl-server-readonly-boundary.md) | wsl-server 只读边界说明 |
| [summary.md](./summary.md) | 审计汇总 — 总结论、三 WSL 定位、分流原则、下一阶段建议 |

## 审计范围

| WSL | 路径 | 状态 |
|-----|------|------|
| wsl-hermes | `/home/hermes/` | ✅ PASS — 只读盘点完成 |
| wsl-codex | `/home/codex/` | ✅ PASS — 只读盘点完成 |
| wsl-server | — | ⏸ 暂缓 — 仅建立只读边界 |

## 排除

- Windows 文件系统 (`/mnt/*`)
- node_modules, venv, dist, build
- 数据库、日志、缓存、备份内容 (仅登记路径, 不入仓)
