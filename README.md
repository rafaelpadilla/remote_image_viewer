# Remote Image Viewer 🖼️

A Flask-based web application that allows users to visualize images from a remote computer through a web browser using localhost.run tunneling. 🌐

## Features ✨

- 🔍 View images from any directory on the remote computer
- 📑 Configurable number of images per page
- 🎨 Support for multiple image formats (jpg, jpeg, png, etc.)
- 🔀 Option to display images in alphabetical order or scrambled
- 🔒 Secure remote access through localhost.run tunneling
- 📝 Image filenames displayed below each image

## Requirements 📋

- Python 3.11+ 🐍

## Installation 💻

1. Clone this repository:
```bash
git clone https://github.com/rafaelpadilla/remote-image-viewer.git
cd remote-image-viewer
```

2. Install the package:
```bash
pip install -e .
```

## Usage 🚀

Run the image visualization server using the `main.py` script:

```bash
python main.py [OPTIONS] DIRECTORY

Options:
  --n INTEGER  Number of images to display per page (default: 20)
  --port INTEGER            Port to run the server on (default: 5000)
  --scrambled              Display images in random order instead of alphabetically
```

Example:
```bash
python main.py /path/to/images --n 30 --port 5000 --scrambled
```

## Development 🛠️

To run tests:
```bash
pytest
```

