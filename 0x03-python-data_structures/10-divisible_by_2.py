#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    if my_list:
        for num in my_list:
            newList.append(False if num % 2 else True)
        return newList

