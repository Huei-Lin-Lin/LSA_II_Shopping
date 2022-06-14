# FROM：基底映像檔
FROM python:alpine3.10

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 
#tk-dev
RUN /usr/local/bin/python -m pip install --upgrade pip

EXPOSE 5000

RUN adduser -D admin
USER admin
WORKDIR /home/admin

# ADD：將檔案加到 images 內
ADD . /admin

# ENV PYTHONUNBUFFERED 1

# 只有build 時使用，會執行此命令
COPY --chown=admin:admin requirements.txt /home/admin
ENV PATH="/home/admin/.local/bin:${PATH}"

RUN pip3 install --user --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

# run container 時要執行的命令 COPY . /home/app
COPY --chown=admin:admin . /home/admin

CMD python3 ./ajax.py
# CMD python3 ./operationDB.py