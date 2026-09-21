#!/usr/bin/env python3
deli = ""
for i in range(0, 10):
    j = i + 1
    while (j < 10):
        print("{:s}{:d}{:d}".format(deli, i, j), end='')
        deli = ", "
        j = j + 1
print("")
