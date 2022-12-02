from fastapi import FastAPI, Query  # import fastapi framework
from typing import Union

from domain.booth import booth_router
from domain.otp import otp_router
from domain.user import user_router
from domain.visits import visits_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(otp_router.router)
app.include_router(visits_router.router)
app.include_router(booth_router.router)