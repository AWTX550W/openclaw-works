# API 密钥申请指南（国内可用方案）

由于阿里云 DashScope 可能无法访问，以下是几个**国内可用的替代方案**，按推荐顺序排列：

---

## 🥇 方案一：智谱 AI GLM-4V-Flash（强烈推荐）

### 优势
- ✅ **完全免费**：注册送 2000 万 token，实名认证再送 2000 万
- ✅ **国内直连**：无需科学上网，访问速度快
- ✅ **支持视觉**：GLM-4V-Flash 专为图像理解设计
- ✅ **稳定可靠**：智谱 AI 官方 API，长期可用

### 申请步骤

1. **访问官网**
   - 网址：https://open.bigmodel.cn/
   - 点击「登录」→ 选择「手机号登录」或「扫码登录」

2. **实名认证**（可选但推荐）
   - 进入「我的」→ 「实名认证」
   - 完成实名后可获得额外 2000 万 token
   - 认证通常 1-2 个工作日完成

3. **创建 API 密钥**
   - 进入「控制台」→ 「API 密钥管理」
   - 点击「创建新密钥」
   - 输入密钥名称（如「他趣抢礼物」）
   - 点击「创建」并**立即复制密钥**（以 `sk-` 开头）
   - ⚠️ 密钥只显示一次，请妥善保存

4. **配置到项目**
   ```bash
   cd C:\Users\Lenovo\.workbuddy\skills\android-device-automation
   copy .env.example .env
   ```
   编辑 `.env` 文件：
   ```env
   MIDSCENE_MODEL_API_KEY=sk-你的实际密钥
   MIDSCENE_MODEL_NAME=glm-4v-flash
   MIDSCENE_MODEL_BASE_URL=https://open.bigmodel.cn/api/paas/v4
   MIDSCENE_MODEL_FAMILY=glm
   ```

### 注意事项
- 免费额度足够个人使用（2000 万 token 约可处理 1 万张图片）
- API 调用频率限制：默认 10 QPS（每秒 10 次）
- 支持的语言：中文、英文等多语言

---

## 🥈 方案二：字节跳动 Doubao（豆包）

### 优势
- ✅ **免费额度**：新用户有一定免费额度
- ✅ **速度快**：字节跳动自建 CDN，响应迅速
- ✅ **模型优秀**：Seed 2.0 Lite 性价比高

### 申请步骤

1. **访问官网**
   - 网址：https://www.volcengine.com/
   - 点击「注册」→ 使用手机号或邮箱

2. **完成实名**
   - 进入「控制台」→ 「实名认证」
   - 上传身份证或使用银行卡验证

3. **开通大模型服务**
   - 搜索「Doubao」或进入「AI 服务」
   - 找到「Doubao Seed 2.0 Lite」模型
   - 点击「开通服务」

4. **获取 API 密钥**
   - 进入「API 密钥管理」
   - 创建新密钥并复制

5. **配置**
   ```env
   MIDSCENE_MODEL_API_KEY=你的豆包API密钥
   MIDSCENE_MODEL_NAME=doubao-seed-2-0-lite
   MIDSCENE_MODEL_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
   MIDSCENE_MODEL_FAMILY=doubao-seed
   ```

---

## 🥉 方案三：Moonshot Kimi（月之暗面）

### 优势
- ✅ **免费额度**：每天有免费调用次数
- ✅ **多模态支持**：K2.6 模型支持视觉推理
- ✅ **界面友好**：控制台操作简单

### 申请步骤

1. **访问官网**
   - 网址：https://platform.kimi.com/
   - 点击「Sign Up」注册

2. **验证邮箱**
   - 输入邮箱 → 接收验证码 → 完成注册

3. **创建 API 密钥**
   - 进入「Dashboard」→ 「API Keys」
   - 点击「Create API Key」
   - 复制密钥（以 `sk-` 开头）

4. **配置**
   ```env
   MIDSCENE_MODEL_API_KEY=你的Kimi_API密钥
   MIDSCENE_MODEL_NAME=kimi-k2-6
   MIDSCENE_MODEL_BASE_URL=https://api.kimi.ai/v1
   MIDSCENE_MODEL_FAMILY=openai-compatible
   ```

---

## 🔧 方案四：ModelScope 魔塔社区（阿里系）

### 优势
- ✅ **完全免费**：每天 2000 次免费调用
- ✅ **模型丰富**：提供 Qwen-VL-Plus 等多模态模型
- ✅ **开源生态**：阿里系开源模型平台

### 申请步骤

1. **访问官网**
   - 网址：https://modelscope.cn/
   - 点击「登录」→ 使用支付宝或手机号

2. **实名认证**
   - 必须完成实名（支付宝授权最快）
   - 认证后每日额度提升至 2000 次

3. **创建 API Token**
   - 进入「个人中心」→ 「模型服务」
   - 找到「API 访问令牌」
   - 点击「创建令牌」并复制

4. **配置**
   ```env
   MIDSCENE_MODEL_API_KEY=你的ModelScope令牌
   MIDSCENE_MODEL_NAME=qwen-vl-plus
   MIDSCENE_MODEL_BASE_URL=https://api-inference.modelscope.cn/v1
   MIDSCENE_MODEL_FAMILY=openai-compatible
   ```

---

## 📊 方案对比

| 平台 | 免费额度 | 速度 | 稳定性 | 推荐指数 |
|------|---------|------|--------|---------|
| 智谱 AI GLM-4V-Flash | 4000 万 token | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 字节 Doubao | 试用额度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Moonshot Kimi | 每日限额 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| ModelScope | 每日 2000 次 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## 🎯 推荐选择

**首选：智谱 AI GLM-4V-Flash**
- 理由：完全免费、额度充足、国内直连、支持视觉
- 适合：个人使用、长期运行、低成本

**备选：字节 Doubao**
- 理由：速度快、模型强、稳定性好
- 适合：对速度要求高、愿意小额付费

---

## ❓ 常见问题

### Q1：智谱 AI 注册后无法实名？
**答**：实名认证通常需要 1-2 个工作日，期间可先用基础额度测试。

### Q2：API 密钥格式不对？
**答**：确保复制完整的密钥（以 `sk-` 开头，长度约 100+ 字符）。

### Q3：调用时返回 401 错误？
**答**：
1. 检查密钥是否正确粘贴
2. 确认密钥未过期（在控制台查看状态）
3. 检查 `.env` 文件格式（无多余空格或引号）

### Q4：免费额度用完怎么办？
**答**：
- 智谱 AI：额度用完后可充值（价格合理）或等待下月重置
- 其他平台：可注册多个账号轮换使用

### Q5：Midscene 支持这些模型吗？
**答**：支持！Midscene 支持 OpenAI 兼容接口，以上平台都兼容。只需正确配置 `BASE_URL` 和 `FAMILY` 即可。

---

## 🚀 快速配置脚本

如果你已经获得了智谱 AI 的 API 密钥，可以运行以下命令自动配置：

```bash
cd C:\Users\Lenovo\.workbuddy\skills\android-device-automation

# 创建 .env 文件（智谱 AI 示例）
echo MIDSCENE_MODEL_API_KEY=sk-你的密钥 > .env
echo MIDSCENE_MODEL_NAME=glm-4v-flash >> .env
echo MIDSCENE_MODEL_BASE_URL=https://open.bigmodel.cn/api/paas/v4 >> .env
echo MIDSCENE_MODEL_FAMILY=glm >> .env
```

---

## 📞 获取帮助

如果申请过程中遇到问题：

1. **智谱 AI 官方支持**
   - 官网：https://open.bigmodel.cn/
   - 客服：控制台右下角「在线客服」

2. **查看文档**
   - API 文档：https://open.bigmodel.cn/api
   - 模型列表：查看「多模态模型」章节

3. **测试密钥**
   ```bash
   # 测试连接
   curl https://open.bigmodel.cn/api/paas/v4/models \
     -H "Authorization: Bearer sk-你的密钥"
   ```

---

**建议**：优先申请**智谱 AI**，完全免费且稳定，最适合个人使用。申请完成后，编辑 `.env` 文件并运行 `python grab_gifts.py` 即可开始抢礼物！
