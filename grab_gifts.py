#!/usr/bin/env python3
"""
他趣抢礼物自动化脚本
基于 Android Device Automation 技能实现
"""

import subprocess
import time
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# ============ 配置区域 ============

# 设备配置
DEVICE_ID = None  # 设为设备ID，如 "emulator-5554"，None 表示自动选择第一个

# 他趣 App 配置
TAQU_PACKAGE = "com.taqu"  # 他趣包名（可能需要根据实际调整）

# 监控配置
MONITOR_DURATION_MINUTES = 30  # 监控时长（分钟）
CHECK_INTERVAL_SECONDS = 3  # 检查间隔（秒），避免过快触发风控
MAX_RETRIES = 3  # 失败重试次数

# 日志配置
LOG_FILE = "grab_gifts_log.txt"

# ============ 工具函数 ============

def log(message, level="INFO"):
    """记录日志"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] [{level}] {message}"
    print(log_msg)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_msg + "\n")

def run_command(cmd, cwd=None, timeout=60):
    """执行命令并返回结果"""
    try:
        # 支持字符串或列表形式
        if isinstance(cmd, str):
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                cwd=cwd,
                timeout=timeout,
                shell=True
            )
        else:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                cwd=cwd,
                timeout=timeout
            )
        # 确保 stdout/stderr 不为 None
        stdout = result.stdout if result.stdout is not None else ""
        stderr = result.stderr if result.stderr is not None else ""
        return result.returncode, stdout, stderr
    except subprocess.TimeoutExpired:
        return -1, "", "命令超时"
    except Exception as e:
        return -1, "", str(e)

def check_adb():
    """检查 ADB 是否可用"""
    log("检查 ADB 工具...")
    # 使用绝对路径确保找到 adb
    adb_path = r"F:\taquclaw\adb_tools\platform-tools\adb.exe"
    code, stdout, stderr = run_command(f'"{adb_path}" version')
    if code == 0:
        log("✅ ADB 工具正常")
        return True
    else:
        log(f"❌ ADB 检查失败: {stderr}", "ERROR")
        return False

def check_devices():
    """检查已连接的设备"""
    log("检查 Android 设备连接状态...")
    adb_path = r"F:\taquclaw\adb_tools\platform-tools\adb.exe"
    code, stdout, stderr = run_command(f'"{adb_path}" devices')
    if code != 0:
        log(f"❌ 检查设备失败: {stderr}", "ERROR")
        return []

    lines = stdout.strip().split('\n')
    devices = []
    for line in lines[1:]:  # 跳过第一行 "List of devices attached"
        if '\tdevice' in line:
            device_id = line.split('\t')[0].strip()
            devices.append(device_id)

    if devices:
        log(f"✅ 发现 {len(devices)} 台设备: {devices}")
    else:
        log("⚠️ 未发现已连接的设备，请检查 USB 调试是否开启", "WARNING")

    return devices

def check_midscene():
    """检查 Midscene 工具是否可用"""
    log("检查 Midscene 工具...")
    code, stdout, stderr = run_command("npx -y @midscene/android@1 version")
    if code == 0:
        version = stdout.strip()
        log(f"✅ Midscene 版本: {version}")
        return True
    else:
        log(f"❌ Midscene 检查失败: {stderr}", "ERROR")
        return False

def connect_device(device_id=None):
    """连接 Android 设备"""
    log(f"连接设备: {device_id or '自动选择'}")
    log("⏳ 正在启动 Midscene Agent（首次可能需要 30-60 秒）...")
    cmd = "npx -y @midscene/android@1 connect"
    if device_id:
        cmd += f" --deviceId {device_id}"

    code, stdout, stderr = run_command(cmd, timeout=120)
    if code == 0:
        log("✅ 设备连接成功")
        # 可选：打印 agent 信息
        if stdout:
            for line in stdout.split('\n')[:5]:  # 只显示前 5 行
                if line.strip():
                    log(f"   {line.strip()}")
        return True
    else:
        log(f"❌ 设备连接失败", "ERROR")
        if stderr:
            log(f"   错误详情: {stderr[:200]}")  # 只显示前 200 字符
        return False

def launch_taqu():
    """启动他趣 App（完全由 AI 视觉操作）"""
    log(f"启动他趣 App: {TAQU_PACKAGE}")

    # 让 AI 自动完成启动（最灵活）
    prompt = """请帮我启动他趣 App。具体步骤：
1. 如果当前不在桌面，先按 Home 键返回桌面。
2. 在桌面或应用列表中，找到他趣 App 图标（通常有"他趣"字样或 TAQU 标识）。
3. 点击该图标打开应用。
4. 等待应用完全加载，进入主界面。"""
    cmd = f'npx -y @midscene/android@1 act --prompt "{prompt}"'
    code, stdout, stderr = run_command(cmd, timeout=180)

    if code == 0:
        log("✅ 他趣 App 启动成功（AI 自动操作）")
    else:
        log(f"❌ 启动失败: {stderr}", "ERROR")
        return False

    log("⏳ 等待 8 秒让应用完全加载...")
    time.sleep(8)

    # 验证：截图确认
    log("📸 拍摄启动后截图验证...")
    screenshot_path = take_screenshot()
    if screenshot_path:
        log(f"✅ 截图成功: {screenshot_path}")
    else:
        log("❌ 截图失败，应用可能未正确启动", "ERROR")
        return False

    return True

def get_device_id():
    """获取当前设备 ID"""
    # 简化：直接返回第一个设备（与 check_devices 逻辑一致）
    devices = check_devices()
    return devices[0] if devices else None

def take_screenshot():
    """截图并返回截图路径"""
    cmd = "npx -y @midscene/android@1 take_screenshot"
    code, stdout, stderr = run_command(cmd, timeout=30)
    if code == 0:
        # 从输出中提取截图路径
        for line in stdout.split('\n'):
            if 'screenshot' in line.lower() and ('.png' in line or '.jpg' in line):
                log(f"📸 截图保存: {line.strip()}")
                return line.strip()
        log("📸 截图完成（路径未解析）")
        return None
    else:
        log(f"❌ 截图失败: {stderr}", "ERROR")
        return None

def grab_gift_once():
    """执行一次抢礼物操作（分两步：识别 + 执行）"""
    log("执行抢礼物操作...")

    # 步骤 1: 识别阶段 - 让 AI 描述看到什么
    identify_prompt = """仔细查看当前群聊界面，回答以下问题：
1. 聊天消息列表中，有没有明确的礼物图标（礼盒🎁或礼品袋）？
2. 如果有，礼物出现在哪条消息？位置在哪里（左/右，第几条）？
3. 礼物旁边有没有"礼物"、"礼"字？
4. 当前界面还有哪些其他元素（表情、红包、链接、图片）？

请直接回答，不要点击任何东西。"""
    cmd = f'npx -y @midscene/android@1 act --prompt "{identify_prompt}"'
    code, stdout, stderr = run_command(cmd, timeout=60)

    if code == 0:
        # 解析 AI 的描述
        description = (stdout + stderr).strip()
        log(f"📋 AI 描述: {description[:200]}")  # 只显示前 200 字符

        # 判断是否有礼物
        has_gift = any(keyword in description.lower() for keyword in ['礼物', '礼盒', '礼品', '🎁', 'gift'])

        if not has_gift:
            log("✅ 未发现礼物，跳过本次检查")
            return False

        log("🎁 检测到礼物，准备点击...")

        # 步骤 2: 执行阶段 - 点击礼物
        execute_prompt = """现在点击刚才看到的礼物图标，然后点击出现的'收下'或'领取'按钮。"""
        cmd = f'npx -y @midscene/android@1 act --prompt "{execute_prompt}"'
        code, stdout, stderr = run_command(cmd, timeout=120)

        if code == 0:
            output = (stdout + stderr).strip()
            log(f"✅ 抢礼物操作完成: {output[:100]}")
            return True
        else:
            log(f"❌ 点击失败: {stderr[:100]}", "ERROR")
            return False
    else:
        log(f"❌ 识别阶段失败: {stderr[:100]}", "ERROR")
        return False

    return False

def disconnect_device():
    """断开设备连接"""
    log("断开设备连接...")
    run_command("npx -y @midscene/android@1 disconnect")
    log("✅ 设备已断开")

# ============ 主流程 ============

def main():
    print("=" * 60)
    print("他趣抢礼物自动化脚本启动")
    print("=" * 60)
    print()

    # 1. 环境检查
    print("【步骤 1】环境检查")
    if not check_adb():
        print("❌ ADB 检查失败，请检查安装")
        return

    if not check_midscene():
        print("❌ Midscene 检查失败，请安装: npm install -g @midscene/android")
        return

    # 2. 设备检查
    log("\n【步骤 2】设备检查")
    devices = check_devices()
    if not devices:
        log("未找到设备，请：")
        log("1. 用 USB 连接手机")
        log("2. 在手机设置中启用 USB 调试")
        log("3. 在电脑上授权 USB 调试")
        return

    device_id = DEVICE_ID if DEVICE_ID else devices[0]
    log(f"使用设备: {device_id}")

    # 3. 连接设备（跳过，act 命令会自动连接）
    log("\n【步骤 3】连接设备")
    log("⏭️ 跳过手动连接（act 命令将自动连接设备）")

    # 4. 启动他趣（已注释，请手动打开他趣并进入群聊界面）
    log("\n【步骤 4】启动他趣")
    log("⚠️ 自动启动暂不可用，请手动操作：")
    log("   1. 在手机上解锁屏幕")
    log("   2. 打开他趣 App")
    log("   3. 进入一个群聊界面（确保聊天界面可见）")
    log("   然后按回车键继续...")
    input()  # 等待用户确认

    # 跳过启动，直接截图验证
    log("\n【步骤 5】截图确认界面")
    take_screenshot()

    # 6. 开始监控抢礼物
    log(f"\n【步骤 6】开始监控抢礼物（持续 {MONITOR_DURATION_MINUTES} 分钟）")
    log(f"检查间隔: {CHECK_INTERVAL_SECONDS} 秒")
    log("按 Ctrl+C 可提前结束")

    start_time = time.time()
    end_time = start_time + MONITOR_DURATION_MINUTES * 60
    gift_count = 0
    check_count = 0

    try:
        while time.time() < end_time:
            check_count += 1
            remaining = int(end_time - time.time())
            log(f"\n--- 第 {check_count} 次检查 (剩余 {remaining//60}分{remaining%60}秒) ---")

            # 执行抢礼物
            success = grab_gift_once()
            if success:
                gift_count += 1
                log(f"🎉 累计抢到 {gift_count} 个礼物！")

            # 等待下次检查
            if time.time() < end_time:
                time.sleep(CHECK_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        log("\n⚠️ 用户中断监控")

    finally:
        # 统计报告
        log("\n" + "=" * 60)
        log("监控结束")
        log(f"总检查次数: {check_count}")
        log(f"成功抢到礼物: {gift_count} 个")
        log(f"运行时长: {int(time.time() - start_time)} 秒")
        log("=" * 60)

        # 断开连接
        disconnect_device()

        # 生成报告文件
        report_file = f"grab_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write("他趣抢礼物自动化报告\n")
            f.write("=" * 60 + "\n")
            f.write(f"开始时间: {datetime.fromtimestamp(start_time)}\n")
            f.write(f"结束时间: {datetime.now()}\n")
            f.write(f"总检查次数: {check_count}\n")
            f.write(f"成功次数: {gift_count}\n")
            f.write(f"成功率: {gift_count/check_count*100:.1f}%\n" if check_count > 0 else "成功率: N/A\n")
            f.write(f"日志文件: {LOG_FILE}\n")

        log(f"📄 报告已保存: {report_file}")

if __name__ == "__main__":
    main()
