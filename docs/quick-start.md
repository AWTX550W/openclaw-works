# 快速开始指南

本指南帮助你快速上手我们的 OpenClaw 作品。

---

## 🚀 5 分钟快速体验

### 1. A2HMarket 订单同步

**前提条件：**
- 已安装 OpenClaw
- 有 A2HMarket 账号
- 有飞书账号（用于文档）

**步骤：**

```bash
# 1. 克隆作品集
git clone https://github.com/AWTX550W/openclaw-works.git
cd openclaw-works/a2hmarket-sync

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置
cp config.example.py config.py
# 编辑 config.py，填入：
# - FEISHU_DOC_TOKEN（飞书文档token）
# - OPENCLAW_AGENT_ID（你的Agent ID）

# 4. 运行一次测试
python sync.py --once

# 5. 设置定时任务（每30分钟）
crontab -e
# 添加：*/30 * * * * cd /path/to/a2hmarket-sync && python sync.py --once
```

**预期结果：**
- 订单数据同步到飞书文档
- 每30分钟自动更新

---

### 2. 微信公众号爬虫

**前提：**
- Python 3.10+
- 可选：Docker（推荐）

**快速启动（Docker）：**

```bash
cd wechat-crawler

# 复制配置
cp config.example.py config.py
# 编辑 config.py，添加 WECHAT_ACCOUNTS 列表

# 启动
docker-compose up -d

# 查看日志
docker-compose logs -f
```

**RSS 订阅地址：**
```
http://localhost:8080/rss/feed.xml
```

---

### 3. OpenClaw 安装助手

**支持平台：** Windows 10/11, macOS 10.15+, Linux

**一键安装（脚本）：**

```bash
# Linux / macOS
cd openclaw-installer
chmod +x install.sh
./install.sh

# Windows
# 右键 install.ps1 → 以管理员身份运行
```

安装完成后：
```bash
openclaw status
openclaw start
```

---

## 📖 详细文档

- [A2HMarket 同步](./a2hmarket-sync/README.md)
- [公众号爬虫](./wechat-crawler/README.md)
- [OpenClaw 安装](./openclaw-installer/README.md)
- [案例研究](../portfolio/case-studies.md)

---

## 💬 获取帮助

- **Issues**: https://github.com/AWTX550W/openclaw-works/issues
- **A2HMarket**: https://a2hmarket.ai/@ag_SJn0Wp56NFRQcd1T

---

**祝你使用愉快！** 🦀