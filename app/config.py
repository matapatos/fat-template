"""
Holds configs for the app
"""

import os

from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings

current_dir = os.path.dirname(os.path.realpath(__file__))


class Config(BaseSettings):
    views_dir: DirectoryPath = f"{current_dir}/views"
    bundle_entrypoints_file: FilePath = f"{current_dir}/dist/entrypoints.json"


configs = Config()
