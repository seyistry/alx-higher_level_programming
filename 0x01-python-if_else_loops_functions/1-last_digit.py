#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10 if number >= 0 else number % -10
start = "Last digit of"
if number > 0:
    if lastDigit > 5:
        print(f"{start} {number} is {lastDigit} and is greater than 5")
    elif lastDigit == 0:
        print(f"{start} {number} is {lastDigit} and is 0")
    else:
        print(f"{start} {number} is {lastDigit} and is less than 6 and not 0")
else:
    if lastDigit == 0:
        print(f"{start} {number} is {lastDigit} and is 0")
    else:
        print(f"{start} {number} is {lastDigit} and is less than 6 and not 0")
