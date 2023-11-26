from src.models.response.error_response_model import ErrorResponseModel


class BaseRedirectException(Exception):
    message: str = "เกิดข้อผิดพลาด"
    code: int = 400

    def error(self) -> str: return self.message

    def response(self): return ErrorResponseModel(content=self.message,code=self.code)