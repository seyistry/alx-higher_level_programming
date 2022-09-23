#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("0 arguments.")
    else:
        s = 's' if len(argv) > 2 else ''
        print("{0} argument{1}:".format(len(argv) - 1, s))
        for i in range(1, len(argv)):
            print("{0}: {1}".format(i, argv[i]))
