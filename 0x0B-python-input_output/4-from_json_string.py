#!/usr/bin/python3
"""Module contains function that deserializes a JSON string"""
import json


def from_json_string(my_str):
    """Function deserializes a JSON string and returns an object
    represented by a JSON string

    args:
        my_str: JSON string

    Returns:
        a string represented by a JSON string
    """
    return json.loads(my_str)
