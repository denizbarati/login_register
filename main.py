from fastapi import FastAPI
from src.routers import admin
from src.routers import users
from src.db import models
from src.db.database import engine

app = FastAPI()


@app.get('/')
def root():
    return {"everyThing is safe <3"}


# Imports Routers
app.include_router(admin.router)
app.include_router(users.router)

# For Create Table Data
models.Base.metadata.create_all(engine)
