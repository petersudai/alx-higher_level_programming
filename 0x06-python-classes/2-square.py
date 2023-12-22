#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent Square"""

    def __init__(self, size=0):
        """Initialize a new Square"""

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
