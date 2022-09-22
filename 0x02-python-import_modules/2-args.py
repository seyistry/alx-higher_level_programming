#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 0:
        print(".")
    else:
        print(f"{len(argv)} arguments:")
        for i in range(1,len(argv)):
            print(f"{i:} {argv[i]}")

