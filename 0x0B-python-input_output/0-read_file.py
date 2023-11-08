#!/usr/bin/python3
"""Module defines a function that reads a file and prints the content to
stdout
"""


def read_file(filename=""):
    """This function reads a file in text mode with uft-8 encoding and prints
    it out to stdout

    Args:
        filename: combination of directory path and file name
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    for line in read_data:
        print(line, end='')
