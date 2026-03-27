#!/bin/bash

# OpenClaw 一键安装脚本 (Linux/macOS)
# 用法: sudo bash install.sh 或 ./install.sh

set -e  # 遇到错误退出

echo "========================================="
echo "  OpenClaw 一键安装助手"
echo "  支持: Ubuntu/Debian/macOS"
echo "========================================="
echo ""

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 检测操作系统
OS="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    echo "检测到: Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    echo "检测到: macOS"
else
    echo -e "${RED}不支持的操作系统${NC}"
    exit 1
fi

# 检查是否为 root (某些步骤需要)
if [[ $EUID -ne 0 ]] && [[ "$OS" == "linux" ]]; then
    echo -e "${YELLOW}警告: 部分步骤需要 sudo 权限${NC}"
    echo "建议使用: sudo ./install.sh"
fi

# 1. 检查并安装 Node.js
echo ""
echo "[1/5] 检查 Node.js..."
if ! command -v node &> /dev/null; then
    echo "Node.js 未安装，开始安装..."

    if [[ "$OS" == "linux" ]]; then
        curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
        sudo apt-get install -y nodejs
    elif [[ "$OS" == "macos" ]]; then
        if command -v brew &> /dev/null; then
            brew install node
        else
            echo -e "${RED}请先安装 Homebrew: https://brew.sh${NC}"
            exit 1
        fi
    fi
else
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓ Node.js 已安装: $NODE_VERSION${NC}"
fi

# 2. 检查并安装 Python
echo ""
echo "[2/5] 检查 Python..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 未安装，开始安装..."

    if [[ "$OS" == "linux" ]]; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip python3-venv
    elif [[ "$OS" == "macos" ]]; then
        brew install python3
    fi
else
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python 已安装: $PYTHON_VERSION${NC}"
fi

# 3. 检查并安装 Git
echo ""
echo "[3/5] 检查 Git..."
if ! command -v git &> /dev/null; then
    echo "Git 未安装，开始安装..."

    if [[ "$OS" == "linux" ]]; then
        sudo apt-get install -y git
    elif [[ "$OS" == "macos" ]]; then
        brew install git
    fi
else
    GIT_VERSION=$(git --version)
    echo -e "${GREEN}✓ Git 已安装: $GIT_VERSION${NC}"
fi

# 4. 克隆 OpenClaw
echo ""
echo "[4/5] 克隆 OpenClaw 仓库..."
INSTALL_DIR="${OPENCLAW_INSTALL_DIR:-$HOME/openclaw}"

if [[ -d "$INSTALL_DIR" ]]; then
    echo "目录已存在: $INSTALL_DIR"
    read -p "是否重新克隆？(y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$INSTALL_DIR"
        git clone https://github.com/openclaw/openclaw.git "$INSTALL_DIR"
    fi
else
    git clone https://github.com/openclaw/openclaw.git "$INSTALL_DIR"
fi

cd "$INSTALL_DIR"

# 5. 安装 OpenClaw 依赖
echo ""
echo "[5/5] 安装 OpenClaw 依赖..."
npm install

echo ""
echo "========================================="
echo -e "${GREEN}安装完成！${NC}"
echo "========================================="
echo ""
echo "下一步："
echo "1. 进入目录: cd $INSTALL_DIR"
echo "2. 配置认证: openclaw gen-auth-code"
echo "3. 启动服务: openclaw start"
echo ""
echo "查看文档: https://docs.openclaw.ai"
echo ""