#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        count = 0
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return
