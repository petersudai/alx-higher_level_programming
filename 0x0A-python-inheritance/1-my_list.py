#!/usr/bin/python3
"""
Module containing the MyList class, which inherits from list
"""

class MyList(list):
    """
    MyList class inherits from list and adds a method to print the sorted list
    """

    def print_sorted(self):
        """
        Print list in sorted (ascending) order
        """
        sorted_list = sorted(self)
        print(sorted_list)
