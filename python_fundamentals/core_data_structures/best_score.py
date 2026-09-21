#!/usr/bin/env python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    res = ""
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            res = key
    return res
