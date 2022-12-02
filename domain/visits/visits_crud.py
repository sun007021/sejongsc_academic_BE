import datetime

from sqlalchemy.orm import Session

from domain.user import user_crud
from domain.visits import visits_schema
from models import Visit, CommonUser

def get_visit(db: Session, visit_id: int):
    db_visit = db.query(Visit).filter(Visit.id == visit_id).first()
    return db_visit

def get_user_visit(db: Session, booth_id: int): #해당 부스 방문 정보 리스트 반환(user_id, booth_id, start_time, end_time)

    visit_list = db.query(Visit).filter(Visit.booth_id == booth_id).all()
    if visit_list:
        return visit_list
    else:
        return False

def create_visit(db: Session, username: str, booth_id: int):
    user_id = db.query(CommonUser).filter(CommonUser.username == username).first().id
    db_visit = Visit(
        user_id=user_id,
        booth_id=booth_id,
        start_time=datetime.datetime.now(),
    )
    db.add(db_visit)
    db.commit()

def update_end_time(db: Session, visit_id:int):
    db_visit = get_visit(db, visit_id)
    db_visit.end_time = datetime.datetime.now()
    db.add(db_visit)
    db.commit()