"""
Creates an ASGI app
"""

import os

from fastapi import FastAPI, Request
from fastapi.exception_handlers import \
    http_exception_handler as original_http_exception_handler
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from routers.api import router as api_router
from routers.pages import router as pages_router
from starlette.exceptions import HTTPException as StarletteHTTPException
from template_engine import templates


def include_routers(app: FastAPI) -> None:
    app.include_router(pages_router)
    app.include_router(api_router)


def mount_dirs(app: FastAPI) -> None:
    """
    Mounts all file directories to be served
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    app.mount(
        "/css",
        StaticFiles(directory=f"{current_dir}/dist/css", check_dir=False),
        name="styles",
    )
    app.mount("/js", StaticFiles(directory=f"{current_dir}/dist/js"), name="scripts")
    app.mount(
        "/static",
        StaticFiles(directory=f"{current_dir}/resources/static"),
        name="static",
    )


def create_app() -> FastAPI:
    app = FastAPI()

    mount_dirs(app)
    include_routers(app)
    return app


app = create_app()


@app.exception_handler(StarletteHTTPException)
async def html_exception_handler(request: Request, exc: StarletteHTTPException):
    endpoint_parts = request.scope["path"].split("/", 2)
    if "api" in endpoint_parts:
        return await original_http_exception_handler(request, exc)

    context = {
        "error": exc,
    }
    return templates.TemplateResponse(
        request=request, name="error.html", context=context
    )
