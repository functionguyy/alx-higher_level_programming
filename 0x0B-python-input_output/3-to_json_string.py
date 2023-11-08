#!/usr/bin/python3
"""Module that contains funtion that returns the JSON representation of an
object"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object string

    args:
        my_obj: object string

    Return:
        JSON representation of the object string
    """
    return json.dumps(my_obj)
