#!/usr/bin/python3
"""Module defines class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define internal for Square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize an instance of a Rectangle object type"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """convert instance to a string"""
        obj_id = self.id
        obj_x = self.x
        obj_y = self.y
        obj_size = self.width
        return "[Square] ({0:d}) {1:d}/{2:d} - {3:d}".format(obj_id, obj_x,
                                                             obj_y, obj_size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """set value of size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""

        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)
