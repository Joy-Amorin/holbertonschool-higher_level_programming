#!/usr/bin/python3
"""write square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(size, size, x, y, id)

        self.__width = size
        self.__height = size

    def __str__(self):

        _str = (f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}")
        return(_str)

    @property
    def size(self):
        """size getter"""
        return(self.__width)

    @size.setter
    def size(self, value):
        """size setter"""

        self.width = value
        self.height = value

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")

        self.width = value
