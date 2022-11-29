from pydantic import BaseModel, validator


class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    student_id: str
    name: str
    permission: int

    @validator('student_id, permission')
    def check_permission_student_id(cls, v, values):  # 재학생, 지인의 경우 student_id가 존재하는지 검사
        if values['permission'] == 1 or values['permission'] == 2:
            if values['student_id'] is None:
                return False
            elif values['studend_id'] is not None:
                return True

        else:  # permission==3 외부인인경우
            return True
