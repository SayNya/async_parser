from fastapi import FastAPI

from src.api.views.router import api_router
from src.containers.container import Container

tags_metadata = [
    {
        'name': 'weather',
        'description': 'Operations with weather.',
    },
]


def create_app() -> FastAPI:
    container = Container()

    application = FastAPI(openapi_tags=tags_metadata)
    application.container = container
    application.include_router(api_router)

    return application


app = create_app()
