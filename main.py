from fastapi import FastAPI
from src.routers import admin
from src.routers import users

app = FastAPI()


@app.get('/')
def root():
    return {"everyThing is safe <3"}


# Imports Routers
app.include_router(admin.router)
app.include_router(users.router)
