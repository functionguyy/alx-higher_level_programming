#!/usr/bin/python3
"""Module that contains definition of a Square class"""


class Square(object):
    """A class that defines a square"""

    def __init__(self, size=None):
        """Initialization of class instance

        Args:
            size (None): size of a square
        """
        self.__size = size
