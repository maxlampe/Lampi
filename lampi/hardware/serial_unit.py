"""Module for base class to be inherited for different serial hardware modules"""

import numpy as np


class SerialUnit:
    """Base class for all hardware units to be """

    def __init__(self, port: str, baud_rate: int):
        self._port = port
        self._baud_rate = baud_rate

    def __call__(self, *args, **kwargs):
        self._open_device()

    def _open_device(self):
        """Open device and establish communication with it."""
        pass

    def close_device(self):
        """End communication with device."""
        pass

    def get_state(self):
        """Get current state of parameters from device."""
        pass

    def send_cmd(self):
        """Send a command to the device."""
        pass
