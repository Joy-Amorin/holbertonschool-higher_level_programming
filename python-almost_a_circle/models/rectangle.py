#!/usr/bin/python3
"""write Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

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
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x getter"""

        return(self.__x)

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y setter"""
        return(self.__y)

    @y.setter
    def y(self, value):

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """return area self"""
        return(self.__width * self.__height)

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""

        for x in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method"""

        _str = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        _str_2 = f" - {self.__width}/{self.__height}"

        return(_str + _str_2)

    def update(self, *args):
        """asigns an argument to each attribute"""

        if args:
    
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.__width = arg
                if count == 2:
                    self.__height = arg
                if count == 3:
                    self.__x = arg
                if count == 3:
                    self.__y = arg

            return(arg)
