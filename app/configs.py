"""Holds configurations for the app"""

import os

from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings

current_dir = os.path.dirname(os.path.realpath(__file__))


class Config(BaseSettings):
    """Environment configs"""

    api_version: str = "v1"
    views_dir: DirectoryPath = f"{current_dir}/resources/views"
    bundle_entrypoints_filepath: FilePath = f"{current_dir}/dist/entrypoints.json"


configs = Config()
