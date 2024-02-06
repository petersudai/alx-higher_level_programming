#!/usr/bin/python3

"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
