from src.custom.exceptions.login.base_login_exception import BaseLoginException


class IncorrectLoginException(BaseLoginException):
    message = "ไม่ถูกต้อง"
    code = 401
