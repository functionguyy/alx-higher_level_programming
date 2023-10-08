#!/usr/bin/python3

def no_c(my_string: str) -> str:
    """Function that removes all characters c and C from a string

    Args:
        my_string: string to be modified

    Return:
        new string
    """

    if type(my_string) is str:
        new_string = ""
        for letter in my_string:
            if letter not in "cC":
                new_string += letter
        return new_string
