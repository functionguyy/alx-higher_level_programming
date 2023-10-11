#!/usr/bin/python3
def multiply_by_2(a_dictionary: dict) -> dict:
    """Function that returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: the initial dictionary
    Return:
        as decribed in the summary above
    """
    new_dict = dict()
    for key, value in a_dictionary.items():
        new_dict[key] = new_dict.get(key, value*2)
    return new_dict
