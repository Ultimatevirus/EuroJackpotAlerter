FROM alpine:3.14
WORKDIR /usr/app/src
COPY config.json ./
COPY mailbody.txt ./
COPY script.py ./
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip install bs4 requests
CMD ["python", "./script.py"]