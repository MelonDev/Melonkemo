from sqlmodel import SQLModel, Field, ARRAY, Column, Text
from datetime import datetime
from typing import List, Optional

from src.tools.converters.datetime_converter import current_datetime_with_timezone


class MelonCloudTwitterDatabase(SQLModel, table=True):
    __tablename__ = "MelonCloud_Twitter_Database"
    __bind_key__ = 'meloncloud'

    id: str = Field(primary_key=True, unique=True, nullable=False)
    tweeted_at: datetime = Field(default_factory=current_datetime_with_timezone(), nullable=False)
    stored_at: datetime = Field(default_factory=current_datetime_with_timezone(), nullable=False)
    message: Optional[str] = Field(nullable=True)
    account_id: str = Field(nullable=False)
    hashtags: Optional[List[str]] = Field(sa_column=Column(ARRAY(Text), nullable=True))
    mentions: Optional[List[str]] = Field(sa_column=Column(ARRAY(Text), nullable=True))
    photos: Optional[List[str]] = Field(sa_column=Column(ARRAY(Text), nullable=True))
    type: Optional[str] = Field(nullable=True)
    thumbnail: Optional[str] = Field(nullable=True)
    videos: Optional[List[str]] = Field(sa_column=Column(ARRAY(Text), nullable=True))
    language: Optional[str] = Field(nullable=True)
    urls: Optional[List[str]] = Field(sa_column=Column(ARRAY(Text), nullable=True))
    event: Optional[str] = Field(nullable=True)
    deleted: Optional[bool] = Field(default=True, nullable=True)
    memories: Optional[bool] = Field(default=True, nullable=True)
