#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    s = 0
    ag = len(argv) - 1
    for i in range(1, ag + 1):
        s += int(argv[i])
    print("{}".format(s))
