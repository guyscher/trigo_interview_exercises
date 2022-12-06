FROM python:3.10-slim

RUN python3 -m pip install requests flask
WORKDIR /code

COPY main.py main.py

ENTRYPOINT [ "python3", "main.py" ]