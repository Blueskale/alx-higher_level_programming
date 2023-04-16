#!/usr/bin/python3
""" Module 8-class_to_json
 returns the dictionary description with a simple
data structure for  JSON serialization of an object
"""


def class_to_json(obj):
    """ Function  retuns the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
