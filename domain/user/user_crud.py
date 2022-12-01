import datetime

from sqlalchemy.orm import Session

from domain.user.user_schema import UserCreate
from models import CommonUser


def create_user(db: Session, user_create: UserCreate):
    db_user = CommonUser(username=user_create.username,
                         password=user_create.password1,
                         name=user_create.name,
                         student_id=user_create.student_id,
                         permission=user_create.permission,
                         create_date=datetime.datetime.now())
    db.add(db_user)
    db.commit()


def get_user(db: Session, username: str):
    return db.query(CommonUser).filter(CommonUser.username == username).first()
