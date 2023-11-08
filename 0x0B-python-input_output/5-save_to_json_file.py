#!/usr/bin/python3
"""Module defines function save_to_json_file.
The function writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON
    representation

    args:
        my_obj: object to be written to text file
        filename: combination of directory path and file name
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
