from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from hotel.db.models import Base
from sqlalchemy.orm import sessionmaker

engine: Engine = None
DBSession = sessionmaker()

def init_db(file: str):
    engine = create_engine(file, echo=True)
    Base.metadata.bind = engine
    DBSession.configure(bind=engine)
    