#!/usr/bin/python3
"""nQueens to add the Q when it posseble"""
import sys


def IsValidPlace(board, row, column, N):
    """IsValidPlace to check if its possible or not"""
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
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def nqueens(board, N, column=0, solutions=[]):
    """nQueens to add the Q when it posseble"""
    if column == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'Q':
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if IsValidPlace(board, i, column, N):
            board[i][column] = 'Q'
            nqueens(board, N, column + 1, solutions)
            board[i][column] = '.'


def main():
    """main function to run the script"""
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
