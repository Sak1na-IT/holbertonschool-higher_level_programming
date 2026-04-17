#!/usr/bin/python3
"""jdblius"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """kgfcf"""
    def __init__(self, size):
        """jgerjhv"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
