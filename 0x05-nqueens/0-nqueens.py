#!/usr/bin/python3
"""N-Queens to add the Q when it is possible"""
import sys


def IsValidPlace(board, row, column, N):
    """Check if it's a valid place to put a queen"""
    # Check the column
    for i in range(row):
        if board[i][column] == 'Q':
            return False

    # Check upper left diagonal
    i, j = row, column
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, column
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def nqueens(board, row, N, solutions):
    """N-Queens to add the Q when it is possible"""
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'Q':
                    solution.append([i, j])
        solutions.append(solution)
        return

    for column in range(N):
        if IsValidPlace(board, row, column, N):
            board[row][column] = 'Q'
            nqueens(board, row + 1, N, solutions)
            board[row][column] = '.'


def main():
    """Main function to run the script"""
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
    nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
