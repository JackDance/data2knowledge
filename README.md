# data2knowledge
这是一个用于将数据转化为知识库的代码仓库。暂定包含以下几种能力：
1. 数据爬虫
2. 数据清洗
3. 知识构建 
4. 知识检索


## 后端
### 后端代码架构
满足FastAPI的三层架构
- repositories
- services
- routers

### 环境管理
本项目使用 [uv](https://github.com/astral-sh/uv) 来管理 Python 环境和依赖。

**快速开始：**
```bash
cd backend
uv sync  # 创建虚拟环境并安装所有依赖
```

详细使用说明请参考 [backend/UV_SETUP.md](docs/UV_SETUP.md)
