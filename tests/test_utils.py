"""
Tests for telepic utility functions.
"""

from pathlib import Path
from unittest.mock import patch

import pytest

from telepic.utils import is_image_file, get_image_files
from telepic.constants import ACCEPTED_IMAGE_EXTENSIONS


class TestIsImageFile:
    """Tests for the is_image_file function."""

    @pytest.mark.parametrize(
        "file_path,expected",
        [
            ("image.jpg", True),
            ("image.jpeg", True),
            ("image.png", True),
            ("image.gif", True),
            ("image.bmp", True),
            ("image.JPG", True),  # Test case insensitivity
            ("image.JPEG", True),
            ("image.PNG", True),
            ("image.GIF", True),
            ("image.BMP", True),
            ("image.txt", False),
            ("image.pdf", False),
            ("image.doc", False),
            ("image", False),
            ("image.jpg.txt", False),
        ],
    )
    def test_string_path(self, file_path, expected):
        """Test with string paths and various extensions."""
        assert is_image_file(file_path) == expected

    @pytest.mark.parametrize(
        "file_extension,expected",
        [
            (".jpg", True),
            (".jpeg", True),
            (".png", True),
            (".gif", True),
            (".bmp", True),
            (".JPG", True),  # Test case insensitivity
            (".JPEG", True),
            (".PNG", True),
            (".GIF", True),
            (".BMP", True),
            (".txt", False),
            (".pdf", False),
            (".doc", False),
            ("", False),
        ],
    )
    def test_path_object(self, file_extension, expected):
        """Test with Path objects and various extensions."""
        path = Path(f"image{file_extension}")
        assert is_image_file(path) == expected


class TestGetImageFiles:
    """Tests for the get_image_files function."""

    @pytest.fixture
    def mock_directory_structure(self):
        """Create a mock directory structure with various files."""
        # Create a structure of mocked file paths that would represent a directory
        file_paths = [
            "img1.jpg",
            "img2.png",
            "img3.gif",
            "document.txt",
            "notes.pdf",
            "subdir/img4.jpg",
            "subdir/img5.bmp",
            "subdir/document.docx",
            "subdir/nested/img6.jpeg",
        ]
        # Return both all paths and only the image paths
        all_paths = [Path(p) for p in file_paths]
        image_paths = [
            p
            for p in all_paths
            if any(str(p).lower().endswith(ext) for ext in ACCEPTED_IMAGE_EXTENSIONS)
        ]
        return {"all": all_paths, "images": image_paths}

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.is_file")
    def test_get_image_files_sorted(
        self, mock_is_file, mock_glob, mock_directory_structure
    ):
        """Test that get_image_files returns sorted image files by default."""
        # Mock the glob to return all files
        mock_glob.return_value = mock_directory_structure["all"]
        # Mock is_file to always return True
        mock_is_file.return_value = True

        directory = Path("/mock/directory")
        result = get_image_files(directory, scrambled=False)

        # Verify that the result contains only image files and is sorted
        expected = sorted(mock_directory_structure["images"])
        assert result == expected

        # Verify glob was called with the correct pattern
        mock_glob.assert_called_once_with("**/*")

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.is_file")
    @patch("random.shuffle")
    def test_get_image_files_scrambled(
        self, mock_shuffle, mock_is_file, mock_glob, mock_directory_structure
    ):
        """Test that get_image_files scrambles images when requested."""
        # Mock the glob to return all files
        mock_glob.return_value = mock_directory_structure["all"]
        # Mock is_file to always return True
        mock_is_file.return_value = True

        directory = Path("/mock/directory")
        result = get_image_files(directory, scrambled=True)

        # Verify that random.shuffle was called on the list of image files
        mock_shuffle.assert_called_once()

        # Verify that the result contains only image files (order checked by previous test)
        assert set(result) == set(mock_directory_structure["images"])

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.is_file")
    def test_get_image_files_string_path(
        self, mock_is_file, mock_glob, mock_directory_structure
    ):
        """Test that get_image_files handles string paths correctly."""
        # Mock the glob to return all files
        mock_glob.return_value = mock_directory_structure["all"]
        # Mock is_file to always return True
        mock_is_file.return_value = True

        # Pass a string directory path instead of Path object
        directory = "/mock/directory"
        result = get_image_files(directory, scrambled=False)

        # Verify that the result contains only image files and is sorted
        expected = sorted(mock_directory_structure["images"])
        assert result == expected

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.is_file")
    def test_get_image_files_empty_directory(self, mock_is_file, mock_glob):
        """Test that get_image_files handles empty directories correctly."""
        # Mock the glob to return an empty list
        mock_glob.return_value = []

        directory = Path("/mock/empty/directory")
        result = get_image_files(directory)

        # Verify that an empty list is returned
        assert result == []

    @patch("pathlib.Path.glob")
    @patch("pathlib.Path.is_file")
    def test_get_image_files_no_images(self, mock_is_file, mock_glob):
        """Test that get_image_files handles directories with no images correctly."""
        # Mock the glob to return non-image files
        mock_glob.return_value = [Path("document1.txt"), Path("document2.pdf")]
        # Mock is_file to always return True
        mock_is_file.return_value = True

        directory = Path("/mock/no-images/directory")
        result = get_image_files(directory)

        # Verify that an empty list is returned
        assert result == []


if __name__ == "__main__":
    pytest.main()
