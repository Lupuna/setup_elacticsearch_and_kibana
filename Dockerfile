FROM python:3.11-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY app /app
WORKDIR /app
EXPOSE 8000

RUN apk add build-base

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password app-user

USER app-user