#!/usr/bin/python3
for num in range(9):
    for num2 in range(num + 1, 10):
        if num * 10 + num2 < 89:
            print("{:d}{:d}".format(num, num2), end=", ")
print("{:d}".format(89))
