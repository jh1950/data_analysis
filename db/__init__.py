from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import db
from .models import Base as BaseModel



engine = create_async_engine(db["url"])
Session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, sync_session_class=sessionmaker())
