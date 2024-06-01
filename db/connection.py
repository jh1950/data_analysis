import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker



load_dotenv()



def createEngine(dbms):
    _dbms = "mysql" if dbms.lower() == "mariadb" else dbms.lower()
    default_port = {
        "mysql": 3306,
        "postgresql": 5432,
    }
    engine = create_async_engine({
        "sqlite": "sqlite+aiosqlite:///%(filename)s",
        "mysql": "mysql+aiomysql://%(user)s:%(pass)s@%(host)s:%(port)s/%(name)s",
        "postgresql": "postgresql+asyncpg://%(user)s:%(pass)s@%(host)s:%(port)s/%(name)s",
    }[_dbms] %{
        "user": quote_plus(os.getenv("DB_USER") or os.getenv("USER")),
        "pass": quote_plus(os.getenv("DB_PASS")),
        "host": os.getenv("DB_HOST") or "localhost",
        "port": os.getenv("DB_PORT") or default_port.get(_dbms),
        "name": quote_plus(os.getenv("DB_NAME") or "fastapi"),
        "filename": os.getenv("DB_PATH") or "./test.db",
    }, echo=True)
    Session = async_sessionmaker(engine, autocommit=False, autoflush=False, sync_session_class=sessionmaker())
    return engine, Session

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



engine, Session = createEngine(os.getenv("DB_ENGINE") or "sqlite")
