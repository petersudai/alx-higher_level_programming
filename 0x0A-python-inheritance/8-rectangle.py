#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a rectangle instance with given width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] {]/{}".format(self.__width, self.__height)
