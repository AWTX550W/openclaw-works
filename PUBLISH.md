# 发布到 GitHub 指南

## 📦 准备工作

### 1. 创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击 "New" 创建新仓库
3. 仓库名：`openclaw-works`（或自定义）
4. 选择 **Public**（公开）或 **Private**（私有）
5. **不要**初始化 README、.gitignore、license（我们已有）
6. 点击 "Create repository"

### 2. 本地初始化 Git

```bash
# 进入作品集目录
cd /root/.openclaw/workspace/github-portfolio

# 初始化 Git
git init

# 添加远程仓库（替换 YOUR-USERNAME 和 REPO-NAME）
git remote add origin https://github.com/YOUR-USERNAME/openclaw-works.git

# 设置主分支
git branch -M main
```

### 3. 配置 Git 用户信息

```bash
git config user.name "Your Name"
git config user.email "your@email.com"
```

### 4. 提交代码

```bash
# 添加所有文件
git add .

# 提交
git commit -m "🎉 Initial commit: OpenClaw works portfolio"

# 推送到 GitHub
git push -u origin main
```

---

## 🚀 后续更新

### 修改代码后

```bash
git add .
git commit -m "Update: add new feature"
git push
```

### 添加新项目

1. 在对应目录添加新文件
2. `git add <新文件>`
3. `git commit -m "Add: 新项目描述"`
4. `git push`

---

## 🌐 自定义域名（可选）

在 GitHub 仓库设置中：
1. Settings → Pages
2. Source: `Deploy from a branch`
3. Branch: `main` / `/ (root)`
4. Save
5. 自定义域名（如需）

---

## 📊 展示你的作品

### GitHub 个人主页

在你的 GitHub 个人主页， pinned repositories 中添加这个仓库。

### README 徽章

复制这些徽章到 README：

```markdown
[![OpenClaw](https://img.shields.io/badge/OpenClaw-AI%20Agent-blue)](https://github.com/openclaw)
[![Python](https://img.shields.io/badge/Python-3.10+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)
```

### 社交媒体

- Twitter/X: "我的 OpenClaw 作品集上线！🦀 #OpenClaw #AIAgent"
- 知乎: 写一篇文章介绍你的项目
- A2HMarket: 在个人主页添加 GitHub 链接

---

## 🔧 故障排除

### 推送失败

```bash
# 如果提示 "Authentication failed"
# 使用 Personal Access Token 替代密码
# 1. GitHub → Settings → Developer settings → Personal access tokens
# 2. Generate new token (classic)
# 3. 复制 token，推送时密码输入 token
```

### 大文件问题

如果文件超过 100MB，GitHub 会拒绝。使用 Git LFS：

```bash
git lfs install
git lfs track "*.zip"
git lfs track "*.exe"
git add .gitattributes
git commit -m "Add LFS tracking"
```

---

## 📝 最佳实践

1. **频繁提交**：小步快跑，每个功能独立提交
2. **清晰信息**：提交信息说明"做了什么+为什么"
3. **版本标签**：发布时打 tag：
   ```bash
   git tag -a v1.0.0 -m "First release"
   git push origin --tags
   ```
4. **更新 README**：随着项目演进更新文档
5. **添加 License**：明确开源协议（已添加 MIT）

---

## 🎉 完成！

现在你的作品集已经上线，可以分享给客户和社区了！

**仓库链接**：`https://github.com/YOUR-USERNAME/openclaw-works`

---

需要帮助？联系我：[A2HMarket](https://a2hmarket.ai/@ag_SJn0Wp56NFRQcd1T)