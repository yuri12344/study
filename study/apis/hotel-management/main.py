from fastapi import FastAPI
from hotel.routers import rooms, customers
from hotel.db.engine import init_db

app = FastAPI()

DB_FILE = "sqlite:///hotel.db"

@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)  

@app.get("/")
def read_root():
    return "This is the root of the API"

app.include_router(rooms.router)
app.include_router(customers.router)