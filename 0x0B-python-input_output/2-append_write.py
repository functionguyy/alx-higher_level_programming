#!/usr/bin/python3
"""Module contains function that appends a string at the end of a text file
encoded with uft-8"""


def append_write(filename="", text=""):
    """Function appends a string at the end of a text file encoded with utf-8
    and returns the number of characters added


    args:
        filename: combination of directory path and filename
        text: string to be appended to file

    Returns:
        int: numbers of characters added.
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        appended_char_num = f.write(text)

    return appended_char_num
