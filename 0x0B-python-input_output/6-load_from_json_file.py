#!/usr/bin/python3
"""Module contains function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file

    args:
        filename: JSON file

    Returns:
        An object
    """
    with open(filename, "r", encoding="utf-8") as f:
        f = json.load(f)

    return f
