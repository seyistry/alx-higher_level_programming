#!/usr/bin/python3
for i in range(100):
    mod = i % 10
    div = i / 10
    if mod > div:
        if i > 88:
            print("{:0>2d}".format(i))
            continue
        print("{:0>2d}".format(i), end=", ")
