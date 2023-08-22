from dataclasses import dataclass
from datetime import date
from fastapi import FastAPI

from hotel.db.engine import init_db, DBSession
from hotel.db.models import DBRoom

app = FastAPI()

DB_FILE = "sqlite:///hotel.db"

@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)  

@app.get("/")
def read_root():
    return "This is the root of the API"

@app.get("/rooms")
def read_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return rooms