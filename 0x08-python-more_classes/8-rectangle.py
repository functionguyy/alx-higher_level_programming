#!/usr/bin/python3
"""defines a Rectangle object type"""


class Rectangle:
    """Define the internals of a Rectangle object type


    Attributes:
        number_of_instances (:obj:`int`, optional): keep the count of object
        reference
        print_symbol (:obj:`str`, optional): use as symbol for string
        representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize an instance of a Rectangle object type"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            row = [str(self.print_symbol) * self.__width for i in
                   range(self.__height)]
            return "\n".join(row)

    def __repr__(self):
        """return the code representation of an instance"""
        return "Rectangle({0.width!r}, {0.height!r})".format(self)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if rect_1.area == rect_2.area or rect_1.area > rect_2.area:
            return rect_1
        return rect_2
