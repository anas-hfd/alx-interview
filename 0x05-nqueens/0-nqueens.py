#!/usr/bin/python3
""" N Queens """
import sys

def is_safe(board, row, col):
    """is safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(0, col)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    """solve func"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        """back track"""
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions
