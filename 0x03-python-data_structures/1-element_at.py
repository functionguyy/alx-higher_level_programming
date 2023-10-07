#!/usr/bin/python3

def element_at(my_list: list, idx: int) -> str:
    """Function that retrieves an element from a list like in C

    my_list: list object
    idx: index of the element to retrieve from my_list

    Return: list element at idx or None if idx is negative or out of range

    """

    n = len(my_list)

    if idx < 0:
        return None
    if idx > (n - 1):
        return None
    return my_list[idx]
