"""
Configuration settings for the telepic application.
"""

from pathlib import Path
from typing import Set, List, Optional

# Static configuration constants
ACCEPTED_IMAGE_EXTENSIONS: Set[str] = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}
DEFAULT_PORT: int = 8080
DEFAULT_IMAGES_PER_PAGE: int = 20


# Runtime configuration (initially empty)
class RuntimeConfig:
    """Runtime configuration that can be modified during execution."""

    images_dir: Optional[Path] = None
    images_per_page: int = DEFAULT_IMAGES_PER_PAGE
    scrambled: bool = False
    image_list: List[Path] = []

    @property
    def total_images(self) -> int:
        """Get the total number of images."""
        return len(self.image_list)


# Create a singleton instance
config = RuntimeConfig()
