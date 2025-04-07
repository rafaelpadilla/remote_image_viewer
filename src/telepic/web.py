"""
Web views and Flask application for the telepic application.
"""

from flask import Flask, render_template, send_file, Response, jsonify, request
from typing import Union, Tuple

from telepic.config import config

# Initialize Flask application
app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Render the main page with the first page of images.

    Returns:
        str: Rendered HTML template for the index page
    """
    page = request.args.get("page", 0, type=int)
    start_idx = page * config.images_per_page
    end_idx = min(start_idx + config.images_per_page, config.total_images)

    # Get only the first page of images
    current_page_images = []
    if config.total_images > 0:
        current_page_images = [
            (i, config.image_list[i]) for i in range(start_idx, end_idx)
        ]

    print(f"Rendering index with {len(current_page_images)} images (page {page})")
    return render_template(
        "index.html",
        images=current_page_images,
        images_per_page=config.images_per_page,
        total_images=config.total_images,
        current_page=page,
    )


@app.route("/api/images")
def get_images() -> Response:
    """
    API endpoint to get a page of images.

    Query Parameters:
        page: The page number (0-indexed)

    Returns:
        Response: JSON response with image data for the requested page
    """
    page = request.args.get("page", 0, type=int)
    start_idx = page * config.images_per_page
    end_idx = min(start_idx + config.images_per_page, config.total_images)

    images_data = []
    for i in range(start_idx, end_idx):
        image_path = config.image_list[i]
        images_data.append({"index": i, "name": image_path.name, "url": f"/image/{i}"})

    return jsonify(
        {
            "images": images_data,
            "page": page,
            "total_pages": (config.total_images + config.images_per_page - 1)
            // config.images_per_page,
            "total_images": config.total_images,
        }
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
        image_path = config.image_list[index]
        # Ensure we're using the absolute path as a string
        absolute_path = str(image_path.absolute())
        print(f"Serving image {index}: {absolute_path}")
        return send_file(absolute_path)
    print(f"Image not found at index {index}")
    return "Image not found", 404
