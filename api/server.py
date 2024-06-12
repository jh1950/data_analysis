from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import logs
from db import init
from .routes import main, NN01, testrouter



app = FastAPI()
app.mount("/static", StaticFiles(directory="api/static"), name="static")

@app.on_event("startup")
async def startup():
    await init()

app.include_router(main)
app.include_router(NN01)
app.include_router(testrouter)
