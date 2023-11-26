from typing import Any

from src.models.response.base_response_model import BaseResponseModel


class ErrorResponseModel(BaseResponseModel):
    code = 400

    def __init__(self, content: str = None, code: int = None):
        super().__init__(content=content, status_code=code if code is not None else self.code)

    def response(self) -> BaseResponseModel: return ErrorResponseModel()

    def render(self, content: Any) -> bytes:
        dictContent: dict = self.base(content=None)
        dictContent['error'] = {
            'code': self.status_code,
            'message': content
        }
        return self.dump(content=dictContent)
