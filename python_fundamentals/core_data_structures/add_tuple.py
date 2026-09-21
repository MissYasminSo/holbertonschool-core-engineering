#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 1:
        ta1 = tuple_a[0]
        ta2 = 0
    elif len(tuple_a) == 0:
        ta1 = 0
        ta2 = 0
    else:
        ta1 = tuple_a[0]
        ta2 = tuple_a[1]

    if len(tuple_b) == 1:
        tb1 = tuple_b[0]
        tb2 = 0
    elif len(tuple_b) == 0:
        tb1 = 0
        tb2 = 0
    else:
        tb1 = tuple_b[0]
        tb2 = tuple_b[1]

    return (ta1 + tb1, ta2 + tb2)
