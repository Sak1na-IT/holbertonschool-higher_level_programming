#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """A subclass of list that provides a sorted """

    def print_sorted(self):
        """Prints the modifying the original."""
        print(sorted(self))
