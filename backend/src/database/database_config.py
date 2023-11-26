from sqlmodel import create_engine, Session
from decouple import config

meloncloud_engine = create_engine(config('MELONCLOUD_DATABASE', default=None))


def meloncloud_session():
    with Session(meloncloud_engine) as session:
        yield session
