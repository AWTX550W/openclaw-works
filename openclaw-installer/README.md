# OpenClaw 一键安装助手

为新手用户提供 OpenClaw 的一键安装和环境配置，支持 Windows/macOS/Linux。

---

## ✨ 功能特点

- ✅ **一键安装**：自动检测系统，安装依赖，配置环境
- ✅ **跨平台**：Windows 10/11, macOS 10.15+, Linux (Ubuntu/Debian/CentOS)
- ✅ **常见问题解决**：自动修复 PowerShell 执行策略、Node.js 版本等
- ✅ **远程协助**：支持 ToDesk/向日葵远程安装（可选服务）
- ✅ **使用指导**：安装后提供基础培训和 Q&A

---

## 📦 项目结构

```
openclaw-installer/
├── install.sh            # Linux/macOS 安装脚本
├── install.ps1           # Windows 安装脚本
├── check_env.py          # 环境检测工具
├── requirements.txt      # Python 依赖
├── README.md            # 本文档
├── docs/
│   ├── troubleshooting.md  # 故障排查
│   └── tips.md            # 使用技巧
└── scripts/
    ├── fix_powershell.ps1  # Windows PowerShell 修复
    └── verify_install.sh   # 安装验证
```

---

## 🚀 快速开始

### Windows 用户

```powershell
# 1. 以管理员身份运行 PowerShell
# 2. 下载 install.ps1
# 3. 执行：
.\install.ps1
```

### macOS / Linux 用户

```bash
# 1. 下载 install.sh
# 2. 添加执行权限：
chmod +x install.sh
# 3. 运行：
./install.sh
```

---

## 📋 安装流程

### 自动检测

安装脚本会自动检测：

| 检测项 | 说明 |
|-------|------|
| 操作系统 | Windows/macOS/Linux |
| Node.js | 版本检测（需要 18+） |
| Python | 版本检测（需要 3.10+） |
| Git | 是否安装 |
| 磁盘空间 | 至少 2GB 可用 |

### 安装步骤

1. **环境准备**
   - 安装 Node.js（如未安装）
   - 安装 Python（如未安装）
   - 安装 Git

2. **下载 OpenClaw**
   ```bash
   git clone https://github.com/openclaw/openclaw.git
   ```

3. **安装依赖**
   ```bash
   cd openclaw
   npm install
   ```

4. **配置认证**
   ```bash
   # 生成 auth code
   openclaw gen-auth-code
   # 在飞书/平台完成认证
   ```

5. **验证安装**
   ```bash
   openclaw status
   ```

---

## 🛠️ 服务选项

| 服务类型 | 内容 | 价格 |
|---------|------|------|
| **自助安装** | 下载脚本，自己运行 | 免费 |
| **远程指导** | 线上会议 + 实时协助 | ¥99 |
| **完整配置** | 远程安装 + 3个技能配置 | ¥199 |
| **上门服务** | 北京地区上门（限区域） | ¥299+ |

---

## 📖 文档

- [故障排查](docs/troubleshooting.md)
- [使用技巧](docs/tips.md)
- [技能安装指南](docs/skills.md)

---

## 🐛 常见问题

### Q: Windows 提示"无法运行脚本"

A: 需要修改 PowerShell 执行策略：

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

或运行我们提供的 `fix_powershell.ps1` 脚本。

### Q: npm install 失败

A: 可能是网络问题，尝试：
```bash
npm config set registry https://registry.npmmirror.com
```

### Q: 安装后无法启动

A: 运行验证脚本：
```bash
./scripts/verify_install.sh
# 或 Windows:
.\scripts\verify_install.ps1
```

---

## 📞 获取帮助

- **GitHub Issues**: [提交问题](../../issues)
- **A2HMarket**: [联系我](https://a2hmarket.ai/@ag_SJn0Wp56NFRQcd1T)
- **OpenClaw 文档**: https://docs.openclaw.ai

---

## 📄 许可证

MIT License - 详见 [../../LICENSE](../../LICENSE)

---

**让 OpenClaw 为你所用！** 🦀