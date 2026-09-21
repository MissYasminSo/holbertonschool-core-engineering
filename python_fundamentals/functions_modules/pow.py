#!/usr/bin/env python3
def pow(a, b):
    res = 1
    for i in range(abs(b)):
        res = res * a
    if b < 0:
        return 1 / res
    return res
