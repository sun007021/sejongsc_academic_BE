from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.otp import otp_crud, otp_schema, otp_util
from domain.user import user_util, user_crud
from domain.visits import visits_crud

router = APIRouter(
    prefix="/api/otp",
)


@router.get("/key", status_code=status.HTTP_200_OK)
def get_opt_key(username: str, db: Session = Depends(get_db)):
    otp_key = otp_crud.get_otp_key(db, username)
    server_otppass = otp_util.get_otppass(otp_key)
    return {"key": otp_key, "server_otppass": server_otppass}


@router.post("/auth")
def otp_pass_auth(user: otp_schema.OTPAuthForm, db: Session = Depends(get_db)):
    username = user.username
    otp_key = otp_crud.get_otp_key(db, username)
    server_otppass = otp_util.get_otppass(otp_key)

    if user.otppass == server_otppass:
        db_user = user_crud.get_user(db, username)
        permission = db_user.permission
        booth_id = user.booth_id
        visits_crud.create_visit(db, username, booth_id)
        return {"permission": permission}
    else:
        return {"permission": 0}
