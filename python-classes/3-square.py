#!/usr/bin/python3
"""Write a class Square that defines a square.
"""


class Square:
    """Write a class Square that defines a square by
    pruvate attribute"""
    def __init__(self, size=0):

        self.__size = 3

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return(self.__size**2)
