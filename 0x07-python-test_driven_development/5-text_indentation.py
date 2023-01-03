#!/bin/usr/python3

'''
Contains a function that prints a text with
2 new lines after each of these characters: '.', '?' and ':'
'''


def text_indentation(text):
    '''Print a square with length size
    Args:
        text (str): The string to indent.

    Returns:
        None: Returns None
    '''
    if type(text) != str:
        raise TypeError('text must be a string')
    chars = (
       ch + '\n\n' if ch in '.?:' else ch for ch in text
    )
    text_indented = ''.join(chars)
    lines = text_indented.split('\n\n')

    for line in lines:
        print(line.strip() + '\n\n' if line else '', end='')
