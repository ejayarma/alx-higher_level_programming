#!/bin/usr/python3

'''
Contains a function that
concatenates two names
'''


def say_my_name(first_name, last_name=""):
    '''Returns a full name

    The full name is the concatenation of
    First name and last name

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Returns:
        str: The return value. Full name
    '''
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    return f'My name is {first_name} {last_name}'
