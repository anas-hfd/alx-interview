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

def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)

    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(" ".join(str(row[i]) for i in range(n) if row[i] == 1))
        print()

if __name__ == "__main__":
    main()