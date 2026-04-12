#!/usr/bin/python3
"""jdfs"""

from abc import ABC, abstractmethod


class VerboseList(list):
    """df"""
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))
    def extend(self, list2):
        x = len(list2)
        super().extend(list2)
        print("Extended the list with [{}] items.".format(x))
    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))
    def pop(self, index = -1):
        d = self[index]
        print("Popped [{}] from the list.".format(d))
        return super().pop(index)
