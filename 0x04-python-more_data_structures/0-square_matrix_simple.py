#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = map(lambda x: [n * n for n in x], matrix)
    return list(new_matrix)
