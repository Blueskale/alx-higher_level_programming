#!/usr/bin/python3
"""
File 0-add_integer
This file is composed of a function that adds two numbers
"""


def add_integer(a, b=98):
    """ Function that adds two integer or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: If a or b are not integers or float numbers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)

