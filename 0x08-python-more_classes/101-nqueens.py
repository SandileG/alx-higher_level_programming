#!/usr/bin/python3
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
