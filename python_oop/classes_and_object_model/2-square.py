#!/usr/bin/env python3
"""Module: Square."""


class Square():
    """Initiate square class with size attribute"""
    def __init__(self, size = 0):
        if (size < 0):
            raise ValueError("size must be >= 0")
        elif (isinstance(size, int) == False):
            raise TypeError("size must be an integer")
        else:
            self.__size = size
