import os
from dotenv import load_dotenv

from .models import Base
from .connection import createEngine, createSession



load_dotenv()



async def get_session():
    async with Session() as session:
        try:
            yield session
            await session.commmit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()

async def init():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        raise e


engine = createEngine(os.getenv("DB_ENGINE"))
Session = createSession(engine)
