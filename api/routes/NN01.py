from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse, JSONResponse
from sqlalchemy import select
from datetime import datetime
import random, asyncio, json

from db import engine, Session
from db.models import TestModel

random.seed()
templates = Jinja2Templates(directory="api/templates")



NN01 = APIRouter(
    prefix="/NN01",
    tags=["NN01"],
)

@NN01.get("/")
async def NN01_Home(req: Request):
    return templates.TemplateResponse("NN01_home.html", {"request": req})

async def generate_random_data():
    while True:
        data = json.dumps({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "value": random.random() * 100,
        })
        yield f"data: {data}\n\n"
        await asyncio.sleep(1)

@NN01.get("/fakeStream")
async def NN01_fakeStream(req: Request):
    res = StreamingResponse(generate_random_data(), media_type="text/event-stream")
    res.headers["Cache-Control"] = "no-cache"
    res.headers["X-Accel-Buffering"] = "no"
    return res
