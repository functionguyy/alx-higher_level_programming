#!/usr/bin/python3
def only_diff_elements(set_1: set, set_2: set) -> set:
    """Function that returns a set of all element present in only one set

    Args:
        set_1: the first set of elements
        set_2: the second set of elements
    Return:
        as decribed in summary above

    """
    return set_1 ^ set_2
