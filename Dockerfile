FROM python:3.7-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev