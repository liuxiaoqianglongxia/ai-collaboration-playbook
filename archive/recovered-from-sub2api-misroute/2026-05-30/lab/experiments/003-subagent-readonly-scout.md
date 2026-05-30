# Experiment 003｜Subagent Readonly Scout

状态：实验设计  
类型：Subagent 只读侦察实验  
是否进入稳定主链路：否

---

## 1. 目标

验证 subagent 是否能承担只读侦察任务，减少主执行线程的上下文污染。

本实验不测试并行写代码。

只测试：

```text
多个只读子代理分别侦察不同范围
输出证据路径
主线程汇总摘要
Codex 复核并收口
```

---

## 2. 适合场景

```text
后端路由侦察
前端流程侦察
测试失败侦察
文档一致性检查
迁移差异分析
安全风险初扫
```

---

## 3. 子代理示例

```text
backend-route-scout
frontend-flow-scout
test-failure-scout
docs-state-scout
ops-risk-scout
```

---

## 4. 默认权限

所有子代理默认只读。

允许：

```text
读取指定文件
搜索指定路径
输出摘要
列出证据
提出风险
建议下一步
```

禁止：

```text
修改文件
运行迁移
访问 .env
改数据库
部署
创建 commit
创建 PR
直接给最终结论
```

---

## 5. Subagent Task Packet 模板

```markdown
# Subagent Task Packet

## agent_id

backend-route-scout

## role

只读后端路由侦察子代理

## scope

只读检查 app/routes、api、auth、billing 相关路径。

## input files

- CURRENT.md
- TASKS.md
- app/
- backend/
- routes/

## forbidden

- 不修改文件
- 不运行迁移
- 不访问 .env
- 不改数据库
- 不部署
- 不创建 commit

## output

1. 发现的相关文件
2. 路由 / 接口结构
3. 风险点
4. 与当前任务的关系
5. 建议是否进入修改阶段
6. 证据路径
```

---

## 6. 主 Codex 职责

Codex 负责：

```text
分派子代理
等待子代理返回
过滤噪音
要求证据
综合判断
最终集成
跑测试
写报告
```

子代理输出不能直接成为最终结论。

---

## 7. 验收标准

PASS：

```text
子代理只读
每个结论带文件证据
主线程收到摘要而不是噪音堆
没有并行改文件
Codex 有复核结论
```

FAIL：

```text
子代理修改文件
子代理越权访问 .env / 数据库 / 生产路径
多个子代理抢同一批文件
主 Codex 照单全收未复核
```

---

## 8. 升级条件

连续稳定只读 PASS 后，可考虑升级为：

```text
modules/READONLY_SUBAGENT_V1.md
```

但即使升级，第一阶段也只允许只读子代理，不允许并行写入。
