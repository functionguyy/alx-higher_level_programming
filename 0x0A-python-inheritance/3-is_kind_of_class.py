#!/usr/bin/python3
"""Module defines function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns True if an object is an instance of a class or of a class that
    inherited from the specified class

    Attributes
        obj(:obj:): object
        a_class(:cls:): class
    """
    if not isinstance(obj, a_class):
        return False
    return True
    
