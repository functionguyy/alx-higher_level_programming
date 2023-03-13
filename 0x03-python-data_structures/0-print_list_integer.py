#!/usr/bin/python3

def print_list_integer(my_list: list = []) -> None:
    """A function that prints all integers of a list

    args:
    my_list: list object

    return: print one integer per line

    """
    if len(my_list) > 0:
        for num in my_list:
            print("{:d}".format(num))
