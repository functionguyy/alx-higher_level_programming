#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Function that executes a function safely

    Args:
        fct: pointer to a function
    Returns:
        the result of the function, otherwise returns None if something happens
        during the function and prints in stderr the error precede by
        Exception:
    """
    try:
        result = fct(*args)
        return result
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
