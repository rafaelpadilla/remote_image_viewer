#!/usr/bin/env python3
"""
Script to serve a directory of images through a web interface using Flask and ngrok.
"""

import random
from pathlib import Path
import subprocess
import threading
from typing import List, Optional

import fire
from flask import Flask, render_template, send_file
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Global variables to store configuration
IMAGES_DIR: Optional[Path] = None
IMAGES_PER_PAGE: int = 20
SCRAMBLED: bool = False
IMAGE_LIST: List[Path] = []


def is_image_file(file_path: Path) -> bool:
    """Check if a file is an image based on its extension."""
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
    return file_path.suffix.lower() in image_extensions


def get_image_files(directory: Path, scrambled: bool = False) -> List[Path]:
    """Get all image files from the directory."""
    image_files = [
        f for f in directory.glob("**/*") if f.is_file() and is_image_file(f)
    ]

    if scrambled:
        random.shuffle(image_files)
    else:
        image_files.sort()

    return image_files


@app.route("/")
def index():
    """Render the main page with image grid."""
    return render_template(
        "index.html", images=enumerate(IMAGE_LIST), images_per_page=IMAGES_PER_PAGE
    )


@app.route("/image/<int:index>")
def serve_image(index):
    """Serve an image file."""
    if 0 <= index < len(IMAGE_LIST):
        return send_file(IMAGE_LIST[index])
    return "Image not found", 404


def start_localhost_run(port: int):
    tunnel = subprocess.Popen(
        [
            "ssh",
            "-o",
            "StrictHostKeyChecking=no",
            "-R",
            f"80:localhost:{port}",
            "localhost.run",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    for line in tunnel.stdout:
        print(line.decode(), end="")


def start_flask(port: int):
    app.run(port=port)


def main(
    directory: str, n: int = 20, port: int = 5000, scrambled: bool = False
) -> None:
    """
    Serve a directory of images through a web interface using Flask and ngrok.

    Args:
        directory: Directory containing images to serve
        n: Number of images to display per page (default: 20)
        port: Port to run the server on (default: 5000)
        scrambled: Whether to display images in random order (default: False)
    """
    # Validate directory
    image_dir = Path(directory)
    if not image_dir.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return 1

    # Set up global variables
    global IMAGES_DIR, IMAGES_PER_PAGE, SCRAMBLED, IMAGE_LIST
    IMAGES_DIR = image_dir
    IMAGES_PER_PAGE = n
    SCRAMBLED = scrambled
    IMAGE_LIST = get_image_files(IMAGES_DIR, SCRAMBLED)

    if not IMAGE_LIST:
        print(f"Error: No images found in {directory}")
        return 1

    # Run Flask in background thread
    threading.Thread(target=start_flask, args=(port,), daemon=True).start()

    start_localhost_run(port)


if __name__ == "__main__":
    fire.Fire(main)
