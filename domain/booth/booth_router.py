import datetime

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.booth import booth_crud
from domain.booth.booth_crud import create_booth_to
from domain.booth.booth_schema import BoothCreate, BoothUpdate
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
    create_booth_to(booth_create, db)

@router.put("/{booth_id}")
def update_booth_info(booth_info: BoothUpdate, booth_id: int = Path(title="booth id"),db: Session = Depends(get_db)):
    booth_crud.update_booth(booth_info, db, booth_id)
