#!/usr/bin/python3
def no_c(my_string):
    new_list= []
    for i in list(my_string):
        if i == "c" or i == "C":
            continue
        new_list.append(i)
    new_string = ""
    return new_string.join(new_list)
