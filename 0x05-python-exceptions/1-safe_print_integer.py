#!/usr/bin/python3
def safe_print_integer(value: int) -> bool:
    """Function that prints an integer

    Args:
        value: the integer to be printed

    Return:
        True if value has been correctly printed(it means the value is an
        integer) otherwise False
    """
    flag = True

    while (flag):
        try:
            if not isinstance(value, int):
                raise TypeError
        except TypeError:
            flag = False
            break
        else:
            print("{:d}".format(value))
            break

    return flag
