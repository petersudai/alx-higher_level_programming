#!/usr/bin/python3
"""
Add item
"""
import sys
from save_to_json_file import save_to_json_file
from load_to_json_file import load_from_json_file


def add_item(args):
    """
    Adds all arguments to a list and saves them to a file
    """
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(args)

    save_to_json_file(items, filename)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_item(arguments)
