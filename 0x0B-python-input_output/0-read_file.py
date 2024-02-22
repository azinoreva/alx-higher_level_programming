#!/usr/bin/python3

def read_file(filename=""):
    """
    This function reads a text file and prints it out to stdout
    """
    with open(filename, encoding="utf-8") as x:
        read_data =x.read()
        print(read_data)

