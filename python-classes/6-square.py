#!/usr/bin/python3
"""Define Square class"""


class Square:
    """define size and position attribute """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size getter"""

        return(self.__size)

    @size.setter
    def size(self, value):
        """size setter """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif type < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """position getter """
        return(self.__position)

    @position.setter
    def position(self, value):
        """position setter """

        if type(size.__position) != tuple or type(value) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """reurn square area """
        return(self.__size**2)

    def my_print(self):
        """prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
