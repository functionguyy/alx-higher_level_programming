#!/usr/bin/python3
def common_elements(set_1: set, set_2: set) -> set:
    """Function that returns a set of common elements in two sets

    Args:
        set_1: the first set of element
        set_2: the second set of element
    Return:
        set of common elements in both set_1 and set_2

    """
    return set_1 & set_2
