#!/usr/bin/python3

"""
N queens problem
"""

import sys


class NQueens:
    """ Class for solving the N Queens problem """

    def __init__(self, n):
        """ Initialize N Queens """
        self.n = n
        self.columns = []
        self.diag1 = []
        self.diag2 = []
        self.solutions = []

    def solve(self):
        """ Solve the N Queens problem """
        self._solve(0)
        self._display()

    def _solve(self, row):
        """ Recursive function to solve N Queens """
        if row == self.n:
            solution = []
            for i in range(self.n):
                solution.append([i, self.columns[i]])
            self.solutions.append(solution)
        else:
            for col in range(self.n):
                if (
                    col not in self.columns and
                    row + col not in self.diag1 and
                    row - col not in self.diag2
                ):
                    self.columns.append(col)
                    self.diag1.append(row + col)
                    self.diag2.append(row - col)
                    self._solve(row + 1)
                    self.columns.pop()
                    self.diag1.pop()
                    self.diag2.pop()

    def _display(self):
        """ Display the solutions """
        for solution in self.solutions:
            print(solution)


if __name__ == "__main__":
    # Check the command-line arguments
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

    # Solve the N Queens problem
    queens = NQueens(n)
    queens.solve()
