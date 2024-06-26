"""Holds application dependencies. This is where you define the services to be used"""

from typing import Annotated

from configs import configs
from fastapi import Depends, Request
from services.template_engine.jinja import JinjaTemplateEngine
from services.template_engine.protocols import Renderable


async def get_template_engine(request: Request) -> Renderable:
    """
    Retrieves the template engine to be used to render HTML pages

    :param Request request: The current request being handled
    :return Renderable: The template engine to be used
    """
    return JinjaTemplateEngine(
        request=request,
        templates_dir=configs.views_dir,
        bundle_entrypoints_filepath=configs.bundle_entrypoints_filepath,
    )


TemplateEngine = Annotated[Renderable, Depends(get_template_engine)]
