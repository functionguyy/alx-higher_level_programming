#!/usr/bin/python3
import argparse
import sys


def my_function():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(prog="test_args")
        parser.add_argument("args", nargs="+")
        args = parser.parse_args()

        if args.args:
            if len(args.args) == 1:
                print("{0:d} argument:".format(len(args.args)))
            elif len(args.args) > 1:
                print("{0:d} arguments:".format(len(args.args)))

            for i, arg in enumerate(args.args):
                print("{0:d}: {1:s}".format(i+1, arg))
    else:
        print("{:d} arguments.".format(0))


if __name__ == '__main__':
    my_function()
