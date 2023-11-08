#!/usr/bin/python3
"""Module contains function that writes to a tex file"""


def write_file(filename="", text=""):
    """function writes to a text file encoded with utf-8

    Args:
        filename: combination of directory path and file name
        text: string to be written to file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        written_char_num = f.write(text)

    return written_char_num
