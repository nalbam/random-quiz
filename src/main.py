#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random

from os import walk

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles


VERSION = os.environ.get("VERSION", "v0.0.0")


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
