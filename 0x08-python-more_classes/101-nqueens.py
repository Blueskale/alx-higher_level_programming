#!/usr/bin/python3
import sys

def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True
    
    def backtrack(board, row):
        nonlocal result
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

if __name__ == '__main__':
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
    solutions = solve_n_queens(n)
    for sol in solutions:
        print("[", end="")
        for i in range(n):
            print("[{}, {}]".format(i, sol[i]), end="")
            if i != n - 1:
                print(", ", end="")
        print("]")
