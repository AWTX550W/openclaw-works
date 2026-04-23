---
name: android-device-automation
displayName: Android Device Automation
description: 基于视觉的 Android 自动化工具，通过 AI 视觉识别控制手机 App，支持点击、输入、滚动等操作，无需 Root 权限
version: 1.0.0
author: WorkBuddy User
category: automation
---

# Android Device Automation 技能

## 概述
这是一个基于视觉的 Android 设备自动化技能，使用 Midscene 工具通过 AI 视觉识别来控制 Android 设备上的任何应用，包括他趣 App 的抢礼物功能。

## 前置要求

### 1. 软件环境
- ✅ Node.js v18+（已安装：v18.19.0）
- ✅ Python 3.8+（已安装：v3.13）
- ✅ ADB 工具（已安装并配置）
- ✅ Android 设备或模拟器（需启用 USB 调试）

### 2. AI 模型配置（必需）
需要配置支持视觉识别的 AI 模型 API。支持以下提供商：

#### 选项 A：智谱 AI GLM-4V-Flash（推荐，完全免费）
```bash
# 申请地址：https://open.bigmodel.cn/
# 注册送 2000 万 token，实名认证再送 2000 万
MIDSCENE_MODEL_API_KEY="sk-xxxxxxxxxxxxxxxx"
MIDSCENE_MODEL_NAME="glm-4v-flash"
MIDSCENE_MODEL_BASE_URL="https://open.bigmodel.cn/api/paas/v4"
MIDSCENE_MODEL_FAMILY="glm"
```

#### 选项 B：字节跳动 Doubao
```bash
# 申请地址：https://www.volcengine.com/
MIDSCENE_MODEL_API_KEY="xxxxxxxxxxxxxxxx"
MIDSCENE_MODEL_NAME="doubao-seed-2-0-lite"
MIDSCENE_MODEL_BASE_URL="https://ark.cn-beijing.volces.com/api/v3"
MIDSCENE_MODEL_FAMILY="doubao-seed"
```

#### 选项 C：Moonshot Kimi
```bash
# 申请地址：https://platform.kimi.com/
MIDSCENE_MODEL_API_KEY="xxxxxxxxxxxxxxxx"
MIDSCENE_MODEL_NAME="kimi-k2-6"
MIDSCENE_MODEL_BASE_URL="https://api.kimi.ai/v1"
MIDSCENE_MODEL_FAMILY="openai-compatible"
```

#### 选项 D：ModelScope 魔塔社区
```bash
# 申请地址：https://modelscope.cn/
# 每天 2000 次免费调用，需实名认证
MIDSCENE_MODEL_API_KEY="your-token"
MIDSCENE_MODEL_NAME="qwen-vl-plus"
MIDSCENE_MODEL_BASE_URL="https://api-inference.modelscope.cn/v1"
MIDSCENE_MODEL_FAMILY="openai-compatible"
```

**注意**：由于阿里云 DashScope 可能无法访问，推荐使用**智谱 AI GLM-4V-Flash**（完全免费、国内直连、支持视觉识别）。

### 3. 配置方法

#### 方式 1：环境变量（临时）
```bash
# Windows PowerShell
$env:MIDSCENE_MODEL_API_KEY="your-api-key"
$env:MIDSCENE_MODEL_NAME="qwen3.5-plus"
$env:MIDSCENE_MODEL_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
$env:MIDSCENE_MODEL_FAMILY="qwen3.5"
```

#### 方式 2：.env 文件（推荐，持久化）
在项目根目录创建 `.env` 文件：
```env
MIDSCENE_MODEL_API_KEY=sk-xxxxxxxxxxxxxxxx
MIDSCENE_MODEL_NAME=qwen3.5-plus
MIDSCENE_MODEL_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
MIDSCENE_MODEL_FAMILY=qwen3.5
```

## 核心能力

### 支持的操作
- **点击**：单击、双击、长按
- **输入**：文本输入、清除文本
- **导航**：返回、主页、最近应用
- **手势**：滑动、滚动、拖拽、双指缩放
- **应用控制**：启动应用、打开 URL
- **截图**：捕获屏幕状态

### 工作原理
1. 截图设备屏幕
2. AI 视觉模型分析截图内容
3. 智能决策下一步操作
4. 执行触摸/输入操作
5. 循环反馈直到任务完成

## 常用命令

### 1. 连接设备
```bash
# 自动连接第一个可用设备
npx -y @midscene/android@1 connect

# 指定设备 ID
npx -y @midscene/android@1 connect --deviceId emulator-5554
```

### 2. 启动他趣 App
```bash
# 通过包名启动（推荐）
npx -y @midscene/android@1 launch --uri com.taqu

# 如果不知道包名，先用 adb 查询
F:\taquclaw\adb_tools\platform-tools\adb.exe shell pm list packages | findstr taqu
```

### 3. 抢礼物核心命令
```bash
# 自然语言指令 - 监控并抢礼物
npx -y @midscene/android@1 act --prompt """
在聊天界面中，如果看到礼物图标或'收到礼物'提示，
立即点击礼物，然后点击'收下'或'谢谢'按钮
"""

# 精确操作 - 点击指定区域
npx -y @midscene/android@1 tap --locate '{
  "prompt": "tap the gift icon in the chat area"
}'
```

### 4. 截图查看
```bash
# 截图并保存
npx -y @midscene/android@1 take_screenshot

# 截图文件保存在 midscene_run/report/ 目录下
```

### 5. 执行 ADB 命令
```bash
# 直接执行 ADB shell 命令
npx -y @midscene/android@1 runadbshell --command "dumpsys window | grep mCurrentFocus"
```

### 6. 断开连接
```bash
npx -y @midscene/android@1 disconnect
```

## 他趣抢礼物实战脚本

### 方案 1：单次抢礼物
```bash
# 连接设备
npx -y @midscene/android@1 connect

# 启动他趣
npx -y @midscene/android@1 launch --uri com.taqu

# 等待应用启动
sleep 3

# 执行抢礼物（需要先手动进入群聊界面）
npx -y @midscene/android@1 act --prompt """
1. 确保当前在群聊聊天界面
2. 监控屏幕上的礼物图标（通常是礼物盒图片或'礼物'文字）
3. 一旦发现礼物，立即点击它
4. 在弹出的礼物详情页点击'收下'按钮
5. 如果出现'谢谢'按钮，也点击一下
"""

# 断开
npx -y @midscene/android@1 disconnect
```

### 方案 2：循环监控（Python 脚本）
创建 `grab_gifts.py`：
```python
import subprocess
import time
import json

def run_midscene_command(prompt):
    """执行 midscene 命令"""
    result = subprocess.run(
        ['npx', '-y', '@midscene/android@1', 'act', '--prompt', prompt],
        capture_output=True,
        text=True,
        cwd='F:/taquclaw'
    )
    return result.stdout, result.stderr

def monitor_gifts(duration_minutes=30, check_interval=2):
    """持续监控并抢礼物"""
    print(f"开始监控礼物，持续 {duration_minutes} 分钟，每 {check_interval} 秒检查一次")

    start_time = time.time()
    gift_count = 0

    while time.time() - start_time < duration_minutes * 60:
        print(f"第 {gift_count + 1} 次检查...")

        # 执行抢礼物操作
        stdout, stderr = run_midscene_command("""
        检查聊天界面是否有新礼物出现。
        如果有礼物图标或礼物提示，立即点击并领取。
        领取完成后返回聊天界面继续监控。
        """)

        if "gift" in stdout.lower() or "礼物" in stdout:
            gift_count += 1
            print(f"✅ 成功抢到第 {gift_count} 个礼物！")

        time.sleep(check_interval)

    print(f"监控结束，共抢到 {gift_count} 个礼物")

if __name__ == "__main__":
    # 先连接设备
    subprocess.run(['npx', '-y', '@midscene/android@1', 'connect'])

    # 启动他趣
    subprocess.run(['npx', '-y', '@midscene/android@1', 'launch', '--uri', 'com.taqu'])
    time.sleep(5)

    # 开始监控
    monitor_gifts(duration_minutes=10, check_interval=3)

    # 断开连接
    subprocess.run(['npx', '-y', '@midscene/android@1', 'disconnect'])
```

### 方案 3：基于通知的抢礼物（更高效）
```python
import subprocess
import time

def listen_notifications():
    """监听他趣通知（礼物通知）"""
    # 使用 ADB 监听通知
    cmd = [
        'F:\\taquclaw\\adb_tools\\platform-tools\\adb.exe',
        'shell',
        'dumpsys',
        'notification'
    ]

    while True:
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout

        # 检测礼物通知
        if 'taqu' in output and ('礼物' in output or 'gift' in output.lower()):
            print("检测到礼物通知！立即抢购...")

            # 唤醒屏幕
            subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'])
            time.sleep(1)

            # 解锁（如果需要）
            subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_MENU'])

            # 点击通知
            subprocess.run([
                'npx', '-y', '@midscene/android@1', 'act',
                '--prompt', '点击礼物通知并立即收下礼物'
            ])

        time.sleep(1)
```

## 界面元素定位技巧

### 1. 使用截图辅助定位
```bash
# 截图后查看
npx -y @midscene/android@1 take_screenshot

# 截图路径示例：
# midscene_run/report/2026-04-23T17-30-00/screenshot/step_0_screenshot.png
```

### 2. 精确定位（使用图像匹配）
如果文字描述不准确，可以截取礼物按钮的参考图：
```bash
npx -y @midscene/android@1 tap --locate '{
  "prompt": "tap the gift icon",
  "images": [
    {
      "name": "gift_button",
      "url": "file:///F:/taquclaw/gift_reference.png"
    }
  ]
}'
```

## 调试与排错

### 1. 检查设备连接
```bash
F:\taquclaw\adb_tools\platform-tools\adb.exe devices
```
应该看到类似：
```
List of devices attached
emulator-5554   device
```

### 2. 查看他趣包名
```bash
F:\taquclaw\adb_tools\platform-tools\adb.exe shell pm list packages | findstr taqu
```
输出示例：
```
package:com.taqu
```

### 3. 测试简单点击
```bash
npx -y @midscene/android@1 act --prompt "点击屏幕中央的任意按钮"
```

### 4. 查看详细日志
Midscene 会生成 HTML 报告，路径：
```
midscene_run/report/YYYY-MM-DDTHH-MM-SS/index.html
```
用浏览器打开可查看完整的操作回放视频。

### 5. 常见问题

| 问题 | 解决方案 |
|------|----------|
| 设备未连接 | 检查 USB 调试是否开启，运行 `adb devices` |
| API 密钥错误 | 确认 `.env` 文件配置正确 |
| 无法识别元素 | 使用更具体的描述，如"右上角的礼物图标" |
| 操作超时 | 增加等待时间，或先截图确认界面状态 |
| App 闪退 | 检查包名是否正确，或尝试重新启动 |

## 风险与注意事项

⚠️ **重要提醒**：

1. **账号安全**：自动化操作违反用户协议，可能导致封号
2. **设备风险**：频繁操作可能被系统检测为异常
3. **推荐做法**：
   - 使用测试账号
   - 不要设置过短的检查间隔（建议 ≥2 秒）
   - 避免在高峰时段运行
   - 定期检查账号状态

## 快速开始 checklist

- [ ] 安装 ADB 工具（已完成）
- [ ] 连接 Android 设备并启用 USB 调试
- [ ] 申请 AI 模型 API 密钥（推荐阿里云 Qwen）
- [ ] 配置 `.env` 文件
- [ ] 测试设备连接：`adb devices`
- [ ] 测试 Midscene：`npx -y @midscene/android@1 connect`
- [ ] 手动打开他趣，确认包名
- [ ] 运行单次抢礼物测试
- [ ] 优化提示词，提高识别准确率
- [ ] 部署持续监控脚本

## 下一步

1. **获取 API 密钥**：注册阿里云/字节跳动/Google 账号
2. **配置环境变量**：将密钥填入 `.env` 文件
3. **连接设备**：用 USB 线连接 Android 手机
4. **测试运行**：执行单次抢礼物命令
5. **优化脚本**：根据实际界面调整提示词

需要我帮你：
- 生成完整的 `.env` 配置文件？
- 编写更完善的 Python 监控脚本？
- 分析他趣 App 的界面元素特征？
