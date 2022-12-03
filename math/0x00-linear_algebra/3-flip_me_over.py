#!/usr/bin/env python3
""" defines function that transposes a 2D matrix """


def matrix_transpose(matrix):
    """ returns new matrix that is a transpose of the given 2D matrix """
    if type(matrix[0]) != list:
        return [len(matrix)]
    else:
        new_matrix = [[matrix[j][i] for j in range(len(matrix))]
                      for i in range(len(matrix[0]))]
    return new_matrix
