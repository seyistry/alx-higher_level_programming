#!/usr/bin/python3
def uppercase(str):
    for i in str:
        sub = 32 if ord(i) in range(97, 123) else 0
        print("{}".format(chr(ord(i)-sub)), end="")
    print("")
