from src.custom.exceptions.login.base_login_exception import BaseLoginException
from src.models.response.error_response_model import ErrorResponseModel


class IncorrectLoginException(BaseLoginException):
    message = "ไม่ถูกต้อง"

    def response(self): return ErrorResponseModel(content=self.message, code=401)
