FROM python:3.9-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    pkg-config

WORKDIR /Refactor_Web

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:25000 app:app
