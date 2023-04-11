#!/usr/bin/python3
"""
Module containing the MyList class
"""


class MyList(list):
    """
    Subclass of the built-in list class
    """
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))

