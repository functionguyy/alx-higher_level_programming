#!/usr/bin/python3
import sys
from add_0 import add


def my_function():
    a = 1
    b = 2
    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
    return 0


if __name__ == '__main__':
    sys.exit(my_function())
