import os
import pandas as pd

from .connection_sync import init, engine
from .models import __all__ as models



def migration():
    init()
    with engine.connect() as conn:
        for model in models:
            table_name = model.__tablename__
            path = os.path.realpath(os.path.join(__file__, "..", "..", "storage", "csv", f"{table_name}.csv"))
            try: ext = os.path.splitext(path)[1]
            except: ext = ".csv"
            try:
                df = pd.read_json(path) if ext == ".json" else pd.read_csv(path)
                df.columns = list(map(lambda x: x.name, model.__table__.columns))[1:]
                df.to_sql(
                    con=conn,
                    name=table_name,
                    if_exists="append",
                    index=False,
                )
                print(f"Success {table_name}")
            except Exception as e:
                print(f"Error: {e}")
