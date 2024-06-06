from sqlalchemy import Column, Integer, String

from .base import Base



class TestModel(Base):
    __tablename__ = "TestModel"

    id    = Column(Integer, primary_key=True)
    name  = Column(String(255), unique=True)
    age   = Column(Integer)
