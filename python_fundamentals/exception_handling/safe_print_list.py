#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    result = 0
    try:
        for item in range(x):
            print("{}".format(my_list[item]), end='')
            result = result + 1
        print("")
        return result
    except Exception as ex:
        print("")
        return result
