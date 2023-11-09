#!/usr/bin/python3
"""Module define function add_attribute"""


def add_attribute(obj, attr_name, attr_value):
    """adds a new attribute to an object if it's possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
