#!/usr/bin/python3
"""Module defines function is_same_class"""


def is_same_class(obj, a_class):
    """returns True if an object is exactly an instance of the specified class;
    otherwise False


    Attributes
        obj(:obj:): object
        a_class(:cls:): class
    """
    if type(obj) is not a_class:
        return False
    return True
