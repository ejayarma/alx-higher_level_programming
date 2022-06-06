#!/usr/bin/python3

def element_at(my_list, idx):
    new_element = None
    if 0 <= idx < len(my_list):
        new_element = my_list[idx]
    return new_element
