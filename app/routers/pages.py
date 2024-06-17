"""
Holds endpoints for HTML pages 
"""

import os

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
current_dir = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory=f"{current_dir}/../views")


@router.get("/", response_class=HTMLResponse)
def index():
    return templates.TemplateResponse(name="index.html")
