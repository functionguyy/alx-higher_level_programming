#!/usr/bin/python3

def new_in_list(my_list: list, idx: int, element) -> list:
    """Function that replaces an element in a list at a specific position
    without modifying the original list

    Args:
        my_list: List object
        idx: integer
        element: value to input and idx position in my_list
    Return:
        modified list or original list if idx is negative or out of my_list
        range

    """
    if type(my_list) is list and type(idx) is int:
        n len(my_list)

        if idx < 0 or idx >= n:
            return my_list

        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
