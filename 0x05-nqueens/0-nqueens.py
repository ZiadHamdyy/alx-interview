#!/usr/bin/python3
"""nQueens to add the Q when it possible."""
import sys


def is_valid_place(board, row, column, n):
    """Check if it's possible to place a queen at the given position."""
    for j in range(column):
        if board[row][j] == 'Q':
            return False

    i, j = row, column
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row, column
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def nqueens(board, n, column=0, solutions=[]):
    """Solve the n-Queens problem."""
    if column == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'Q':
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_valid_place(board, i, column, n):
            board[i][column] = 'Q'
            nqueens(board, n, column + 1, solutions)
            board[i][column] = '.'


def main():
    """Main function to run the script."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    nqueens(board, n, 0, solutions)

    solutions.sort()
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
