#!/usr/bin/env python3
"""Module: Square."""


class Square():
    """Initiate square class with size and position attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def __str__(self):
        result = ""
        if self.__size == 0:
            return result
        else:
            i = 0
            for line in range(self.position[1]):
                result = result + "\n"
            for index in range(self.__size):
                for row in range(self.position[0]):
                    result = result + " "
                for index in range(self.__size):
                    result = result + "#"
                if i < self.__size - 1:
                    result = result + "\n"
                i = i + 1
            return result

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, size):
        self.__position = position
