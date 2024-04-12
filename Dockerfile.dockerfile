FROM alpine:3.19
WORKDIR /usr/app/src
COPY config.json ./
COPY mailbody.txt ./
COPY script.py ./
COPY trigger.py ./
ENV PYTHONUNBUFFERED=1
ENV SMTPAUTH="b64encodedstring"
RUN apk add --no-cache python3 py3-pip
RUN pip3 install --no-cache --upgrade pip setuptools --break-system-packages
RUN pip install --no-cache bs4 requests schedule --break-system-packages
RUN pip install --no-cache cryptography requests schedule --break-system-packages
CMD ["python", "./script.py"]