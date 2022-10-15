#!/usr/bin/python3
""" a function that divides all
    elements of a matrix

    with matrix_divided as the only function
    """


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix

    Args:
        matrix (list): a list of lists of integers or floats,
        div (int, float): be a number (integer or float),
        otherwise raise a TypeError

    Raises:
        TypeError: matrix (list of lists) of integers/floats
            Each row of the matrix must have the same size
            and div must be a number
        ZeroDivisionError: division by zero

    Returns:
        list: a new matrix

    """
    err_one = "matrix must be a matrix (list of lists) of integers/floats"
    err_two = "Each row of the matrix must have the same size"
    new_matrix = []
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        if not (isinstance(matrix, list) and len(matrix) > 0):
            raise TypeError(
                err_one)
        for i in range(len(matrix)):
            if not (isinstance(matrix[i], list) and len(matrix[i]) > 0):
                raise TypeError(err_one)
            inner_list = []
            if i != 0:
                if len(matrix[i]) != len(matrix[i - 1]):
                    raise TypeError(err_two)
            for j in matrix[i]:
                if not (isinstance(j, int) or isinstance(j, float)):
                    raise TypeError(err_one)
                inner_list.append(round(j/div, 2))
            new_matrix.append(inner_list)
    return new_matrix
