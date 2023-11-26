from fastapi import APIRouter, Depends
from sqlmodel import select, Session, SQLModel

from src.custom.exceptions.login.base_login_exception import BaseLoginException
from src.custom.exceptions.login.login_exception import IncorrectLoginException
from src.database.database_config import meloncloud_session, meloncloud_engine
from src.database.poc.meloncloud_twitter_database import MelonCloudTwitterDatabase
from src.models.response.base_response_model import BaseResponseModel

router = APIRouter()

@router.get("/exception", response_class=BaseResponseModel, include_in_schema=True)
async def exception(name: str):
    try:
        print("Exception trigger")
        if name != "Admin":
            raise IncorrectLoginException()
        return "Hi Admin!"
    except BaseLoginException as ex:
        return ex.response()


@router.get("/count", response_class=BaseResponseModel, include_in_schema=True)
async def count(session: Session = Depends(meloncloud_session)):
    statement = select(MelonCloudTwitterDatabase)
    tweets = session.exec(statement).all()
    return len(tweets)


@router.get("/create_database", response_class=BaseResponseModel, include_in_schema=False)
async def create_database():
    # RedirectDatabase.__table__.create(meloncloud_engine)
    return "create_database"


