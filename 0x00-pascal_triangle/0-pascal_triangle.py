#!/usr/bin/python3
"""0. Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for x in range(1, i + 1):
                level.append(C)
                C = C * (i - x) // x
            res.append(level)
    return res