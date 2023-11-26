from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field
import uuid

from src.tools.converters.datetime_converter import current_datetime_with_timezone


class RedirectDatabase(SQLModel, table=True):
    __tablename__ = "Redirect_Database"
    __bind_key__ = 'meloncloud'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, unique=True, nullable=False)
    created_at: datetime = Field(default_factory=current_datetime_with_timezone(), nullable=False)
    updated_at: datetime = Field(default_factory=current_datetime_with_timezone(), nullable=False)
    path: str = Field(nullable=False, unique=True)
    url: str = Field(nullable=False)
    active: bool = Field(default=True, nullable=False)

    @property
    def serialize(self):
        return {
            'path': f"/{self.path}",
            'url': self.url
        }
