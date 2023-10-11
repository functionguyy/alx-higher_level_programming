#!/usr/bin/python3
def update_dictionary(a_dictionary: dict, key: str, value) -> dict:
    """Function that replaces or adds key/value in dictionary

    Args:
        a_dictionary: dictionary object
        key: value to key to be updated
        value: new value to input for key
    Return:
        dictionary with updated key/value pairs

    """
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary[key] = a_dictionary.get(key, value)
    return a_dictionary
