import re

import wikipedia
from app.wikipedia_api import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from googlesearch import search
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test/")
async def test():
    return {"message": "API was called successfully."}


@app.post("/{bird_name}/summary/")
async def bird_summary(bird_name):
    bird_wiki_summary = bird_summary_wikipedia(bird_name)
    bird_wiki_summary = str(bird_wiki_summary)
    return {"message": bird_wiki_summary}


@app.post("/{bird_name}/page/")
async def bird_page(bird_name):
    bird_wiki_page = bird_wikipedia_page(bird_name)
    bird_wiki_page = str(bird_wiki_page)
    return {"message": bird_wiki_page}
