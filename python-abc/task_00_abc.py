#!/usr/bin/python3
"""hbfdsjfh"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """bfhd"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """JGFDSH"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """hdsg"""
    def sound(self):
        return "Meow"
