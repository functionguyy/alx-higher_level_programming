#!/usr/bin/python3
"""Module defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """define internal for Rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize an instance of a Rectangle object type"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of the rectangle"""
        return self.width * self.height

    def display(self):
        """display"""
        rec_height = self.__height
        y = self.__y
        x = self.__x

        if y > 0:
            for y_pos in range(y):
                print()
        while rec_height > 0:
            for x_pos in range(x):
                print(" ", end="")
            for n in range(self.__width):
                print("#", end="")
            print()
            rec_height -= 1

    def __str__(self):
        """convert instance to a string"""
        obj_id = self.id
        obj_x = self.x
        obj_y = self.y
        obj_w = self.width
        obj_h = self.height
        return "[Rectangle] ({0:d}) {1:d}/{2:d} - {3:d}/{4:d}".format(obj_id,
                                                                      obj_x,
                                                                      obj_y,
                                                                      obj_w,
                                                                      obj_h)

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""

        if len(args) > 0:
            try:
                super().__init__(args[0])
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    if k == "id":
                        super().__init__(v)
                        continue
                    setattr(self, k, v)
