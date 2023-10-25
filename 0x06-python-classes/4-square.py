#!/usr/bin/python3
"""Module contains the class definition of a Square type"""


class Square(object):
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialization of Square instance

        A square instance can be initialize with a integer which is then
        assigned to the size attribute of the instance. The size attribute
        is a managed attribute so any value that is passed during instantiation
        is checked using the property methods defined with the same name.

        Args:
            size (:obj: `int`, optional): zero or positive number

        """
        self.size = size

    @property
    def size(self):
        """property method to retrieve the value of private instance attribute
        size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of private instance attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Method that returns current square area"""
        return self.__size**2
