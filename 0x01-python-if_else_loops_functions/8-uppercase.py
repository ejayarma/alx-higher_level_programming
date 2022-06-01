#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            upper = chr(ord(c) - 32)
        else:
            upper = c
        print('{}'.format(upper), end='')
    print()
