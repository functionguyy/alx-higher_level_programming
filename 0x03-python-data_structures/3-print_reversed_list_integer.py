#!/usr/bin/python3
def print_reversed_list_integer(my_list: list = []) -> int:
    """Function that prints all integers of a list, in reverse order

    Args:
        my_list: list containing the integer

    Return:
        print one integer per line
    """
    if len(my_list) > 0:
        for num in sorted(my_list, reverse=True):
            print("{:d}".format(num))
    return my_list
