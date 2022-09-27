#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        pass
    else:
        for i in matrix:
            for j in range(len(i)):
                if j == len(i) - 1:
                    print("{:d}".format(i[j]))
                    continue
                print("{:d}".format(i[j]), end=" ")
