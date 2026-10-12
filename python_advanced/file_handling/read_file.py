#!/usr/bin/env python3
"""Module: File Handling."""

def read_file(filename=""):
    """Read a file"""

    with open(filename) as f:
        for line in f:
            print(line, end='')
