#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: [n * n for n in x], matrix))
