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

    def to_json(self, attrs=None):
        """retrieve dictionary representation of Student instance"""
        instance_attrs = self.__dict__

        if type(attrs) is list:
            """
            Validate the elements in the attr list are strings.
            Create a list comprehension to create a new list of Boolean values.
            Logic returns True if the element is a string and False if
            otherwise
            """
            string_statuses = [isinstance(value, str) for value in attrs]
            condition_status = all(string_statuses)
            if condition_status is True:
                list_attr_dict = {}
                for attr in attrs:
                    if hasattr(self, attr):  # does instance have attr
                        list_attr_dict[attr] = instance_attrs[attr]
                return list_attr_dict

        return instance_attrs
