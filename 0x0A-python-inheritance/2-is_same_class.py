#!/usr/bin/python3
"""
Module containeing is_same_class function
"""


def is_same_class(obj, a_class):
    """Return True if object is exactly an instance of specified class"""
    return type(obj) is a_class
