#!/usr/bin/python3
"""defin Rectangle class"""


class Rectangle:
    """define width and height attribute and values """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return Rectangle area"""
        return(self.__width * self.__height)

    def perimeter(self):
        """return Rectangle perimeter"""
        if width == 0 or heigth == 0:
            return(0)

        return(self.__width * self.__height)

    def perimeter(self):
        return ((self.__width + self.__height)*2)
