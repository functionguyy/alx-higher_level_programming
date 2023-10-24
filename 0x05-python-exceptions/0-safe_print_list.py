#!/usr/bin/python3
def safe_print_list(my_list: list = [], x: int = 0) -> int:
    """Function that prints x elements of a list

    Args:
        my_list: list object
        x: numbers of elements to print
    Return:
        real number of elements printed.
    """
    elem_count = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
        except IndexError:
            break
        else:
            elem_count += 1
    print("")
    return elem_count
