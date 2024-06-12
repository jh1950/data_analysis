import os, re
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy import create_engine as create_sync_engine
from sqlalchemy.orm import sessionmaker as sync_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker



load_dotenv()

def createEngine(dbms="sqlite", sync=False):
    _dbms = "mysql" if dbms.lower() == "mariadb" else dbms.lower()
    string = {
        "sqlite": "sqlite+aiosqlite:///%(filename)s",
        "mysql": "mysql+aiomysql://%(user)s:%(pass)s@%(host)s:%(port)s/%(name)s",
        "postgresql": "postgresql+asyncpg://%(user)s:%(pass)s@%(host)s:%(port)s/%(name)s",
    }[_dbms] %{
        "user": quote_plus(os.getenv("DB_USER") or os.getenv("USER")),
        "pass": quote_plus(os.getenv("DB_PASS")),
        "host": os.getenv("DB_HOST") or "localhost",
        "port": os.getenv("DB_PORT") or {
            "mysql": 3306,
            "postgresql": 5432,
        }.get(_dbms),
        "name": quote_plus(os.getenv("DB_NAME") or "fastapi"),
        "filename": os.getenv("DB_PATH") or "./test.db",
    }
    if sync:
        create_engine = create_sync_engine
        string = re.sub(r"\+[^:]+", "", string)
    else:
        create_engine = create_async_engine
    return create_engine(string, echo=True)

def createSession(engine, sync=False):
    sessionmaker = sync_sessionmaker if sync else async_sessionmaker
    return sessionmaker(engine, autocommit=False, autoflush=False)
