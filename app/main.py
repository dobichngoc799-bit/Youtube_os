from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import APP_NAME, APP_VERSION
from app.database import Base, engine
from app.routers import dashboard, projects
from app import models

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(dashboard.router)
app.include_router(projects.router)