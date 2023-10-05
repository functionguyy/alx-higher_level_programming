#!/usr/bin/python3
# Program that imports all functions from the file
# calculator_1.py and handles basic operations

import argparse
import sys
from calculator_1 import add, sub, mul, div


def my_calculator():
    """My calculator function
    Usage ./100-my_calculator.py a operator b

    Returns:
    value of operation or exit with value 1 if the number of
    arguments is not 3 or if operator is invalid
    """

    if len(sys.argv) == 4:

        parser = argparse.ArgumentParser()
        parser.add_argument('a', metavar='integer1', type=int, nargs=1)
        parser.add_argument('op', metavar='[+-*/]', nargs=1)
        parser.add_argument('b', metavar='integer2', type=int, nargs=1)
        args = parser.parse_args()

        math_op = args.op[0]
        a = args.a[0]
        b = args.b[0]

        if math_op == '+':
            print("{0:d} {1:s} {2:d} = {3:d}".format(a, math_op, b, add(a, b)))
        elif math_op == '-':
            print("{0:d} {1:s} {2:d} = {3:d}".format(a, math_op, b, sub(a, b)))
        elif math_op == '*':
            print("{0:d} {1:s} {2:d} = {3:d}".format(a, math_op, b, mul(a, b)))
        elif math_op == '/':
            print("{0:d} {1:s} {2:d} = {3:d}".format(a, math_op, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)


if __name__ == '__main__':
    my_calculator()
