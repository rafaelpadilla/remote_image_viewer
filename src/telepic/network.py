"""
Network-related functions for telepic application.
"""

import socket
import subprocess
from typing import Any, Tuple


def find_available_port(start_port: int, max_attempts: int = 10) -> int:
    """
    Find an available port starting from start_port.

    Args:
        start_port: Port to start checking from
        max_attempts: Maximum number of ports to try

    Returns:
        An available port number
    """
    for port_offset in range(max_attempts):
        port = start_port + port_offset
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(("localhost", port)) != 0:
                return port
    # If we couldn't find an available port, return the original
    # (it will fail, but at least with the original error)
    return start_port


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


def start_flask(app: Any, port: int) -> Tuple[bool, int]:
    """
    Start the Flask web server.

    Args:
        app: The Flask application to run
        port: The port on which to run the Flask server

    Returns:
        Tuple containing:
        - Success status (True if started successfully)
        - The actual port used (may differ from requested port if it was in use)
    """
    # Try to find an available port if the specified one is in use
    available_port = find_available_port(port)
    if available_port != port:
        print(f"Port {port} is in use, using port {available_port} instead")
        port = available_port

    try:
        app.run(port=port)
        return True, port
    except OSError as e:
        print(f"Error starting Flask server: {e}")
        return False, port
