- video 转 gif ok
- 获取video列表 ok
- 获取gif列表 ok
- 图片上传 ok

**todo**
- socket,前端socket.io 示例

## 启动
### 1. 安装依赖
```python
pip3 install -r requirements.txt
```

### 2. 非python 包依赖安装

- ffmpeg: 如果不安装会报错`RuntimeError: No ffmpeg exe could be found. Install ffmpeg on your system, or set the IMAGEIO_FFMPEG_EXE environment variable.`

```shell
brew install ffmpeg

# 如果提示需要安装xcode-select:xcode-select: error: command line tools are already installed, use "Software Update" to install
# 执行以下命令
xcode-select --install
```

### 2. 启动命令
```

```

## python 虚拟环境
```shell 
# 创建虚拟环境
python3 -m venv env.dev 
# 激活虚拟环境
source env.dev/bin/activate 
# 查看当前环境
# mac linux
which python
# windows
where python
# 第三方库查看
pipenv --venv

# 退出虚拟环境
deactivate
```

**conda激活虚拟环境**
```shell
# 项目根目录下
# 激活虚拟环境
conda activate ./canda/myenv 

# 退出虚拟环境
conda deactivate
```