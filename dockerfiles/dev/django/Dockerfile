FROM python:3.10-slim-buster

LABEL maintainer="reza72rg@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install --default-timeout=100 -r requirements.txt

COPY ./core .
CMD ["python3","manage.py","runserver","0.0.0.0:8000" ]