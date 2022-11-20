#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import random
import uuid

from boto3 import client

from fastapi import FastAPI, Response
from starlette.staticfiles import StaticFiles

from .models import QuizModel


VERSION = os.environ.get("VERSION", "v0.0.0")

BUCKET_NAME = os.environ.get("BUCKET_NAME", "repo.demo.nalbam.com")
BUCKET_PATH = os.environ.get("BUCKET_PATH", "face-quiz")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    html = "<!doctype html><html><head><meta http-equiv='refresh' content='0; url=/static/quiz.html' /></head></html>"
    return Response(content=html, media_type="text/html")


@app.get("/healthz")
def health():
    return {"result": "ok", "version": VERSION}


@app.get("/quiz/{type}")
def get_quiz(type: str):
    # scan db
    list = QuizModel.scan(
        (QuizModel.type == type),
        # index_name="type_idx",
    )

    result = []
    for item in list:
        result.append(
            {
                "code": item.code,
                "name": item.name,
                "title": item.title,
            }
        )

    item = random.sample(result, 1)

    return {
        "type": type,
        "item": item[0],
        "version": VERSION,
    }


@app.post("/quiz/{type}")
def post_quiz(type: str, code: str, name: str, title: str):
    print("+ post_quiz", type, name, title)

    list = QuizModel.scan(
        (QuizModel.type == type) & (QuizModel.code == code),
    )

    quiz = None
    for item in list:
        quiz = item
        break

    if quiz is None:
        quiz = QuizModel()
        quiz.id = str(uuid.uuid4())
        quiz.type = type
        quiz.code = code
        # quiz.reg_date = datetime.datetime.now()

    quiz.name = name
    quiz.title = title

    if VERSION != "v0.0.0":
        quiz.save()

    return {"result": "ok", "version": VERSION}


@app.get("/api/face")
def face():
    conn = client("s3")

    names = []
    for key in conn.list_objects(Bucket=BUCKET_NAME, Prefix=BUCKET_PATH)["Contents"]:
        key = key["Key"]
        if not key.endswith("/"):
            names.append(key.split("/")[1])

    name = random.choice(names)

    print(name)

    return {"result": "ok", "name": name, "version": VERSION}


if __name__ == "__main__":
    health()
