from sejong_univ_auth import auth, PortalSSOToken


def auth_sejong_univ(student_id: str, password: str):
    result = auth(id=student_id, password=password, methods=PortalSSOToken)
    if result.is_auth:
        return student_id
    return None
