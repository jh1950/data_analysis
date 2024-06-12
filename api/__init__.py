import uvicorn, os
from dotenv import load_dotenv

from .server import app as server
from .client import run as client

load_dotenv()



host = os.getenv("HOST") or "127.0.0.1"
port = int(os.getenv("PORT") or 8000)

def run(app="app:app", *args, **kwargs):
    if app == "client":
        client(
            *args,
            host=host,
            port=port,
        )
    else:
        uvicorn.run(
            app,
            host=host,
            port=port,
            reload=str(os.getenv("RELOAD") or os.getenv("DEBUG")).lower() == "true",
        )
