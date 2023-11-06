"""Module defines function lookup"""


def lookup(obj) -> list:
    """returns list of attributes and methood of an object"""
    return dir(obj)
