#!/usr/bin/python3
def number_keys(a_dictionary: dict) -> dict:
    """Function that returns the number of keys in a dictionary

    Args:
        a_dictionary: dictionary object

    """
    keys = a_dictionary.keys()
    return len(keys)
