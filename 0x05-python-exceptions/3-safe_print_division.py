#!/usr/bin/python3
def safe_print_division(a: int, b: int) -> int:
    """Function that divides 2 integers and prints the result

    Args:
        a: integer
        b: integer

    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
