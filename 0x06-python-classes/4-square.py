#!/usr/bin/python3
"""Define class Square"""


class Square:

    """Square class represents square"""

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def are (self):
        """computes and returns area of square"""

        return self.__size ** 2

    @property
    def size(self):
        """getter for size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter for size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
