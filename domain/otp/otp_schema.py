from typing import Union

from pydantic import BaseModel, validator


class OTPAuthForm(BaseModel):
    username: str
    otppass: str