"""
Jinja template engine to render HTML pages
"""

import json
from pathlib import Path

from configs import configs
from fastapi import HTTPException, Request
from fastapi.templating import Jinja2Templates


class JinjaTemplateEngine:
    """Renders HTML templates using Jinja2"""

    def __init__(
        self, request: Request, templates_dir: Path, bundle_entrypoints_filepath: Path
    ):
        self._templates = Jinja2Templates(directory=str(templates_dir))
        self._templates.env.globals.update(bundle_urls_for=self._bundle_urls_for)
        self._bundle_entrypoints_filepath = bundle_entrypoints_filepath
        self._request = request

    def render(self, name: str, **kwargs):
        """
        Renders a HTML template

        :param str name: Template name
        :param **kwargs: Additional context properties
        """
        return self._templates.TemplateResponse(
            request=self._request, name=name, context=kwargs
        )

    def _bundle_urls_for(self, name: str) -> list[str]:
        """
        Retrieves the bundles to be included for that script

        :param str name: Bundle name e.g. index.js or index.css
        :return list[str]: A collection of scripts or styles that are part of the bundle
        """
        if "." not in name:
            raise HTTPException(
                status_code=500,
                detail="Missing dot in bundle name. Expected something like "
                f"'{name}.js' or '{name}.css' but got '{name}'",
            )

        name, type_ = name.split(".", 1)
        if not hasattr(self._request.app.state, "bundle_entrypoints"):
            with open(configs.bundle_entrypoints_filepath, "rb") as file:
                self._request.app.state.bundle_entrypoints = json.load(file)

        entrypoints = self._request.app.state.bundle_entrypoints
        bundle_entrypoints = entrypoints.get(name, {}).get(type_, [])
        return [f"/{bundle}" for bundle in bundle_entrypoints]
