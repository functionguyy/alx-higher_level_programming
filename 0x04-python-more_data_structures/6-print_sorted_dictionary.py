#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict) -> None:
    """Function that prints a dictionary by ordered keys

    Args:
        a_dictionary: dictionary object

    Return:
        None

    """
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
