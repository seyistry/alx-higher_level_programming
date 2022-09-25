#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, mul, sub, div
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] not in ['+', '-', '*', '/']:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            if argv[2] == '+':
                print(f"{a} {argv[2]} {b} = {add(a, b)}")
            if argv[2] == '-':
                print(f"{a} {argv[2]} {b} = {sub(a, b)}")
            if argv[2] == '*':
                print(f"{a} {argv[2]} {b} = {mul(a, b)}")
            if argv[2] == '/':
                print(f"{a} {argv[2]} {b} = {div(a, b)}")
            exit(0)
