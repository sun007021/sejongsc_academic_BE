import hashlib

import pyotp


def create_otp_key():
    rand_key = pyotp.random_base32()
    return rand_key


# otp 생성하는 함수
def get_otppass(otpkey):
    otp = pyotp.TOTP(otpkey, digest=hashlib.sha256)
    return otp.now()
