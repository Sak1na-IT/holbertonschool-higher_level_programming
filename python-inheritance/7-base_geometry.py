#!/usr/bin/python3
"""ftghs"""


class BaseGeometry:
    """hsdg"""
    def area(self):
        """rjkhegfds"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """dhsilud"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
