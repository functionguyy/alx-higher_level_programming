#!/usr/bin/python3

def replace_in_list(my_list: list, idx: int, element) -> list:
    """Function that replaces an element of a list at a specific position

    Args:
        my_list: list object
        idx: list index
        element: value to input at list index
    Return:
        modified list or original list if idx is negative or out of list range
    """

    n = len(my_list)
    if idx < 0 or idx > n or idx == n:
        return my_list
    my_list[idx] = element

    return my_list
