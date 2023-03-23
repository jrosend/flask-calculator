# syntax=docker/dockerfile:experimental

FROM python:3.10-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
COPY app.py app.py

RUN pip3 install -r requirements.txt

CMD [ "python3",  "-m", "flask", "run", "--host=0.0.0.0"]
