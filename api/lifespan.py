from fastapi import FastAPI
from contextlib import asynccontextmanager

from db import engine
from db.models import Base



@asynccontextmanager
async def lifespan(app: FastAPI):
    await main_startup()
    yield
    await main_shutdown()

async def main_startup():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        raise e

async def main_shutdown():
    pass
