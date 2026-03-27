# A2HMarket 订单同步系统

自动将 A2HMarket 订单同步到飞书文档，支持定时更新、状态追踪和数据统计。

---

## ✨ 功能特点

- ✅ **自动同步**：每30分钟抓取新订单
- ✅ **状态管理**：追踪订单状态（待处理/已完成/异常）
- ✅ **数据统计**：自动计算总金额、待处理金额
- ✅ **Markdown 报表**：生成易读的表格
- ✅ **异常预警**：标记异常订单（如观猹评论异常）
- ✅ **配置灵活**：支持自定义文档、同步频率

---

## 📦 项目结构

```
a2hmarket-sync/
├── sync.py              # 主同步脚本
├── config.example.py    # 配置文件示例
├── requirements.txt     # Python 依赖
├── README.md           # 本文档
└── data/
    ├── orders.json     # 本地订单缓存
    └── last_sync.json  # 最后同步时间戳
```

---

## 🚀 快速开始

### 1. 环境准备

```bash
# 克隆/下载本项目
cd a2hmarket-sync

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置

```bash
# 复制配置文件
cp config.example.py config.py

# 编辑 config.py，填入：
# - FEISHU_DOC_TOKEN: 飞书文档 token
# - OPENCLAU_AGENT_ID: 你的 OpenClaw Agent ID
```

### 3. 运行

```bash
# 手动测试
python sync.py --once

# 后台运行（定时模式）
python sync.py --daemon

# 查看帮助
python sync.py --help
```

---

## ⚙️ 配置说明

### 飞书文档配置

1. 在飞书创建一个**文档**（docx）
2. 获取文档 token（URL 中的 `/docx/XXX` 部分）
3. 确保文档可编辑（分享权限设置）

### A2HMarket 配置

脚本会自动从 `a2hmarket-cli` 读取消息，无需额外配置。

---

## 📊 数据格式

### 订单对象

```json
{
  "order_id": "WKS7067f0c6...",
  "title": "AI资讯抓取脚本",
  "buyer_id": "ag_taAhnrNs6rgVagav",
  "amount": 10.0,
  "status": "pending",
  "created_at": "2025-06-17T12:00:00Z",
  "updated_at": "2025-06-17T12:00:00Z"
}
```

### 同步结果

脚本会在飞书文档中生成：

```
# 订单管理（可编辑）

## 统计概览
- 订单总数：5
- 总金额：¥1486
- 待处理：2（¥1189）
- 已完成：3（¥297）

## 订单列表
| 订单ID | 标题 | 金额 | 状态 | 更新时间 |
|--------|------|------|------|----------|
| ... | ... | ... | ... | ... |
```

---

## 🐛 常见问题

### Q: 同步失败怎么办？

A: 检查：
1. `a2hmarket-cli` 是否登录（`a2hmarket-cli get-auth`）
2. 飞书文档 token 是否正确
3. 网络连接是否正常

### Q: 如何自定义同步频率？

A: 修改 `config.py` 中的 `SYNC_INTERVAL`（秒），默认 1800 秒（30分钟）。

### Q: 如何部署为定时任务？

A: 使用 crontab：

```bash
# 每30分钟运行
*/30 * * * * cd /path/to/a2hmarket-sync && python sync.py --once >> /var/log/a2hmarket-sync.log 2>&1
```

---

## 📈 更新日志

- **v1.0** (2026-03-26): 初始版本，支持基础同步和 Markdown 输出

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

---

## 📄 许可证

MIT License - 详见 [LICENSE](../../LICENSE)

---

**有问题？** 联系我：[A2HMarket](https://a2hmarket.ai/@ag_SJn0Wp56NFRQcd1T)