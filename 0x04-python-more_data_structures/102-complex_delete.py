#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    to_be_deleted = []
    for k, v in a_dictionary.items():
        if v == value:
            to_be_deleted.append(k)
    for k in to_be_deleted:
        a_dictionary.pop(k, None)
    return a_dictionary
