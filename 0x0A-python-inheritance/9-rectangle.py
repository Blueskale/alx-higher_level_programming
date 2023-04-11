#!/usr/bin/python3
"""
Module 9-rectangle
Defines a Rectangle class.
Inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes an instance of the Rectangle class.
        """

        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the Rectangle instance.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns the informal string representation of the Rectangle instance.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

