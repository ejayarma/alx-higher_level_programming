#!/usr/bin/python3

for i in reversed(range(97, 123)):
    c = chr(i)
    if i % 2 == 0:
        print('{}'.format(c), end='')
    else:
        print('{}'.format(c.upper()), end='')
