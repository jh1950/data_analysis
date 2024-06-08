import uvicorn, os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import init
from .routes import main, NN01, testrouter

load_dotenv()



app = FastAPI()
app.mount("/static", StaticFiles(directory="api/static"), name="static")

@app.on_event("startup")
async def startup():
    await init()

app.include_router(main)
app.include_router(NN01)
app.include_router(testrouter)



def run(app="app:app"):
    uvicorn.run(
        app,
        host=os.getenv("HOST") or "127.0.0.1",
        port=int(os.getenv("PORT") or 8000),
        reload=str(os.getenv("RELOAD") or os.getenv("DEBUG")).lower() == "true",
    )
