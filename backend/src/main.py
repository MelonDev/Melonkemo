import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import select, Session

from src.database.database_config import meloncloud_session
from src.database.poc.meloncloud_twitter_database import MelonCloudTwitterDatabase
from src.models.base.response.base_response_model import BaseResponseModel

app = FastAPI()


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/connect", response_class=BaseResponseModel, include_in_schema=True)
async def connect():
    return "Connected!"


@app.get("/count", response_class=BaseResponseModel, include_in_schema=True)
async def count(session: Session = Depends(meloncloud_session)):
    statement = select(MelonCloudTwitterDatabase)
    tweets = session.exec(statement).all()
    return len(tweets)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=False)
