#!/usr/bin/python3
"""Module contains function that add all items passed in the command line into
a list"""
import argparse
import sys
sjf = __import__('5-save_to_json_file').save_to_json_file
ljf = __import__('6-load_from_json_file').load_from_json_file


def add_item() -> None:
    """function add all items passed in the command line into a python list and
    saves the list as a JSON string in a file"""
    # if argument is present on command line
    if len(sys.argv) > 1:
        # create command line parser object
        parser = argparse.ArgumentParser(prog="add_item")
        parser.add_argument("args", nargs="*")
        args = parser.parse_args()

        if args.args:
            try:
                arg_list = ljf("add_item.json")
            except FileNotFoundError:
                arg_list = []
            arg_list.extend(args.args)
            sjf(arg_list, "add_item.json")
