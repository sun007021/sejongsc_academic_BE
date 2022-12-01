import datetime

from sqlalchemy.orm import Session

from domain.user import user_crud
from domain.visits import visits_schema
from models import Visit


def get_user_visit(db: Session, booth_id: int):

    visit_list = db.query(Visit).filter(Visit.booth_id == booth_id).all()
    if visit_list:
        return visit_list

    else:
        return False

def create_visit(db: Session, visit_create: visits_schema.VisitCreate):
    db_visit = Visit(
        user_id=visit_create.user_id,
        booth_id=visit_create.booth_id,
        start_time=datetime.datetime.now(),
        end_time=datetime.datetime.now()
    )
    db.add(db_visit)
    db.commit()
