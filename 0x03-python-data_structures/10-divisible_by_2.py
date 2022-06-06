#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        div_by_2 = (my_list[i] % 2 == 0)
        new_list.append(div_by_2)
    return new_list
