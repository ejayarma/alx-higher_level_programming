#!/usr/bin/python3

def max_integer(my_list=[]):
    if not len(my_list) > 0:
        return None
    max_n = my_list[0]
    for i in range(1, len(my_list)):
        n = my_list[i]
        if n > max_n:
            max_n = n
    return max_n
