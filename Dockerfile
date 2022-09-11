# Dockerfile

# FROM python:3.10-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim-2021-10-02

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt update && \
#     apt install -y bash curl jq && \
#     apt clean

WORKDIR /app

COPY . .

# RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

EXPOSE 8000

CMD ["bash", "entrypoint.sh"]
