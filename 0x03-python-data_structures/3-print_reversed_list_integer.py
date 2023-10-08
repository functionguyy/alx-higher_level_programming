#!/usr/bin/python3

def print_reversed_list_integer(my_list: list = []) -> int:
    """Function that prints all integers of a list, in reverse order

    Args:
        my_list: list containing the integer

    Return:
        print one integer per line
    """

    if type(my_list) is list:
        for num in reversed(my_list):
            print("{:d}".format(num))
