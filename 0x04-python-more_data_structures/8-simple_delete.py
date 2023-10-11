#!/usr/bin/python3
def simple_delete(a_dictionary: dict, key: str = "") -> dict:
    """Function that deletes a key in a dictionary

    Args:
        a_dictionary: the initial dictionary
        key: string for dictionary key
    Return:
        returns modified original dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
