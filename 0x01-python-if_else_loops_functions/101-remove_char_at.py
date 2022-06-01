#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ''
    if 0 <= n < len(str):
        for i in range(len(str)):
            if i != n:
                new_str += str[i]
    else:
        new_str = str
    return new_str
