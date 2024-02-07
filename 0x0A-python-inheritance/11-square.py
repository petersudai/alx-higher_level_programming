#!/usr/bin/python3

"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance with the given size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
