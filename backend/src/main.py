import uvicorn
from fastapi import FastAPI

from src.models.base.response.base_response_model import BaseResponseModel

app = FastAPI()


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/connect", response_class=BaseResponseModel, include_in_schema=True)
async def connect():
    return BaseResponseModel("Connected!")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=False)
