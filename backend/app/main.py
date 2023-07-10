import json
import os
import re

import wikipedia
from app.wikipedia_api import *
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from googlesearch import search
from pydantic import BaseModel

app = FastAPI()
UPLOAD_DIR = "/upload_directory"

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


@app.post("/api/photo")
async def upload_photo(photo: UploadFile = File(...)):
    # Create upload directory if it does not exist
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Unique filename for uploaded photo
    filename = f"photo_{photo.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Save the uploaded photo to the server
    with open(file_path, "wb") as f:
        f.write(await photo.read())

    results = photo.filename  #
    prediction = None
    #predicted = prediction()
    # results = predict_one_path(file_path)

    return {
        "subtitle": json.dumps(results),
        "prediction": json.dumps(prediction)
    }


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
