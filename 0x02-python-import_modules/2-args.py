#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    ag = len(argv) - 1
    text = "argument" if ag == 1 else "arguments"
    print("{:d} {:s}:".format(ag, text))
    for i in range(1, ag):
        print("{:d}: {:s}".format(i, argv[i]))
