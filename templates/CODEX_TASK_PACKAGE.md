# Codex 长任务包模板

> 用途：ChatGPT 在用户明确说“进入执行 / 可以安排 Codex / 给任务包”后，把本模板适配为项目内任务文件。不得只在聊天里派活。

## 任务名

`<short-kebab-task-name>`

## 用户短公告

```text
任务：<TASK-ID>
能实现：
- <one concrete outcome>
- <one concrete outcome>
- <one concrete outcome>
不做：<key boundary>
你发给 Codex：任务已写入 Drive：tasks/codex/YYYYMMDD/<task-name>.md；请读取该任务包执行，完成后写 Drive 报告。
详情：任务包已在 Drive。
```

## 背景

说明为什么要做这件事，当前项目状态来自哪些 Drive 日常事实和 GitHub 稳定事实。

必须写明：

- 已读取的事实源文件。
- 当前阶段。
- 本轮不解决的问题。

## 目标

用可验收的方式描述本轮目标。

示例：

- 修复某个明确 bug。
- 完成某个限定范围功能。
- 只读诊断某个问题。
- 建立某个协作底座。

## 范围

本轮允许操作的目录、文件、模块或环境。

```text
允许范围：
- <path-or-module>
- <path-or-module>

只读范围：
- <path-or-module>

禁止范围：
- <path-or-module>
```

## 执行通道

```text
当前 Codex 通道：ACTIVE_CODEX_TASK / NO_ACTIVE_CODEX_TASK
当前 Claude Code 通道：ACTIVE_CLAUDE_TASK / NO_ACTIVE_CLAUDE_TASK
本阶段规则：one active execution lane
新发现处理：记录为候选下一步，不在当前任务未关闭时启动第二个 active Codex task
```

如需 Claude Code，必须写明：

```text
Claude Code：允许 / 要求 / 禁止
用途：只读分析 / 局部草案 / diff 复审 / 不适用
最终集成者：Codex
```

## 禁止事项

默认必须包含：

- 不改密钥。
- 不改生产数据库。
- 不做未授权部署。
- 不 force push。
- 不跨项目写入。
- 不把实验室能力升级为稳定模块。
- 不修改本任务未授权的目录。
- 不创建第二条 active Codex execution lane。
- 不让 Claude Code 替代 Codex 做最终集成。

按项目需要补充更多禁止事项。

## 执行步骤

1. 先做只读核验：确认仓库、分支、当前状态、相关文件。
2. 输出执行计划或在报告中记录计划。
3. 在允许范围内修改文件。
4. 运行必要检查或测试。
5. 检查 diff，确认没有越界修改。
6. 写回执行报告。
7. 提供提交建议或实际提交信息。

## 验收标准

本轮必须可用 PASS / PARTIAL PASS / FAIL / BLOCKED 判断。

示例：

- 相关测试通过。
- 指定文件存在且内容符合要求。
- 未修改禁止范围。
- 报告写回 Drive；稳定成果同步时再写回 GitHub。
- 仍然保留回滚路径。

## 报告要求

Codex 报告必须包含：

- 结论：PASS / PARTIAL PASS / FAIL / BLOCKED。
- 实际修改文件列表。
- 实际执行命令或检查。
- 测试结果。
- diff 摘要。
- 禁止范围确认。
- 未完成项。
- 下一步建议。

## 停止条件

遇到以下情况必须停止：

- 目标仓库或分支不匹配。
- 发现任务描述与事实源冲突。
- 需要生产权限、密钥、数据库或部署授权。
- 测试失败且无法在范围内修复。
- 发现跨项目污染风险。

## 下一步预案

- 如果 PASS：建议进入验收或下一任务。
- 如果 PARTIAL PASS：列出剩余项并建议下一轮任务包。
- 如果 FAIL：说明失败原因和回滚建议。
- 如果 BLOCKED：说明需要用户提供什么信息或授权。
