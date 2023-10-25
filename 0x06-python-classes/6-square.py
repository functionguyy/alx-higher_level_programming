#!/usr/bin/python3
"""Module contains the class definition of a Square type"""


class Square(object):
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of Square object

        Args:
            size (:obj: `int`, optional): zero or positive number
            position(:obj: `tuple`, optional): two positive integers

        """
        self.size = size
        self.position = position

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
            y = self.__position[1]
            x = self.__position[0]
            if y > 0:
                for y_pos in range(y):
                    print()
            while n > 0:
                for x_pos in range(x):
                    print(" ", end="")
                for num in range(self.__size):
                    print("#", end="")
                print()
                n = n - 1

    @property
    def position(self):
        """Getter method for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position attribute"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if abs(value[0]) != value[0] or abs(value[1]) != value[1]:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
