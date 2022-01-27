FROM python:3

RUN pip install requests

WORKDIR /Corsy

COPY . /Corsy
