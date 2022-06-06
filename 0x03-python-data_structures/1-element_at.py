#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    new_element = None
    if 0 <= idx < len(my_list):
        new_element = my_list[idx]
    return new_element
