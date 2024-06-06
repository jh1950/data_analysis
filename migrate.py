import os, asyncio
import pandas as pd

from db import engine
from db.models import TestModel



models = {
    # db model: path,
    TestModel: "csv/test.csv",
}

async def migration():
    async with engine.begin() as conn:
        for model, path in models.items():
            path = os.path.realpath(os.path.join(__file__, "..", path))
            try:
                ext = os.path.splitext(path)[1]
            except:
                ext = ".csv"
            df = pd.read_json(path) if ext == ".json" else pd.read_csv(path)
            df.columns = list(map(lambda x: x.name, model.__table__.columns))[1:]
            table_name = model.__tablename__
            try:
                await conn.run_sync(lambda con: df.to_sql(
                    con=con,
                    name=table_name,
                    if_exists="append",
                    index=False,
                ))
                print(f"Success {table_name}({table_name})")
            except Exception as e:
                print(f"Error: {e}")



if __name__=="__main__":
    asyncio.run(migration())
