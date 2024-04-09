#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    if col >= N:
        queens_positions = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    queens_positions.append([i, j])
        solutions.append(queens_positions)
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                pass
            board[i][col] = 0

    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("Usage: ./101-nqueens.py N")
        sys.exit(0)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []

    solve_n_queens(board, 0)

    if not solutions:
        print("No solution found.")
    else:
        for solution in solutions:
            print(solution)
