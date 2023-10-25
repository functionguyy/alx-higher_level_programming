#!/usr/bin/python3
"""Module contains the class definition of a Square type"""


class Square(object):
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialization of Square object

        Args:
            size (:obj: `int`, optional): zero or positive number

        """
        self.size = size

    @property
    def size(self):
        """getter method for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Method that returns current square area"""
        return self.__size**2

    def my_print(self):
        """Method that prints in stdout the square with character #

            if size of the square is equal to 0, it prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            n = self.__size
            while n > 0:
                for num in range(self.__size):
                    print("#", end="")
                print()
                n = n - 1
