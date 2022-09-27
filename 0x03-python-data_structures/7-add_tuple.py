#!/usr/bin/python3
def check_tuple(tuple_x=()):
    new_tup = list(tuple_x)
    x = ''
    if len((tuple_x)) < 2:
        for i in range(2):
            new_tup.append(0)
            if len(new_tup) == 2:
                break
        x = tuple(new_tup)
        return x
    else:
        x = tuple(new_tup[:2])
        return x


def add_tuple(tuple_a=(), tuple_b=()):
    x = check_tuple(tuple_a)
    y = check_tuple(tuple_b)
    return (x[0] + y[0], x[1] + y[1])
