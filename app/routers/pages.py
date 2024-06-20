"""
Holds endpoints for HTML pages 
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from template_engine import templates

router = APIRouter(tags=["Pages"], default_response_class=HTMLResponse)


@router.get("/")
def homepage(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
