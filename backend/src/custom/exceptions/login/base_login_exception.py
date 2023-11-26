from src.models.response.base_response_model import BaseResponseModel


class BaseLoginException(Exception):
    message: str = "เกิดข้อผิดพลาด"

    def error(self) -> str: return self.message

    def response(self) -> BaseResponseModel: return BaseResponseModel(content=self.message)
