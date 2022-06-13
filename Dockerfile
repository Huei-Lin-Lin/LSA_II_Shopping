# FROM：基底映像檔
FROM python:alpine3.10

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 
#tk-dev
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN adduser -D app
USER app
WORKDIR /home/app

# ADD：將檔案加到 images 內
ADD . /app

ENV PYTHONUNBUFFERED 1

# 只有build 時使用，會執行此命令
COPY --chown=app:app requirements.txt requirements.txt

ENV PATH="/home/app/.local/bin:${PATH}"

RUN pip3 install --user -r requirements.txt

# run container 時要執行的命令 COPY . /home/app
COPY --chown=app:app . /home/app

CMD python3 ./ajax.py