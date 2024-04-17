#!/usr/bin/env python3

from fastapi import FastAPI
from settings import host, port, reload
import uvicorn



app = FastAPI()

@app.get("/")
def home():
    return {
        "Python": "Framework",
    }



if __name__ == "__main__":
    uvicorn.run("app:app", host=host, port=port, reload=reload)
