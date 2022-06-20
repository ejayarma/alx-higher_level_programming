#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    print_count = 0
    if not len(my_list) or x <= 0:
        return print_count
    for i in range(x):
        try:
            print(my_list[i], end='')
            print_count += 1
        except Exception:
            pass
    print()
    return print_count
