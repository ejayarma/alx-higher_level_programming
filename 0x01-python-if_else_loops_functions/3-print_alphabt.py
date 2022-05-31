#!/usr/bin/python3
for i in range(97, 97 + 26):
    if not chr(i) in 'qe':
        print("{}".format(chr(i)), end='')
