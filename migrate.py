import asyncio
import pandas as pd

from db import engine
from db.models import CSCIDS2017_BALANCED_ATTK, CSCIDS2017_FRI_PM_PORTSCAN



models = {
    # db model: Filename,
    CSCIDS2017_BALANCED_ATTK: "web_attacks_balanced",
    CSCIDS2017_FRI_PM_PORTSCAN: "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX",
}

async def migration():
    async with engine.begin() as conn:
        for model, file in models.items():
            df = pd.read_csv(f'./csv/{file}.csv')
            df.columns = list(map(lambda x: x.name, model.__table__.columns))[1:]
            table_name = model.__tablename__
            try:
                await conn.run_sync(lambda con: df.to_sql(
                    con=con,
                    name=table_name,
                    if_exists="append",
                ))
                print(f"Success {table_name}({table_name})")
            except Exception as e:
                print(f"Error: {e}")



if __name__=="__main__":
    asyncio.run(migration())
