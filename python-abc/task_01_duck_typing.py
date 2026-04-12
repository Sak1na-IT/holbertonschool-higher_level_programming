#!/usr/bin/python3
"""bhdsi"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """dgjs"""
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """dfuh"""
    def __init__(self, radius):
        self.radius = abs(radius)
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """sdihs"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(figur):
    print("Area: {}".format(figur.area()))
    print("Perimeter: {}".format(figur.perimeter()))
