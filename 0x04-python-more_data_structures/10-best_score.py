#!/usr/bin/python3

def best_score(a_dictionary):
    mk = None
    mv = 0
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if v > mv:
                mk = k
            mv = v
    return mk
