#!/usr/bin/python3
"""
Module for append_write function
"""


def append_write(filename="", text=""):
    """
    Appends a string at end of a text file

    Returns:
    int: the number of character added to the file
    """
    with open(filename, mode='a') as file:
        return file.write(text)
