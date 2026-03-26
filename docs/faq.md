# 常见问题 (FAQ)

## A2HMarket 订单同步

### Q: 同步失败，提示"认证错误"？

**A:** 检查：
1. `a2hmarket-cli get-auth` 是否已登录
2. `config.py` 中的 `FEISHU_DOC_TOKEN` 是否正确
3. 飞书文档是否可编辑（分享权限设置）

---

### Q: 如何自定义同步频率？

**A:** 修改 `config.py`：
```python
SYNC_INTERVAL = 1800  # 单位：秒，默认30分钟
```

---

### Q: 可以同步历史订单吗？

**A:** 可以。脚本会从 `a2hmarket-cli` 拉取所有可访问的订单。首次运行会同步全部历史订单。

---

## 微信公众号爬虫

### Q: 抓取失败，提示 403 Forbidden？

**A:** 微信反爬严格，尝试：
1. 降低频率：`UPDATE_INTERVAL = 7200`（2小时）
2. 使用代理：配置 `HTTP_PROXY` 环境变量
3. 添加 Cookie：在 `config.py` 中设置 `COOKIES`

---

### Q: 图片无法显示？

**A:** 微信公众号图片有防盗链。需要在 `config.py` 中添加：
```python
ALLOWED_IMG_DOMAINS = ["mmbiz.qpic.cn"]
```

---

### Q: 如何部署到服务器？

**A:**
1. 上传代码到服务器
2. 安装 Docker 或 Python 环境
3. 配置 `config.py`
4. 使用 systemd 或 supervisord 守护进程

示例 systemd 配置：
```ini
[Unit]
Description=WeChat Crawler
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/wechat-crawler
ExecStart=/usr/bin/python3 crawler.py --daemon
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## OpenClaw 安装助手

### Q: Windows 提示"无法运行脚本"？

**A:** 需要修改 PowerShell 执行策略：
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
或运行 `fix_powershell.ps1` 脚本。

---

### Q: npm install 很慢/失败？

**A:** 切换 npm 源：
```bash
npm config set registry https://registry.npmmirror.com
```

---

### Q: 安装后无法启动 OpenClaw？

**A:** 运行验证脚本：
```bash
# Linux/macOS
./scripts/verify_install.sh

# Windows
.\scripts\verify_install.ps1
```

---

## 通用问题

### Q: 如何联系技术支持？

**A:**
- GitHub Issues: https://github.com/AWTX550W/openclaw-works/issues
- A2HMarket: https://a2hmarket.ai/@ag_SJn0Wp56NFRQcd1T

---

### Q: 可以商业使用吗？

**A:** 本项目采用 MIT License，可自由使用。但建议：
- 保留版权声明
- 商业用途前进行充分测试
- 如需定制开发，请联系我们。

---

### Q: 如何贡献代码？

**A:** 欢迎 PR！
1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 开启 Pull Request

---

**还有其他问题？** 请提 [Issue](../../issues)。