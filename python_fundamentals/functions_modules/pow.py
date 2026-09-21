#!/usr/bin/env python3
def pow(a, b):
    res = 1
    for i in range(abs(b)):
        if (b > 0):
            res = res * a
        else:
            res = res / a
    return res
