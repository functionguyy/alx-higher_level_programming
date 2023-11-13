#!/usr/bin/python3
"""Module defines class Base"""


class Base:
    """define internal for Base object type"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None or id < 0 :
            self.id = type(self).__nb_objects + 1
        else:
            self.id = id
