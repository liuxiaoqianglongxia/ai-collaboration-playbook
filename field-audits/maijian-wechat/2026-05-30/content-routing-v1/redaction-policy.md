# Redaction Policy — maijian-wechat Publishing Assets

**Version:** v1  
**Date:** 2026-05-30  
**Scope:** maijian-wechat content routing v1 publishing audit assets  

---

## 1. 审计范围

本政策适用于 `maijian-wechat` 公众号发布链路中产生的以下资产：

- `publish_map.jsonl` — 发布记录映射文件
- `content_routing_*.json` — 内容路由配置
- WeChat Open Platform API 返回的原始响应快照
- 草稿/图文/素材相关的 media ID 引用
- 与发布流程相关的 HTML 模板、缩略图资源
- Canary 发布测试记录

**不适用范围：**
- 线上生产数据库
- 任何 `.env`、凭据存储、token 缓存文件
- 用户个人信息（openid、unionid 等）

---

## 2. 敏感字段脱敏规则

### 2.1 media_id 脱敏规则

| 项目 | 规则 |
|------|------|
| 定义 | 微信公众号素材库中的永久素材 ID |
| 脱敏方式 | 替换为 `REDACTED_MEDIA_ID` |
| 理由 | media_id 可被用于直接访问对应素材，泄露后可被重放 |

**Before:**
```json
{
  "media_id": "真实media_id_abcdefg1234567"
}
```

**After:**
```json
{
  "media_id": "REDACTED_MEDIA_ID"
}
```

---

### 2.2 draft_media_id 脱敏规则

| 项目 | 规则 |
|------|------|
| 定义 | 草稿素材 ID，用于引用未发布图文 |
| 脱敏方式 | 替换为 `REDACTED_DRAFT_MEDIA_ID` |
| 理由 | 草稿 ID 可暴露未发布内容结构，且同样可被 API 重放 |

**Before:**
```json
{
  "draft_media_id": "真实draft_media_id_xyz98765"
}
```

**After:**
```json
{
  "draft_media_id": "REDACTED_DRAFT_MEDIA_ID"
}
```

---

### 2.3 thumb_media_id 脱敏规则

| 项目 | 规则 |
|------|------|
| 定义 | 图文缩略图素材 ID |
| 脱敏方式 | 替换为 `REDACTED_THUMB_MEDIA_ID` |
| 理由 | 缩略图 ID 可被用于下载图片资源 |

**Before:**
```json
{
  "thumb_media_id": "真实thumb_media_id_qwerty01"
}
```

**After:**
```json
{
  "thumb_media_id": "REDACTED_THUMB_MEDIA_ID"
}
```

---

### 2.4 appid / appsecret / token 脱敏规则

| 项目 | 规则 |
|------|------|
| 定义 | 微信公众号 AppID、AppSecret、Access Token |
| 脱敏方式 | 全部替换为固定占位符，不得保留任何前缀/后缀/掩码 |
| 理由 | 凭据泄露可导致公众号被完全接管 |

**Before:**
```json
{
  "appid": "wx真实appid1234567890ab",
  "appsecret": "真实appsecret32chars000000000000",
  "token": "真实access_token_very_long_string"
}
```

**After:**
```json
{
  "appid": "REDACTED_APPID",
  "appsecret": "REDACTED_APPSECRET",
  "token": "REDACTED_TOKEN"
}
```

**补充规则：**
- URL 参数中的 access_token 一律删除整个参数，不留空值
- 日志行中的 `access_token=xxx` 替换为 `access_token=REDACTED_TOKEN`
- 不得保留 token 的任意片段（包括长度、前缀、后缀）
- appid 保留 `"REDACTED_APPID"` 占位符即可，不需要 `wx` 前缀

---

### 2.5 publish_map.jsonl 脱敏规则

`publish_map.jsonl` 每行为一条 JSON 发布记录。脱敏规则如下：

| 字段 | 操作 |
|------|------|
| `media_id` | → `REDACTED_MEDIA_ID` |
| `draft_media_id` | → `REDACTED_DRAFT_MEDIA_ID` |
| `thumb_media_id` | → `REDACTED_THUMB_MEDIA_ID` |
| `appid` | → `REDACTED_APPID` |
| `article_id` | → `REDACTED_ARTICLE_ID`（若关联真实文章 URL） |
| `url` | → `REDACTED_URL`（若指向真实发布链接） |
| `openid` / `unionid` | 整行删除该字段 |
| `title` / `content` / `author` | 保留，视为业务上下文 |
| `status` | 保留 |
| `created_at` / `updated_at` | 保留时间戳格式，不修改值 |

**Before (单行):**
```json
{"article_id":"真实article_id","status":"stopped_at_draft","draft_media_id":"真实draft_id","thumb_media_id":"真实thumb_id","title":"示例文章标题","created_at":"2026-05-30T10:00:00Z"}
```

**After (单行):**
```json
{"article_id":"REDACTED_ARTICLE_ID","status":"stopped_at_draft","draft_media_id":"REDACTED_DRAFT_MEDIA_ID","thumb_media_id":"REDACTED_THUMB_MEDIA_ID","title":"示例文章标题","created_at":"2026-05-30T10:00:00Z"}
```

---

## 3. 文件类型保留策略

### 3.1 JSON / JSONL 结构

**允许保留结构。**

- JSON 键名（key names）可以保留
- JSON 嵌套层级可以保留
- 数组长度可以保留
- 所有值（value）按第 2 节规则逐字段脱敏

**允许：**
```json
{
  "articles": [
    {
      "article_id": "REDACTED_ARTICLE_ID",
      "media_id": "REDACTED_MEDIA_ID",
      "status": "published"
    }
  ],
  "total": 1
}
```

### 3.2 HTML

**不允许保留原始 HTML。**

- HTML 中可能内嵌图片 URL、API endpoint、token 参数
- 导出前应将 HTML 转换为纯文本摘要，或删除 `<script>` / `<style>` / `<img>` / `<a href>` 等标签及其属性
- 如需保留结构用于审计，可将 HTML 转为 Markdown 并删除所有 URL 属性

**处理方式：**
- `<img src="https://真实url/image.jpg">` → `[IMAGE_REDACTED]`
- `<a href="https://真实url">标题</a>` → `标题`（删除 href）
- `<script src="...">` 和 `<script>...</script>` 全部删除

### 3.3 图片

**不允许保留原始图片。**

- 缩略图、封面图等可能包含品牌敏感内容
- 图片文件名若含 media_id 需重命名

**处理方式：**
- 替换为占位图文件 `placeholder.png`（统一 1x1 像素透明 PNG）
- 文件名改为 `REDACTED_IMAGE_N.png`（N 为序号）

### 3.4 Canary Run 记录

**不允许保留 canary run 的实际输出。**

- Canary 记录中包含真实 API 响应、真实 media_id、真实 token
- 仅允许保留 canary 的**状态摘要**（如 `canary_status: passed|failed|skipped`）

**允许：**
```json
{
  "canary_run_id": "REDACTED_CANARY_ID",
  "canary_status": "passed",
  "canary_timestamp": "2026-05-30T12:00:00Z",
  "canary_details": "REDACTED"
}
```

**不允许：**
```json
{
  "canary_run_id": "真实canary_id",
  "canary_status": "passed",
  "canary_details": {
    "api_response": "{...真实响应...}",
    "media_id": "真实media_id"
  }
}
```

---

## 4. 脱敏流程

```
1. 扫描
   └── 识别所有包含敏感字段的文件
       ├── JSON / JSONL 文件
       ├── 日志文件
       ├── HTML 模板
       └── 图片资源

2. 分类
   └── 按敏感级别标记每个文件
       ├── HIGH: 含 appid / appsecret / token
       ├── MEDIUM: 含 media_id / draft_media_id / thumb_media_id
       └── LOW: 仅含业务上下文（标题、状态、时间戳）

3. 脱敏
   └── 按第 2 节规则逐字段替换
       ├── 使用 sed / jq / 脚本自动化
       ├── 人工复查脱敏结果
       └── 确认无遗漏

4. 替换图片
   └── 按 3.3 规则替换所有图片为占位图

5. 转换 HTML
   └── 按 3.2 规则转换或删除 HTML

6. 验证
   └── 运行脱敏检查脚本
       ├── 扫描输出目录中是否仍包含 media_id / appsecret 等模式
       ├── 确认无真实 URL 泄露
       └── 生成脱敏报告

7. 归档
   └── 仅将脱敏后的资产移入审计仓库
```

---

## 5. 分流建议

| 资产类型 | 存放位置 | 可见性 |
|----------|----------|--------|
| 脱敏后的发布记录 | 公开仓库 `ai-collaboration-playbook` | 公开 |
| 脱敏后的路由配置 | 公开仓库 `ai-collaboration-playbook` | 公开 |
| 真实发布记录（含凭据） | **仅限 private repository** | 私有，仅审计人员 |
| 真实 canary 输出 | **仅限 private repository** 或删除 | 私有，仅审计人员 |
| 真实 HTML / 图片 | **仅限 private repository** 或删除 | 私有，仅审计人员 |
| .env / 凭据文件 | **禁止提交到任何仓库** | N/A |

**原则：真实发布记录（含任何未脱敏的 media_id、appid、secret、token）只能存在于 private repository 中，绝不出现在公开仓库或公开审计报告中。**

---

## 6. 下一步建议

1. **编写脱敏脚本**：用 `jq` + `sed` 编写 `redact.sh`，一键处理 JSON/JSONL 文件中的敏感字段，输出到 `redacted/` 目录
2. **集成到 CI**：在 PR 流程中添加 pre-commit hook，自动扫描未脱敏字段并阻止提交
3. **建立模板仓库**：将本政策作为模板，后续其他公众号审计项目可直接复用
4. **审计人员培训**：确保所有参与审计的人员了解本政策，尤其是 canary 记录和 HTML 的处理方式
5. **定期审查**：每季度审查本政策是否覆盖新增的字段类型，更新脱敏规则

---

*本政策 v1 适用于 maijian-wechat content-routing-v1 审计。后续版本迭代将在同一目录以 `redaction-policy-v2.md` 等形式保存。*
