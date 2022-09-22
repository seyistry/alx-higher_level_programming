#!/usr/bin/python3
def remove_char_at(str, n):
    if n > 0:
        rchar = str[:n] + str[n + 1:]
    else:
        rchar = str
    return rchar
