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
        if value is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
