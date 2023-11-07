#!/usr/bin/python3
"""Module defines class MyInt
MyInt is a subclass of int
"""


class MyInt(int):
    """Defines the internal representation of a MyInt object type"""

    def __init__(self, value):
        """initialize an instance of MyInt"""
        self.value = value

    def __ne__(self, number):
        """return self == number"""
        return self.value == number

    def __eq__(self, number):
        """return self != number"""
        return self.value != number
