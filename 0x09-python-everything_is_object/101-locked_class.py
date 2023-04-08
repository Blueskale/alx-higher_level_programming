#!/usr/bin/python3
"""
File 101-locked_class
"""


class LockedClass:
    """
    This is a file that contains a class that avoids
    dynmaically created attributes
    """
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
