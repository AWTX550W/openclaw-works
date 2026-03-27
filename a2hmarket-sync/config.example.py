"""
A2HMarket 订单同步系统配置文件
复制为 config.py 并填写实际值
"""

# ============ 必填配置 ============

# 飞书文档 Token（URL 中 /docx/ 后面的部分）
FEISHU_DOC_TOKEN = "your_doc_token_here"

# OpenClaw Agent ID（你的 Agent ID）
OPENCLAW_AGENT_ID = "ag_SJn0Wp56NFRQcd1T"

# ============ 可选配置 ============

# 同步间隔（秒），默认 1800（30分钟）
SYNC_INTERVAL = 1800

# 日志级别：DEBUG, INFO, WARNING, ERROR
LOG_LEVEL = "INFO"

# 数据存储路径
DATA_DIR = "data"
ORDERS_FILE = "data/orders.json"
LAST_SYNC_FILE = "data/last_sync.json"

# 飞书文档标题（自动更新）
DOC_TITLE = "订单管理（可编辑）"

# 启用调试模式（打印详细日志）
DEBUG = False

# ============ 高级配置 ============

# 消息队列配置（用于实时同步）
# MQTT_BROKER = "localhost"
# MQTT_PORT = 1883

# 异常订单关键词（匹配订单标题）
EXCEPTION_KEYWORDS = ["观猹", "异常", "问题"]

# 邮件通知（如需发送邮件）
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587
# EMAIL_FROM = "your@email.com"
# EMAIL_TO = ["admin@example.com"]