#!/usr/bin/python3
"""Module defines function inherits_from"""


def inherits_from(obj, a_class):
    """check if an object inherits from a specified class

    Attributes
        obj(:obj:): Object
        a_class(:class:): a class

    """
    obj_class = type(obj)
    if issubclass(obj_class, a_class) and obj_class is not a_class:
        return True
    return False
