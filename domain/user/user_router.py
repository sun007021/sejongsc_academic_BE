from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status
from domain.user import user_crud, user_schema, user_util

router = APIRouter(
    prefix="/api/user",
)


@router.post("/authSejong", status_code=status.HTTP_200_OK)
def user_auth_sejong(student_id: str, password: str):
    return {"student_id": user_util.auth_sejong_univ(student_id, password)}
