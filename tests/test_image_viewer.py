import os
import tempfile
from pathlib import Path
import pytest
from remote_image_viewer.export_visualization import (
    is_image_file,
    get_image_files,
    app
)

@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def temp_image_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test image files
        image_files = [
            'test1.jpg',
            'test2.png',
            'test3.jpeg',
            'notanimage.txt'
        ]
        for filename in image_files:
            Path(temp_dir, filename).touch()

        yield Path(temp_dir)

def test_is_image_file():
    """Test image file detection."""
    assert is_image_file(Path('test.jpg'))
    assert is_image_file(Path('test.jpeg'))
    assert is_image_file(Path('test.png'))
    assert is_image_file(Path('test.gif'))
    assert not is_image_file(Path('test.txt'))
    assert not is_image_file(Path('test'))

def test_get_image_files(temp_image_dir):
    """Test getting image files from directory."""
    image_files = get_image_files(temp_image_dir)
    assert len(image_files) == 3  # Should find 3 image files

    # Test file names are sorted
    assert image_files[0].name == 'test1.jpg'
    assert image_files[1].name == 'test2.png'
    assert image_files[2].name == 'test3.jpeg'

def test_get_image_files_scrambled(temp_image_dir):
    """Test getting scrambled image files."""
    # Run multiple times to ensure we get different orders
    orders = set()
    for _ in range(10):
        files = get_image_files(temp_image_dir, scrambled=True)
        orders.add(tuple(f.name for f in files))

    # Should have at least 2 different orders out of 10 tries
    assert len(orders) > 1

def test_serve_image_not_found(test_client):
    """Test serving non-existent image."""
    response = test_client.get('/image/999')
    assert response.status_code == 404

def test_index_page(test_client):
    """Test index page rendering."""
    response = test_client.get('/')
    assert response.status_code == 200