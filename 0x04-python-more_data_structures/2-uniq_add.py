#!/usr/bin/python3
def uniq_add(my_list: list = []) -> int:
    """Function that adds all unique integers in a list(only once for each
    integer)

    Args:
        my_list: the initial list
    Return:
        summation of integers

    """
    uniq_values = {x for x in my_list}   # Set comprehension
    total = 0
    for x in uniq_values:
        total += x
    return total
