#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import os
import random

from os import walk

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
    # s3 = boto3.resource('s3')
    # bucket = s3.Bucket('%s/%s/'.format(BUCKET_NAME, BUCKET_PATH))

    filenames = next(walk("static/photos"), (None, None, []))[2]

    # print(filenames)

    filename = random.choice(filenames)

    print(filename)

    return {"result": "ok", "filename": filename, "version": VERSION}


@app.get("/api/music")
def music():
    filenames = next(walk("static/photos"), (None, None, []))[2]

    # print(filenames)

    filename = random.choice(filenames)

    print(filename)

    return {"result": "ok", "filename": filename, "version": VERSION}


if __name__ == "__main__":
    face()
