#!/bin/usr/python3

'''
Contains a function that adds two numbers
'''


def add_integer(a, b=98):
    '''Returns the sum of two numbers
    Args:
        a (int, float): The first number.
        param2 (int, float): The second number.

    Returns:
        int: The return value. An integer if computation is a success
    '''
    valid_a = isinstance(a, (int, float))
    valid_b = isinstance(b, (int, float))
    if not valid_a:
        raise TypeError('a must be an integer')
    elif not valid_b:
        raise TypeError('b must be an integer')
    else:
        a = int(a)
        b = int(b)
        return a + b
