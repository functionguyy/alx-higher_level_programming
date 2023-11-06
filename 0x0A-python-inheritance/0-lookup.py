#!/usr/bin/python3
"""Module defines function lookup"""


def lookup(obj):
    """returns list of attributes and methood of an object

    Attributes:
        obj (:obj): object

    """
    return dir(obj)
