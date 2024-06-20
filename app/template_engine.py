"""
Creates template engine that renders HTML pages
"""

import json

from config import configs
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory=configs.views_dir)


def bundle_urls_for(name: str) -> list[str]:
    bundles = []
    if "." not in name:
        raise Exception(
            f"Missing dot in bundle name. Expected something like '{name}.js' or '{name}.css' but got '{name}'"
        )

    name, type_ = name.split(".", 1)
    if "bundle_entrypoints" not in templates.env.globals:
        with open(configs.bundle_entrypoints_file, "rb") as file:
            templates.env.globals.update(bundle_entrypoints=json.load(file))

    entrypoints = templates.env.globals["bundle_entrypoints"]
    return entrypoints.get(name, {}).get(type_, [])


templates.env.globals.update(bundle_urls_for=bundle_urls_for)
