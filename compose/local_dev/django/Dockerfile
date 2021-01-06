FROM python:3.8
ENV PYTHONUNBUFFERED=1 pypiMirror="https://mirrors.aliyun.com/pypi/simple"
WORKDIR /app
COPY ./requirements.txt /
RUN pip install -i $pypiMirror -r /requirements.txt --no-cache-dir --timeout 300
