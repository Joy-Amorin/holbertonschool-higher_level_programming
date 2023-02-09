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
