#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    ag = len(argv)
    if ag != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == "*":
        c = mul(a, b)
    elif operator == "+":
        c = add(a, b)
    elif operator == "-":
        c = sub(a, b)
    elif operator == "/":
        c = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {}".format(a, operator, b, c))
