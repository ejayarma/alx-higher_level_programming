#!/bin/usr/python3

'''
Contains a function that
prints a square
'''


def print_square(size):
    '''Print a square with length size
    Args:
        size (int): The size of the square.

    Returns:
        None: Returns None
    '''

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        print('#' * size)
