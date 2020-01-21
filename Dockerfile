FROM python:3.7-slim

WORKDIR /app

RUN pip install flask numpy==1.15.4 pillow tensorflow==1.14.0 keras==2.2.4