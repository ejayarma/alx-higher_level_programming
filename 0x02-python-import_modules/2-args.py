#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    ag = len(argv) - 1
    text = "argument" if ag == 1 else "arguments"
    sign = "." if ag == 0 else ":"
    print("{} {}{}".format(ag, text, sign))
    for i in range(1, ag + 1):
        print("{}: {}".format(i, argv[i]))
