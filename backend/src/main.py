import uvicorn
from fastapi import FastAPI, Depends
from src.configure import configure_app
from src.models.response.base_response_model import BaseResponseModel


app: FastAPI = configure_app()


@app.get("/")
def main():
    return {"Hello": "World"}


@app.get("/connect", response_class=BaseResponseModel, include_in_schema=True)
async def connect():
    return "Connected!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=False)
