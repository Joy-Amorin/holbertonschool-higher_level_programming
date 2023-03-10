#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Define a size attribute """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return area size """
        return(self.__size**2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#"*self.__size)
