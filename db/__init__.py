import asyncio
from .models import Base as BaseModel
from .connection import engine, Session, get_session



async def init():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.create_all)
    except Exception as e:
        raise e

asyncio.run(init())
