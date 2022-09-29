#!/usr/bin/python3
def weight_average(my_list=[]):
    upper = 0
    deno = 0
    for i in my_list:
        upper += (i[0] * i[1])
        deno += i[1]
    return upper / deno
