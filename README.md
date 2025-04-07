<p align="center">
  <img src="assets/telepic.png" alt="Telepic" width="400">
</p>

# Telepic

Telepic – "tele" (distance) + "pic" (picture) – is a lightweight and easy-to-use CLI tool + Flask web app that allows you to remotely visualize images from a server (e.g. a VM or EC2) in your browser – wherever you are 🌍.

No need to set up complex SSH tunnels or file syncing — just run `telepic <YOUR-IMAGE-FOLDER` on the remote machine, and get a shareable link to view your images from anywhere!

----------

## Features ✨

- 📁 View images in any folder on a remote server
- 🔄 Sort images alphabetically or shuffle them randomly
- 🖼️ Supports common formats: JPG, PNG, JPEG, etc.
- 🔢 Paginate results: control how many images per page
- 🔗 Shareable public URL via localhost.run
- 🧾 Clean UI with filenames under each image

----------

## Requirements 📋

- Python 3.11+ 🐍

----------

## ⚙️ Installation

1. Clone this repository:
```bash
git clone https://github.com/rafaelpadilla/telepic.git
cd telepic
pip install -e .
```
----------

##  🚀 Usage

Run the server on your *remote machine (VM, EC2, etc.)*:

```bash
python telepic <DIRECTORY-WITH-IMAGES> [OPTIONS]

Options:
  --n INTEGER  Number of images to display per page (default: 20)
  --port INTEGER            Port to run the server on (default: 5000)
  --scrambled              Display images in random order instead of alphabetically
```

Example:
```bash
python telepic /path/to/images --n 30 --port 5000 --scrambled
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
----------

## 📝 License

This project is licensed under the MIT License.

----------

## 🤝 Contribution

Contributions are welcome! 🙌

Found a bug or have a feature idea? Feel free to open an issue or a pull request.

Check out our [CONTRIBUTING.md](CONTRIBUTING.md) to get started.



