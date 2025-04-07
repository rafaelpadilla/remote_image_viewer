"""
Network-related functions for telepic application.
"""

import subprocess
from typing import Any


def start_localhost_run(port: int) -> None:
    """
    Start a localhost.run tunnel to expose the local server to the internet.

    This function establishes an SSH tunnel using localhost.run service
    to make the local Flask server accessible from the internet.

    Args:
        port: The local port where the Flask server is running
    """
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

    for line in tunnel.stdout:  # type: ignore
        print(line.decode(), end="")


def start_flask(app: Any, port: int) -> None:
    """
    Start the Flask web server.

    Args:
        app: The Flask application to run
        port: The port on which to run the Flask server
    """
    app.run(port=port)
