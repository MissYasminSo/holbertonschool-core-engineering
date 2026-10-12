#!/usr/bin/env python3
"""Module: File Handling."""


def append_write(filename="", text=""):
    """Append and write a file"""

    with open(filename, "a") as f:
        return f.write(text)
