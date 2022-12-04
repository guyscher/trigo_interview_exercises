FROM python:3.10-slim

RUN python3 -m pip install flask
WORKDIR /code

COPY main.py main.py

RUN apt update && apt install -y curl

ENTRYPOINT [ "python3", "main.py" ]