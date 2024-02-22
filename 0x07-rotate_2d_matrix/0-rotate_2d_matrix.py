#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise"""
    n = len(matrix)
    # transpose the matrix
    for i in range (n):
        for j in range (i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for i in range (n):
        matrix[i].reverse()
