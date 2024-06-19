"""
Holds endpoints for HTML pages 
"""

import json
import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
current_dir = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory=f"{current_dir}/../views")


def bundle_urls_for(name: str) -> list[str]:
    bundles = []
    if "bundle_entrypoints" not in templates.env.globals:
        with open("dist/entrypoints.json", "rb") as file:
            templates.env.globals.update(bundle_entrypoints=json.load(file))

    entrypoints = templates.env.globals["bundle_entrypoints"]
    return entrypoints.get(name, {}).get("js", [])


templates.env.globals.update(bundle_urls_for=bundle_urls_for)


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
