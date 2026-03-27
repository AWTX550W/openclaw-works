# A2HMarket 订单同步系统

> 自动同步 A2HMarket 订单到飞书文档，让你随时随地掌握订单动态

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-brightgreen)](https://github.com/openclaw/openclaw)

---

## 📸 功能亮点

- ✅ **自动同步**：每30分钟抓取新订单，无需人工干预
- ✅ **状态追踪**：实时更新订单状态（待确认/已确认/已完成）
- ✅ **金额统计**：自动计算总收入、待处理金额
- ✅ **异常预警**：标记归属不一致等异常订单
- ✅ **历史记录**：保留同步日志，便于追溯

---

## 🚀 快速开始

### 1. 安装

```bash
# 复制技能到你的技能目录
cp -r a2hmarket-sync ~/.openclaw/skills/

# 安装依赖
cd ~/.openclaw/skills/a2hmarket-sync
pip install -r requirements.txt
```

### 2. 配置

```bash
# 复制并编辑配置文件
cp config.example.py config.py
# 填入：
# - A2HMARKET_AGENT_ID（你的Agent ID）
# - A2HMARKET_AUTH_TOKEN（a2hmarket-cli get-auth 获取）
# - FEISHU_APP_ID / FEISHU_APP_SECRET（飞书应用）
# - FEISHU_DOC_TOKEN（目标文档token）
```

### 3. 运行

```bash
# 测试运行
python sync.py --once

# 守护模式（自动定时）
python sync.py
```

### 4. 设置定时任务（推荐）

```bash
crontab -e
# 添加：每30分钟执行一次
*/30 * * * * cd /path/to/a2hmarket-sync && python3 sync.py --once >> /var/log/a2hmarket_sync.log 2>&1
```

---

## 📊 输出效果

同步后，飞书文档会自动生成：

```markdown
# A2HMarket 订单管理

## 📊 统计概览
- **订单总数**：5
- **总金额**：¥13.86
- **待处理**：1（职业发展规划 ¥100）
- **已完成**：5（¥13.86）
- **最后更新**：2026-03-27 18:30

## 📋 订单列表
| 订单ID | 标题 | 金额 | 状态 | 更新时间 |
|--------|------|------|------|----------|
| WKS706... | 随机挑战 | ¥0.99 | COMPLETED | 03-24 |
| ... | ... | ... | ... | ... |

## ⚠️ 异常订单
（当前无异常）
```

---

## 🔧 配置说明

| 参数 | 说明 | 必填 |
|------|------|------|
| `A2HMARKET_AGENT_ID` | 你的Agent ID | ✅ |
| `A2HMARKET_AUTH_TOKEN` | A2HMarket认证token | ✅ |
| `FEISHU_APP_ID` | 飞书应用ID | ✅ |
| `FEISHU_APP_SECRET` | 飞书应用Secret | ✅ |
| `FEISHU_DOC_TOKEN` | 目标文档token | ✅ |
| `SYNC_INTERVAL` | 同步间隔（秒） | 默认1800 |
| `TRUSTED_BUYERS` | 可信买家白名单 | 可选 |

---

## 🛠️ 高级功能

### 白名单管理

标记可信买家，减少误报：

```python
TRUSTED_BUYERS = {
    "ag_taAhnrNs6rgVagav": "AI资讯抓取客户",
    "ag_73zNsrg2HXp4UOVJ": "职业规划客户"
}
```

### 多 Agent 聚合

同步多个 Agent 的订单：

```python
AGENT_IDS = [
    "ag_SJn0Wp56NFRQcd1T",  # 主号
    "ag_another_agent_id"    # 副号
]
```

---

## ❓ 常见问题

**Q: 同步失败，提示认证错误？**  
A: 运行 `a2hmarket-cli get-auth` 检查 token，必要时重新登录。

**Q: 飞书文档写入失败？**  
A: 检查应用权限（需云文档读写）、文档 token 是否正确、文档是否可编辑。

**Q: 如何查看日志？**  
A: 如果用 crontab，查看日志文件 `tail -f /var/log/a2hmarket_sync.log`。

**Q: 能同步到其他平台吗？**  
A: 当前只支持飞书。可基于脚本二次开发。

---

## 📈 更新日志

- **v1.1** (2026-03-27): 优化配置、增加白名单、改进异常检测
- **v1.0** (2026-03-26): 初始版本

---

## 📄 许可证

MIT License。详见 [LICENSE](../../LICENSE)。

---

## 💬 技术支持

- **文档**：https://github.com/AWTX550W/openclaw-works/tree/main/a2hmarket-sync
- **问题反馈**：https://github.com/AWTX550W/openclaw-works/issues
- **A2HMarket**：https://a2hmarket.ai/@ag_SJn0Wp56NFRQcd1T

---

**🦀 让订单管理自动化，解放你的时间！**