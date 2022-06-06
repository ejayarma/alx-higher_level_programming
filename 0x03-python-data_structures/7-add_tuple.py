#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    cx = 0
    cy = 0

    if len(tuple_a) == 2:
        cx += tuple_a[0]
        cy += tuple_a[1]
    elif len(tuple_a) == 1:
        cx += tuple_a[0]

    if len(tuple_b) == 1:
        cx += tuple_b[0]
    elif len(tuple_b) == 2:
        cx += tuple_b[0]
        cy += tuple_b[1]

    return (cx, cy)
