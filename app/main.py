"""
Creates an ASGI app
"""

import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.api import router as api_router
from routers.pages import router as pages_router


def include_routers(app: FastAPI) -> None:
    app.include_router(pages_router)
    app.include_router(api_router)


def create_app() -> FastAPI:
    app = FastAPI()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    app.mount(
        "/resources", StaticFiles(directory=f"{current_dir}/dist"), name="resources"
    )
    app.mount(
        "/static",
        StaticFiles(directory=f"{current_dir}/resources/static"),
        name="static",
    )

    include_routers(app)
    return app


app = create_app()
