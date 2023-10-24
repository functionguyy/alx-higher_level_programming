#!/usr/bin/python3
def raise_exception_msg(message: str = "") -> None:
    """Function that raises a exception with a message

    Args:
        message: exception message string
    Return:
        None
    """
    raise NameError(message)
