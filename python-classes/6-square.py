#!/usr/bin/python3
"""Defines a square class with size, position, validation, and printing"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size (int): The size of the new square
            position (int, int): The position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square"""
        return self.__member_position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__member_position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character and position spaces"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__member_position[1])]

        for i in range(self.__size):
            print(" " * self.__member_position[0] + "#" * self.__size)
