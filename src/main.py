#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import os
import random

from os import walk

from boto3 import client

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles


VERSION = os.environ.get("VERSION", "v0.0.0")

BUCKET_NAME = os.environ.get("BUCKET_NAME", "repo.demo.nalbam.com")
BUCKET_PATH = os.environ.get("BUCKET_PATH", "face-quiz")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/healthz")
def health():
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
            "title": "PSY - GANGNAM STYLE(강남스타일)",
        },
        {
            "id": "CHp0Kaidr14",
            "title": "뉴진스(NewJeans) - Attention",
        },
        {
            "id": "WZwr2a_lFWY",
            "title": "IZ*ONE(아이즈원) - 라비앙로즈 (La Vie en Rose)",
        },
        {
            "id": "8AMBslo1zng",
            "title": "IVE(아이브) - LOVE DIVE",
        },
        {
            "id": "0ZukHxqOA0o",
            "title": "IU(아이유) - Lost Child(미아)",
        },
        {
            "id": "WH0iiU0cv00",
            "title": "서태지(SEOTAIJI) - 소격동(Sogyeokdong)",
        },
        {
            "id": "mZz9uYdj_v4",
            "title": "악동뮤지션(AKMU) - 어떻게 이별까지 사랑하겠어, 널 사랑하는 거지",
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
