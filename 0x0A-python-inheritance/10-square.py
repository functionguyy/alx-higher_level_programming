#!/usr/bin/python3
"""Module defines class Square"""
rectangle = __import__('9-rectangle')


class Square(rectangle.Rectangle):
    """Define the internals of a Square object type.

    Square is a subclass of Rectangle
    """

    def __init__(self, size):
        """initialize an instance of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculate the area of a Square"""
        return self.__size * self.__size
