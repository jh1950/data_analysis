import random, asyncio, json, logging
from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse, JSONResponse
from sqlalchemy import select
from datetime import datetime

from ml import ML
from db import engine, Session
from db.models import TestModel
from ..models import DataInput, PredictOutput

random.seed()
logger = logging.getLogger("NN01")
templates = Jinja2Templates(directory="api/templates")



NN01 = APIRouter(
    prefix="/NN01",
    tags=["NN01"],
    # lifespan=lifespan,
)

ml_models = {}
@NN01.on_event("startup")
def NN01_startup():
    ml_models["predict"] = ML("NN01").predict
    ml_models["train"] = ML("NN01").train
@NN01.on_event("shutdown")
def NN01_shutdown():
    ml_models.clear()



@NN01.get("/")
async def NN01_Home(req: Request):
    return templates.TemplateResponse("NN01_home.html", {"request": req})

async def generate_random_data(req: Request):
    logger.info("Client %s connected", req.client.host)
    while True:
        data = json.dumps({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "value": random.random() * 100,
        })
        yield f"data: {data}\n\n"
        await asyncio.sleep(1)

@NN01.get("/fakeStream")
async def NN01_fakeStream(req: Request):
    res = StreamingResponse(generate_random_data(req), media_type="text/event-stream")
    res.headers["Cache-Control"] = "no-cache"
    res.headers["X-Accel-Buffering"] = "no"
    return res

@NN01.post("/predict", tags=['NN01'], response_model=PredictOutput)
async def NN01_predict(data: DataInput, req: Request):
    logger.info("Client %s connected for prediction result", req.client.host)
    result =  ml_models["predict"](data.x)
    return {'prediction' : result}

@NN01.post("/train", tags=['NN01'], response_model=PredictOutput)
async def NN01_train(req: Request):
    logger.info("Client %s connected for train", req.client.host)
    result =  ml_models["train"]()
    return {'prediction' : result}
