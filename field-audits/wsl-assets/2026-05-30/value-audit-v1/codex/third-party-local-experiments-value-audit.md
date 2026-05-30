# C-F: SillyTavern / bendi / 第三方实验资产价值审计

## 1. 审计范围

- 项目: SillyTavern 系列、bendi-llm-gateway、feishu_docs_tool、codex-smoke-test 及其他第三方/实验资产
- 本地路径: /home/codex/projects/SillyTavern, sillytavern-lab, sillytavern-lab-source-test, sillytavern-runtime-patched, sillytavern-runtime-patched.pre-l2-*, bendi-llm-gateway, feishu_docs_tool, codex-smoke-test
- 仅登记，不读取代码内容
- 未读取: node_modules, dist, build, .env, db

## 2. 资产清单

| 资产 | 路径 | 大小 | 类型 | 说明 |
|------|------|------|------|------|
| SillyTavern | /home/codex/projects/SillyTavern | 435M | 第三方源码 | 非 git，完整 SillyTavern 副本 |
| sillytavern-lab | /home/codex/projects/sillytavern-lab | 519M | 实验环境 | 含 SillyTavern 子目录 |
| sillytavern-lab-source-test | /home/codex/projects/sillytavern-lab-source-test | 145M | 源码测试 | 含 ST-release.tar.gz |
| sillytavern-runtime-patched | /home/codex/projects/sillytavern-runtime-patched | 74M | git 仓库 | dream-soul/runtime-patched-local 分支，本地 origin |
| sillytavern-runtime-patched.pre-l2-20260517145531 | /home/codex/projects/sillytavern-runtime-patched.pre-l2-20260517145531 | 385M | 备份副本 | 时间戳命名的旧版本 |
| bendi-llm-gateway | /home/codex/projects/bendi-llm-gateway | ~10M | git 仓库 | main 分支，无 origin，服务器 /opt 镜像 |
| feishu_docs_tool | /home/codex/projects/feishu_docs_tool | ~24K | Python 脚本 | feishu_docs.py 单文件 |
| codex-smoke-test | /home/codex/projects/codex-smoke-test | 0 | git 仓库 | master 分支，空仓库，无 origin |
| home | /home/codex/projects/home | 未知 | 不明 | 内容不明 |

## 3. 资产评分表

| 资产 | 路径 | 建议归属 | 复用价值 | 完整度 | 整合难度 | 风险分 | 业务相关度 | 总分 | 分类 | 处理建议 |
|------|------|---------|---------|--------|----------|--------|-----------|------|------|----------|
| sillytavern-runtime-patched | sillytavern-runtime-patched/ | 仅本地 | 4 | 3 | 4 | 4 | 4 | 19 | **B** | 唯一有 git 历史的 patched 版，建议保留 |
| bendi-llm-gateway | bendi-llm-gateway/ | sub2api-maijian/仅本地 | 3 | 3 | 4 | 4 | 3 | 17 | **B** | 服务器镜像，无远程，值得远程化 |
| feishu_docs_tool | feishu_docs_tool/feishu_docs.py | 仅本地 | 2 | 2 | 5 | 5 | 2 | 16 | **B** | 单文件工具，复用价值低但无风险 |
| SillyTavern (完整副本) | SillyTavern/ | X | 1 | 5 | 5 | 3 | 2 | 16 | **X** | 第三方源码，不入仓 |
| sillytavern-lab | sillytavern-lab/ | X | 1 | 3 | 5 | 3 | 2 | 14 | **X** | 实验环境 + 第三方源码，不入仓 |
| sillytavern-lab-source-test | sillytavern-lab-source-test/ | X | 1 | 2 | 5 | 3 | 2 | 13 | **X** | 含 ST-release.tar.gz，不入仓 |
| sillytavern-runtime-patched.pre-l2-* | ...pre-l2-*/ | X | 1 | 3 | 5 | 3 | 2 | 14 | **X** | 旧版本备份，不入仓 |
| codex-smoke-test | codex-smoke-test/ | X | 1 | 1 | 5 | 5 | 1 | 13 | **X** | 空仓库，无价值 |
| home | projects/home/ | 不确定 | 0 | 0 | 5 | 5 | 0 | 10 | **D** | 内容不明，需人工确认 |

## 4. A 类资产

无。第三方实验资产中没有达到 A 级 (20-25分) 的资产。

## 5. B 类资产

1. **sillytavern-runtime-patched** — 唯一有 git 历史的 patched 版 (19分) — 保留，建议作为 DreamSoul runtime 的实验基础
2. **bendi-llm-gateway** — 服务器 /opt 镜像，无远程 (17分) — 建议后续远程化为私有仓库
3. **feishu_docs_tool** — 单文件飞书工具 (16分) — 低价值但无风险，保留

## 6. C/D 类资产

| 资产 | 总分 | 说明 |
|------|------|------|
| home | 10 | 内容不明，需人工确认后再决定是否清理 |

## 7. X 类禁止入仓资产

| 资产 | 路径 | 总大小 | 原因 |
|------|------|--------|------|
| SillyTavern 完整源码 | SillyTavern/ | 435M | 第三方源码，许可证不明 |
| sillytavern-lab | sillytavern-lab/ | 519M | 实验环境 + 第三方源码 |
| sillytavern-lab-source-test | sillytavern-lab-source-test/ | 145M | 含 ST-release.tar.gz 压缩包 |
| sillytavern-runtime-patched.pre-l2-* | 时间戳副本/ | 385M | 旧版本备份 |
| **SillyTavern 总计** | — | **~1.5GB** | **不入仓，不提交，不清理** |

## 8. 分流建议

| 目标 | 资产 |
|------|------|
| **ai-collaboration-playbook** | 无 |
| **sub2api-maijian** | 无 (SillyTavern 是第三方项目，不归入) |
| **仅本地保留** | sillytavern-runtime-patched, bendi-llm-gateway, feishu_docs_tool |
| **仅登记，不入仓** | 全部 SillyTavern 系列 (~1.5GB) |

## 9. 需要总控裁决的问题

1. **bendi-llm-gateway 远程化** — 是否应创建私有 GitHub 仓库并推送，还是保持本地服务器镜像
2. **SillyTavern 保留策略** — 1.5GB 第三方源码 + patch 占用大量磁盘，是否可缩减为仅保留 sillytavern-runtime-patched (74M)
3. **codex-smoke-test 空仓库** — 是否应删除或转为有意义的测试项目
4. **home 目录内容** — 需要人工确认内容后再决定去留

## 10. 下一步建议

1. P1: 确认 bendi-llm-gateway 是否值得远程化 (是生产网关还是实验原型)
2. P2: SillyTavern 保留策略 — 建议仅保留 sillytavern-runtime-patched，清理其余 1.4GB
3. P2: codex-smoke-test 空仓库清理
4. P2: home 目录人工确认
