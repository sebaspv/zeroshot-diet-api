# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get -y update && apt-get -y install git && apt-get -y install wget && pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]