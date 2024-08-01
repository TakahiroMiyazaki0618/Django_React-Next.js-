FROM python:3

WORKDIR /app

# pycファイル(および__pycache__)の生成を行わないようにする
ENV PYTHONDONTWRITEBYTECODE 1
# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements