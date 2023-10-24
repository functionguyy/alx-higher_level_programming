#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Function that prints an integer

    Args:
        value: can be any type(integer, string, etc)

    Description:
        The integer should be printed followed by a new line
    Return:
        Returns True if value has been correctly printed(it means the value is
        an integer). Otherwise, returns False and prints in stderr the error
        precede by Exception:
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        sys.stderr.write(f"Exception: {e}\n")

    return False
