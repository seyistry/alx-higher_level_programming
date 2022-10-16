#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

print("===========Testing Basics=============")
say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")

print("===========Handle errors==============")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

try:
    say_my_name("Dupe", None)
except Exception as e:
    print(e)

try:
    say_my_name(None)
except Exception as e:
    print(e)

print("==========Testing Numeric Int=========")

try:
    say_my_name("12", "Luke")
except Exception as e:
    print(e)

try:
    say_my_name("Dada", "13")
except Exception as e:
    print(e)

try:
    say_my_name("20", "13")
except Exception as e:
    print(e)