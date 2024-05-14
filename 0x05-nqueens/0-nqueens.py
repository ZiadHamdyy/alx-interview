#!/usr/bin/python3
import sys

def IsValidPlace(board, row, column, N):

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

def nqueens(board, N, column=0):
    if column == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'Q':
                    solution.append([i, j])
        print(solution)
        return True
    
    res = False
    for i in range(N):
        if IsValidPlace(board, i, column, N):
            board[i][column] = 'Q'
            res = nqueens(board, N, column + 1) or res
            board[i][column] = '.'
    
    return res
def main():
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
    nqueens(board, N)
if __name__ == "__main__":
    main()
