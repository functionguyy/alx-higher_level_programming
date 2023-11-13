#!/usr/bin/python3
"""Module defines class Base"""


class Base:
    """define internal for Base object type"""
    __nb_object = 0

    def __init__(self, id=None):
        if id is None or id < 0:
            self.__nb_object += 1
            self.id = self.__nb_object
        else:
            self.id = id
