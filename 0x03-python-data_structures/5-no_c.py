def no_c(my_string: str) -> str:
    """Function that removes all characters c and C from a string

    Args:
        my_string: string to be modified

    Return:
        new string
    """
    if type(my_string) is str:
        letter_list = list(my_string)
        letter_list = [x for x in my_string if x not in "cC"]
        return "".join(letter_list)
