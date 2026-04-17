#!/usr/bin/python3
"""
asdfghjkl
"""


class Student:
    """
    asdfghjkl
    """

    def __init__(self, first_name, last_name, age):
        """
        asdfghjkl
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        asdfghjkl
        """
        if isinstance(attrs, list) and \
           all(isinstance(x, str) for x in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        asdfghjkl
        """
        for key, value in json.items():
            setattr(self, key, value)
