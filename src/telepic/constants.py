"""
Constants used throughout the telepic application.
"""

from pathlib import Path
from typing import List, Optional, Set

# Image-related constants
ACCEPTED_IMAGE_EXTENSIONS: Set[str] = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}

# Application configuration constants
IMAGES_DIR: Optional[Path] = None
IMAGES_PER_PAGE: int = 20
SCRAMBLED: bool = False
IMAGE_LIST: List[Path] = []
