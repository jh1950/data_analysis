from dotenv import load_dotenv
import os

load_dotenv()



api = {
    "host": os.getenv("HOST", "127.0.0.1"),
    "port": int(os.getenv("PORT") or 8000),
    "reload": str(os.getenv("RELOAD") or os.getenv("DEBUG")).lower() == "true",
}

db = {
    "user": os.getenv("DB_USERNAME"),
    "pass": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT") or 3306),
    "db": os.getenv("DB_DATABASE"),
    "url": os.getenv("DATABASE_URL"),
}
