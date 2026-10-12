#!/usr/bin/env python3
"""Module: File Handling."""


def write_file(filename="", text=""):
    """Write in a file"""

    with open(filename, "w") as f:
        return f.write(text)
