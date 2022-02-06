from fastapi import FastAPI

from src.api.views.router import api_router


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router)
    return application


app = create_app()
