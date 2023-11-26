from src.models.response.error_response_model import ErrorResponseModel


class UnknownException(Exception):
    message: str = "เกิดข้อผิดพลาด"
    code: int = 400

    def error(self) -> str: return self.message

    def response(self, exception: Exception = None): return ErrorResponseModel(
        content=str(exception) if exception is not None else self.message, code=self.code)
