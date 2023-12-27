#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Square class represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a new instance of Square class"""

        self.size = size
        self.position = position

    def area(self):
        """Getter for size attribute"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for postion attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute"""
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints sqaure with the character #"""

        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
