#!/bin/usr/python3

'''
Contains a function that divides a matrix
'''


def matrix_divided(matrix, div):
    '''Returns the sum of two numbers
    Args:
        matrix: The matrix.
        div: The divisor

    Returns:
        The return value. A matrix
    '''
    # Validate matrix
    valid_matrix = type(matrix) == list
    message = 'matrix must be a matrix (list of lists) of integers/floats'
    if not valid_matrix:
        raise TypeError(message)

    # Validate div
    valid_div = type(div) == int or type(div) == float
    if not valid_div:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Validate rows
    if len(matrix):
        row_length = len(matrix[0]) if type(matrix[0]) == list else 0
        for row in matrix:
            if type(row) != list:
                raise TypeError(message)
            if row_length and row_length != len(row):
                message = 'Each row of the matrix must have the same size'
                raise TypeError(message)

            # Validate each column
            for num in row:
                valid_num = type(num) == int or type(num) == float
                if not valid_num:
                    raise TypeError(message)

    return list(map(
            lambda x: list(map(lambda y: round(y / div, 2), x)),
            matrix
        ))
