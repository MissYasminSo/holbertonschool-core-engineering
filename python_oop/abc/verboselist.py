#!/usr/bin/env python3
"""Module: ABC."""


class VerboseList(list):
    def append(self, value):
        super().append(value)
        print(f"Added [{value}] to the list.")

    def extend(self, value):
        super().extend(value)
        print(f"Extended the list with [{len(value)}] items.")

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        super().pop(index)
