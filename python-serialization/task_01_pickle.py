#!/usr/bin/python3
"""
asdfghjkl
"""
import pickle


class CustomObject:
    """
    asdfghjkl
    """

    def __init__(self, name, age, is_student):
        """
        asdfghjkl
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        asdfghjkl
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        asdfghjkl
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        asdfghjkl
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
        except Exception:
            return None
