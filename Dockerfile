FROM python:3.7-alpine3.8

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python",  "corsy.py"]
