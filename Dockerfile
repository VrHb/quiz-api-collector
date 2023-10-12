FROM python:3.11.6-alpine

WORKDIR /usr/src/app

RUN pip install -U pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . . 
