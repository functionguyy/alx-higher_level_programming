#!/usr/bin/python3
"""defines a Rectangle object type"""


class Rectangle:
    """Define the internals of a Rectangle object type"""
    def __init__(self, width=0, height=0):
        """Initialize an instance of a Rectangle object type"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """convert instance to a string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            row = ["#" * self.__width for i in range(self.__height)]
            return "\n".join(row)

    def __repr__(self):
        """return the code representation of an instance"""
        return "Rectangle({0.width!r}, {0.height!r})".format(self)

    def __del__(self):
        print("Bye rectangle...")
