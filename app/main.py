"""Creates an ASGI app"""

import os

from dependencies import get_template_engine
from fastapi import FastAPI, Request
from fastapi.exception_handlers import (
    http_exception_handler as original_http_exception_handler,
)
from fastapi.staticfiles import StaticFiles
from routers.api import router as api_router
from routers.pages import router as pages_router
from starlette.exceptions import HTTPException as StarletteHTTPException


def include_routers(app_inst: FastAPI) -> None:
    """Registers all app routers"""
    app_inst.include_router(pages_router)
    app_inst.include_router(api_router)


def mount_dirs(app_inst: FastAPI) -> None:
    """Mounts all file directories to be served"""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    app_inst.mount(
        "/css",
        StaticFiles(directory=f"{current_dir}/dist/css", check_dir=False),
        name="styles",
    )
    app_inst.mount(
        "/js", StaticFiles(directory=f"{current_dir}/dist/js"), name="scripts"
    )
    app_inst.mount(
        "/static",
        StaticFiles(directory=f"{current_dir}/resources/static"),
        name="static",
    )


def create_app() -> FastAPI:
    """Retrieves an ASGI app"""
    app_inst = FastAPI()

    mount_dirs(app_inst)
    include_routers(app_inst)
    return app_inst


app = create_app()


@app.exception_handler(StarletteHTTPException)
@app.exception_handler(Exception)
async def html_exception_handler(request: Request, exc):
    """
    Error handler that decides if either an HTML or JSON response should be rendered
    """
    endpoint_parts = request.scope["path"].split("/", 2)
    if "api" in endpoint_parts:
        return await original_http_exception_handler(request, exc)

    # Dependencies don't work in exception handlers
    template_engine = await get_template_engine(request)
    return template_engine.render(name="error.html", error=exc)
