from sqlalchemy.orm import Session

from domain.user import user_crud


def get_otp_key(db: Session, username: str):
    db_user = user_crud.get_user(db, username)
    if db_user:
        return db_user.otp_key
    else:
        return False