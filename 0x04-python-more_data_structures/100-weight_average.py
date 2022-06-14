#!/usr/bin/python3

def weight_average(my_list=[]):
    total_sum = 0
    total_weight = 0
    if not len(my_list):
        return total_sum
    for t in my_list:
        score, weight = t
        total_weight += weight
        total_sum += score * weight
    return total_sum/total_weight
