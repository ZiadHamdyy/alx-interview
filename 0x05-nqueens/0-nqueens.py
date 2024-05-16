#!/usr/bin/python3
""" N queens problem """


def nQueen(n):
    """ N queens problem """
    invalid = set()
    pos = set()
    neg = set()
    res = []
    board = [['.'] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            res.append([[i, j] for i in range(n)
                        for j in range(n) if board[i][j] == 'Q'])
            return
        for col in range(n):
            if col in invalid or (row - col) in neg or (row + col) in pos:
                continue
            invalid.add(col)
            neg.add(row - col)
            pos.add(row + col)
            board[row][col] = 'Q'
            backtrack(row + 1)
            invalid.remove(col)
            neg.remove(row - col)
            pos.remove(row + col)
            board[row][col] = '.'
    backtrack(0)
    return res


if __name__ == "__main__":
    """ the entry point """
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    for solution in nQueen(int(sys.argv[1])):
        print(solution)
