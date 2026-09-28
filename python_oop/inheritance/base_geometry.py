#!/usr/bin/env python3
"""Module: Inheritance."""


class BaseGeometry:
    """Base class for Geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            self.__value = value
