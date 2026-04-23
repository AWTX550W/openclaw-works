# Android Device Automation - 他趣抢礼物专用

基于 Midscene 视觉 AI 的 Android 自动化工具，专为他趣 App 抢礼物场景优化。

## 📦 已安装组件

| 组件 | 版本/状态 | 位置 |
|------|-----------|------|
| ADB 工具 | 1.0.41 | `F:\taquclaw\adb_tools\platform-tools\` |
| Midscene CLI | v1.7.5 | `npm global (@midscene/android)` |
| Node.js | v18.19.0 | `C:\Users\Lenovo\.workbuddy\binaries\node\` |
| Python | 3.13 | `C:\Users\Lenovo\AppData\Local\Programs\Python\Python313\` |

## 🚀 快速开始（5分钟）

### 第 1 步：申请 API 密钥（1分钟）

推荐使用**阿里云 Qwen**（国内速度快，免费额度充足）：

1. 访问 https://dashscope.aliyuncs.com/
2. 注册/登录阿里云账号
3. 进入「控制台」→ 「API 密钥管理」
4. 创建新的 API 密钥（以 `sk-` 开头）
5. 复制密钥

### 第 2 步：配置环境（1分钟）

在 `android-device-automation` 目录下创建 `.env` 文件：

```bash
cd C:\Users\Lenovo\.workbuddy\skills\android-device-automation
copy .env.example .env
```

用记事本打开 `.env`，填入你的 API 密钥：

```env
MIDSCENE_MODEL_API_KEY=sk-你的实际密钥
MIDSCENE_MODEL_NAME=qwen3.5-plus
MIDSCENE_MODEL_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
MIDSCENE_MODEL_FAMILY=qwen3.5
```

### 第 3 步：连接手机（1分钟）

1. 用 USB 线连接 Android 手机
2. 在手机上开启「开发者选项」→ 「USB 调试」
3. 在电脑上运行：

```bash
F:\taquclaw\adb_tools\platform-tools\adb.exe devices
```

看到类似 `emulator-5554   device` 或 `你的设备ID   device` 即表示连接成功。

### 第 4 步：测试连接（1分钟）

```bash
cd C:\Users\Lenovo\.workbuddy\skills\android-device-automation
npx -y @midscene/android@1 connect
```

看到 `✅ Device connected` 表示成功。

### 第 5 步：首次抢礼物测试（1分钟）

```bash
# 1. 手动打开他趣 App，进入一个群聊界面
# 2. 运行以下命令
npx -y @midscene/android@1 act --prompt "点击聊天界面中最新的一个礼物图标，然后点击'收下'按钮"
```

观察手机屏幕，看 AI 是否正确识别并点击了礼物。

## 📁 项目结构

```
android-device-automation/
├── SKILL.md              # 技能完整说明文档
├── README.md             # 本文件（快速开始指南）
├── .env.example          # 环境配置模板
├── .env                  # 你的实际配置（需自行创建）
├── grab_gifts.py         # 完整 Python 自动化脚本
├── run_grab.bat          # Windows 快捷启动脚本（可选创建）
├── requirements.txt      # Python 依赖（如需扩展功能）
└── logs/                # 日志目录（自动创建）
    └── grab_gifts_log.txt
```

## 🎯 使用方式

### 方式 1：单次命令（快速测试）

直接在命令行执行：

```bash
cd C:\Users\Lenovo\.workbuddy\skills\android-device-automation

# 连接设备
npx -y @midscene/android@1 connect

# 启动他趣
npx -y @midscene/android@1 launch --uri com.taqu

# 执行抢礼物（需要先手动进入群聊界面）
npx -y @midscene/android@1 act --prompt "点击聊天区域出现的礼物图标，然后点击'收下'按钮"

# 断开
npx -y @midscene/android@1 disconnect
```

### 方式 2：Python 脚本（推荐，持续监控）

```bash
cd C:\Users\Lenovo\.workbuddy\skills\android-device-automation
python grab_gifts.py
```

脚本会自动：
1. 连接设备
2. 启动他趣
3. 持续监控 30 分钟（可配置）
4. 每 2 秒检查一次并尝试抢礼物
5. 记录所有操作日志
6. 生成报告文件

**自定义配置**：编辑 `grab_gifts.py` 顶部的配置区域：

```python
MONITOR_DURATION_MINUTES = 60  # 监控 1 小时
CHECK_INTERVAL_SECONDS = 1.5   # 每 1.5 秒检查一次
DEVICE_ID = "emulator-5554"    # 指定设备（可选）
```

### 方式 3：创建桌面快捷方式

创建 `run_grab.bat`：

```batch
@echo off
cd /d C:\Users\Lenovo\.workbuddy\skills\android-device-automation
echo 正在启动他趣抢礼物自动化...
python grab_gifts.py
pause
```

双击即可运行。

## 🔧 高级功能

### 1. 多设备支持

如果有多个设备，指定设备 ID：

```python
# 在 grab_gifts.py 中设置
DEVICE_ID = "your_device_id"  # 从 adb devices 获取
```

或命令行：

```bash
npx -y @midscene/android@1 connect --deviceId 你的设备ID
npx -y @midscene/android@1 act --deviceId 你的设备ID --prompt "抢礼物"
```

### 2. 自定义提示词优化

如果 AI 识别不准确，可以优化 `grab_gifts.py` 中的 `prompt`：

```python
prompt = """
任务：抢礼物
位置：群聊聊天界面的右下角或消息列表中间
特征：礼物图标是一个礼盒图片，通常带有"礼物"文字或动画效果

操作步骤：
1. 扫描整个聊天区域
2. 找到最新的礼物通知（通常是最后一条消息附近）
3. 点击礼物图标
4. 在新页面点击"收下"按钮（通常在底部中间）
5. 如果弹出"谢谢"按钮，也点击确认
6. 返回聊天界面

注意事项：
- 礼物可能出现的位置：消息气泡中、悬浮窗、底部导航栏
- 如果没找到，向下滚动一屏再试
- 动作要快，避免被其他人抢走
"""
```

### 3. 截图调试

运行截图命令查看当前屏幕：

```bash
npx -y @midscene/android@1 take_screenshot
```

截图保存在：
```
midscene_run/report/2026-04-23T17-30-00/screenshot/step_0_screenshot.png
```

用图片查看器打开，确认礼物图标的外观特征。

### 4. 查看详细报告

每次运行后会生成 HTML 报告，包含：
- 每一步操作的回放视频
- 截图和时间戳
- AI 决策过程
- 错误信息

打开 `midscene_run/report/最新时间/index.html` 查看。

## 🐛 常见问题

### Q1：`adb devices` 看不到设备

**原因**：USB 调试未开启或驱动未安装

**解决**：
1. 手机：设置 → 关于手机 → 连点「版本号」7 次 → 开启开发者选项
2. 手机：设置 → 系统 → 开发者选项 → 开启「USB 调试」
3. 电脑：安装手机 USB 驱动（华为/小米等官网下载）
4. 重新插拔 USB 线，手机弹窗点「允许」

### Q2：`npx` 命令报错 "command not found"

**原因**：Node.js 未正确安装或 PATH 未配置

**解决**：
```bash
# 检查 Node.js
C:\Users\Lenovo\.workbuddy\binaries\node\v18.19.0\node.exe -v

# 如果正常，将 npm 全局 bin 目录加入 PATH
setx PATH "%PATH%;C:\Users\Lenovo\AppData\Roaming\npm"
```

### Q3：API 密钥错误或模型不可用

**原因**：密钥无效、过期或模型名称错误

**解决**：
1. 登录控制台确认密钥状态
2. 检查 `.env` 文件格式（无引号、无空格）
3. 尝试其他模型（如 `qwen3.5-plus` → `qwen-turbo`）
4. 查看 API 额度是否用完

### Q4：AI 点错位置或找不到礼物

**原因**：提示词不够精确或界面有变化

**解决**：
1. 先截图 `npx -y @midscene/android@1 take_screenshot`
2. 查看礼物图标的实际位置和样式
3. 优化提示词，加入具体位置描述：
   - "右上角的礼物图标"
   - "聊天输入框上方的礼物按钮"
   - "最后一条消息右侧的礼盒图片"

### Q5：运行一段时间后断开

**原因**：设备屏幕关闭、ADB 超时或内存不足

**解决**：
1. 手机设置 → 显示 → 休眠时间 → 设为「10分钟」
2. 在脚本中添加唤醒命令：
   ```python
   subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'])
   ```
3. 减少监控频率（`CHECK_INTERVAL_SECONDS = 3`）

### Q6：他趣 App 闪退或重启

**原因**：内存不足或 App 版本不兼容

**解决**：
1. 关闭其他后台应用
2. 清除他趣缓存：`adb shell pm clear com.taqu`
3. 更新他趣到最新版本
4. 检查包名是否正确（可能随版本变化）

## 📊 性能优化建议

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| `CHECK_INTERVAL_SECONDS` | 2.0 | 不要太快，避免被检测 |
| `MONITOR_DURATION_MINUTES` | 30 | 单次运行不宜过长 |
| `MAX_RETRIES` | 3 | 失败重试次数 |
| `timeout` | 90 | 单次操作超时时间 |

**最佳实践**：
- 在 WiFi 环境下运行（减少网络延迟）
- 使用测试小号，不要用主号
- 避开高峰时段（如晚上 8-10 点）
- 每天总运行时间不超过 2 小时

## 🔒 安全与合规

⚠️ **风险提示**：

1. **账号风险**：自动化操作违反《他趣用户协议》，可能导致：
   - 警告
   - 功能限制
   - 临时封禁
   - 永久封号

2. **建议措施**：
   - ✅ 使用小号测试
   - ✅ 控制运行频率（不要秒级刷新）
   - ✅ 不要同时监控多个群
   - ✅ 定期人工登录确认账号状态
   - ❌ 不要用于商业牟利
   - ❌ 不要干扰其他用户

3. **免责声明**：
   本工具仅供技术研究和学习使用。使用者需自行承担使用风险，开发者不承担任何责任。

## 📚 相关资源

- **Midscene 官方文档**：https://midscene.js.org/
- **Android Device Automation 技能**：https://skills.sh/web-infra-dev/midscene-skills/android-device-automation
- **他趣 App 包名查询**：`adb shell pm list packages | findstr taqu`
- **ADB 完整命令参考**：https://developer.android.com/tools/adb

## 🆘 获取帮助

如遇到问题：

1. 查看日志文件：`grab_gifts_log.txt`
2. 检查 HTML 报告：`midscene_run/report/最新/index.html`
3. 截图当前界面：`npx -y @midscene/android@1 take_screenshot`
4. 查看设备状态：`F:\taquclaw\adb_tools\platform-tools\adb.exe logcat`

## 📝 更新日志

- **2026-04-23**：v1.0.0 初始版本
  - 集成 Midscene Android 自动化
  - 实现抢礼物 Python 脚本
  - 添加环境配置模板
  - 支持持续监控和日志记录

---

**开始使用**：`cd C:\Users\Lenovo\.workbuddy\skills\android-device-automation && python grab_gifts.py`

祝抢礼物愉快！ 🎁
