#!/usr/bin/env python3
def uppercase(str):
    for letter in str:
        letter_num = ord(letter)
        if (letter_num >= ord('a')):
            print(chr(letter_num - 32), end='')
        else:
            print(letter, end='')
    print("")
