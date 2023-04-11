#!/usr/bin/python3
"""
Module 2-is_same_class

A module that contains a function that checks if an object is an instance of
a specified class.
"""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is an instance of a specified class.

    Args:
    - obj: object to check
    - a_class: class to compare with

    Return: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class

