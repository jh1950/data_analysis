import os
from dotenv import load_dotenv

from .models import Base
from .connection import createEngine, createSession



load_dotenv()



def get_session():
    with Session() as session:
        try:
            yield session
            session.commmit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

def init():
    Base.metadata.create_all(engine)


engine = createEngine(os.getenv("DB_ENGINE"), sync=True)
Session = createSession(engine, sync=True)
