#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    ag = len(argv) - 1
    if ag != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator not in "**+/-":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    c = 0
    if operator == '*':
        c = a * b
    elif operator == '+':
        c = a + b
    elif operator == '-':
        c = a - b
    elif operator == '/':
        c = a / float(b)
    print("{:d} {:s} {:d} = {}".format(a, operator, b, c))
