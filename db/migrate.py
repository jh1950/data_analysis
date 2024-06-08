import os, asyncio
import pandas as pd

from .connection import init, engine
from .models import __all__ as models



async def migration():
    await init()
    async with engine.begin() as conn:
        for model in models:
            table_name = model.__tablename__
            path = os.path.realpath(os.path.join(__file__, "..", "..", "storage", "csv", f"{table_name}.csv"))
            try: ext = os.path.splitext(path)[1]
            except: ext = ".csv"
            try:
                df = pd.read_json(path) if ext == ".json" else pd.read_csv(path)
                df.columns = list(map(lambda x: x.name, model.__table__.columns))[1:]
                await conn.run_sync(lambda con: df.to_sql(
                    con=con,
                    name=table_name,
                    if_exists="append",
                    index=False,
                ))
                print(f"Success {table_name}")
            except Exception as e:
                print(f"Error: {e}")
