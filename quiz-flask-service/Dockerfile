# 使用官方的 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 并安装依赖
COPY requirements.txt .
RUN pip install -r requirements.txt

# 复制当前目录下的所有文件到工作目录
COPY . .

# 设置容器启动时执行的命令
CMD ["python", "main.py"]