#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            column = row[j]
            print("{:d}".format(column), end='')
            if j < len(row) - 1:
                print("{}".format(' '), end='')
        print("{}".format('\n'), end='')
