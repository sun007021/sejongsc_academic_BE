from fastapi import FastAPI, Query #import fastapi framework
from typing import Union

from domain.otp import otp_router
from domain.user import user_router

app = FastAPI()


app.include_router(user_router.router)
app.include_router(otp_router.router)