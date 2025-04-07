"""
Telepic - A Flask-based image viewer for local directories.
"""

# Get version from installed package metadata (which comes from pyproject.toml)
try:
    from importlib.metadata import version as get_version

    __version__ = get_version("telepic")
except (ImportError, ModuleNotFoundError):
    # Fallback for older Python versions or when package is not installed
    __version__ = "0.1.10"

from telepic.web import app
from telepic.constants import IMAGES_DIR, IMAGES_PER_PAGE, SCRAMBLED, IMAGE_LIST
from telepic.utils import get_image_files, is_image_file
from telepic.network import start_localhost_run, start_flask

__all__ = [
    "app",
    "IMAGES_DIR",
    "IMAGES_PER_PAGE",
    "SCRAMBLED",
    "IMAGE_LIST",
    "get_image_files",
    "is_image_file",
    "start_localhost_run",
    "start_flask",
]
