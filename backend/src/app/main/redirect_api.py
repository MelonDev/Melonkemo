from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from starlette.responses import RedirectResponse

from src.custom.exceptions.redirect.base_redirect_exception import BaseRedirectException
from src.custom.exceptions.redirect.redirect_exception import PathRedirectNotFoundException, \
    PathRedirectExpiredException
from src.custom.exceptions.share.unkhown_exception import UnknownException
from src.database.database_config import meloncloud_session
from src.database.redirect.redirect_database import RedirectDatabase
from src.models.response.base_response_model import BaseResponseModel

router = APIRouter()


@router.get("/shared/{path}", response_class=BaseResponseModel, include_in_schema=True)
async def shared(path: str, session: Session = Depends(meloncloud_session)):
    try:
        return RedirectResponse(url=_get_url(session, path).url)
    except BaseRedirectException as ex:
        return ex.response()
    except Exception as e:
        return UnknownException(e)


@router.get("/redirect/{path}", response_class=BaseResponseModel, include_in_schema=True)
async def check_redirect_path(path: str, session: Session = Depends(meloncloud_session)):
    try:
        return _get_url(session, path).serialize
    except BaseRedirectException as ex:
        return ex.response()
    except Exception as e:
        return UnknownException(e)


def _get_url(session, path):
    statement = select(RedirectDatabase).where(RedirectDatabase.path == path)
    redirect_target = session.exec(statement).first()
    if redirect_target is None: raise PathRedirectNotFoundException(path)
    if redirect_target.active is False: raise PathRedirectExpiredException(path)
    return redirect_target
