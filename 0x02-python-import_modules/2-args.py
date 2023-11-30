#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    arg_str = "arguments" if argc != 1 else "argument"
    plural_suffix = 's' if argc != 1 else ''

    print("{} {}{}{}".format(argc, arg_str, plural_suffix, ":" if argc else "."))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
