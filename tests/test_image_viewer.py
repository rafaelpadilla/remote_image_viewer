import tempfile
from pathlib import Path
import pytest
from telepic.web import app


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def temp_image_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test image files
        image_files = ["test1.jpg", "test2.png", "test3.jpeg", "notanimage.txt"]
        for filename in image_files:
            Path(temp_dir, filename).touch()

        yield Path(temp_dir)


def test_serve_image_not_found(test_client):
    """Test serving non-existent image."""
    response = test_client.get("/image/999")
    assert response.status_code == 404


def test_index_page(test_client):
    """Test index page rendering."""
    response = test_client.get("/")
    assert response.status_code == 200
