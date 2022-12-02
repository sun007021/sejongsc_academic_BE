from datetime import timedelta, datetime

from jose import jwt
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_crud, user_schema, user_util
from domain.user.user_schema import UserAuth, UserCreate

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"

router = APIRouter(
    prefix="/api/user",
)


@router.post("/", status_code=status.HTTP_200_OK)
def user_register(_user_register: UserCreate, db: Session = Depends(get_db)):
    user_crud.create_user(db=db, user_create=_user_register)


@router.post("/authsejong", status_code=status.HTTP_200_OK)
def user_auth_sejong(userAuth: UserAuth):
    return {"student_id": user_util.auth_sejong_univ(userAuth.student_id, userAuth.password)}


@router.post("/login", response_model=user_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    # check username and password
    user = user_crud.get_user(db, form_data.username)
    if not user or not (user.password == form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # make access token
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    otp_key = user.otp_key

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
        "otp_key": otp_key
    }


@router.post("/admin/login", response_model=user_schema.TokenAdmin)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):
    # check username and password
    user = user_crud.get_admin(db, form_data.username)
    if not user or not (user.password == form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # make access token
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
        "booth_id": user.booth_id
    }
