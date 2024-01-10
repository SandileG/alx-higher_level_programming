#!/usr/bin/python3
"""
N-Queens Solver

This module provides a program to solve the N-Queens problem. The N-Queens problem is the challenge of placing N non-attacking queens on an N×N chessboard.

Usage:
    ./101-nqueens.py N

    If the user called the program with the wrong number of arguments, print
    'Usage: 101-nqueens.py N', followed by a new line, and exit with the status 1,
    where N must be an integer greater or equal to 4.

    If N is not an integer, print 'N must be a number', followed by a new line,
    and exit with the status 1.

    If N is smaller than 4, print 'N must be at least 4', followed by a new line,
    and exit with the status 1.

    The program prints every possible solution to the N-Queens problem, one solution per line.
    The format of each solution is a list of coordinates representing the positions of the queens on the chessboard.

    You don’t have to print the solutions in a specific order.

    The program uses backtracking to find the solutions.

Example:
    ./101-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]

    ./101-nqueens.py 6
    [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""

import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same row
    if any(board[row][c] == 1 for c in range(N)):
        return False

    # Check if there is a queen in the same column
    if any(board[r][col] == 1 for r in range(N)):
        return False

    # Check if there is a queen in the same diagonal (left-up to right-down)
    if any(board[r][c] == 1 for r, c in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # Check if there is a queen in the same diagonal (left-down to right-up)
    if any(board[r][c] == 1 for r, c in zip(range(row, N, 1), range(col, -1, -1))):
        return False

    return True

def solve_nqueens_util(board, row, N, solutions):
    if row == N:
        solutions.append([[r, c] for r in range(N) for c in range(N) if board[r][c] == 1])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0

def solve_nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
