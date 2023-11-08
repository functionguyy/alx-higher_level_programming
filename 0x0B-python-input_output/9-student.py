#!/usr/bin/python3
"""Module defines a class Student"""


class Student:
    """defines the internal representtation of a Student object"""

    def __init__(self, first_name, last_name, age):
        """intialize an instance of Student

        Attributes:
            first_name(:obj:): string 
            last_name(:obj:): string
            age(:obj:): integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve dictionary representation of Student instance"""
        return self.__dict__
