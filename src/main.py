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

    # for name in names:
    #     print(name)

    name = random.choice(names)

    print(name)

    return {"result": "ok", "name": name, "version": VERSION}


@app.get("/api/music")
def music():
    music = "music"

    print(music)

    return {"result": "ok", "music": music, "version": VERSION}


if __name__ == "__main__":
    face()
