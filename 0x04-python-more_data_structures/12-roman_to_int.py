#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if (isinstance(roman_string, str) and roman_string is not None):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        prev_value = 0
        for i in reversed(range(len(roman_string))):
            c = roman_string[i]
            curr_value = roman_values[c]
            if curr_value >= prev_value:
                result += curr_value
            else:
                result -= curr_value
            prev_value = curr_value
    return result
