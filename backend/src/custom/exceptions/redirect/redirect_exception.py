from src.custom.exceptions.redirect.base_redirect_exception import BaseRedirectException


class PathRedirectNotFoundException(BaseRedirectException):
    code = 404

    def __init__(self, path: str):
        self.message = f"ไม่พบเส้นทาง /{path} ที่คุณต้องการเรียกใช้"

class PathRedirectExpiredException(BaseRedirectException):
    code = 403

    def __init__(self, path: str):
        self.message = f"เส้นทาง /{path} ที่คุณต้องการเรียกใช้ถูกปิดการใช้งานแล้ว"
