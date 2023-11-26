from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.main import core_api, redirect_api


def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


def include_main_router(root):
    root.include_router(core_api.router, tags=["Core"])
    root.include_router(redirect_api.router, tags=["Redirect"])



# def configure_application(root):
#     root.mount("/v1/melonkemo", melonkemo_app)


def configure_app():
    root = FastAPI(title="Melonkemo", version="ทดสอบ")
    include_main_router(root)
    configure_cors(root)

    # configure_application(root)

    return root
