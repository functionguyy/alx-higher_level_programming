#!/usr/bin/python3
"""Module defines class Base"""


class Base:
    """define internal for Base object type"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
