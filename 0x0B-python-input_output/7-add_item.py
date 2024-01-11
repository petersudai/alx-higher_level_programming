#!/usr/bin/python3
"""
Add item
"""
import sys


def add_item(args):
    """
    Adds all arguments to a list and saves them to a file
    """
    filename = "add_item.json"

    items = []
    if exists(filename):
        items = load_from_json_file(filename)

    items.extend(args)

    save_to_json_file(items, filename)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_item(arguments)
