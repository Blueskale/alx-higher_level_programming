#!/usr/bin/python3
"""
is_kind_of_class function module.
Define is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherited from a_class"""
    return isinstance(obj, a_class)
