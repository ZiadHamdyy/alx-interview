#!/usr/bin/python3
"""nQueens to add the Q when it possible"""
import sys


def is_valid_place(board, row, column, N):
    """Check if placing a queen at the given position is valid."""
    for j in range(column):
        if board[row][j] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, N), range(column, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def nqueens(board, N, column=0, solutions=None):
    """Find all possible solutions for N-Queens problem."""
    if solutions is None:
        solutions = []

    if column == N:
        solutions.append([[i, j] for i in range(N) for j in range(N) if board[i][j] == 'Q'])
        return

    for i in range(N):
        if is_valid_place(board, i, column, N):
            board[i][column] = 'Q'
            nqueens(board, N, column + 1, solutions)
            board[i][column] = '.'


def main():
    """Main function to run the script."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    nqueens(board, N, 0, solutions)

    solutions.sort()
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
