from fastapi import FastAPI
from app.routers import task
from app.database import engine, base
from app import models

base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(task.router)
