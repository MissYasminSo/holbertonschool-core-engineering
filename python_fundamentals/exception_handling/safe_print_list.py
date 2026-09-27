#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    try:
        for item in range(x):
            print("{}".format(my_list[item]), end='')
        print("")
        return x
    except Exception as ex:
        print("")
        print("Error: {}".format(ex))
