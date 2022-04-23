from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Welcome": "To Tyson's anime website! It's a work in progress.."}