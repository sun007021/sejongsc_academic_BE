from typing import Union

from pydantic import BaseModel, validator


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str
    otp_key: str

class TokenAdmin(BaseModel):
    access_token: str
    token_type: str
    username: str
    booth_id: int
class UserAuth(BaseModel):  # sejong 확인
    student_id: str
    password: str


class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    student_id: Union[str, None] = None
    name: str
    permission: int

    # @validator('student_id, permission')
    # def check_permission_student_id(cls, values):  # 재학생, 지인의 경우 student_id가 존재하는지 검사
    #     if values['permission'] == 1 or values['permission'] == 2:
    #         if values['student_id'] is None:
    #             return False
    #         elif values['studend_id'] is not None:
    #             return True
    #
    #     else:  # permission==3 외부인인경우
    #         return True
