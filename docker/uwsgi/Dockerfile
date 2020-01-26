FROM python:3.7-slim

RUN mkdir /var/www
WORKDIR /var/www

RUN apt update && apt install build-essential -y

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install --dev --system
