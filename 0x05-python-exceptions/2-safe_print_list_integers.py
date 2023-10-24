#!/usr/bin/python3
def safe_print_list_integers(my_list: list = [], x: int = 0) -> int:
    """Function that prints the first x elements of a list and only integers

    Args:
        my_list: list containing elements of different types
        x: number of elements to access in my_list

    Return:
        the real number of integers printed
    """
    element_count = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
        except (TypeError, ValueError):
            continue
        else:
            element_count += 1

    print("")
    return element_count
