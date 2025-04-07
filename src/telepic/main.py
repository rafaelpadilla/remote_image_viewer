#!/usr/bin/env python3
"""
Script to serve a directory of images through a web interface using Flask and localhost.run.
"""

import threading
from pathlib import Path

import fire
from dotenv import load_dotenv

from telepic.utils import get_image_files
from telepic.web import app
from telepic.network import start_localhost_run, start_flask, is_port_in_use
from telepic.config import config, DEFAULT_IMAGES_PER_PAGE, DEFAULT_PORT
from telepic import __version__

# Load environment variables
load_dotenv()


def main(
    directory: str = "",
    n: int = DEFAULT_IMAGES_PER_PAGE,
    port: int = DEFAULT_PORT,
    scrambled: bool = False,
    version: bool = False,
):
    """
    Serve a directory of images through a web interface using Flask and localhost.run.

    Args:
        directory: Directory containing images to serve
        n: Number of images to display per page (default: 20)
        port: Port to run the server on (default: 5000)
        scrambled: Whether to display images in random order (default: False)
        version: If True, print the version and exit
    """
    # Check if the port is already in use
    if is_port_in_use(port):
        print(
            f"Error: Port {port} is already in use. Please specify a different port with the --port option."
        )
        return

    # Check if version flag is provided
    if version:
        print(f"telepic version {__version__}")
        return

    # Check if directory is provided
    if not directory:
        print("Error: Please provide a directory containing images")
        return

    # Validate directory
    image_dir = Path(directory)
    if not image_dir.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return

    # Set up configuration
    config.images_dir = image_dir
    config.images_per_page = n
    config.scrambled = scrambled
    config.image_list = get_image_files(config.images_dir, config.scrambled)

    print(f"Total images found: {config.total_images}")
    if not config.image_list:
        print(f"Error: No images found in {directory}")
        return

    # Run Flask in background thread
    flask_thread = threading.Thread(target=start_flask, args=(app, port), daemon=True)
    flask_thread.start()

    # Start localhost.run with the provided port
    start_localhost_run(port)


def _entry_point():
    fire.Fire(main)


if __name__ == "__main__":
    _entry_point()
