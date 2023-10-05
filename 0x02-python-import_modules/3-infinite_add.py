#!/usr/bin/python3
import argparse
import sys


def my_function():
    if len(sys.argv) > 1:
        n = 0
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument("integers", metavar="N", type=int, nargs="+")
        args = parser.parse_args()
        if args.integers:
            for args in args.integers:
                n += args
        print("{:d}".format(n))
    else:
        print("{:d}".format(0))


if __name__ == '__main__':
    my_function()
