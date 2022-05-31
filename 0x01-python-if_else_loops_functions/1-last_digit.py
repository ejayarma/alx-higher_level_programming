#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
sign = '-' if number and number < 0 else ''
suffix_text = 'haha'
string = 'Last digit of {} is {}{} and is {}'
if last_digit == 0:
    suffix_text = '0'
elif number > 0 and last_digit > 5:
    suffix_text = 'greater than 5'
elif number < 0 or last_digit <= 5:
    suffix_text = 'less than 6 and not 0'
print(string.format(number, sign, last_digit, suffix_text))
