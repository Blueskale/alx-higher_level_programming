#!/usr/bin/python3
""" Module 9-student
defines the class Student
"""


class Student:
    """ Class creates student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method is initialized """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method  returns directory description """
        return self.__dict__.copy()
