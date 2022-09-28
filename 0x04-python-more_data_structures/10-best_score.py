#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    top, val= None, 0
    for key, value in a_dictionary.items():
        if value > val:
            top, val = key, value
    return top
