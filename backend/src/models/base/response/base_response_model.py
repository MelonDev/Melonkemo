import datetime
from typing import Any
import orjson

from fastapi import Response

from src.tools.converters.datetime_converter import current_datetime_with_timezone


class BaseResponseModel(Response):
    media_type = "application/json"
    timestamp: datetime

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps({"timestamp": current_datetime_with_timezone(), "data": content},
                            option=orjson.OPT_INDENT_2)
