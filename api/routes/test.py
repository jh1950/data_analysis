from fastapi import APIRouter
from sqlalchemy import select

from db import engine, Session
from db.models import TestModel



testrouter = APIRouter(
    prefix="/test",
)

@testrouter.get("/select")
async def test_select():
    result = None

    async with Session() as session:
        result = await session.execute(select(TestModel))
        result = result.scalars().all()

    return {
        TestModel.__tablename__: result,
    }
