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


@router.get("/user/{username}", status_code=status.HTTP_200_OK)
def get_user_visits_booth(username: str = Path(title="user name"), db: Session = Depends(get_db)):
    result = visits_crud.get_user_visits_booth(db, username)
    return result


@router.get("/booth/{booth_id}", status_code=status.HTTP_200_OK)
def get_booth_visits(booth_id: int = Path(title="booth id"), db: Session = Depends(get_db)):
    _result = visits_crud.get_user_visit(db, booth_id)
    if _result:
        return _result
    else:
        return False


@router.post("/")
def create_visits(visit_create: visits_schema.VisitCreate, db: Session = Depends(get_db)):
    visits_crud.create_visit(db, visit_create)


@router.put("/{visit_id}")
def update_end_time(visit_id: int = Path(title="visit id"), db: Session = Depends(get_db)):
    visits_crud.update_end_time(db, visit_id)


@router.get("/recent/{booth_id}", status_code=status.HTTP_200_OK)
def get_recent_visit_user_num(booth_id: int = Path(title="booth id"), db: Session = Depends(get_db)):
    return {"recent_visit_user_num": visits_crud.get_recent_booth_visit_user_number(db, booth_id)}
    #return {"recent_visit_user_num": 7}
