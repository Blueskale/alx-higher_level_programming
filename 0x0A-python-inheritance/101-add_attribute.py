#!/usr/bin/python3
"""
Module 101-add_attribute.py
"""


def add_attribute(obj, attribute, value):
    """Add new attribute to an object if possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__setattr__(attribute, value)

