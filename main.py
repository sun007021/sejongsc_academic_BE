from fastapi import FastAPI, Query #import fastapi framework
from typing import Union

from domain.user import user_router

app = FastAPI()


app.include_router(user_router.router)