#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        delim = ""
        for element in row:
            print("{:s}{:d}".format(delim, element), end='')
            delim = " "
        print("".format(""))
