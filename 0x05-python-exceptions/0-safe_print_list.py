#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        count =0
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print("")
    return
