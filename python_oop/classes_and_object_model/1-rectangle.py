#!/usr/bin/env python3
"""Module: Recgtangle."""


class Rectangle():
    """Initiate rectangle class with dimentions"""
    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
