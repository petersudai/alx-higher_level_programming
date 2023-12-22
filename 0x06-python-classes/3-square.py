#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represents square"""

    def __init__(self, size=0):
        """Initialize new square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """computes the area of the square and returns it"""
        return self.__size ** 2
