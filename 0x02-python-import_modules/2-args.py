#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    args_list = argv[1:]
    plural_suffix = 's' if num_args != 1 else ''

    print("{} argument{}:".format(num_args, plural_suffix))

    if num_args > 0:
        for i, arg in enumerate(args_list, start=1):
            print("{}: {}".format(i, arg))
