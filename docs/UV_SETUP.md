# UV 环境管理指南

本项目使用 [uv](https://github.com/astral-sh/uv) 来管理 Python 环境和依赖。

## 安装 uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或者使用 pip
pip install uv
```

## 初始化项目

在 `backend` 目录下运行：

```bash
# 创建虚拟环境并安装依赖
uv sync

# 或者使用 uv venv 创建虚拟环境
uv venv
source .venv/bin/activate  # macOS/Linux
# 或 .venv\Scripts\activate  # Windows

# 安装依赖
uv pip install -e .
```

## 常用命令

```bash
# 安装所有依赖
uv sync

# 添加新依赖
uv add <package-name>

# 添加开发依赖
uv add --dev <package-name>

# 移除依赖
uv remove <package-name>

# 更新依赖
uv sync --upgrade

# 运行 Python 脚本
uv run python main.py

# 激活虚拟环境
source .venv/bin/activate  # macOS/Linux
```

## 注意事项

- 虚拟环境默认创建在 `.venv` 目录下（已在 `.gitignore` 中忽略）
- `uv.lock` 文件应该提交到版本控制中以确保依赖版本的一致性
- 使用 `uv sync` 会自动创建虚拟环境并安装所有依赖

