from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import engine
from db.models import Base
from .routes import testrouter
from .routes import NN01



app = FastAPI()
app.mount("/static", StaticFiles(directory="api/static"), name="static")

@app.on_event("startup")
async def startup():
    # https://stackoverflow.com/questions/68230481/sqlalchemy-attributeerror-asyncengine-object-has-no-attribute-run-ddl-visit
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
def shutdown():
    pass

@app.get("/")
def index():
    return {
        "Python": "Framework",
    }

app.include_router(NN01)
