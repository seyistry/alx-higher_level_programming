#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(f"{my_list[i]}", end = "")
            count += 1
    except IndexError:
        pass
    finally:
        if x > 0:
            print("")
            return count
