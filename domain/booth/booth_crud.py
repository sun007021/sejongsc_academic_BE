import datetime

from sqlalchemy import and_
from sqlalchemy.orm import Session

from domain.booth.booth_schema import BoothCreate
from models import Visit, Booth


def get_booth_list(db: Session):  # 해당 유저가 방문한 기록 중 endtime 존재하는 것들 반환
    visit_list = db.query(Booth).order_by(Booth.id).all()
    return visit_list


def create_booth_to(booth_create: BoothCreate, db: Session):
    db_booth = Booth(name=booth_create.name,
                     description=booth_create.description,
                     mapx=booth_create.mapx,
                     mapy=booth_create.mapy)
    db.add(db_booth)
    db.commit()


def update_booth(booth_info: BoothCreate, db: Session, booth_id: int):
    db_booth = db.query(Booth).filter(Booth.id == booth_id).first()
    db_booth.name = booth_info.name
    db_booth.description = booth_info.description

    db.add(db_booth)
    db.commit()
