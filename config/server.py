from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("HOST") or "127.0.0.1"
port = int(os.getenv("PORT") or 8000)
reload = str(os.getenv("RELOAD") or os.getenv("DEBUG")).lower() == "true"
