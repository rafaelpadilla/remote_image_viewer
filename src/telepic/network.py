"""
Network-related functions for telepic application.
"""

import socket
import subprocess
import sys
from typing import Any


def is_port_in_use(port: int) -> bool:
    """
    Check if a port is already in use.

    Args:
        port: Port to check

    Returns:
        True if the port is in use, False otherwise
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(("localhost", port)) == 0


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
    # Check if the port is already in use
    if is_port_in_use(port):
        print(
            f"Error: Port {port} is already in use. Please specify a different port with the --port option."
        )
        sys.exit(1)

    try:
        app.run(port=port)
    except OSError as e:
        print(f"Error starting Flask server: {e}")
        sys.exit(1)
