import datetime

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.booth import booth_crud
from domain.booth.booth_schema import BoothCreate
from domain.visits import visits_crud, visits_schema
from models import Visit

router = APIRouter(
    prefix="/api/booth",
)


@router.get("/", status_code=status.HTTP_200_OK)
def get_booth_list(db: Session = Depends(get_db)):
    result = booth_crud.get_booth_list(db)
    return result


@router.post("/", status_code=status.HTTP_200_OK)
def create_booth(booth_create: BoothCreate, db: Session = Depends(get_db)):
    booth_create(booth_create=booth_create, db=db)
