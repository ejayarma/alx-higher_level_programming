#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    try:
        for i in range(list_length):
            a = my_list_1[i]
            b = my_list_2[i]
            nifa = isinstance(a, (int, float))
            nifb = isinstance(b, (int, float))
            wt = not nifa or not nifb
            if wt:
                print('wrong type')
            if b == 0:
                print('division by 0')
            if wt or b == 0:
                new_list.append(result)
                continue
            new_list.append(a / b)
    except IndexError:
        print('out of range')
    finally:
        return new_list
