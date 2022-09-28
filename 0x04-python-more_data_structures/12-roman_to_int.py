#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str or roman_string is None:
        return 0
    form = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    cal = 0
    prev = 1000
    for i in roman_string:
        cal += form[i]
        if form[i] > prev:
            cal = cal - (prev * 2)
        prev = form[i]
    return cal
