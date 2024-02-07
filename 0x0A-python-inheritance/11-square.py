#!/usr/bin/python3

"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance with the given size"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of a square"""
        return self.__size ** 2

    def __Str__(self):
        """Returns and print the square description"""
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))
