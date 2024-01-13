#!/usr/bin/python3
"""Defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """
    Creates an object from JSON file

    Returns:
    The python object represented by the JSON File
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
