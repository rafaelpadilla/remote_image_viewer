"""
Utility functions for the telepic application.
"""

import random
from pathlib import Path
from typing import List, Union

from telepic.config import ACCEPTED_IMAGE_EXTENSIONS


def is_image_file(file_path: Union[Path, str]) -> bool:
    """
    Determine if a file is an image based on its file extension.

    This function checks if the file extension matches common image formats.
    Supported formats include: JPG, JPEG, PNG, GIF, BMP, and WEBP.

    Args:
        file_path: A Path object pointing to the file to be checked

    Returns:
        bool: True if the file has a recognized image extension, False otherwise
    """
    if isinstance(file_path, str):
        return Path(file_path).suffix.lower() in ACCEPTED_IMAGE_EXTENSIONS

    return file_path.suffix.lower() in ACCEPTED_IMAGE_EXTENSIONS


def get_image_files(directory: Union[Path, str], scrambled: bool = False) -> List[Path]:
    """
    Get all image files from the directory.

    Args:
        directory: Path to the directory containing image files
        scrambled: If True, the images will be returned in random order
                  If False, the images will be returned in alphabetical order

    Returns:
        List[Path]: A list of Path objects pointing to image files
    """
    if isinstance(directory, str):
        directory = Path(directory)

    image_files = [
        f for f in directory.glob("**/*") if f.is_file() and is_image_file(f)
    ]

    if scrambled:
        random.shuffle(image_files)
    else:
        image_files.sort()

    return image_files
