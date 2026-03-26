#!/usr/bin/env python3
"""
A2HMarket 订单同步系统
自动同步订单到飞书文档

用法:
    python sync.py --once       # 单次运行
    python sync.py --daemon     # 后台守护模式
    python sync.py --help       # 查看帮助
"""

import json
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class A2HMarketSync:
    """A2HMarket 订单同步器"""

    def __init__(self, config):
        self.config = config
        self.data_dir = Path(config.get('DATA_DIR', 'data'))
        self.data_dir.mkdir(exist_ok=True)
        self.orders_file = self.data_dir / 'orders.json'
        self.last_sync_file = self.data_dir / 'last_sync.json'

        # 加载已同步的订单
        self.known_orders = self._load_orders()

    def _load_orders(self) -> Dict[str, dict]:
        """加载本地缓存的订单"""
        if self.orders_file.exists():
            try:
                with open(self.orders_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"加载订单失败: {e}")
        return {}

    def _save_orders(self):
        """保存订单到本地"""
        with open(self.orders_file, 'w', encoding='utf-8') as f:
            json.dump(self.known_orders, f, ensure_ascii=False, indent=2)

    def _get_last_sync_time(self) -> Optional[float]:
        """获取上次同步时间"""
        if self.last_sync_file.exists():
            try:
                with open(self.last_sync_file, 'r') as f:
                    data = json.load(f)
                    return data.get('last_sync')
            except Exception:
                pass
        return None

    def _update_last_sync_time(self):
        """更新同步时间"""
        with open(self.last_sync_file, 'w') as f:
            json.dump({'last_sync': time.time()}, f)

    def fetch_orders_from_a2hmarket(self) -> List[dict]:
        """
        从 A2HMarket 获取新订单
        这里简化为模拟数据，实际使用 a2hmarket-cli
        """
        # TODO: 实际实现调用 a2hmarket-cli
        # 例如: subprocess.run(['a2hmarket-cli', 'inbox', 'pull', ...])

        # 模拟数据
        mock_orders = [
            {
                "order_id": "WKS7067f0c6",
                "title": "观猹评论交付",
                "buyer_id": "ag_xxx",
                "amount": 10.0,
                "status": "pending",
                "created_at": "2025-06-17T12:00:00Z",
                "updated_at": "2025-06-17T12:00:00Z"
            }
        ]
        return mock_orders

    def detect_exceptions(self, order: dict) -> bool:
        """检测异常订单"""
        exception_keywords = self.config.get('EXCEPTION_KEYWORDS', [])
        title = order.get('title', '').lower()
        return any(keyword.lower() in title for keyword in exception_keywords)

    def generate_markdown(self) -> str:
        """生成 Markdown 报表"""
        orders = list(self.known_orders.values())

        total_count = len(orders)
        total_amount = sum(o.get('amount', 0) for o in orders)
        pending_count = sum(1 for o in orders if o.get('status') == 'pending')
        pending_amount = sum(o.get('amount', 0) for o in orders if o.get('status') == 'pending')
        completed_count = total_count - pending_count
        completed_amount = total_amount - pending_amount

        # 构建 Markdown
        md_lines = [
            "# 订单管理（可编辑）",
            "",
            "## 统计概览",
            f"- **订单总数**：{total_count}",
            f"- **总金额**：¥{total_amount:.2f}",
            f"- **待处理**：{pending_count}（¥{pending_amount:.2f}）",
            f"- **已完成**：{completed_count}（¥{completed_amount:.2f}）",
            "",
            "## 订单列表",
            "",
            "| 订单ID | 标题 | 金额 | 状态 | 更新时间 |",
            "|--------|------|------|------|----------|"
        ]

        for order in sorted(orders, key=lambda x: x.get('updated_at', ''), reverse=True):
            order_id = order.get('order_id', 'N/A')[:12] + '...'
            title = order.get('title', 'N/A')
            amount = f"¥{order.get('amount', 0):.2f}"
            status = order.get('status', 'unknown')
            updated = order.get('updated_at', '')[:10]

            # 标记异常订单
            if self.detect_exceptions(order):
                title = f"⚠️ {title}"

            md_lines.append(f"| {order_id} | {title} | {amount} | {status} | {updated} |")

        md_lines.extend([
            "",
            f"**最后更新**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "---",
            "*此文档由 A2HMarket 同步系统自动生成*"
        ])

        return '\n'.join(md_lines)

    def update_feishu_doc(self, content: str):
        """更新飞书文档（占位方法）"""
        # TODO: 实际实现调用飞书 API
        logger.info(f"准备更新飞书文档: {self.config.get('FEISHU_DOC_TOKEN')}")
        logger.info(f"文档内容长度: {len(content)} 字符")
        # 实际实现:
        # from feishu_doc import feishu_doc
        # feishu_doc(action='write', doc_token=..., content=...)

    def sync_once(self):
        """执行一次同步"""
        logger.info("开始同步订单...")

        # 获取新订单
        new_orders = self.fetch_orders_from_a2hmarket()

        # 合并订单
        for order in new_orders:
            order_id = order.get('order_id')
            if order_id and order_id not in self.known_orders:
                self.known_orders[order_id] = order
                logger.info(f"新订单: {order_id} - {order.get('title')}")

        # 保存
        self._save_orders()

        # 生成报表
        markdown = self.generate_markdown()

        # 更新飞书文档
        self.update_feishu_doc(markdown)

        # 更新同步时间
        self._update_last_sync_time()

        logger.info(f"同步完成，共 {len(self.known_orders)} 个订单")

    def run_daemon(self):
        """守护模式运行"""
        interval = self.config.get('SYNC_INTERVAL', 1800)
        logger.info(f"守护模式启动，同步间隔: {interval}秒")

        while True:
            try:
                self.sync_once()
            except Exception as e:
                logger.error(f"同步失败: {e}", exc_info=True)

            logger.info(f"等待 {interval} 秒后下次同步...")
            time.sleep(interval)

def main():
    """主入口"""
    import argparse

    parser = argparse.ArgumentParser(description='A2HMarket 订单同步')
    parser.add_argument('--once', action='store_true', help='单次运行')
    parser.add_argument('--daemon', action='store_true', help='守护模式')
    parser.add_argument('--config', default='config.py', help='配置文件路径')
    args = parser.parse_args()

    # 加载配置
    try:
        # 简单实现：直接导入 config.py
        # 实际应该用 importlib 或 configparser
        import sys
        sys.path.append('.')
        import config as cfg
        config = {
            'FEISHU_DOC_TOKEN': cfg.FEISHU_DOC_TOKEN,
            'OPENCLAW_AGENT_ID': cfg.OPENCLAW_AGENT_ID,
            'SYNC_INTERVAL': getattr(cfg, 'SYNC_INTERVAL', 1800),
            'EXCEPTION_KEYWORDS': getattr(cfg, 'EXCEPTION_KEYWORDS', []),
            'DATA_DIR': getattr(cfg, 'DATA_DIR', 'data'),
            'LOG_LEVEL': getattr(cfg, 'LOG_LEVEL', 'INFO'),
        }
    except Exception as e:
        print(f"加载配置失败: {e}")
        print(f"请确保 config.py 存在且配置正确")
        print(f"复制 config.example.py 为 config.py 并编辑")
        return 1

    # 设置日志级别
    logging.getLogger().setLevel(getattr(logging, config.get('LOG_LEVEL', 'INFO')))

    # 创建同步器
    syncer = A2HMarketSync(config)

    # 运行
    if args.once:
        syncer.sync_once()
    elif args.daemon:
        syncer.run_daemon()
    else:
        parser.print_help()
        print("\n示例:")
        print("  python sync.py --once       # 运行一次")
        print("  python sync.py --daemon     # 后台运行")

    return 0

if __name__ == '__main__':
    exit(main())