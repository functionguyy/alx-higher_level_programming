#!/usr/bin/python3
"""Module defines class Rectangle"""
base_geometry = __import__('7-base_geometry')


class Rectangle(base_geometry.BaseGeometry):
    """Define the internals of a Rectangle object type.

    Rectangle is a subclass of BaseGeometry
    """

    def __init__(self, width, height):
        """initialize an instance of Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
