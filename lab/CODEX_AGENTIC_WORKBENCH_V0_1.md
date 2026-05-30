# Codex Agentic Workbench Lab V0.1

## 一、定位

V4 继续保持 ChatGPT / GitHub / Codex / Claude Code 四件套稳定主链路。

本仓库新增 `lab/` 实验室，用于探索 Codex 更强的 agentic 工作台能力，但实验室内容默认不进入稳定主链路。

原先讨论中的 “Codex-Hermes Fusion” 统一改名为 **Codex Agentic Workbench Lab**。

## 二、命名原因

不再使用 Fusion，是为了避免误解为要把 Hermes 原样搬进 Codex。

更准确的方向是：

- 保留 V4 的稳定项目协作主链路。
- 在 lab 中只读验证 Codex 的自动化、技能、子代理、记忆蒸馏、MCP 文档上下文等能力。
- 证明有效后，再把可复用部分升级成稳定模块。

## 三、第一批只读实验

```text
lab/experiments/001-heartbeat-readonly.md
lab/experiments/002-skill-start-here-audit.md
lab/experiments/003-subagent-readonly-scout.md
lab/experiments/004-memory-distillation.md
lab/experiments/005-mcp-docs-context.md
```

这些实验全部默认只读，不写生产自动化，不改业务项目代码，不做部署。

## 四、升级原则

实验要升级为稳定模块，必须满足：

1. 在只读范围内证明有价值。
2. 有明确输入、输出、禁止事项和验收标准。
3. 不破坏 V4 主链路。
4. 不要求用户反复复制粘贴小任务。
5. 不把某个工具的局部能力包装成默认协作制度。

## 五、当前禁止事项

- 不做业务开发。
- 不做 Claude Code 能力测试。
- 不写生产自动化。
- 不做自动部署。
- 不把 lab 实验直接升级成稳定模块。
- 不改任何业务项目仓库。

实验室的使命是探索，不是替代 V4。
