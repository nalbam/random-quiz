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

    items = random.sample(result, 5)

    return {
        "type": type,
        "items": items,
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


@app.get("/api/music")
def music():
    musics = [
        {
            "id": "9bZkp7q19f0",
            "singer": "PSY",
            "title": "GANGNAM STYLE(강남스타일)",
        },
        {
            "id": "CHp0Kaidr14",
            "singer": "뉴진스(NewJeans)",
            "title": "Attention",
        },
        {
            "id": "WZwr2a_lFWY",
            "singer": "IZ*ONE(아이즈원)",
            "title": "라비앙로즈 (La Vie en Rose)",
        },
        {
            "id": "8AMBslo1zng",
            "singer": "IVE(아이브)",
            "title": "LOVE DIVE",
        },
        {
            "id": "0ZukHxqOA0o",
            "singer": "IU(아이유)",
            "title": "Lost Child(미아)",
        },
        {
            "id": "WH0iiU0cv00",
            "singer": "서태지(SEOTAIJI)",
            "title": "소격동(Sogyeokdong)",
        },
        {
            "id": "mZz9uYdj_v4",
            "singer": "악동뮤지션(AKMU)",
            "title": "어떻게 이별까지 사랑하겠어, 널 사랑하는 거지",
        },
        {
            "id": "MCEcWcIww5k",
            "singer": "Ailee(에일리)",
            "title": "I will show you(보여줄게)",
        },
        {
            "id": "1VdPvAqVrow",
            "singer": "코요태 (Koyote)",
            "title": "실연 (Broken Heart)",
        },
        {
            "id": "ePpPVE-GGJw",
            "singer": "TWICE(트와이스)",
            "title": "TT(티티)",
        },
        {
            "id": "Amq-qlqbjYA",
            "singer": "BLACKPINK",
            "title": "마지막처럼 (AS IF IT'S YOUR LAST)",
        },
        {
            "id": "nXJcDtPj1VM",
            "singer": "서태지와 아이들(Seo Taiji and Boys)",
            "title": "하여가 (Hayeoga)",
        },
    ]

    music = random.choice(musics)

    print(music)

    return {
        "result": "ok",
        "music": music,
        "version": VERSION,
    }


if __name__ == "__main__":
    music()
