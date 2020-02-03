FROM python:3.7-slim

RUN mkdir -p /var/www/api

RUN apt update && apt install build-essential -y
RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /var/www
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install --dev --system --verbose

WORKDIR /var/www/api