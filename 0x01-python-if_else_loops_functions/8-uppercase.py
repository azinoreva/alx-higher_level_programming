#!/usr/bin/python3
def uppercase(str):
    for num in str:
        if ord("a") <= ord(num) <= ord("z"):
            num = chr(ord(num) - 32)
        print("{:s}".format(num), end="")
    print()
