#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    result = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end='')
            result = result + 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return result
