#!/usr/bin/python3
"""Square Module"""
from rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self._Rectangle__x, self._Rectangle__y, self._Rectangle__width)

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update attributes based on *args and **kwargs"""
        if args:
            attributes = ["id", "size", "x", "y"]

            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "_Rectangle__width", value)
                    setattr(self, "_Rectangle__height", value)
                else:
                    setattr(self, key, value)
