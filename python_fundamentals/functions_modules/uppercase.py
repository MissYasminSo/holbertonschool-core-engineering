#!/usr/bin/env python3
def uppercase(str):
    for letter in str:
        letter_num = ord(letter)
        upper_num = letter_num
        if (letter_num >= ord('a')):
            upper_num = letter_num - 32
        print("{:s}".format(chr(upper_num)), end='')
    print("".format(""))
