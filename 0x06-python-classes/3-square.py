#!/usr/bin/python3
"""Module that contains definition of a Square class"""


class Square(object):
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialization of class instance

        Args:
            size (:obj: `int`, optional): zero or positive number

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that returns current square area"""

        return self.__size**2
