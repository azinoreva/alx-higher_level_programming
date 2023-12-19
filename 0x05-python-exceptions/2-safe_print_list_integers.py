#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_integers = 0

    try:
        for i in range(x):
            element = int(my_list[i])
            print("{:d}".format(element), end=" ")
            count_integers += 1

    except (ValueError, IndexError):
        pass

    finally:
        print()
        return count_integer
