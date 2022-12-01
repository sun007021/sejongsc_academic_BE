import datetime

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.visits import visits_crud, visits_schema
from models import Visit

router = APIRouter(
    prefix="/api/visits",
)


@router.get("/booth/{booth_id}", response_model=list[visits_schema.Visits], status_code=status.HTTP_200_OK)
def get_booth_visits(booth_id: int = Path(title="booth id"), db: Session = Depends(get_db)):
    _result = visits_crud.get_user_visit(db, booth_id)
    return _result

@router.post("/")
def create_visits(visit_create:visits_schema.VisitCreate, db: Session = Depends(get_db)):
    visits_crud.create_visit(db,visit_create)


