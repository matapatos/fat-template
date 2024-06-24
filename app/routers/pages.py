"""
Holds endpoints for HTML pages 
"""

from dependencies import TemplateEngine
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["Pages"], default_response_class=HTMLResponse)


@router.get("/")
def homepage(template_engine: TemplateEngine):
    """Example of a page endpoint"""
    return template_engine.render(name="index.html")
