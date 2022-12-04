import datetime

from sqlalchemy.orm import Session

from domain.otp import otp_util
from domain.user.user_schema import UserCreate
from models import CommonUser, AdminUser


def create_user(db: Session, user_create: UserCreate):
    if get_user_num_by_student_id(db, user_create.student_id) > 3:
        return False

    db_user = CommonUser(username=user_create.username,
                         password=user_create.password1,
                         name=user_create.name,
                         student_id=user_create.student_id,
                         otp_key=otp_util.create_otp_key(),
                         permission=user_create.permission,
                         create_date=datetime.datetime.now())
    db.add(db_user)
    db.commit()


def get_user(db: Session, username: str) -> CommonUser:
    return db.query(CommonUser).filter(CommonUser.username == username).first()

def get_user_num_by_student_id(db: Session, student_id: str):
    return db.query(CommonUser).filter(CommonUser.student_id==student_id).count()

def get_admin(db: Session, username: str) -> AdminUser:
    return db.query(AdminUser).filter(AdminUser.username == username).first()
