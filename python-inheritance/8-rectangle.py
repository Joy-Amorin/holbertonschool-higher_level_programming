#!/usr/bin/python3
"""write BaseGeometry empty class"""


class BaseGeometry:
    """empty class"""
    pass

    def area(self):
        """area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value """

        if type(value) != int:
            raise TypeError("<name> must be an integer>")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.name = value


class Rectangle(BaseGeometry):
    """class  inherits from BaseGeometry """

    def __init__(self, width, height):
        """define attributes width, height"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", height)
        self.integer_validator("height", width)
