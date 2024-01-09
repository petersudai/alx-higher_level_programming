#!/usr/bin/python3

"""Write string from textfile"""


def write_file(filename="", text=""):
    """
    Function that writes string to a text file

    Returns:
    int: number of characters written to the file
    """
    with open(filename, mode='w') as file:
        return file.write(text)
