# Experiment 001｜Heartbeat Readonly

状态：实验设计  
类型：只读巡检  
是否进入稳定主链路：否

---

## 1. 目标

验证 Codex / automation 能否承担项目状态心跳巡检。

心跳不是自动修复。

心跳第一阶段只做：

```text
读取状态
发现冲突
输出报告
建议下一步
```

---

## 2. 输入

```text
CHATGPT_START_HERE.md
CURRENT.md
TASKS.md
reports/latest.md
reports/codex/latest.md
reports/claude/latest.md
```

如涉及部署，再读：

```text
DEPLOYMENT.md
PORTS.md
RUNBOOK.md
reports/deploy/latest.md
```

---

## 3. 只读范围

允许：

```text
读取项目状态文件
读取最近报告
读取任务列表
读取 PR / issue 状态摘要
生成心跳报告
```

禁止：

```text
修改业务代码
修改任务状态
自动提交
自动创建 PR
自动部署
改 .env
改数据库
重启服务
```

---

## 4. 检查项

心跳巡检应检查：

```text
CURRENT.md 与 TASKS.md 是否冲突
reports/latest.md 是否过期
reports/codex/latest.md 是否缺失
任务是否长时间未收口
是否有 BLOCKED 状态未处理
是否有部署报告缺失
是否有生产风险未关闭
```

---

## 5. 输出

输出文件建议：

```text
reports/heartbeat/latest.md
```

报告格式：

```text
结论：PASS / ATTENTION / BLOCKED
检查时间
读取文件
发现的问题
风险等级
建议下一步
是否需要人工介入
```

---

## 6. 验收标准

PASS：

```text
只读执行
报告结构清晰
能发现状态冲突
没有修改任何业务文件
没有触发部署或服务操作
```

FAIL：

```text
修改了文件
尝试自动修复
触发生产操作
输出没有证据
```

---

## 7. 升级条件

只有连续多次稳定只读 PASS，才可考虑升级为稳定模块。

第一阶段仅允许：

```text
L0：只读巡检，只报告
L1：报告 + 建议任务包
```

不允许：

```text
自动修复
自动提交
自动部署
```
