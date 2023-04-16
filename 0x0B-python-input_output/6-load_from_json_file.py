#!/usr/bin/python3
""" Module 6-load_from_json_file
that creates  Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function that creates  Object from a JSON file
    Args:
        filename: textfile name
    Raises:
        Exception: when  object can't be encoded
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
