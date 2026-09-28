#!/usr/bin/env python3
"""Module: Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Basic Square Class"""

    def __init__(self, size):
        super().integer_validator("size", size)

        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
