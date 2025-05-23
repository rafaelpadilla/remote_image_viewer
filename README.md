<p align="center">
  <img src="https://github.com/rafaelpadilla/telepic/blob/main/assets/telepic.png?raw=true" alt="Telepic" width="400">
</p>

<p align="center">
  <a href="https://github.com/rafaelpadilla/telepic/actions/workflows/ci.yml"><img alt="CI Status" src="https://github.com/rafaelpadilla/telepic/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://pypi.org/project/telepic/"> <img src="https://img.shields.io/pypi/v/telepic.svg" alt="Version"></a>
  <a href="https://pypi.org/project/telepic/"> <img src="https://img.shields.io/pypi/pyversions/telepic.svg" alt="Python Versions"></a>
  <a href="https://opensource.org/licenses/Apache-2.0"> <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://github.com/sponsors/rafaelpadilla"> <img src="https://img.shields.io/badge/Sponsor-Support%20us-brightgreen?logo=github&logoColor=white&style=flat" alt="Sponsor: Support us"></a>
</p>

**Telepic** (*tele* = distance + *pic* = picture) is a lightweight and easy-to-use CLI tool + Flask-based web application for sharing images from a remote machine or server (e.g. a VM or EC2 instance). With just one command, Telepic generates a shareable link or QR code, letting others instantly view your images in their browser.

No need to set up complex SSH tunnels or file syncing — just run `telepic <YOUR-IMAGE-FOLDER` on the remote machine, and get a shareable link to view your images from anywhere!


## Features ✨

- 📁 View images in any folder on a remote server
- 🔄 Sort images alphabetically or shuffle them randomly
- 🖼️ Supports common formats: JPG, PNG, JPEG, etc.
- 🔢 Paginate results: control how many images per page
- 🔗 Shareable public URL via localhost.run
- 🧾 Clean UI with filenames under each image


## Requirements 📋

- Python 3.11+ 🐍


## ⚙️ Installation

### Option 1: Install from PyPI

```bash
pip install telepic
```

### Option 2: Install from source

1. Clone this repository:
```bash
git clone https://github.com/rafaelpadilla/telepic.git
cd telepic
pip install -e .
```

##  🚀 Usage

Run the server on your *remote machine (VM, EC2, etc.)*:

```bash
telepic <DIRECTORY-WITH-IMAGES> [OPTIONS]

Options:
  --n INTEGER  Number of images to display per page (default: 20)
  --port INTEGER            Port to run the server on (default: 5000)
  --scrambled              Display images in random order instead of alphabetically
```

Example:
```bash
telepic /path/to/images --n 30 --port 5000 --scrambled
```

This will start the server and generate a public URL via `localhost.run`. Open it in your browser and you're good to go!

## 🧪 Testing

First, install the package with development dependencies:

```bash
pip install -e .[dev]
```

Then run the tests:

```bash
./bin/lint && ./bin/test
```

## 📝 License

This project is licensed under the Apache 2.0.


## 🤝 Contribution

Contributions are welcome! 🙌

Found a bug or have a feature idea? Feel free to open an issue or a pull request.

Check out our [CONTRIBUTING.md](CONTRIBUTING.md) to get started.



