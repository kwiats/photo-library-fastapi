from fastapi import FastAPI

from src.configs import database
from src.routers.v1.auth_router import AuthRouter

app = FastAPI()
database.init()


app.include_router(AuthRouter, prefix="/api/v1/")
