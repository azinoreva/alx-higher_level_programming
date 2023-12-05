#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            newString += elements
    return newString
