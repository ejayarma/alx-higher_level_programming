#!/bin/usr/python3

'''
Contains a function that adds two numbers
'''


def add_integer(a, b=98):
    '''Returns the sum of two numbers
    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int: The return value. An integer if computation is a success
    '''

    valid_a = type(a) == int or type(a) == float
    valid_b = type(b) == int or type(b) == float
    if not valid_a:
        raise TypeError('a must be an integer')
    if not valid_b:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
