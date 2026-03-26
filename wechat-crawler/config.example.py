"""
微信公众号爬虫配置
复制为 config.py 并填写
"""

# ============ 必填配置 ============

# 要监控的公众号列表（支持名称或biz ID）
WECHAT_ACCOUNTS = [
    "AI前线",
    "36氪",
    "机器之心",
    # 添加更多...
]

# ============ 抓取配置 ============

# 每个公众号最多抓取文章数
MAX_ARTICLES_PER_ACCOUNT = 20

# 更新间隔（秒），默认1小时
UPDATE_INTERVAL = 3600

# 请求超时（秒）
REQUEST_TIMEOUT = 30

# 最大重试次数
MAX_RETRIES = 3

# ============ RSS 配置 ============

RSS_TITLE = "我的公众号订阅"
RSS_LINK = "https://your-domain.com/rss"
RSS_DESCRIPTION = "精选公众号文章订阅"
RSS_LANGUAGE = "zh-cn"

# RSS 文件保存路径
RSS_OUTPUT_DIR = "data/feeds"
RSS_FILENAME = "feed.xml"

# ============ 代理配置（可选）============

# 如果触发反爬，配置代理
# HTTP_PROXY = "http://127.0.0.1:7890"
# HTTPS_PROXY = "http://127.0.0.1:7890"

# 代理列表（轮换使用）
# PROXY_POOL = [
#     "http://proxy1:port",
#     "http://proxy2:port",
# ]

# ============ 数据库配置 ============

DATABASE_PATH = "data/articles.json"

# ============ 浏览器配置 ============

# Playwright 浏览器类型：chromium, firefox, webkit
BROWSER_TYPE = "chromium"

# 是否使用无头模式（True=后台运行）
HEADLESS = True

# 是否忽略 HTTPS 错误
IGNORE_HTTPS_ERRORS = True

# ============ 高级配置 ============

# User-Agent 列表（轮换）
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
]

# Cookie（如需登录查看历史文章）
# COOKIES = "your_cookie_string"

# 启用调试日志
DEBUG = False