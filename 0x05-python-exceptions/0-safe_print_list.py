#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end=' ')
            i += 1
        print()
        return i
    except IndexError:
        print("The list is empty or index out of range. Cannot access elements.")
        return i
