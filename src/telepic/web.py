"""
Web views and Flask application for the telepic application.
"""

from flask import Flask, render_template, send_file, Response
from typing import Union, Tuple

from telepic.config import config

# Initialize Flask application
app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Render the main page with image grid.

    Returns:
        str: Rendered HTML template for the index page
    """
    print(f"Rendering index with {config.total_images} images")
    return render_template(
        "index.html",
        images=enumerate(config.image_list),
        images_per_page=config.images_per_page,
        total_images=config.total_images,
    )


@app.route("/image/<int:index>")
def serve_image(index: int) -> Union[Response, Tuple[str, int]]:
    """
    Serve an image file.

    Args:
        index: Index of the image in the image_list to serve

    Returns:
        Response: Flask response containing the image file
        or Tuple[str, int]: Error message and HTTP status code if image not found
    """
    if 0 <= index < config.total_images:
        print(f"Serving image {index}: {config.image_list[index]}")
        return send_file(config.image_list[index])
    print(f"Image not found at index {index}")
    return "Image not found", 404
