#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    powx = []
    for line in matrix:
        powx.append([c**2 for c in line])
    return powx
