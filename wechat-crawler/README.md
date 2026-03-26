# 微信公众号爬虫 + RSS 转换

批量抓取微信公众号文章，自动转换为 RSS 2.0 feed，支持定时更新和高可用部署。

---

## ✨ 功能特点

- ✅ **多公众号监控**：同时追踪多个公众号
- ✅ **反爬虫处理**：IP轮换、headers伪装、验证码识别
- ✅ **完整内容抓取**：标题、正文、图片、阅读量、在看数
- ✅ **标准 RSS 2.0**：兼容所有 RSS 阅读器
- ✅ **Docker 部署**：一键启动，易于运维
- ✅ **容错机制**：自动重试、断点续传
- ✅ **定时更新**：可配置抓取频率

---

## 📦 项目结构

```
wechat-crawler/
├── crawler.py            # 主爬虫
├── rss_generator.py      # RSS 生成器
├── config.example.py     # 配置示例
├── requirements.txt      # Python 依赖
├── Dockerfile           # Docker 镜像
├── docker-compose.yml   # Docker Compose
├── README.md           # 本文档
└── data/
    ├── articles.json    # 抓取的文章缓存
    └── feeds/          # 生成的 RSS 文件
```

---

## 🚀 快速开始

### 方式一：Docker（推荐）

```bash
# 克隆项目
cd wechat-crawler

# 复制配置
cp config.example.py config.py
# 编辑 config.py，添加公众号列表

# 启动
docker-compose up -d

# 查看日志
docker-compose logs -f
```

### 方式二：本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 配置
cp config.example.py config.py
# 编辑 config.py，添加公众号列表

# 测试运行
python crawler.py --once

# 后台运行
python crawler.py --daemon
```

---

## ⚙️ 配置说明

### `config.py` 配置项

```python
# 公众号列表（公众号名称或biz ID）
WECHAT_ACCOUNTS = [
    "AI前线",      # 公众号名称
    "36氪",
    "机器之心",
]

# 抓取配置
MAX_ARTICLES_PER_ACCOUNT = 20    # 每个账号最多抓取文章数
UPDATE_INTERVAL = 3600          # 更新间隔（秒），默认1小时

# RSS 配置
RSS_TITLE = "我的公众号订阅"
RSS_LINK = "https://your-domain.com/rss"
RSS_DESCRIPTION = "精选公众号文章"

# 代理配置（可选，用于反爬虫）
HTTP_PROXY = "http://proxy:port"
HTTPS_PROXY = "https://proxy:port"

# 数据库
DATABASE_PATH = "data/articles.json"
```

---

## 📡 支持的公众号

理论上支持**所有微信公众号**，包括：

- ✅ 普通订阅号
- ✅ 服务号
- ✅ 企业号
- ✅ 已认证/未认证

**注意**：部分公众号有严格反爬，可能需要：
- 使用代理 IP
- 降低抓取频率
- 添加 Cookie（需登录）

---

## 📰 RSS 输出

### RSS 2.0 格式

生成的 RSS 包含完整信息：

```xml
<item>
  <title>文章标题</title>
  <link>原文链接</link>
  <description>文章摘要（含图片）</description>
  <pubDate>2025-06-17T12:00:00Z</pubDate>
  <author>公众号名称</author>
  <source>原创/转载</source>
</item>
```

### 订阅地址

部署后，RSS 地址为：
```
http://your-server/rss/feed.xml
```

可用于：
- RSS 阅读器（Feedly, Inoreader）
- OpenClaw 订阅
- 自定义通知推送

---

## 🐳 Docker 部署

### 构建镜像

```bash
docker build -t wechat-crawler .
```

### 运行容器

```bash
docker run -d \
  -p 8080:8080 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/config.py:/app/config.py \
  --name wechat-crawler \
  wechat-crawler
```

### 使用 Docker Compose

```bash
# 编辑 docker-compose.yml，配置 volumes
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止
docker-compose down
```

---

## 🔧 技术栈

- **Python 3.10+**
- **Playwright**：浏览器自动化，支持动态渲染
- **Requests**：HTTP 请求
- **feedgen**：RSS 生成
- **SQLite**：数据存储（可选）
- **Docker**：容器化部署

---

## 🐛 常见问题

### Q: 抓取失败/403 Forbidden？

A: 可能触发反爬，尝试：
1. 使用代理（配置 `HTTP_PROXY`）
2. 降低频率（`UPDATE_INTERVAL` 改为 7200）
3. 添加 User-Agent 轮换

### Q: 图片无法显示？

A: 微信公众号图片有防盗链，需要在配置中添加：
```python
ALLOWED_IMG_DOMAINS = ["mmbiz.qpic.cn"]
```

### Q: 如何部署到服务器？

A:
1. 上传代码到服务器
2. 安装 Docker（或直接运行 Python）
3. 配置 `config.py`
4. 使用 systemd 或 supervisord 守护进程

---

## 📈 更新日志

- **v1.0** (2026-03-26): 初始版本，支持基础抓取 + RSS

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

---

## 📄 许可证

MIT License - 详见 [../../LICENSE](../../LICENSE)

---

**有问题？** 联系我：[A2HMarket](https://a2hmarket.ai/@ag_SJn0Wp56NFRQcd1T)